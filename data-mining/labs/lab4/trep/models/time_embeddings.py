import torch
from torch import nn

# Time2Vec implementation from https://github.com/ojus1/Time2Vec-PyTorch


def t2v(tau, f, out_features, w, b, w0, b0, arg=None):
    if arg:
        v1 = f(torch.matmul(tau, w) + b, arg)
    else:
        v1 = f(torch.matmul(tau, w) + b)
    v2 = torch.matmul(tau, w0) + b0
    return torch.cat([v1, v2], -1)


class T2vSin(nn.Module):
    def __init__(self, in_features, out_features, normalise=True):
        super(T2vSin, self).__init__()
        self.out_features = out_features
        self.w0 = nn.parameter.Parameter(torch.randn(in_features, 1))
        self.b0 = nn.parameter.Parameter(torch.randn(1))
        self.w = nn.parameter.Parameter(torch.randn(in_features, out_features - 1))
        self.b = nn.parameter.Parameter(torch.randn(out_features - 1))
        self.f = torch.sin
        self.sigmoid = nn.Sigmoid()
        self.normalise = normalise

    def forward(self, tau):
        out = t2v(tau, self.f, self.out_features, self.w, self.b, self.w0, self.b0)
        out = self.sigmoid(out)
        if self.normalise:
            return out / torch.sum(out, dim=-1)[..., None]
        return out


class T2vCos(nn.Module):
    def __init__(self, in_features, out_features):
        super(T2vCos, self).__init__()
        self.out_features = out_features
        self.w0 = nn.parameter.Parameter(torch.randn(in_features, 1))
        self.b0 = nn.parameter.Parameter(torch.randn(1))
        self.w = nn.parameter.Parameter(torch.randn(in_features, out_features - 1))
        self.b = nn.parameter.Parameter(torch.randn(out_features - 1))
        self.f = torch.cos
        self.sigmoid = nn.Sigmoid()
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, tau):
        out = t2v(tau, self.f, self.out_features, self.w, self.b, self.w0, self.b0)
        out = self.sigmoid(out)
        return out / torch.sum(out, dim=-1)[..., None]


class LearnablePositionalEncodingHybrid(nn.Module):
    def __init__(self, in_features, out_features, hidden_features=32, dropout=0.1):
        super(LearnablePositionalEncodingHybrid, self).__init__()

        self.t2v_sin = T2vSin(
            in_features=in_features, out_features=out_features // 2, normalise=False
        )
        self.t2v_fc = LearnablePositionalEncodingBig(
            in_features=in_features,
            hidden_features=hidden_features,
            out_features=out_features // 2,
            dropout=dropout,
            normalise=False,
        )

    def forward(self, x):
        out_t2v_sin = self.t2v_sin(x)
        out_t2v_fc = self.t2v_fc(x)
        out = torch.cat((out_t2v_sin, out_t2v_fc), dim=-1)
        return out / torch.sum(out, dim=-1)[..., None]


class LearnablePositionalEncodingSmall(nn.Module):
    def __init__(self, in_features, out_features, hidden_features=32, dropout=0.1):
        super(LearnablePositionalEncodingSmall, self).__init__()
        self.dropout = nn.Dropout(p=dropout)
        self.fc = nn.Linear(in_features, out_features)
        self.dropout = nn.Dropout(p=dropout)
        self.tanh = nn.Tanh()
        self.sigmoid = nn.Sigmoid()
        self.relu = nn.ReLU()

    def forward(self, t):
        out = self.sigmoid(self.fc(t))
        return out / torch.sum(out, dim=-1)[..., None]


