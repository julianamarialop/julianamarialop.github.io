---
title: "What the Spider-Verse Taught Me About Taking Claude Skills to Microsoft Foundry"
slug: "what-the-spider-verse-taught-me-about-taking-claude-skills-to-foundry"
date: 2026-07-17T17:33:00Z
summary: "The most beautiful premise of Spider-Man: Across the Spider-Verse isn't visual, it's philosophical. In every universe there's a Spider-Man. Miles Morales in one, Gwen Stacy in another, Peter B. Parker in a hoodie in a third, a…"
tags: ["AI Agents", "Claude", "MCP"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/o-que-aranhaverso-me-ensinou-sobre-levar-skills-do-claude-lopes-pwdkf"
cover:
  image: cover.jpg
  alt: "What the Spider-Verse Taught Me About Taking Claude Skills to Microsoft Foundry"
  relative: true
---

### In Every Universe There's a Spider-Man

The most beautiful premise of Spider-Man: Across the Spider-Verse isn't visual, it's philosophical. In every universe there's a Spider-Man. Miles Morales in one, Gwen Stacy in another, Peter B. Parker in a hoodie in a third, a noir Peter in black and white, even a pig named Peter Porker. The suits change, the powers vary in the details, each world's art style is completely different. But there's something that crosses every universe intact: the canon. The bite, the loss, the responsibility. The events that define what it means to be Spider-Man don't belong to any specific universe. They belong to the story.

And the movie holds a second detail, less poetic and more technical. When someone visits a universe that isn't their own, their body starts to fail. Miles in another world suffers glitches: pixels breaking, limbs misaligning, reality rejecting what wasn't written for it. What belongs to the character travels well. What belongs to the home universe doesn't.

Migrating Claude skills to Microsoft Foundry follows exactly that physics. What is canon crosses the portal intact. What is suit has to be re-stitched. And what is glitch you learn to spot before you jump.

### The Canon: The Open Standard

A skill is a SKILL.md file: a YAML header with a name and description, followed by instructions in plain markdown. Anthropic launched Agent Skills in October 2025 and, in December of the same year, published the format as an open standard at agentskills.io. From then on, the story stopped being about a Claude feature and became a story about interoperability: OpenAI's Codex CLI, Google's Gemini CLI and GitHub Copilot adopted the same format. Microsoft itself now maintains entire repositories of skills in this standard, such as MicrosoftDocs/Agent-Skills, with skills that work in any compatible assistant.

That means the protocol you wrote for Claude, with your KPI definitions, your validation rules, your analysis workflow, was born multiversal. The markdown is the canon. It doesn't belong to the platform where it was written.

### A New Universe: Native Skills in Foundry

In 2026 the portal opened on Microsoft's side. Microsoft Foundry began offering, in preview, native support for skills through a versioned Skills REST API. The flow: you author the SKILL.md, store it centrally in Foundry with version control, and attach the skill to toolboxes or hosted agents.

The problem this solves is the same one that motivated skills in Claude, and Microsoft's documentation describes it with surgical precision. Teams building agents accumulate behavioral guidelines that need to be consistent across every conversation: the support agent follows a fixed escalation policy, the code review agent applies the same checklist, the sales agent respects the same messaging constraints. When these guidelines live embedded in each agent's system prompt or code, duplication is born. The policy changes, and you update and redeploy every agent that uses it. The skill decouples the guideline from the code: written once, versioned centrally, inherited by all.

If that description sounds familiar, it's because it's the same governance-as-code argument I've been making here in the newsletter. What's new is that it now holds on both sides of the portal.

### The Migration: What Crosses Intact

In practice, a skill built in Claude has three layers, and each one crosses the portal in its own way.

The first layer is the markdown protocol, and it migrates almost by copy. Business definitions, validation rules, complexity rulers, step-by-step workflows: all of that is canon. At most you adjust the trigger description to the vocabulary of the new environment. If your skill was written as structured knowledge rather than as an automation script, this layer is most of the file.

The second layer is the references to the source runtime, and those need re-stitching. Paths like /mnt/skills, mentions of artifacts, names of Claude-specific tools, orchestration instructions where one skill invokes another by name. None of that exists in the Foundry universe. There, orchestration logic becomes the responsibility of the hosted agent, typically built with Microsoft Agent Framework, LangGraph or a custom framework in Python or C#. The protocol still says what to do; who coordinates the execution changes shape.

The third layer is the code engines that many mature skills carry: deterministic Python scripts for calculation, file generation, validation. These don't cross by copy, they cross by engineering. There are two natural paths: run them inside the containerized hosted agent itself, or expose the engine as an MCP server and let any platform consume it as a tool. MCP, by the way, is the universal bridge in this story: while the skill carries the knowledge, MCP carries the ability to act, and both are open standards that Claude and Foundry speak.

### The Glitch: What Breaks Outside the Home Universe

Miles learns the hard way that his body wasn't written for the wrong universe. With skills, the glitch shows up in the lines that assume the source environment without saying so. Compare:

```
Salve o resultado em /mnt/user-data/outputs e gere
um artifact React com o dashboard.        
```
```
Gere o dashboard no formato interativo disponível
no ambiente e disponibilize o arquivo ao usuário.        
```

The first version works perfectly in Claude and glitches anywhere else. The second crosses universes. The practical lesson: write the protocol in terms of intent and business rules, isolate what's platform-specific in clearly marked sections, and delegate external actions to MCP tools instead of assuming native tools. A portable skill isn't one that avoids the runtime, it's one that knows exactly where the runtime begins.

### What Changes for Data Teams

For those leading architecture, the strategic consequence is bigger than the technical one: the protocol repository becomes a platform-independent asset. A single Git repo with the team's SKILL.md files, versioned with pull requests and an owner, serves Claude today, Foundry tomorrow and whatever comes next. The investment in documenting your domain's rules stops being a bet on a vendor and becomes an asset of the organization. It's the concrete answer to the lock-in question every architecture committee asks.

And the caveats matter, because technical honesty is what separates an article from an ad. Skills support in Foundry is preview: no SLA, not recommended for production. And there's a restriction that weighs heavily in regulated environments: the Skills API doesn't support private networking, so you can't create, manage or download skills in a Foundry resource with public access disabled. For a banking client on a closed network, that's currently an adoption blocker that needs to go into the solution design, not a footnote.

### Availability and Access

In Claude, skills are available on paid plans and, on Team and Enterprise plans, with central admin control over what is provisioned for the organization. In Microsoft Foundry, skills support is in preview and requires an active Foundry project and the Foundry User role on the project, with authoring and management through the Skills REST API. The open standard, with its specification and examples, is published at agentskills.io.

### Conclusion: The Canon Crosses Over

In the Spider-Verse, what makes someone Spider-Man was never the suit, the universe or the art style. It's the canon: the essential story that repeats intact in every world. The suits are re-stitched in each universe. The glitches teach what shouldn't have crossed over.

With skills, the physics is the same. Your domain knowledge written in markdown is the canon, and it now crosses from Claude to Foundry, to Codex, to Gemini CLI, to Copilot. The runtime is the suit, re-stitched on each platform. The paths and native tools are the glitch, and you learn to isolate them before you jump.

Write your protocols as canon. Because in the multiverse of agents taking shape, the question is no longer which platform you're betting on. It's become: what part of your architecture survives the trip between all of them?

### References

- Microsoft Learn. Use skills with Microsoft Foundry agents (preview). <https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills>
- Agent Skills. Open standard specification. <https://agentskills.io>
- Anthropic. Equipping agents for the real world with Agent Skills. <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills>
- MicrosoftDocs. Agent-Skills: Curated Agent Skills for Microsoft & Azure. <https://github.com/MicrosoftDocs/Agent-Skills>
