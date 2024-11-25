---
marp: true
# class: invert
theme: uncover
paginate: true
_paginate: false
backgroundColor: white
# style: |
#     section {
#       justify-content: flex-start;
#     }

---

![w:1000](image-16.png)

---

# Contents
- Introduction
- Applications
- Data
- Architecture
- Challenges/limitations

---

# What is SORA?
- SORA means sky in Japanese.
- A text-to-video **multimodal** generative diffusion transformer model by OpenAI (February, 2024)
- **Not** an official technical report
![w:1000](image-17.png)

---

# Emergent properties

<!-- Talk about how multimodality may facilitiate better model performance.
Also mention how the model size impacts the results. -->


![w:700](image-28.png)  ![w:350](image-27.png)


---

![w:900](image-7.png)


---


# Applications

![w:1000](image-18.png)

<!-- If you feel like it doesnt take 5 minutes then append some slides with examples -->

---

# Data

- The main challanges of variable durations, resolutions and aspect ratios
- Traditional methods often resize, crop or adjust the aspect ratios of videos to fit a uniform standard


---

![w:800](image-19.png)

---

<!-- - expand on the PnP
- try to either not mention VAE and also encoder is not the data formatting method -->
### Unified Visual Representation

![w:1200](image-20.png)

---

### Video Compression Network

#### Spatial Patch Compression

- Convert video frames into fixed size patches
- Temporal dimension variability, Pre-trained visual encoders, Temporal information aggregation

---

![w:1000](image-21.png)

---

#### Spatial-Temporal Patch Compression

- Captures dynamic changes across the frames.
- 3D convolution - fixed kernel sizes, strides and output channels
- Since, Sora aims to generate high fidelity videos, a large patch size/ kernel size is used for efficient compression.
- Varying-size patches could also be used but it would compromise the positional embeddings.
- Still a concern how to handle varying number of patches.

---

![w:1200](image-22.png)

---

### Spacetime Latent Patches

- Solution - Patch n' pack
- Enables variable resolution, preserves aspect ratio.
- Addresses two challenges:-
    1. Compact Packing
    2. Token Dropping

---

#### Why It Matters:
- The PNP technique optimizes transformer-based models for variable-length inputs by:

    1. Efficiently handling sequence lengths through compact packing.
    2. Reducing unnecessary computational load by discarding redundant tokens.
    3. Using the fixed sequence lengths necessary for batched operations.

---

![w:1100](image-23.png)

---


# Presumed Architecture
How do the experts think the SORA works?

---

#### Video Compression
> An encoder aims aiming to reduce the dimensionality of input data and output a latent representation that is compressed both temporally and spatially.

![bg left:50% w:600](image.png)

---

#### Variational Autoencoder
![w:1100](image-1.png)

<!-- Sora’s team is expected to train their own compression network with a
decoder (the video generator) from scratch via the manner employed in training latent diffusion models – since this method primarily focuses on spatial patch compression, it necessitates an additional mechanism for aggregating temporal information within the model -->

---

Regular Autoencoder | Variational Autoencoder
-----|:-----:|
![w:350](image-2.png) | ![w:350](image-3.png)

--- 

#### Vision Transformers
<!-- ![w:1000](image-4.png) -->

![bg left:45% w:600](image-5.png)

> The U-ViT architecture for diffusion models, which is characterized by treating all inputs including the time, condition and noisy image patches as tokens and employing skip connections known from U-Net.

---


#### Imagen Video Framework

Allows the system to focus computational resources on producing fine details only where needed, rather than generating high-resolution outputs in a single, computationally expensive pass.

![w:1100](image-6.png)

<!-- 
SSR = spatial super-resolution
TSR = temporal super-resolution
-->

---

![w:1100](image-8.png)

---

# Latent Diffusion Models
1. Convert input into latent representation
2. Perform diffusion
3. Convert back to the regular representation

---

![w:1200](image-9.png)

---

![w:800](image-10.png)

---

![w:1100](image-11.png)

---



# Prompt Engineering
How do we talk with SORA?

---

![w:1100](image-12.png)

---

![w:1100](image-13.png)

---

![w:1100](image-14.png)



---

# Alignment and Learning with Human Feedback

---

![w:1000](image-25.png)

---

<!-- plausible sora approach to RL alignment -->
> Proximal Policy Optimization (PPO) is an algorithm in the field of reinforcement learning that trains a computer agent’s decision function to accomplish difficult tasks. PPO was developed by John Schulman in 2017,had become the default reinforcement learning algorithm at American artificial intelligence company OpenAI.


---

![w:1200](image-26.png)

---

# Final Remarks

---

# Sources
- [SORA](https://arxiv.org/pdf/2402.17177)
- [U-Vit](https://arxiv.org/pdf/2209.12152)
- [Imagen Video](https://arxiv.org/pdf/2210.02303)
- [Latent Diffusion Models](https://arxiv.org/pdf/2304.08818)

---

# End
![](https://user-images.githubusercontent.com/6876788/96633009-d1818000-1318-11eb-9f1d-7f914f4ccb16.gif)

