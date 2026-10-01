---
title: "Beast Didn't Build Cerebro in a Day: The Evolutionary Journey with Claude Managed Agents"
slug: "beast-didnt-build-cerebro-in-a-day-claude-managed-agents"
date: 2026-04-20T21:51:00Z
summary: "When the X-Men go into battle, the world sees Wolverine, Storm, Cyclops. Nobody sees Hank McCoy, the Beast, working on the systems underneath. But he's the one who designed Cerebro. He's the one who keeps the Danger Room…"
tags: ["AI Agents", "Claude", "Prompt Engineering", "Microsoft Fabric", "Data Engineering", "Costs"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/o-fera-n%C3%A3o-construiu-cerebro-em-um-dia-jornada-evolutiva-lopes-fdjqf"
cover:
  image: cover.jpg
  alt: "Beast Didn't Build Cerebro in a Day: The Evolutionary Journey with Claude Managed Agents"
  relative: true
---

### The Scientist Nobody Sees

When the X-Men go into battle, the world sees Wolverine, Storm, Cyclops. Nobody sees Hank McCoy, the Beast, working on the systems underneath. But he's the one who designed Cerebro. He's the one who keeps the Danger Room running. He's the one who makes sure the Xavier Mansion infrastructure can handle any mission, no matter how complex.

Hank doesn't build for the moment. He builds to evolve.

That's the distinction that separates people who use AI agents from people who actually design agentic systems. And it was exactly with that philosophy that Anthropic built **Claude Managed Agents** from
[Anthropic](https://www.linkedin.com/company/anthropicresearch?trk=article-ssr-frontend-pulse_little-mention)
, launched in April 2026.

In simple terms: Managed Agents is infrastructure managed by Anthropic that lets you create autonomous Claude agents without building the whole underlying structure from scratch. Before it, putting an agent into production took months of engineering: containers, state management, authentication, error recovery, memory across sessions. Managed Agents eliminates that work. You define the behavior. Anthropic makes sure it works.

And all of it is configurable directly from the Claude Console, without writing a single line of code.

### Why the Order Matters

The most common mistake people make when they start building agents is jumping straight to complexity. The right evolutionary journey has three stages, and each one has to be solid before the next: well-defined skills, memory across sessions, and an autonomous agent in production.

Skills handle defined, repeatable tasks. Memory turns isolated sessions into accumulated knowledge. The autonomous agent is the result of the two working together. Trying to build the third without the first two is like Hank trying to build Cerebro before understanding how telepathy works.

### Understanding the Two Core Objects

Before building anything, it's essential to understand the distinction between the two main objects in Managed Agents.

The **Environment** is the lab. It defines the container where the agent runs, which packages are installed, which external systems it can reach, and, crucially, where the skill files are stored and persist across sessions. It's the bookshelf of manuals in Beast's lab: the manuals stay there, available to any mission that uses that lab.

![Example of the MCP connection.](img-01.png)

\_Example of the MCP connection.\_

![Example of the Environments screen](img-02.png)

\_Example of the Environments screen\_

The **Agent** is the brain. It defines the model, the system prompt, the available tools, and the skills it will load from the Environment. It's versioned: every update creates a new version with a full history for auditing.

![Example of an Agent](img-03.png)

\_Example of an Agent\_

The relationship between the two is simple: the Environment persists the knowledge. The Agent applies the knowledge. A **Session** is when the two meet to carry out a specific mission.

![Example of Session Creation](img-04.png)

\_Example of Session Creation\_

![Example of Session Execution](img-05.png)

\_Example of Session Execution\_

### Phase 1: Building the Skills

The first step in the Console is to create the Environment at [**console.anthropic.com**](http://console.anthropic.com) **→ Managed Agents → Environments**. Next, create the Agent under **Managed Agents → Agents** with the model, the system prompt, and the skills it will load from the Environment.

**The concrete scenario:** a data team that manages 200 pipelines in Microsoft Fabric. Every day, failures show up, logs need to be analyzed, and incidents need to be documented. Today that eats up hours of the engineering team's time.

The first skills for this agent: revisar-pipeline (review pipeline), which analyzes files and returns a status and risk report. gerar-incidente (generate incident), which formats the report with severity and next steps, always in the same pattern. diagnosticar-erro (diagnose error), which interprets logs and suggests the root cause.

These files are persisted in the Environment. If you tweak a skill, you edit the file and every future session already uses the updated version.

Validate each skill individually before moving on. If Claude hesitates or returns a format different from the one expected, the skill needs refining.

### When a Skill Is No Longer Enough

There are four clear signs that it's time to evolve into an agent with memory:

The context you need is bigger than a single conversation can hold, and the agent needs information from previous sessions. The task involves multiple interdependent steps that require decisions along the way. The volume justifies autonomy, with the team triggering the same skill dozens of times a day. The error repeats because nobody remembered: the skill doesn't learn, but the agent with memory does.

Hank didn't build Cerebro because the attendance list was complicated. He built it because the scale of the mission demanded something no manual process could deliver.

### Phase 2: Adding Memory and Evolving to Multiple Agents

In the Console, when editing the Agent, turn on the **Memory** toggle. Update the system prompt to instruct Claude to check its memory at the start of each session and record what it discovered at the end.

With that instruction, the agent stops starting from zero. By the fifth session, it already spots the timeout on the vendas\_diarias pipeline before checking the log, because it recognizes the pattern. By the twentieth, it automatically includes the historical recurrence in the incident report.

When complexity grows even further, it's time to split responsibilities. In the Fabric scenario with 200 pipelines, a single agent may not be enough. The natural evolution is to create specialized agents: one for monitoring, another for diagnosis, another for report generation. An orchestrator agent receives the goal, delegates to the specialists, and consolidates the results. Each specialist has its own set of skills in the Environment and its own accumulated memory.

That split isn't complexity for complexity's sake. It's the difference between a scientist who does everything alone and a lab with specialists who collaborate.

### Phase 3: Publishing to the Team with Governance

With solid skills and working memory, the agent is ready for the team. And here's the point that changes the adoption equation: **end users don't need a Claude license**. The organization pays for the API through tokens and runtime. Users interact through whatever interface the organization chooses, with no Anthropic account and no Pro plan.

In the Fabric scenario, the most natural way to publish is through **Microsoft Teams** using MCP. Any engineer mentions the agent in the channel, the message arrives as an event, the agent processes it with its skills and memory, and it replies with the formatted report. The engineer gets the diagnosis in two minutes instead of spending an hour analyzing logs.

For other contexts: via **Slack** with the same pattern, via an **internal interface** built by the IT team, or via the **Claude Console** for technical users who need full visibility.

And visibility is the right word. In the Console, the **Sessions** tab records every session with its full history: every tool called, every decision made, every file generated, with a timestamp and cost per session. For a data leader, that answers the question that always comes up in enterprise environments: what did the agent do, why, and when? Auditing isn't an add-on feature. It's part of the architecture.

### What It Costs

Managed Agents charges along two dimensions: tokens consumed at the standard API rates, with Prompt Caching cutting the cost of reused skills and system prompts by up to 90%, and session runtime at $0.08 per hour, charged only while the agent is in **running** status.

In the Fabric scenario with 500 checks a day and 5-minute sessions: 500 × (5/60) × $0.08 = **$3.33/day in runtime**.

The Batch API doesn't apply to Managed Agents. For workloads that don't need state, the standard API with Batch is cheaper. Managed Agents is the right choice when state, memory, and autonomy are required.

### Conclusion: Build to Evolve

Hank McCoy became famous not for the most complex system, but for the most durable one. Cerebro survived decades of missions because every component was validated before being integrated with the next.

Start with the skills in the Environment. Validate each one. Notice when context, volume, or repeated errors signal that it's time to evolve. Add memory. Split into specialists when the mission demands it. Publish via Teams, Slack, or an internal interface.

The engineers on the team will interact with an agent that learns, remembers, and improves. Without knowing what runs underneath. Without needing a Claude license.

The mansion can handle any mission because the infrastructure was built for it. One step at a time.

### References

- *Anthropic. Claude Managed Agents Overview.* [*https://platform.claude.com/docs/en/managed-agents/overview*](https://platform.claude.com/docs/en/managed-agents/overview)
- *Anthropic. Claude Managed Agents: get to production 10x faster.* [*https://claude.com/blog/claude-managed-agents*](https://claude.com/blog/claude-managed-agents)
- *Anthropic. Cloud Environment Setup.* [*https://platform.claude.com/docs/en/managed-agents/environments*](https://platform.claude.com/docs/en/managed-agents/environments)
- *Verdent. Claude Managed Agents Pricing.* [*https://www.verdent.ai/guides/claude-managed-agents-pricing*](https://www.verdent.ai/guides/claude-managed-agents-pricing)