class LearnablePositionalEncodingBig(nn.Module):
    def __init__(
        self, in_features, out_features, hidden_features=32, dropout=0.1, normalise=True
    ):
        super(LearnablePositionalEncodingBig, self).__init__()
        self.normalise = normalise
        self.dropout = nn.Dropout(p=dropout)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
        self.fc = nn.Sequential(
            nn.Linear(in_features, hidden_features),
            self.relu,
            nn.Linear(hidden_features, out_features),
            self.sigmoid,
        )
        self.dropout = nn.Dropout(p=dropout)

    def forward(self, x):
        out = self.dropout(self.fc(x))
        if self.normalise:
            return out / torch.sum(out, dim=-1)[..., None]


class GaussianPositionalEncoding(nn.Module):
    def __init__(self, in_features, out_features):
        super(GaussianPositionalEncoding, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.sigmoid = nn.Sigmoid()

        self.w0 = nn.parameter.Parameter(torch.randn(in_features, 1))
        self.b0 = nn.parameter.Parameter(torch.randn(1))

        self.a = nn.parameter.Parameter(torch.randn(in_features, out_features - 1))
        self.mu = nn.parameter.Parameter(torch.randn(out_features - 1))
        self.sigma = nn.parameter.Parameter(torch.randn(out_features - 1))

    def forward(self, t):
        linear_feature = torch.matmul(t, self.w0) + self.b0
        gaussian_features = (torch.matmul(t, self.a) - self.mu) / (2 * self.sigma**2)
        out = torch.cat([linear_feature, gaussian_features], -1)
        out = self.sigmoid(out)
        return out / torch.sum(out, dim=-1)[..., None]


class T2vFourier(nn.Module):
    def __init__(self, num_components=100, in_features=1, out_features=1):
        super().__init__()
        self.sigmoid = nn.Sigmoid()
        self.num_components = num_components
        self.out_features = out_features
        self.fc = nn.Linear(in_features, out_features)
        self.freqs = nn.Parameter(torch.randn(1, num_components))
        self.amps = nn.Parameter(torch.randn(1, num_components))
        self.phases = nn.Parameter(torch.randn(1, num_components))

    def forward(self, t):
        ft = torch.sum(
            self.amps * torch.cos(self.freqs * t.unsqueeze(-1) + self.phases), dim=-1
        )
        return self.sigmoid(self.fc(ft))


class T2vFourierHybrid(nn.Module):
    def __init__(self, in_features, out_features, num_components=100, normalise=True):
        super(T2vFourierHybrid, self).__init__()
        self.out_features = out_features
        self.num_components = num_components
        self.w0 = nn.Parameter(torch.randn(in_features, 1))  # Frequency term for second part
        self.b0 = nn.Parameter(torch.randn(1))  # Bias for second part
        self.w = nn.Parameter(torch.randn(in_features, out_features - 1))  # For Fourier terms
        self.b = nn.Parameter(torch.randn(out_features - 1))  # Bias for Fourier terms

        # Fourier-specific parameters
        self.freqs = nn.Parameter(torch.randn(1, num_components))  # Frequencies
        self.amps = nn.Parameter(torch.randn(1, num_components))  # Amplitudes
        self.phases = nn.Parameter(torch.randn(1, num_components))  # Phases

        self.sigmoid = nn.Sigmoid()
        self.normalise = normalise

    def fourier(self, tau):
        """Fourier function that computes the sum of cosines"""
        return torch.sum(
            self.amps * torch.cos(self.freqs * tau.unsqueeze(-1) + self.phases), dim=-1
        )

    def forward(self, tau):
        # Use Fourier as the function (f) in t2v
        out = t2v(tau, self.fourier, self.out_features, self.w, self.b, self.w0, self.b0)
        
        # Apply sigmoid activation
        out = self.sigmoid(out)
        
        if self.normalise:
            return out / torch.sum(out, dim=-1)[..., None]
        
        return out


# class T2vFourierFFT(nn.Module):
#     def __init__(self, num_components=200, **kwargs):
#         super().__init__()
#         self.sigmoid = nn.Sigmoid()
#         self.num_components = num_components

#         # Learn complex Fourier coefficients
#         self.fourier_coeffs = nn.Parameter(
#             torch.complex(torch.zeros(num_components), torch.zeros(num_components))
#         )
#         self.reset_parameters()

#     def forward(self, t):
#         # Handle input shape (batch, values, 1)
#         batch_size, seq_len, _ = t.shape

#         # Reshape t to (batch, values)
#         t_reshaped = t.squeeze(-1)

#         # Process first sequence (assuming all sequences in batch are identical)
#         t_first = t_reshaped[0]
#         result = self._compute_fourier(t_first)
#         result = self.sigmoid(result)  # prevent gradient explosion

#         # Replicate for all batches and reshape to match input
#         batched_result = result.unsqueeze(0).expand(batch_size, -1)

#         # Add the trailing dimension to match input shape (batch, values, 1)
#         return batched_result.unsqueeze(-1)

#     def _compute_fourier(self, t):
#         # Get sequence length
#         seq_len = t.shape[0]

#         # Create a zero-padded spectrum with our learned coefficients
#         spectrum = torch.zeros(seq_len, dtype=torch.complex64, device=t.device)

#         # Place coefficients in the correct frequency bins
#         # First coefficient (DC component) at index 0
#         spectrum[0] = self.fourier_coeffs[0]

#         # Positive frequencies at indices 1 to num_components-1 (or up to seq_len//2)
#         pos_freqs = min(self.num_components - 1, seq_len // 2)
#         spectrum[1 : pos_freqs + 1] = self.fourier_coeffs[1 : pos_freqs + 1]

#         # Negative frequencies (conjugate symmetry for real output)
#         for i in range(1, pos_freqs + 1):
#             neg_idx = seq_len - i
#             spectrum[neg_idx] = self.fourier_coeffs[i].conj()  # Complex conjugate

#         # Transform to time domain using inverse FFT
#         time_domain = torch.fft.ifft(spectrum)

#         # Scale the output to match the amplitude range
#         time_domain = time_domain * seq_len

#         # Return the real part (imaginary part should be near zero)
#         return time_domain.real

#     def reset_parameters(self):
#         # Initialize with small random values
#         with torch.no_grad():
#             self.fourier_coeffs.real.normal_(0, 0.01)
#             self.fourier_coeffs.imag.normal_(0, 0.01)


class T2vFourierFFT(nn.Module):
    def __init__(self, in_features, out_features, normalise=True):
        super(T2vFourierFFT, self).__init__()
        self.out_features = out_features
        self.normalise = normalise
        self.sigmoid = nn.Sigmoid()

        # Learnable complex coefficients for frequency-domain features
        self.freq_weights = nn.Parameter(torch.randn(in_features, dtype=torch.cfloat))
        self.bias = nn.Parameter(torch.randn(1, dtype=torch.cfloat))

        # Optional linear term for real output (like v2 in the sine-based version)
        self.w0_real = nn.Parameter(torch.randn(in_features, 1))
        self.b0_real = nn.Parameter(torch.randn(1))

    def forward(self, tau):
        # tau: shape (..., in_features)
        
        # Apply FFT to get frequency-domain representation
        freq = torch.fft.fft(tau, dim=-1)

        # Apply learnable complex weights and bias
        weighted_freq = freq * self.freq_weights + self.bias

        # Inverse FFT to transform back to time-domain
        time_encoded = torch.fft.ifft(weighted_freq, dim=-1).real  # discard imaginary part

        # Concatenate the real and imaginary parts of the frequency domain
        real_part = weighted_freq.real
        imag_part = weighted_freq.imag

        # Final linear projection (optional for output)
        v2 = torch.matmul(tau, self.w0_real) + self.b0_real

        # Concatenate real, imaginary, and additional term
        features = torch.cat([real_part, imag_part, v2], dim=-1)

        # Apply sigmoid
        out = self.sigmoid(features)

        # Optional normalization
        if self.normalise:
            out = out / torch.sum(out, dim=-1, keepdim=True)

        return out
