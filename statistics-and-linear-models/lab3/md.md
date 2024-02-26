Smooth test was introduced by Neyman (1937) to verify simple null hypothesis asserting that observations obey completely known continuous distribution function F. Smooth test statistic (with k components) can be interpreted as score statistic in an appropriate class of auxiliary models indexed by a vector of parameters $theta in R^k, k >= 1$.

Pertaining auxilary null hypothesis asserts $theta=theta_0=0$. Therefore, in this case, the smooth test statistic based on n i.i.d. observations $Z_1,...,Z_n$ has the form $W_k=[1/sqrt(n) sum_i=1^n l(Z_i)]I^-1[1/sqrt(n) sum_i=1^n l(Z_i)]'$,

where $l(Z_i)$, i=1,...,n, is k-dimensional (row) score vector, the symbol ' denotes transposition while $I=Cov_theta_0[l(Z_1)]'[l(Z_1)]$. Following Neyman's idea of modelling underlying distributions one gets $l(Z_i)=(phi_1(F(Z_i)),...,phi_k(F(Z_i)))$ and I being the identity matrix, where $phi_j$'s, j >= 1, are zero mean orthonormal functions on [0,1], while F is the completely specified null distribution function.

In case of composite null hypothesis there is also unspecified vector of nuisance parameters $gamma$ defining the distribution of observations. Smooth statistic (with k components) in such applications is understood as efficient score statistic for some class of models indexed by an auxiliary parmeter $theta in R^k$, k >= 1. Pertaining efficient score vector $l^*(Z_i;gamma)$ is defined as the residual from projection the score vector for $theta$ onto the space spanned by score vector for $gamma$. As such, smooth test is alternative name for $C(alpha)$ Neyman's test. See Neyman (1959), Buhler and Puri (1966) as well as Javitz (1975) for details. Hence, smooth test, based on n i.i.d. variables $Z_1,...,Z_n$ rejects hypothesis $theta=theta_0=0$ for large values of

$W_k^*(tilde gamma)=[1/sqrt(n) sum_i=1^n l^*(Z_i;tilde gamma)][I^*(tilde gamma)]^-1[1/sqrt(n) sum_i=1^n l^*(Z_i;tilde gamma)]'$, where $tilde gamma$ is an appropriate estimator of $gamma$ while $I^*(gamma)=Cov_theta_0[l^*(Z_1;gamma)]'[l^*(Z_1;gamma)]$. More details can be found in Janic and Ledwina (2008), Kallenberg and Ledwina (1997 a,b) as well as Inglot and Ledwina (2006 a,b).

Auxiliary models, mentioned above, aim to mimic the unknown underlying model for the data at hand. To choose the dimension k of the auxilary model we apply some model selection criteria. Among several solutions already considered, we decided to implement two following ones, pertaining to the two above described problems and resulting $W_k$ and $W_k^*(tilde gamma)$. The selection rules in the two cases are briefly denoted by T and $T^*$, respectively, and given by

$T = min1 <= k <= d: W_k-pi(k,n,c) >= W_j-pi(j,n,c), j=1,...,d$

and

$T^* = min1 <= k <= d: W_k^*(tilde gamma)-pi^*(k,n,c) >= W_j^*(tilde gamma)-pi^*(j,n,c), j=1,...,d$.

Both criteria are based on approximations of penalized loglikelihoods, where loglikelihoods are replaced by $W_k$ and $W_k^*(tilde gamma)$, respectively. The penalties for the dimension j in case of simple and composite null hypothesis are defined as follows

$pi(j,n,c)=jlog n, if max1 <= k <= d|Y_k| <= sqrt(c log(n)), 2j, if max1 <= k <= d|Y_k|>sqrt(c log(n)). $

and

$pi^*(j,n,c)=jlog n, if max1 <= k <= d|Y_k^*| <= sqrt(c log(n)),2j if max(1 <= k <= d)|Y_k^*| > sqrt(c log(n))$.

respectively, where c is some calibrating constant, d is maximal dimension taken into account,

$(Y_1,...,Y_k)=[1/sqrt(n) sum_i=1^n l(Z_i)]I^-1/2$

while

$(Y_1^*,...,Y_k^*)=[1/sqrt(n) sum_i=1^n l^*(Z_i; tilde gamma)][I^*(tilde gamma)]^-1/2$.

In consequence, data driven smooth tests for the simple and composite null hypothesis reject for large values of $W_T$ and $W_T^* = W_T^*(tilde gamma)$, respectively. For details see Inglot and Ledwina (2006 a,b,c).

The choice of c in T and $T^*$ is decisive to finite sample behaviour of the selection rules and pertaining statistics $W_T$ and $W_T^*(tilde gamma)$. In particular, under large c's the rules behave similarly as Schwarz's (1978) BIC while for c=0 they mimic Akaike's (1973) AIC. For moderate sample sizes, values c in (2,2.5) guarantee, under ‘smooth’ departures, only slightly smaller power as in case BIC were used and simultaneously give much higher power than BIC under multimodal alternatives. In genral, large c's are recommended if changes in location, scale, skewness and kurtosis are in principle aimed to be detected. For evidence and discussion see Inglot and Ledwina (2006 c).

It c>0 then the limiting null distribution of $W_T$ and $W_T^*(tilde gamma)$ is central chi-squared with one degree of freedom. In our implementation, for given n, both critical values and p-values are computed by MC method.

Empirical distributions of T and $T^*$ as well as $W_T$ and $W_T^*(tilde gamma)$ are not essentially influenced by the choice of reasonably large d's, provided that sample size is at least moderate.

For more details see: http://www.biecek.pl/R/ddst/description.pdf.

