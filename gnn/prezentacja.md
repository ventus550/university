---
marp: true
# class: invert
theme: uncover
paginate: true
_paginate: false
backgroundColor: white
math: katex


# style: |
#     section {
#       justify-content: flex-start;
#     }


---

# Link Prediction

---

# Link prediction methods

---

![bg left:40%](https://media.discordapp.net/attachments/732346178062254183/1300174252473061577/file-2nzvfNZEY3szDOJQora8wRKS.png?ex=671fe121&is=671e8fa1&hm=d6a07b18b88c1bbcbc56261eace7cb942538e8ef8a62b844023cac47058cb721&=&format=webp&quality=lossless&width=396&height=396)

- **Friend Suggestions**
Predicts potential connections based on mutual friends and shared interests.
- **Fraud Detection**
Identifies suspicious patterns, such as clusters of fake profiles
that attempt to connect to real users.

---

![bg left:40%](https://media.discordapp.net/attachments/732346178062254183/1300175862469234698/file-vQWy9eTYx3haZW7ZfpBVIObx.png?ex=671fe2a1&is=671e9121&hm=3b0a1a5c7636a5a950a1ad55f11e1650dbb904e286b25d43a90e781d6067cba3&=&format=webp&quality=lossless&width=396&height=396)

- **Product Recommendations**
Suggests items based on previous purchases and browsing history.
- **Personalized Experience**
Enhances user engagement by predicting relevant content.

---

![bg left:40%](https://media.discordapp.net/attachments/732346178062254183/1300176092585263307/file-BP69KPgBszQsW0jHgxcN6ZX9.png?ex=671fe2d8&is=671e9158&hm=8fc0ca6b21f769ef808b9551289a1b8e3d4f4208f1ac46aa808e769bd895522d&=&format=webp&quality=lossless&width=396&height=396)

- **Protein Interactions**
Predicts potential interactions between proteins, aiding in functional discovery.
- **Genetic Disease Understanding**
Assists in understanding genetic diseases by predicting gene-gene interactions.

---

# Traditional Methods
<!-- In order to better understand the role of GNNs let us first examine the traditional approaches to the link prediction problem. -->

---
<style scoped>section{font-size:30px;}</style>
<!-- We will explore the three most prominent categories -->
##  Categories of link prediction methods

- **Heuristic methods**
	use simple node similarity scores as the likelihood of links

- **Embedding (latent-feature) methods**
	produce latent representations of nodes using a variety of optimization algorithms

- **Content-based methods**
	use node-only features, disregarding the graph structure

---

## Local heuristics
This class of heuristics considers only the local subgraphs of the nodes in question.
![w:1000](https://media.discordapp.net/attachments/732346178062254183/1300183745390841866/image.png?ex=671fe9f9&is=671e9879&hm=377135a5883ff750aa17116988d9f68ea9f8f1937e8e8b461954011046edb3c0&=&format=webp&quality=lossless&width=1305&height=353)

Here $\Gamma(x)$ denotes the neighbours of x.

---

## Global Heuristics
These heuristics, also known as high order heuristics, make their judgement based on the entire network.

---
<style scoped>section{font-size:20px;}</style>

<!-- ![bg 100%](image.png) -->
# Rooted PageRank
Let $\pi_x$ be a stationary distribution representing the long-term behavior of a random walker on a graph that following a set of rules:

- move to one of its neighboring nodes with probability $\alpha$ 
- return to $x$ with probability $1-\alpha$ 

Therefore, $[\pi_x]_y$ essentially estimates how likely it is to reach node $y$ from node $x$, which can be interpreted as the strength or likelihood of a connection (link) from $x$ to $y$.

![alt text](image-13.png)


---
<style scoped>section{font-size:30px;}</style>

### Heuristic limitations
![bg left:50% w:90%](image-1.png)

- Most heuristics only work for homogeneous graphs
- Work well only when the network formation aligns with the heuristic
- They only capture a small subset of all possible structure patterns

---

## Embedding methods
The second class of traditional link prediction methods, known as embedding methods (or latent-feature methods), compute hidden node representations. These features, derived from network structures like adjacency or Laplacian matrices, are not directly interpretable.

---
<style scoped>section{font-size:20px;}</style>

# Matrix Factorization
Matrix factorization decomposes the observed adjacency matrix $A$ into the product of a low-rank latent-embedding matrix $Z$ and its transpose, allowing for the edges reconstruction:
![alt text](image-14.png)
The latent embeddings are learned by minimizing the mean-squared error between the reconstructed and true adjacency matrices:
![alt text](image-16.png)

<!-- Variants of matrix factorization include using powers of A -->
<!-- One can also use other node similarity matrices to A -->

---

### DeepWalk
![bg 100%](image-3.png)

---

### Comparison?

---

### Content-based methods
> Content-based methods leverage explicit content features associated with nodes for link prediction (...) However, they usually have worse performance than heuristic and latent-feature methods (...) Thus, they are usually used together with the other two types of methods.

---

# GNN Methods
Can graph neural network compete with the other methods?

---

##  Link prediction paradigms

- **Node-based**
	aggregate the pairwise node representations learned by a GNN as the link representation

- **Subgraph-based**
	extract a local subgraph around each link and use the subgraph representation learned by a GNN as the link representation.

---
<style scoped>section{font-size:20px;}</style>

# Graph Convolutional Network (GCN)
![w:1000](image-5.png)
The convolution is neighbourhood aggregation and resembles that of the regular convolutional networks if we think of the closest pixels as a neighbourhood subgraph.

---
<style scoped>section{font-size:20px;}</style>

# Graph AutoEncoder (GAE)
<!-- Let us consider Graph AutoEncoder (GAE) based on a Graph Convolutional Network (GCN). -->
![alt text](image-6.png)
Such node-based model is trained to minimize the binary cross entropy between the true adjacency matrix and its reconstruction.

![alt text](image-7.png)
- Identity matrix may be substituted for X should there be no node feature data to consider.
- The probability of there being a link is defined as a sigmoid of the similarity between the representations of the two considered nodes with respect to their dot product.
- In practice, the loss from existing edges is usually upscaled by the ratio between the existing and missing edges to balance out the data.

---
<style scoped>section{font-size:20px;}</style>

# Variational AutoEncoders (VAEs)
Variational AutoEncoders are a bayesian inference approach to data generation. We presuppose the existance of a some hidden variable $z$ which generates an observation $x$ and we would like to compute $p(z|x)$.
![alt text](image-8.png)
This is troublesome to compute and so we approximate the $p(z|x)$ with $q(z|x)$ and minimize
![alt text](image-9.png)

---

![w:1000](image-10.png)

---

![w:800](image-11.png)

---
<style scoped>section{font-size:20px;}</style>

# Variational Graph AutoEncoder (VGAE)

![w:1000](image-12.png)
Just like in GAE a GCN encoder and a simple dot product decoder are proposed.

---


# SEAAAL

---



# End
