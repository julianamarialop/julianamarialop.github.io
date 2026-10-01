---
title: "Pawn, Rook, Queen: How to Field the Right Model for Each Agent"
slug: "pawn-rook-queen-how-to-field-the-right-model-for-each-agent"
date: 2026-08-21T14:00:00Z
summary: "Every chess player learns a table early on and carries it for life: a pawn is worth 1, knight and bishop are worth 3, a rook is worth 5, the queen is worth 9. It isn't a rule of the game, it's centuries of accumulated wisdom about the relative power of each…"
tags: ["Costs", "AI Agents", "Generative AI", "Claude", "Microsoft Fabric", "Azure"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/pe%C3%A3o-torre-dama-como-escalar-o-modelo-certo-para-cada-lopes-llmsf"
cover:
  image: cover.jpg
  alt: "Pawn, Rook, Queen: How to Field the Right Model for Each Agent"
  relative: true
---

### The Value of the Pieces

Every chess player learns a table early on and carries it for life: a pawn is worth 1, knight and bishop are worth 3, a rook is worth 5, the queen is worth 9. It isn't a rule of the game, it's centuries of accumulated wisdom about the relative power of each piece. And from it come the lessons that separate people who play from people who understand. You don't use the queen for pawn work, because every move she makes on a small task is a move in which she isn't deciding the game. Philidor wrote in the 18th century that pawns are the soul of chess: games are won and lost on their structure, the humble pieces that do the volume work. And the king, curiously the least powerful piece on the board, is the only irreplaceable one: he moves one square at a time, but everything revolves around him, and when he falls, it's over.

The language model market in 2026 is that board. Public prices range from about 10 cents to 75 dollars per million tokens, a gap that makes the chess pawn and queen look close: on the board the queen is worth 9 pawns, in the catalog she can be worth 60. And even so, the most common scene in enterprise AI projects is still a board set up with nothing but queens: the most expensive model in the catalog running text classification, field extraction, and rule validation, pawn tasks, at a queen's fee.

In this article I introduce the pieces one by one, with real specs and numbers, and then I set up a full game: a multi-agent project on [Microsoft Fabric](https://www.linkedin.com/company/microsoft-fabric-world/) and Foundry in which every function runs on the model that matches its value.

### The Queens: Frontier Models

The queen is the deep reasoning model, and in August 2026 three of them dominate the top of the independent indexes.

Anthropic's Claude Opus 4.8 leads the aggregate intelligence rankings and is the king of code: comparisons report 88.6% on SWE-bench Verified, the benchmark that measures fixing real bugs in real repositories, with the ability to coordinate parallel subagents on large-scale tasks. A 200,000-token context, priced at the high end of the market. It's the queen for complex engineering, ambiguous multi-step analysis, and orchestration. On Foundry, Claude models have been generally available since July 2026, in two hosting variants.

OpenAI's GPT-5.6 family, launched in July 2026, brought the context artillery: a 1,050,000-token window, with variants that balance cost and capability. The previous generation, GPT-5.5, is still strong in agentic and multimodal flows, and comparisons put it side by side with Opus on code. It's the queen for missions that need to see entire codebases or documents at once.

Google's Gemini 3.1 Pro is the best-value queen at the frontier: comparisons report 80.6% on SWE-bench, practically tied with the leaders, at a fraction of the cost, with a 1 million token context. Honesty at the board: it doesn't live in the Foundry catalog, so for architectures anchored in the Microsoft ecosystem it's a queen from the club next door.

When to use a queen: planning, breaking down ambiguous problems, complex multi-file code, final judgment. When not to: any task that can be described in one sentence and verified with a rule.

### The Rooks: The Workhorses

The rook is worth 5: strong, direct, and it's the piece that carries the middlegame. These are the balanced models, and the rule of thumb is that they handle the vast majority of enterprise tasks for a fraction of the queen's cost.

Claude Sonnet 4.6 is the canonical example: comparisons report 79.6% on SWE-bench, a few points behind Opus, with much lower cost and latency. For everyday code, data analysis, document generation, and production agents, the rook delivers close to the queen while costing much less. GPT-5.4 sits on the same square on the OpenAI side, with reported strength in structured reasoning and computer use (75% on OSWorld, above the human expert baseline) and the same expanded 1.05 million token window. And Meta's Llama 4 Maverick is the open-weight rook that even shows up in the Foundry Model Router pool.

When to use it: as the default. The rook should be your architecture's default model, with the queen coming in by justified exception and the pawn by volume optimization.

### The Bishops: Single-Color Specialists

The bishop is powerful with a structural limitation: it only sees the squares of its own color. These are the specialized models, unbeatable on their diagonal and useless off it.

xAI's Grok 4.1 fast reasoning, available in the Foundry router, is the speed bishop: fast reasoning for agentic cases where latency matters more than maximum depth. Embedding models are pure bishops: they don't converse, they just turn text into vectors, and no semantic search or RAG exists without them. Vision and image generation models follow the same logic. And DeepSeek V3.2 and the new V4, open under the MIT license, are the cost bishops: comparisons put them a few points behind the proprietary queens on code, at dozens of times lower cost, which redefines the math of massive batch work. With the honest diagonal stated up front: in a regulated context, the data path and operational maturity have to enter the risk analysis before price does.

### The Knights: The Move Nobody Else Makes

The knight is worth the same 3 points as the bishop, but it has the only move in the game that jumps over other pieces. These are the open-weight models and the SLMs, which reach where the closed ones can't: inside your data center, at the edge, on the device, in deep fine-tuning with your own data.

Microsoft's Phi family is the house knight on Foundry: small models that run at minimal cost and even locally, ideal for well-scoped tasks at very high volume. Llama 4 in its smaller sizes plays the same role with the largest community ecosystem. The knight's jump is the answer to the requirements that stall projects: data that can't leave the perimeter, millisecond latency, cost per call trending toward zero.

### The Pawns: The Soul of the Operation

And we arrive at Philidor's piece. The pawns are the lightweight models from the frontier families: Claude Haiku 4.5, GPT-5.4-nano and mini, the Flash and Flash-Lite models of the world, priced in the cents per million tokens. Individually modest, in structure they decide games: classification, field extraction, message routing, rule validation, everything that runs thousands of times a day and can be checked against an objective criterion.

Your architecture's pawn structure is the validation and triage layer. A team that builds that structure well spends cents where competitors spend dollars, and reaches the endgame with its queens intact for what matters.

### The King and the Chess Player

Two figures are missing, and the distinction between them organizes the whole architecture.

The king is the orchestrator: the agent that receives the mission, breaks it down into tasks, calls on each piece, and judges the results. As on the board, it isn't the one that moves the most; it makes few moves, but each one decides the game, and if it falls, the whole mission falls. That's why the king justifies a frontier model or a top-tier balanced one: getting a classification wrong costs cents, getting the decomposition wrong costs the battle.

And the chess player is you. Here it's worth clearing up a common confusion on Foundry: the Model Router, which routes each prompt across 28 models while optimizing cost and quality, is a valuable tool, but it's a piece selector per move, not a player. Mission orchestration, with state, sequence, and judgment, is the job of an agent you design, typically with the king running on a strong model and carrying the operation's protocols, the skills, which can now be hosted on Foundry itself.

### The Game: The Multi-Agent Project

Now the full game, in my world: the data quality control tower with a daily executive report, on Fabric and Foundry.

The opening is an event, not a prompt: Fabric's Activator detects the arrival of the daily load in OneLake and triggers the mission, with no tokens spent asking whether the data has arrived.

The king wakes up: the orchestrator, on Claude Opus or GPT-5.6, reads the operation's protocol and breaks the mission down into four tasks with dependencies.

The pawns advance: validation agents on Haiku and Phi sweep through hundreds of quality rules, counts, duplicates, and domains. Pure volume, cost in cents, results verifiable by rule.

The rook enters the middlegame: an analysis agent on Sonnet or GPT-5.4 investigates the day's variations by talking to the Fabric Data Agent, which answers grounded in the semantic models where the official KPI definitions live. The definition of net revenue lives in the semantic model, not copied into five prompts.

The bishop writes: a writer agent turns the findings into the executive report, in the protocol's format.

And the final move comes from modern chess tradition: no grandmaster trusts the analysis of a game to a single engine. They use Stockfish and Leela, engines with different styles, because the disagreement between them is where the learning lives. The fifth agent is that second engine: a critic from a different model family than the writer's. If the writer is Claude, the critic is GPT, and vice versa. Cross-family review reduces style bias and lineage complacency, a cousin of the sycophancy I've already written about. Only with the critic's approval does the king publish and close out.

One mission, six models, four piece values, two families. Cost plummets compared with the all-queens board, and quality goes up, because disagreement became architecture.

### What Changes for Data Teams

Three chess club rules to take with you. First: size by volume, not by prestige. List the functions that run thousands of times a day and push them to pawns and knights; the savings pay for the orchestrator's queen with room to spare. Second: institute the second engine. Cross-family review as an architecture rule, which Foundry's unified catalog, with more than 1,900 models under the same governance and central deployment policy, makes trivial. Third: benchmarks change monthly and the lead changes hands every quarter, so build to swap pieces cheaply: a model is configuration, not foundation. Anyone who couples their architecture to a specific model is playing today's game with last year's opening theory.

And the usual honesty: multi-agent is an endgame, not an opening. If a single agent solves it, five agents are complexity with no return. Set up the full board when the functions are genuinely different enough to call for different pieces.

### Conclusion: Who Wins the Game

In chess, both players start with exactly the same pieces. The board is public, the values are known, and yet someone wins. The difference was never in the pieces; it was in who understands their relative value and places each one on the right square, on the right move.

With LLMs, the catalog is also public and the same for everyone. Your competitors have access to the same queens, rooks, and pawns you do. The competitive advantage isn't in having the strongest model, it's in the lineup: the queen kept for what decides the game, the pawns structured for volume, the second engine checking the analysis, and the king protected at the center of the architecture.

The question left on the board: how many of your project's queens are, right now, doing pawn work?

### References

- Microsoft Learn. Model router for Microsoft Foundry concepts. <https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-router>
- Microsoft Azure. Foundry Models. <https://azure.microsoft.com/en-us/products/ai-foundry/models>
- LM Council. AI Model Benchmarks. <https://lmcouncil.ai/benchmarks>
- Iternal. LLM Comparison 2026: 30+ Models Benchmarked. <https://iternal.ai/llm-selection-guide>
- TechieHub. Best AI Models Compared 2026. <https://techiehub.blog/best-ai-models-compared/>
