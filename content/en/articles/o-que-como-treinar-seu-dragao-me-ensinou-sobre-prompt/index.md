---
title: "What How to Train Your Dragon Taught Me About Prompt, Context, Harness, and Loop Engineering"
slug: "how-to-train-your-dragon-prompt-context-harness-loop-engineering"
date: 2026-08-19T13:45:00Z
summary: "On Berk, Vikings solve their dragon problem the only way they know: by force. Hiccup has no force. When he finally comes face to face with a Night Fury, the fastest and most feared dragon of all, the…"
tags: ["AI Agents", "Prompt Engineering", "Microsoft Fabric"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/o-que-como-treinar-seu-drag%C3%A3o-me-ensinou-sobre-prompt-lopes-bcpmf"
cover:
  image: cover.jpg
  alt: "What How to Train Your Dragon Taught Me About Prompt, Context, Harness, and Loop Engineering"
  relative: true
---

### The Boy Who Shouted at the Dragon

On Berk, Vikings solve their dragon problem the only way they know: by force. Hiccup has no force. When he finally comes face to face with a Night Fury, the fastest and most feared dragon of all, the boy discovers that shouting commands doesn't work. Toothless is absurdly powerful and doesn't understand orders.

What Hiccup does from there is what sets the movie apart from every other story about taming beasts. He stops shouting and starts observing. He learns what the dragon perceives: the fish he accepts, the grass that hypnotizes him, how to approach without being a threat. Then he realizes that Toothless can't fly because he lost half his tail, and he builds the solution: a prosthetic tail fin, a saddle, a pedal system. An entire rig around the dragon, calibrated on every test flight. And in the final act of that evolution, Hiccup builds an automatic tail fin that opens and adjusts on its own. Toothless gets the sky without needing the rider on his back.

Shout better. Understand what the other one perceives. Build the rig around it. Get off its back. These four stages have gotten names in AI engineering over the past few months, and they form the progression that explains where the agent market is right now: prompt engineering, context engineering, harness engineering, and loop engineering.

So nobody gets lost, I'll use a single example from start to finish: your company's sales report. The same report, climbing layer by layer.

### Layer 1. Shouting Commands: Prompt Engineering

Prompt engineering is polishing the request. In our example: instead of "make a sales report," you write "generate the first-half sales report with net revenue by month and average ticket by region, in a table, with an executive paragraph at the top." The request got better, and the answer gets better with it.

It was the dominant skill of the early years, and it's still useful. But it has a low ceiling, for the same reason shouting louder didn't make Toothless fly: the problem was never the volume of the order. It was everything the dragon didn't know about you.

### Layer 2. Understanding What the Dragon Sees: Context Engineering

The model answers based on what it sees at that moment. If it doesn't know your tables' schema, your company's official definition of net revenue, and the format of previous reports, the perfect prompt produces a generic report. Context engineering is the discipline of deciding what enters the model's field of view: which files, which documentation, which memories of past interactions and, just as important, what stays out so it doesn't pollute.

In the example: you attach the data dictionary, the KPI calculation rules, and an old report as a format reference. The same prompt as before, now with vision, produces a different quality of answer. Hiccup discovering that Toothless hates eels and loves fish is exactly this: you didn't change the dragon, you changed what it perceives.

In the Microsoft ecosystem, this layer has a name and an address: Fabric. OneLake as the single source of data, semantic models carrying the official definitions of each metric, and Data Agents answering questions grounded in those models. When the net revenue rule lives in the semantic model, you stop attaching it to every conversation: context stops being an attachment and becomes infrastructure.

### Layer 3. The Saddle and the Tail Fin: Harness Engineering

Here the word helps, because a harness is literally the gear you put on an animal. And the scene of Hiccup building the prosthetic tail fin with pedals is the perfect visual definition of the concept.

Harness engineering is designing everything that exists around the model: the tools it can call, the isolated environment where it runs code, the validations that run before and after each action, the permissions for what it can and can't touch. The formula that crystallized the concept came from Mitchell Hashimoto, creator of Terraform, in February 2026, after an OpenAI post about its internal agent infrastructure: agent = model + harness. The model is the brain; the harness is the body, the senses, and the limits. Martin Fowler and Birgitta Böckeler, from Thoughtworks, organized the vocabulary that became the standard: the harness has guides, which steer the agent before it acts, and sensors, which detect and fix problems afterwards.

In the report example: the agent now has a SQL tool to calculate the numbers instead of estimating them, a written protocol with the mandatory quality validations, read permission on the data and no write permission, and a sensor that checks whether row counts reconcile before releasing the result. If you follow this newsletter, you recognized it: skills are harness engineering. Anyone who writes protocols in markdown has been building saddles for months, maybe without using the name.

And on the enterprise side, Microsoft Foundry is exactly this, sold as a managed service: hosted agents with tools, guardrails, observability and, since this year, native skills support in preview, with a versioned API to store protocols centrally and attach them to agents. The agent = model + harness formula became product architecture: you choose the model, Foundry provides the saddle.

The detail that matters: a harness isn't just about safety. A well-built saddle isn't there to tie the dragon down, it's there to help it fly better. A well-designed harness gives the model the right context, the right tool, and the right constraint at the right time, and that's what turns an impressive demo into a reliable system.

### Layer 4. The Automatic Tail Fin: Loop Engineering

Up to this point, you're still on the dragon's back, dictating every flight. The fourth layer is getting off.

Every agent already runs in a cycle: it reasons, acts, observes the result, and decides the next step. Loop engineering, the term that took over conversations starting in June 2026, is designing that cycle on purpose: defining the goal, the verification, and the stopping condition, and letting the system write the prompts for the agent. The spark was a remark by Boris Cherny, creator of Claude Code, saying he no longer prompts directly; he keeps loops running, and it's the loops that decide what to ask the model. Addy Osmani, from Google, named and structured the practice a few days later.

In the sales report example, the change is concrete: instead of you asking for the report every Monday, there's a scheduled loop that ingests the new data, runs the protocol's validations, generates the report, checks the result against the quality rules, and publishes it. If the check fails, the loop tries to fix it; if it can't, that's when it calls you. You stepped out of execution and became the designer of the flight.

Building that flight with Microsoft pieces, the design gets concrete: Fabric's Activator triggers the cycle when new data lands in OneLake, the agent hosted in Foundry runs the protocol with its validations, and the result goes back to Fabric, where the report and the verification trail stay auditable. Fabric is the territory where the dragon flies, Foundry is the saddle, and the loop is the flight plan that connects the two.

Two lessons from this layer that enthusiasts usually skip. First: the bottleneck of the loop is the verifier, not the model. A loop without reliable verification is a dragon flying blind, burning budget convinced it's making progress. Second, and here it's worth recording the warning IBM formalized when defining the discipline: there's a line between delegating execution and giving up critical thinking, which they call cognitive surrender. Stepping out of the execution loop is not stepping out of the judgment loop.

And to prove that layer 4 doesn't require sophistication, the community has a folk example: the Ralph technique, by Geoffrey Huntley, which runs an agent inside a simple while loop, with the same prompt against a written specification, starting over until the work is done. It's named after Ralph Wiggum from The Simpsons because it looks too simple to work. And it works, precisely because the specification and the verification carry the weight.

### What Changes for Data Teams

The progression becomes an honest maturity diagnosis. Most teams I know are somewhere between layers 1 and 2: better and better prompts, more and more organized context. The immediate jump in value is in layer 3, and data teams have an unfair advantage there: governance, validation, and count reconciliation are already our culture; all that changed is where we write the rules. A data quality protocol is a saddle ready to go.

And layer 4 has a prerequisite nobody gets to skip: only automate the cycle for work whose verification you know how to write. Recurring reports with clear quality rules are the perfect candidate for a first loop. Open-ended exploratory analysis, not yet. The criterion isn't what the agent can do on its own, it's what you can verify on your own.

### Conclusion: The Flight

Hiccup's genius was never taming the dragon. It was understanding that Toothless's strength had always been there, and that what was missing was engineering around it: first the eyes, then the saddle, then the tail fin that flies on its own.

With AI, the model's strength is already there too, and it grows with every version. The lever has moved: from writing the perfect request to designing the vision, the rig, and the cycle. Prompt, context, harness, loop. Four layers, one diagnostic question: which one is your team spending energy on, and which one should it be?

The dragon has been ready for a long time. The saddle is your responsibility.

### References

- Martin Fowler / Birgitta Böckeler. Harness engineering for coding agent users. <https://martinfowler.com/articles/harness-engineering.html>
- Addy Osmani. Agent Harness Engineering. <https://addyosmani.com/blog/agent-harness-engineering/>
- IBM. What Is Loop Engineering? <https://www.ibm.com/think/topics/loop-engineering>
- Hugging Face. Harness, Scaffold, and the AI Agent Terms Worth Getting Right. <https://huggingface.co/blog/agent-glossary>
