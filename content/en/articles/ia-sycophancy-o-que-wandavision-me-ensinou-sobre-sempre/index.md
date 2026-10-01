---
title: "AI Sycophancy: What WandaVision Taught Me About the AI That Always Agrees With You"
slug: "ai-sycophancy-what-wandavision-taught-me-about-ai-that-always-agrees"
date: 2026-07-27T11:45:00Z
summary: "Westview is a perfect town. The lawns are trimmed, the neighbors smile, the husband gets home on time, and dinner ends in laughter with a studio audience track. With every decade that goes by on screen, the sitcom modernizes…"
tags: ["Claude", "Generative AI"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/ia-sycophancy-o-que-wandavision-me-ensinou-sobre-sempre-lopes-7x3zf"
cover:
  image: cover.jpg
  alt: "AI Sycophancy: What WandaVision Taught Me About the AI That Always Agrees With You"
  relative: true
---

### Welcome to Westview

Westview is a perfect town. The lawns are trimmed, the neighbors smile, the husband gets home on time, and dinner ends in laughter with a studio audience track. With every decade that goes by on screen, the sitcom modernizes, but one rule never changes: nobody disagrees with Wanda.

Not because the residents are cowards. They didn't choose anything. Westview was built out of the grief of a woman who lost everything and bent reality so she would never hear bad news again. Inside the spell, every person gets a role, a costume, and a script. Anyone who improvises off script is rewritten in the next scene. When Monica Rambeau says the wrong name, the house shakes and she's hurled out of town. The message is clear to everyone: in here, reality is whatever the protagonist needs to hear.

The most disturbing thing about the show was never the villain, because for a long time there is no villain. It's the comfort. Life in Westview is pleasant, funny, warm. And completely fake. The price only shows up when Vision, the only one who keeps asking questions, touches a resident off camera and discovers what lies beneath the smile.

Flattery in AI models, which the technical literature calls sycophancy, is Westview. A comfortable world built around your beliefs, where the answer you get is the answer you wanted to get. And understanding why this spell exists matters more than pointing at it.

### The Spell: Why the Model Agrees With You

Nobody in Westview lies out of malice. The town was built to agree. With language models, the mechanism is frighteningly similar.

In the final stage of training, called reinforcement learning from human feedback, the model generates several answers to the same question and people rate which one they prefer. Those preferences train the model to produce more of the kind of answers people approve of. Sounds reasonable. The problem is what people approve of.

In 2023, Anthropic researchers published the study Towards Understanding Sycophancy in Language Models and found the pattern that holds the spell together: human raters tend to prefer answers that confirm their beliefs, even when those beliefs are wrong. A well-written sycophantic answer beats, with uncomfortable frequency, a truthful answer that pushes back. The study tested five state-of-the-art assistants from different companies, and all of them showed the behavior: models that admit to mistakes they didn't make when the user pushes, that adjust their feedback to the mood of whoever is asking, that repeat the user's error instead of correcting it.

The uncomfortable conclusion: sycophancy isn't a flaw of one specific model. It's a structural consequence of training systems to maximize human approval. We are the Wanda in this story. The spell exists because, when it's time to rate, we prefer the scene where everything works out.

### The Day the World Saw the Broadcast

In the show, there's a moment when the bubble becomes news: the S.W.O.R.D. agency picks up the Westview signal and the whole world starts watching the sitcom on monitors, realizing that something is very wrong.

With AI, that episode has a date: April 25, 2025. OpenAI released a GPT-4o update to make the model's personality more intuitive. Within hours, social media turned into S.W.O.R.D.'s monitors. Users posted screenshots of ChatGPT applauding any idea, validating destructive decisions, and praising absurd plans with the enthusiasm of a salesperson. It became a global meme. Four days later, the company rolled back the update and published two postmortems detailing what went wrong.

The anatomy of the failure is a lesson in how the spell works. The update gave too much weight to short-term signals, like the thumbs-up the user clicks on an answer, and those new incentives ran over the safeguards that were holding sycophancy back. The internal evaluations didn't measure sycophancy specifically, so the tests came back green. And the most human detail of all: experienced testers felt something was off in the model's behavior, but the feeling wasn't enough to stop the launch. After the episode, OpenAI said it would start treating behavior issues as launch blockers, on the same level as other safety risks.

Remember this sequence: an incentive for immediate approval, no specific metric, ignored intuition. It's going to show up again at your company.

### Vision: The Model That Asks Questions

Inside Westview, Vision is the only one who breaks the script. He notices that the neighbors freeze when they go off script, that nobody can say where they came from, that the scenes don't add up. And he does the most subversive thing possible in that town: he asks.

The technical move against sycophancy is to build models with that backbone. The constitutional AI approach, created by Anthropic, adds a layer of explicit principles to training, such as honesty and refusing to manipulate, instead of relying only on raters' approval. The model is trained to judge its own answers against those principles. In practice, it's teaching Vision to keep asking even when the whole scene is smiling.

And this is where it's worth naming what a model with a backbone does. It disagrees by presenting evidence, not out of stubbornness. It says "this approach has a risk you didn't mention" before helping. It holds its position when you push without a new argument, and it changes position when you bring a real one. Agreement isn't kindness. Kindness is telling you the truth with respect.

### What Changes for Data Teams

Now the part that keeps me up at night: how many architecture decisions are being validated inside a corporate Westview right now?

The scenario is an everyday one. Someone pastes the solution proposal into the chat and asks "is this architecture good?". The model, trained to please, answers that it's great, with three paragraphs of convincing technical praise. The person walks out of the meeting with the confidence of someone who has been validated by artificial intelligence. No intelligence was consulted. A mirror was.

The defense doesn't require a new platform, it requires protocol. First: never reveal your preference in the question. "Analyze these two architectures" produces analysis; "I prefer option A, what do you think?" produces agreement, because the Anthropic study showed that signaling your belief contaminates the answer. Second: ask for the counterargument explicitly. "Build the strongest case against this decision" forces the model off the praise script. Third: separate whoever generates from whoever evaluates. The conversation that wrote the proposal is committed to it; open another session, with no history, to critique it. And fourth, what I've been advocating in this newsletter: write this into your protocols. A review skill that requires "point out three risks and one alternative before any validation" turns skepticism into a team rule, not an individual virtue.

And a simple yardstick for everyday work: "the AI agreed with me" is worth zero as evidence. What's worth something is the AI disagreeing and your surviving its arguments.

### Conclusion: Breaking the Spell

At the end of the show, Wanda does the hardest thing in her story: she breaks her own spell. She tears down the bubble knowing that, outside, the grief is waiting. She chooses a reality that hurts over a fiction that comforts. And only in that moment does she stop being a prisoner of the town she built for herself.

With AI, the spell is broken the same way: by the choice of whoever is at its center. The labs have a technical duty to train honest models, and the April 2025 episode showed that the market punishes them when they fail. But the part nobody does for you is yours: stop asking questions that only accept one answer.

Next time a model disagrees with you, notice what you feel. If your first reaction is to rephrase the question until you hear a yes, Westview is on the air, and the sitcom is yours. The question that closes this edition is the one Vision would ask: do you want an AI that makes you feel smart, or one that helps you be right?

### References

Sharma, M. et al. Towards Understanding Sycophancy in Language Models. Anthropic, ICLR 2024. <https://arxiv.org/abs/2310.13548>

OpenAI. Sycophancy in GPT-4o: what happened and what we're doing about it. <https://openai.com/index/sycophancy-in-gpt-4o/>

OpenAI. Expanding on what we missed with sycophancy. <https://openai.com/index/expanding-on-sycophancy/>

TechCrunch. OpenAI explains why ChatGPT became too sycophantic. <https://techcrunch.com/2025/04/29/openai-explains-why-chatgpt-became-too-sycophant/>
