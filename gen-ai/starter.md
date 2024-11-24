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

# Reasoning with Language Model is Planning with World Model

---

# World Model
What is a world model and why is it useful?

---

- predicts the next state after applying an action to the current state
- enforces a more prinicipled planning approach
- both the agent and the world are the same but repurposed LLM

![bg left:50% w:600](https://cdn.discordapp.com/attachments/732346178062254183/1180916124171386920/image.png?ex=657f28d8&is=656cb3d8&hm=6a8a5b7ab7cae84b6d923eecef6788a23a45a1b4e2648484640e6d0daff10b65&)

---
<style scoped>
* {
	font-size: 20px;
}
</style>
### Prompt prefix

```
I am playing with a set of blocks where
I need to arrange the blocks into
stacks. Here are the actions I can
do

Pick up a block
Unstack a block from on top of another
block

Put down a block
Stack a block on top of another block

I have the following restrictions on my
actions:
<restrictions>
```

---
<style scoped>
* {
	font-size: 20px;
}
</style>
### Agent few-shot

```
[STATEMENT]
As initial conditions I have that, the
orange block is clear, the yellow
block is clear, the hand is empty,
the blue block is on top of the red
block, the orange block is on top
of the blue block, the red block is
on the table and the yellow block
is on the table.
My goal is to have that the blue block
is on top of the red block and the
yellow block is on top of the
orange block.

My plan is as follows:

[PLAN]
pick up the yellow block
stack the yellow block on top of the
orange block
[PLAN END]
```

---
<style scoped>
* {
	font-size: 20px;
}
</style>
### World few-shot
```
[SCENARIO 1]
[STATE 0] I have that, the white block
is clear, the cyan block is clear,
the brown block is clear, the hand
is empty, the white block is on top
of the purple block, the purple
block is on the table, the cyan
block is on the table and the brown
block is on the table.
[ACTION] Pick up the brown block.
[CHANGE] The hand was empty and is now
holding the brown block, the brown
block was on the table and is now
in the hand, and the brown block is
no longer clear.
[STATE 1] I have that, the white block
is clear, the cyan block is clear,
the brown block is in the hand, the
hand is holding the brown block,
```


---

# Monte Carlo Tree Search
How to reason with a world model?
![bg 100%, opacity:0.3](https://www.cs.us.es/~fsancho/Blog/posts/img/chessmcts.gif)

---

![w:1100](https://media.discordapp.net/attachments/732346178062254183/1180945323749810346/image.png?ex=657f440a&is=656ccf0a&hm=682dd69f969c23a16306df8c2af3bfb6f4c6ceb016bb886f81cff083d6bc78c1&=&format=webp&quality=lossless&width=2881&height=1248)


![w:500](https://media.discordapp.net/attachments/732346178062254183/1180954073428656208/image.png?ex=657f4c30&is=656cd730&hm=a2456f554eddfe4e50a05621c957a8eadb7e01bd5ac870f82933c0c5bda73bc5&=&format=webp&quality=lossless&width=2073&height=453)

---
<style scoped>
* {
	font-size: 20px;
}
</style>
![w:800](https://cdn.discordapp.com/attachments/732346178062254183/1180914667317641277/image.png?ex=657f277d&is=656cb27d&hm=bfd1781d73ab5e94f1f09c8c40ca1f5280adff4ebf1f91113086d692eeef8887&)

> Planning, a central ability in intelligent agents, involves generating a series of actions to achieve a specific goal

---
<style scoped>
* {
	font-size: 20px;
}
</style>

# Reward design

Table on GSM8k benchmarking
![w:600](https://media.discordapp.net/attachments/732346178062254183/1180981581704339587/image.png?ex=657f65ce&is=656cf0ce&hm=f20647dadcff495e0a81c5d6ddeabfe7cf766a2fba567981ce4cb3af7ada5ea6&=&format=webp&quality=lossless&width=2124&height=746)

- **State confidence** (R1)
	*the empirical probability of the state's validity*

- **Likelihood** (R2)
	*likelihood of an action being chosen by the agent*

- **Self-evaluation** (R3)
	*model's confidence in the reasoning step*

- **Heuristics**

---

### Examples
![w:1200](https://media.discordapp.net/attachments/732346178062254183/1180940074028904518/image.png?ex=657f3f26&is=656cca26&hm=d66aaaf7668d111070a48b1384a0e97e600b0a8304c45206747de27b668ce7f7&=&format=webp&quality=lossless&width=2881&height=1170)

---

![bg w:1100](https://media.discordapp.net/attachments/732346178062254183/1180958127265423571/image.png?ex=657f4ff6&is=656cdaf6&hm=2d1150e19c9de95003f3aa96bb69ad26ab1013116743c13a1a2a890e4f54c187&=&format=webp&quality=lossless&width=2881&height=1215)

---

# Results

![bg opacity:0.55](https://media.discordapp.net/attachments/732346178062254183/1180969110218227794/iStock-884076090.jpg?ex=657f5a31&is=656ce531&hm=85fccd1c92687986c3a3ff58bb98c0c400de15ed605b257cf72c3b5bc3d2166a&=&format=webp&width=2497&height=1560)

---
<style scoped>
* {
	font-size: 20px;
}
</style>

Blockworld | Math (GSM8k) | Logic (ProntoQA)
-----|:-----:|------
![w:350](https://media.discordapp.net/attachments/732346178062254183/1180961364378918952/image.png?ex=657f52fa&is=656cddfa&hm=8c300a0f737ae84bf63591e0baebc35c99585e329cc9d17d44111e43d29a9121&=&format=webp&quality=lossless&width=2183&height=1037) | ![w:350](https://media.discordapp.net/attachments/732346178062254183/1180962326191550534/image.png?ex=657f53df&is=656cdedf&hm=789cdbb8d5b5bbb10b8ef623961733fb1fe899ee1ef841e909ae63db0e5dc2c8&=&format=webp&quality=lossless&width=1841&height=1297) | ![w:350](https://media.discordapp.net/attachments/732346178062254183/1180962576394375208/image.png?ex=657f541b&is=656cdf1b&hm=72a7ae763c53909ef86d85af77a9bed6788732a4db04cf888e74fd0401e93428&=&format=webp&quality=lossless&width=1837&height=748)


*The model used by authors is LLaMA-33B.
All figures refer to the success frequency.
The superscripts indicate the number of samples or iterations.*

---
<style scoped>
* {
	font-size: 20px;
}
</style>
![w:1000](https://cdn.discordapp.com/attachments/732346178062254183/1180983754391556116/image.png?ex=657f67d4&is=656cf2d4&hm=72ef9588a5fcb7732b25d056deb8cfa6c6adc21f1f371d087e5c45c026d4ecc7&)

Chain of Thoughts drops of significantly with time in comparison to RAP.


---
<style scoped>
* {
	font-size: 20px;
}
</style>

![w:500](https://media.discordapp.net/attachments/732346178062254183/1180970804595400815/image.png?ex=657f5bc5&is=656ce6c5&hm=1106960106be27bce3e0a5589e25844d76957df00106a6704546e62b9219871c&=&format=webp&quality=lossless&width=1989&height=1560)

The reward used is a geometric mean of state confidence and self evaluation.

---

# Tree search algorithms
Can we do better?

---

![bg fit](https://cdn.discordapp.com/attachments/732346178062254183/1180938577236987944/image.png?ex=657f3dc1&is=656cc8c1&hm=69cdc574b53233640518d18942a7f64e624ef0e63ca9003fb3ddbaffb315f1fe&)

---
<style scoped>
* {
	font-size: 10px;
}
</style>
Methods comparison on coding dataset HumanEval
![w:600](https://cdn.discordapp.com/attachments/732346178062254183/1181252194188673064/image.png?ex=658061d5&is=656decd5&hm=94db102699f94b77508835d0343b00855108e23d461c7f0734fcdcf829ad8671&)

![w:600](https://cdn.discordapp.com/attachments/732346178062254183/1181256593535410269/image.png?ex=658065ee&is=656df0ee&hm=984b0d8cc96b506e9b1e9f59e4d939d1da3295f2bde8f18a4b9a6af479abc095&)
[*Language agent tree search unifies reasoning acting and planning in language models](https://arxiv.org/pdf/2310.04406.pdf)

---

### Self-Refine
![w:1000](https://media.discordapp.net/attachments/732346178062254183/1181261204233146478/image.png?ex=65806a39&is=656df539&hm=a837116248974066ac1550936e5d77b3bcceddbedee6c6d468dc4be063388947&=&format=webp&quality=lossless&width=2465&height=1284)

---

### Decision-making
![w:1000](https://media.discordapp.net/attachments/732346178062254183/1181262906264932445/image.png?ex=65806bcf&is=656df6cf&hm=60a5500fa8d3a67e7be542541661d239b11288cf721270de99a4f04901e70030&=&format=webp&quality=lossless&width=2881&height=1109)

---
<style scoped>
* {
	font-size: 20px;
}
</style>

![w:800](https://media.discordapp.net/attachments/732346178062254183/1181253617362145381/image.png?ex=65806329&is=656dee29&hm=1293f2dcd6b31a5541bb979de7f115ef0f7b3dfaadf55bd741982b9930e33778&=&format=webp&quality=lossless&width=2881&height=1409)


> **Reflection**. Upon encountering an unsuccessful terminal node, the model is prompted with the trajectory and final reward to provide a verbal self-reflection that summarizes the errors in the reasoning or acting process and proposes superior alternatives. We store both failed trajectories and corresponding reflections in the memory. In sub-sequent iterations, these are integrated as additional context to the agent. This imparts a semantic gradient signal more useful than a scalar value, enabling the agent to learn from trial and error without the cost of expensive optimization processes such as reinforcement learning.

---

![bg fit](https://github.com/Ber666/llm-reasoners/raw/main/images/image.png#pic_center)

---

# End
