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
- introduction
- applications
- data
- architecture
- challenges/limitations

---

# What is SORA?
- SORA means sky in Japanese.
- A text-to-video **multimodal** generative diffusion transformer model by OpenAI (February, 2024)
- Not an official technical report
![w:1000](image-17.png)

---

# Emergent properties

<!-- Talk about how multimodality may facilitiate better model performance.
Also mention how the model size impacts the results. -->

![w:900](image-24.png)

---

![w:900](image-7.png)


---


# Applications

![w:1000](image-18.png)

<!-- If you feel like it doesnt take 5 minutes then append some slidees with examples -->

---


# Data
- The main challanges of variable durations, resolutions and aspect ratios
- Improvements over the traditional models
- Video embeddings


---

![w:800](image-19.png)
Traditional methods often resize, crop or adjust the aspect ratios of videos to fit a uniform standard

---


![w:800](image-20.png)
- expand on the PnP
- try to either not mention VAE and also encoder is not the data formatting method


---

![w:800](image-21.png)

---

![w:800](image-22.png)

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

