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

# Google Cloud
Project Proposal

---

- orchestrate a model training pipieline
- integrate with github CI/CD
- setup an endpoint for model inference

![bg left:50% w:600](https://static.wixstatic.com/media/ae2a18_da5e51a6483b46a4add6e7b5f44c4ec2~mv2.jpg/v1/fill/w_640,h_430,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/ae2a18_da5e51a6483b46a4add6e7b5f44c4ec2~mv2.jpg)

---

### Example pipeline

1. Import and preprocess data
2. Train the model
3. Explain results, store relevant artifacts and log metrics
4. Conditionally deploy to an endpoint

![bg left:50% w:600](https://codelabs.developers.google.com/static/vertex-pipelines-intro/img/e2epipeline.png)

---

### Tools and services
- Google Cloud Storage (+gcsfuse)
- Cloud Run + Github
- Pytorch 2.0
- Vertex AI
	- Kubeflow pipielines
	- Model registry
	- [Experiment logs](https://cloud.google.com/vertex-ai/docs/experiments/log-data?hl=en#summary-metrics)