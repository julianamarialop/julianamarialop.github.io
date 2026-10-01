---
title: "What Batman's Protocols Taught Me About Business Intelligence Inside Claude"
slug: "what-batmans-protocols-taught-me-about-business-intelligence-in-claude"
date: 2026-07-13T18:20:00Z
summary: "In 2000, in the Tower of Babel arc, Ra's al Ghul took down the entire Justice League without firing a single beam. He stole the Batcave's secret files: the contingency protocols Batman himself had…"
tags: ["Claude", "SQL", "AI Agents"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/o-que-os-protocolos-do-batman-me-ensinaram-sobre-business-lopes-bjidf"
cover:
  image: cover.png
  alt: "What Batman's Protocols Taught Me About Business Intelligence Inside Claude"
  relative: true
---

### The Man Without Superpowers

In 2000, in the Tower of Babel arc, Ra's al Ghul took down the entire Justice League without firing a single beam. He stole the Batcave's secret files: the contingency protocols Batman himself had written to neutralize each hero, in case any of them ever went rogue. Superman, Wonder Woman, The Flash. They all fell to documents.

That story stays with me because it reveals Batman's true power. He doesn't fly, he has no super strength, he can't outrun sound. He writes. For every possible scenario, there's a protocol documented before the scenario happens. The utility belt is ridiculously simple, but it was never about the belt. The power was always the protocol that says which tool to use, when and in what order.

Building an end-to-end Business Intelligence project inside Claude works exactly like that. You don't need superpowers: no dedicated platform, no cluster, no pipeline. You need three simple things: a protocol written in markdown, basic SQL and your data. In this article I'll show you how to put that project together, step by step.

### Before You Start: The Three Pieces

The whole architecture boils down to this:

- The **skill** is your protocol. A folder with a file called SKILL.md, written in plain markdown, where you record the rules of your BI: how each KPI is calculated, which validations run before any delivery, what format the result takes. Anthropic launched Agent Skills in October 2025 and published the format as an open standard in December of the same year, at agentskills.io. The same file works today in Claude, Codex CLI and Gemini CLI.
- The **code execution environment** is your Batcave. Claude has a sandbox where it writes and runs real Python, and that's where the secret of reliability lives: the model writes the code, and the code calculates the numbers. No number in your analysis comes out of the model's "head". They all come from executed queries, with deterministic results.
- **Simple SQL** is the Batarang. Inside the sandbox, DuckDB runs analytical SQL directly over CSV files, in memory, with no server. SELECT, JOIN, GROUP BY and CTEs cover the whole path from raw data to KPI.

### Step 1: Write the Protocol

Open any text editor and create a file called SKILL.md. It has two parts: a YAML header between dashes, with a name and description, and a markdown body with the instructions. The description is the trigger: it's how Claude decides when to activate the protocol, so be specific. Here's a complete, working protocol for sales BI:

```
---
name: bi-vendas
description: Protocolo de análise de dados comerciais. Ativar
  sempre que a análise envolver vendas, receita ou pedidos.
---

# Protocolo de BI de Vendas

## Definições de KPI
- Receita líquida = valor bruto - devoluções - impostos.
  Nunca reportar receita bruta como "receita".
- Ticket médio = receita líquida / número de pedidos distintos.

## Validações obrigatórias na chegada do dado
1. Imprimir nomes de colunas, tipos e contagem de linhas.
2. Verificar duplicidade pela chave pedido_id.
3. Se houver datas fora do período informado, parar e perguntar.

## Regras de transformação
- Toda transformação em SQL via DuckDB, nunca cálculo estimado.
- Reportar linhas de entrada e saída em cada etapa.
- A cadeia de contagens precisa reconciliar do bruto ao final.

## Entrega
- Dashboard interativo como artifact, paleta azul corporativa.
- Toda métrica exibida vem de código executado.
- Documentar as queries usadas ao final da análise.        
```

Read it again slowly, because each block solves a classic BI problem. The KPI definitions put an end to "every department calculates it its own way". The arrival validations kill analysis on dirty data. The transformation rules guarantee traceability. And the delivery section standardizes the result no matter who asked for it. That's a Batman protocol in file form. Written once, executed the same way every time.

### Step 2: Install the Protocol in the Batcave

In Claude, skills live in your account settings, in the capabilities section. There you enable the feature and upload your skill as a zipped folder containing the SKILL.md. On Team and Enterprise plans, the admin centrally controls which skills are available to the organization, which turns your protocol into the standard for the whole team.

One elegant detail of the format: the progressive disclosure mechanism. Claude loads only the name and description of each installed skill. The full instructions enter the context only when the task matches the description. You can keep dozens of protocols installed with no meaningful context cost. Batman doesn't carry every plan on his belt; he knows where each one is stored.

### Step 3: Hand Over the Data

Open a new conversation and drag in the files. The environment accepts CSV, TSV and Excel, with a 30 MB limit per file and up to 20 files per conversation. Then, a direct prompt:

> "Analyze first-half sales using the sales BI protocol. I want net revenue by month, average ticket by region and the 10 products with the biggest drop."

The skill activates through its description, and the first thing that happens isn't the analysis. It's the validation, because the protocol said to validate first. Claude prints columns, types, row counts and date range. If the file has duplicate orders or 2019 dates in a 2026 slice, it stops and asks, instead of producing a beautiful dashboard on wrong data.

### Step 4: Let SQL Do the Work

With the data validated, Claude writes the transformations. You can think of it as a miniature medallion architecture: bronze is the raw CSV, silver is the cleanup, gold is the final aggregation. In DuckDB, the silver and gold stages for monthly revenue look like this:

```
WITH pedidos_limpos AS (
  SELECT DISTINCT ON (pedido_id) *
  FROM read_csv_auto('vendas_s1.csv')
  WHERE data_pedido BETWEEN '2026-01-01' AND '2026-06-30'
)
SELECT
  DATE_TRUNC('month', data_pedido) AS mes,
  SUM(valor_bruto - devolucoes - impostos) AS receita_liquida,
  SUM(valor_bruto - devolucoes - impostos)
    / COUNT(DISTINCT pedido_id) AS ticket_medio
FROM pedidos_limpos
GROUP BY 1
ORDER BY 1;        
```

You don't need to write this query. Claude writes it, following the protocol's definitions, and runs it in the sandbox. But you can read it, and that matters: simple SQL can be audited by anyone on the team. At every stage, it reports the counts: 48,210 rows came in, 1,432 duplicates went out, 46,778 remained. If the chain doesn't reconcile, the protocol says to stop.

### Step 5: Ask for the Deliverable in the Audience's Format

The same environment that runs SQL generates the final deliverable, and here you choose based on the audience:

> "Generate the interactive dashboard with these results."

And out comes a browsable artifact for exploration. Or:

> "Put together a 5-slide executive presentation with these numbers for the committee."

And out comes a .pptx. The environment also produces .xlsx files with working formulas and .docx files, all ready to download. Wrap up by asking for the documentation: the executed queries in markdown, alongside the result. Analysis without traceability is just a loose number.

### Step 6: Repeat, Because Now It's Repeatable

The next month, the new file arrives. You open another conversation, drag in the CSV and use the same prompt. The protocol is the same, the definitions are the same, the result is comparable. And when the business rule changes, you don't retrain the team: you edit the SKILL.md, version it in Git with a pull request and an owner, and everyone inherits the new rule in their next conversation. Governance stopped being oral tradition. It became an auditable file.

### What Changes for Data Teams

The uncomfortable question: if this works, what's the BI platform for?

It's for what it was always for, and honesty matters here. Volumes above 30 MB, scheduled refresh, row-level security, a corporate catalog and hundreds of concurrent users are platform territory. Claude doesn't replace Fabric or Power BI, and anyone selling that story is manufacturing the governance disaster of 2027.

What changes is the layer before that. The exploratory phase, which today takes weeks between request, queue and first delivery, compresses into a single session. The business person validates the hypothesis before any platform investment, inside rules the data team wrote. The classic fear of self-service was never access to data; it was everyone calculating the KPI their own way. With the protocol loaded, you get autonomy with boundaries.

### Availability and Access

Code execution and file creation are available to all Claude users, including the free plan, on web, desktop and mobile. Skills are enabled in settings, and Team and Enterprise admins centrally control what is provisioned for the organization. On new Enterprise accounts, the environment comes enabled with network egress turned off by default, keeping the sandbox isolated.

### Conclusion: Preparation Beats Raw Power

In Tower of Babel, the League didn't fall to someone stronger. It fell to tactical knowledge documented rigorously enough to be executable by anyone. That was always the Batcave's real weapon: not the gadgets, the files.

Your BI project inside Claude follows the same logic. The power isn't in the model. It's in the protocol you wrote in Step 1: the definitions, the validations, the delivery format. Markdown is the language of protocols. Simple SQL is the Batarang. And the analyst who documents their rules is the Batman in the room: without a single superpower, prepared for every scenario.

Write your first SKILL.md this week. Start with one KPI and three validations. The gods and the platforms are still necessary, but whoever decides the course of the battle is the one who showed up with the plan written down.

### References

- Anthropic. Equipping agents for the real world with Agent Skills. <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills>
- Agent Skills. Open standard specification. <https://agentskills.io>
- Anthropic. Create and edit files with Claude. <https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude>
- Anthropic. Official skills repository. <https://github.com/anthropics/skills>
