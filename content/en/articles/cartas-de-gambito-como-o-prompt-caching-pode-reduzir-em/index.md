---
title: "Gambit's Cards: How Prompt Caching Can Cut the Cost of Your Claude Solutions by Up to 90%"
slug: "gambits-cards-how-prompt-caching-can-cut-claude-costs-by-up-to-90"
date: 2026-05-05T15:02:00Z
summary: "Imagine that every time you start a meeting, the assistant reads all the company rules out loud before getting started. Two hundred pages. Every day. In every meeting. Even though everyone already knows what's written there."
tags: ["Costs", "Prompt Engineering", "Claude", "AI Agents", "Microsoft Fabric"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/cartas-de-gambito-como-o-prompt-caching-pode-reduzir-em-lopes-mfwpf"
cover:
  image: cover.jpg
  alt: "Gambit's Cards: How Prompt Caching Can Cut the Cost of Your Claude Solutions by Up to 90%"
  relative: true
---

### The Invisible Cost of Every Call

Imagine that every time you start a meeting, the assistant reads all the company rules out loud before getting started. Two hundred pages. Every day. In every meeting. Even though everyone already knows what's written there.

Sounds absurd. But it's exactly what happens in most AI solutions built with Claude via the API. On every call, the same context, the same instructions, the same reference documents are sent and reprocessed from scratch. As if Claude had never seen them before.

The cost of this doesn't show up as a single line item on the bill. It builds up silently, call after call, until it becomes a number nobody can explain.

There's a solution. And it has everything to do with the way Gambit plays his cards.

### The Mutant Who Never Wastes Energy

Gambit isn't the strongest of the X-Men. He doesn't have Wolverine's adamantium, Xavier's telepathy or Storm's weather control. What he has is something rarer: the ability to charge any object with kinetic energy and release it at exactly the right moment, with no waste.

He doesn't recharge a card that's already charged. He doesn't spend new energy on what has already been processed. Every joule is applied once, with precision, and reused as much as possible before being discarded.

That's exactly how **Prompt Caching** in the Claude API works.

In any solution built with Claude via the API, the biggest source of invisible cost isn't the response Claude generates. It's the context you send on every call: the system prompt with the business rules, the document being analyzed, the conversation history. All of it is reprocessed from scratch on every request, as if Gambit recharged every card before every play.

Prompt Caching fixes that. You load the context once, it gets stored, and on the following calls Claude reads from the cache at a fraction of the original cost. The card is already charged. Just play it.

### The Problem Nobody Sees on the Bill

To understand the impact of Prompt Caching, you need to understand how the Claude API works under the hood.

The Claude API is **stateless**: each call is processed from scratch, with no memory of previous ones. That means if you have a 5,000-token system prompt describing your solution's business rules, those 5,000 tokens are sent and reprocessed on every call.

Imagine a customer service solution that handles 10,000 conversations a day. In each conversation, the 5,000-token system prompt is reprocessed. That's 50 million input tokens of repeated context alone, every day, paid at the same rate as new tokens.

Or imagine a document analysis agent that reads a 50,000-token contract and answers ten different questions about it. Without caching, the contract is reprocessed ten times. With caching, it's processed once and read nine times at 10% of the cost.

Gambit doesn't throw the same cards again from scratch. He keeps the ones that are already charged and uses energy where it hasn't been applied yet.

### How Prompt Caching Works in Practice

The mechanism is straightforward. When the engineering team makes the first API call with a content block marked for caching, Anthropic processes and stores that content. On subsequent calls that use the same content, Claude reads from the cache instead of reprocessing.

The pricing structure reflects exactly that behavior:

The **first call**, which creates the cache, costs 1.25x the normal input token price for a 5-minute cache, or 2x for a 1-hour cache. That's the cost of charging the card.

The **following calls**, which read from the cache, cost only 10% of the normal input token price. That's the cost of reusing the already charged card.

Break-even is immediate: with a 5-minute cache, the second call already pays for the write cost and starts generating savings. With a 1-hour cache, savings start on the third call.

In practice, for an agent that receives 100 calls with the same 10,000-token system prompt using Claude Sonnet 4.6:

Without cache: 100 calls × 10,000 tokens × $3/MTok = **$3.00** With cache: 1 write (12,500 tokens × $3/MTok = $0.038) + 99 reads (10,000 tokens × $0.30/MTok = $0.297) = **$0.34**

An **88% reduction in input cost** with an implementation change that takes less than an hour.

### What It Looks Like in Code: The Minimum the Team Needs to Implement

If you're going to hold the engineering team accountable for this, it's important to understand what the implementation involves. It's a small, surgical change: adding the cache\_control parameter to the content block that should be cached.

Here's the difference between a call without cache and one with cache for a Microsoft Fabric pipeline monitoring agent:

**Without cache: context reprocessed on every call:**

```python
import anthropic

client = anthropic.Anthropic()

# System prompt com regras do agente: reprocessado em CADA chamada
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="""Você é um agente de monitoramento de pipelines do Microsoft Fabric.
    Analise o status reportado e classifique a severidade seguindo estas regras:
    - CRÍTICO: pipeline com falha que afeta dados de produção em Gold
    - ALTO: pipeline com falha em Silver com impacto em relatórios
    - MÉDIO: pipeline com falha em Bronze sem impacto imediato
    - BAIXO: alertas de performance sem falha confirmada
    Sempre inclua: severidade, diagnóstico provável e próximo passo recomendado.""",
    messages=[
        {"role": "user", "content": f"Status do pipeline: {status_pipeline}"}
    ]
)        
```

**With cache: system prompt loaded once, reused on the rest:**

```python
import anthropic

client = anthropic.Anthropic()

# System prompt cacheado: processado apenas na primeira chamada
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": """Você é um agente de monitoramento de pipelines do Microsoft Fabric.
            Analise o status reportado e classifique a severidade seguindo estas regras:
            - CRÍTICO: pipeline com falha que afeta dados de produção em Gold
            - ALTO: pipeline com falha em Silver com impacto em relatórios
            - MÉDIO: pipeline com falha em Bronze sem impacto imediato
            - BAIXO: alertas de performance sem falha confirmada
            Sempre inclua: severidade, diagnóstico provável e próximo passo recomendado.""",
            "cache_control": {"type": "ephemeral"}  # ← essa linha ativa o cache
        }
    ],
    messages=[
        {"role": "user", "content": f"Status do pipeline: {status_pipeline}"}
    ]
)

# Verificando se o cache está funcionando
uso = response.usage
print(f"Tokens escritos no cache: {uso.cache_creation_input_tokens}")
print(f"Tokens lidos do cache: {uso.cache_read_input_tokens}")        
```

The difference is one line: "cache\_control": {"type": "ephemeral"}. The rest of the logic doesn't change. For the engineering team, this is one of the highest-return, lowest-effort optimizations in the Claude ecosystem.

### A Real Case: Data Quality Agent on Fabric

To make the impact concrete, consider a data quality agent built on Microsoft Fabric. It monitors Silver layer tables, detects anomalies and generates alerts for the data team.

The agent has an 8,000-token system prompt with the quality rules, acceptable thresholds by data domain, naming standards and the expected alert format. It runs 500 checks a day, one for each monitored table.

**Without Prompt Caching:** 500 calls × 8,000 tokens × $3/MTok = **$12.00/day = $360/month** in repeated context alone.

**With Prompt Caching:** 1 write (10,000 tokens × $3/MTok = $0.03) + 499 reads (8,000 tokens × $0.30/MTok = $1.197) = **$1.23/day = $36.90/month**

A savings of **$323/month** with one line of code added to the system prompt. Over a year, that's more than $3,800 saved on a single agent.

And that's a conservative scenario. Higher-volume agents, with longer system prompts or that process long documents, see proportionally bigger savings.

### What Can and Can't Be Cached

Gambit knows not every object is worth charging. Cards that are too small don't build up enough energy to justify the move. The same reasoning applies to Prompt Caching.

**Ideal candidates for caching:**

The **system prompt** is the most obvious candidate. If the solution has a fixed set of instructions, business rules or personas that go with every call, that content should be cached. It never changes between calls, but it's reprocessed on every one of them.

**Reference documents** are another powerful candidate. An agent that analyzes technical specifications, data contracts or API documentation can cache that content and ask multiple questions without reprocessing it for each question.

**Tool definitions** in agentic systems with many tools also benefit. If the agent has 20 tools defined and uses only 3 on each call, caching all the definitions avoids constant reprocessing.

**When caching doesn't pay off:**

Content that changes on every call can't be cached efficiently. If the context varies significantly between requests, there's no cache hit and you pay the write cost without the read benefit.

Content also has to be at least **1,024 tokens** to be eligible for caching on Sonnet and Haiku models. Smaller blocks are processed normally with no error, but without caching.

### How an Architect Should Hold the Team Accountable

You don't need to implement Prompt Caching yourself. But you do need to know when to require it and how to validate that it's working.

**The right questions for the engineering team:**

"Is the solution's system prompt being cached?" This is the most basic question. If the answer is no, or if the team can't answer, there's an immediate opportunity to cut costs.

"What's the ratio of cache hits to cache misses in production calls?" The API returns cache metrics in every response: cache\_creation\_input\_tokens for writes and cache\_read\_input\_tokens for reads. A dashboard monitoring that ratio is the bare minimum expected of any solution in production.

"What TTL is configured: 5 minutes or 1 hour?" For solutions with a high volume of calls in short windows, the 5-minute cache is usually enough and cheaper to write. For solutions with spaced-out peaks, the 1-hour cache ensures the context stays available between peaks.

**The sign that caching isn't working:**

If the cost per call doesn't drop as volume grows, the cache probably isn't active or is being invalidated. In a healthy solution with Prompt Caching, the marginal cost of each additional call should drop progressively as the cache is reused.

### Prompt Caching and the Batch API: The Combination That Changes the Game

Prompt Caching doesn't exist in isolation. Combined with Anthropic's **Batch API**, the cost reduction potential goes up to 95%.

The Batch API processes requests asynchronously with a 50% discount on all tokens. For workloads that don't need a real-time response, such as report generation, batch classification, document analysis or data enrichment, the Batch API + Prompt Caching combination delivers the lowest possible cost in the Claude ecosystem.

The logic is simple: the Batch API cuts standard output and input costs by 50%. Prompt Caching cuts repeated input costs by 90%. Applied together to eligible workloads, the result is a tiny fraction of the original cost.

Gambit doesn't just choose the right card. He chooses the right moment to throw it.

### When to Require Prompt Caching in a Solution

For an architect evaluating or reviewing a solution that uses Claude via the API, Prompt Caching should be a requirement in any scenario where:

The system prompt is longer than 1,024 tokens and is sent on every call. Call volume is above 10 per hour with the same base context. The solution analyzes large documents with multiple questions in the same session. The agent has many tool definitions loaded on every call. API cost is growing in proportion to volume with no marginal reduction.

If these criteria are present and Prompt Caching isn't implemented, the solution is paying full price for what should already be in the cache. It's Gambit's cards being recharged from scratch before every play.

### Conclusion: The Right Energy at the Right Moment

What makes Gambit lethal isn't how much energy he has. It's the precision with which he applies it. Charging a card once and using it multiple times is more efficient than recharging before every play.

Prompt Caching is the direct implementation of that philosophy in Claude solutions. Context that doesn't change doesn't need to be reprocessed. The energy, in this case the cost of tokens, should be applied where there's actually something new to process.

For leaders and architects taking Claude to production, this isn't an optional optimization. It's an architecture decision with a direct impact on the solution's economic viability. A high-volume solution without Prompt Caching is like Gambit throwing all his cards without having charged any of them.

The cost will always be higher than it should be.

### References

- *Anthropic. Prompt Caching.* [*https://platform.claude.com/docs/en/build-with-claude/prompt-caching*](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- *Anthropic. Pricing.* [*https://platform.claude.com/docs/en/about-claude/pricing*](https://platform.claude.com/docs/en/about-claude/pricing)
- *Anthropic. Batch API.* [*https://platform.claude.com/docs/en/build-with-claude/batch*](https://platform.claude.com/docs/en/build-with-claude/batch)
