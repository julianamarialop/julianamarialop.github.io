---
title: "The Art of Transformation: How to Write Claude Code Skills with Mystique's Precision"
slug: "art-of-transformation-how-to-write-claude-code-skills"
date: 2026-04-14T12:50:00Z
summary: "Mystique isn't the strongest mutant. She doesn't have Wolverine's adamantium, Xavier's telepathy, or Cyclops's optic blasts. What she has is something rarer: the ability to do the most with the least."
tags: ["Claude", "Costs", "AI Agents"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/arte-da-transforma%C3%A7%C3%A3o-como-escrever-skills-claude-code-lopes-jxdlf"
cover:
  image: cover.jpg
  alt: "The Art of Transformation: How to Write Claude Code Skills with Mystique's Precision"
  relative: true
---

Mystique isn't the strongest mutant. She doesn't have Wolverine's adamantium, Xavier's telepathy, or Cyclops's optic blasts. What she has is something rarer: the ability to do the most with the least.

To transform into anyone, she doesn't need equipment, long preparation, or outside resources. She reads the environment, identifies exactly what she needs to replicate, and executes with surgical precision. No wasted movement. No unnecessary detail. Every transformation uses exactly the energy needed to complete the mission.

Writing a skill in [Anthropic](https://www.linkedin.com/company/anthropicresearch/)'s Claude Code demands exactly that mindset.

A poorly written skill is like a Mystique who turns into ten people at once for no reason: it burns energy, confuses the environment, and delivers less than it promised. A well-written skill is the perfect transformation: Claude reads it, understands it, and executes without waste.

This is the manual Mystique would use if she had to teach someone how to write skills.

### What a Skill Is and How Claude Loads It

Before writing, you need to understand what happens when Claude loads a skill.

A skill in Claude Code is a SKILL.md file stored in your project's .claude/skills/ folder. It instructs Claude to carry out a specific set of tasks in a standardized, reusable way. Think of it as a set of instructions that turns Claude into a temporary specialist for that task.

What most developers don't realize is how loading works. When the session starts, Claude loads only the metadata of every available skill: name and description. The full body of the skill is loaded only when Claude determines it's relevant to the task at hand. Additional files referenced in the skill are loaded only when needed.

That has a direct implication: **every token in your skill's body competes with the conversation, the history, and other context files.** A skill with 2,000 unnecessary tokens is 2,000 tokens taken away from what Claude needs to reason about the real problem.

Mystique doesn't pack a suitcase before every mission. She takes exactly what she needs.

### The Anatomy of a Well-Written Skill

An efficient skill has three components: frontmatter, body, and optional reference files.

The frontmatter is required and defines how Claude will discover and trigger the skill:

```yaml
---
name: sql-optimizer
description: Otimiza queries SQL para Databricks, incluindo análise de plano de execução, particionamento e uso de cache. Use quando o usuário pedir para otimizar, revisar ou melhorar performance de queries SQL.
allowed-tools:
  - bash
  - read
---        
```

The description is the most critical element of the frontmatter. It's what Claude uses to decide whether the skill is relevant. A vague description makes Claude ignore the skill. An overly long description wastes tokens that get loaded in every session. The target is between 20 and 40 words, specific enough to trigger in the right cases and stay quiet in the wrong ones.

Mystique knows exactly when to reveal her identity and when to stay in the shadows. A skill's description works the same way.

### Writing Best Practices: What Goes in the Body

The body of the skill is where most developers go wrong. The natural instinct is to put in everything Claude might need to know. The result is a bloated skill that degrades performance and wastes context.

The golden rule is simple: **include only what Claude doesn't know by default.**

Claude already knows what SQL is, what Databricks is, how an execution plan works, and what the general optimization best practices are. Explaining that in the skill is like Mystique rehearsing in the mirror before turning into someone she already knows by heart.

**Bad example:**

```markdown
## Otimização de SQL

SQL (Structured Query Language) é uma linguagem de consulta utilizada para
interagir com bancos de dados relacionais. Para otimizar queries SQL, é
importante entender como o banco de dados executa as consultas. O Databricks
utiliza Apache Spark por baixo, que tem características específicas de
performance. Sempre analise o plano de execução antes de otimizar...        
```

That block is about 150 tokens. Claude already knows all of it. Zero added value.

**Good example:**

```markdown
## Contexto do ambiente
- Databricks Runtime: 14.x ou superior
- Catálogo Unity: obrigatório para todas as queries
- Padrão de nomenclatura de tabelas: `catalog.schema.table_name`
- Particionamento padrão: por `data_referencia` (formato yyyy-MM-dd)

## Processo de otimização
1. Execute `EXPLAIN EXTENDED` antes de qualquer alteração
2. Identifique shuffles desnecessários no plano
3. Verifique uso de cache com `spark.catalog.isCached()`
4. Aplique otimizações na ordem: filtros → particionamento → joins → cache
5. Valide com `EXPLAIN COST` após cada alteração significativa

## Restrições do projeto
- Nunca use `SELECT *` em tabelas com mais de 50 colunas
- Joins em tabelas acima de 1TB requerem broadcast hint explícito
- Máximo de 3 níveis de CTEs por query        
```

That block is about 120 tokens and delivers context Claude genuinely doesn't have: the specifics of your environment, your conventions, and your constraints. It's what Mystique would need to know before passing herself off as someone on your team.

### Cutting Tokens: The Progressive Transformation Technique

Mystique doesn't turn into a different person for every detail of a mission. She takes on one identity and extracts what she needs incrementally, as the situation demands.

Well-architected skills work the same way, with a technique called **progressive disclosure**: the main file contains only the essentials, and additional details live in separate files loaded on demand.

**Recommended structure:**

```
.claude/skills/
  sql-optimizer/
    SKILL.md          ← corpo principal, máximo 500 linhas
    patterns.md       ← padrões de otimização detalhados
    anti-patterns.md  ← erros comuns a evitar
    examples.md       ← exemplos de antes e depois        
```

In [SKILL.md](http://SKILL.md), you reference the additional files:

```markdown
## Referências
- Para padrões detalhados de otimização: ver `patterns.md`
- Para anti-padrões comuns: ver `anti-patterns.md`
- Para exemplos práticos: ver `examples.md`        
```

Claude loads patterns.md only when it's working on a problem that requires that level of detail. The other files sit on the filesystem consuming zero context tokens until they're needed.

The impact is significant. A monolithic 3,000-token skill loaded in full consumes context even when only 20% of its content is relevant to the task. The same skill structured into files loads an average of 400 tokens in SKILL.md and reaches for the rest only when necessary.

### The Most Common Mistakes and How to Avoid Them

Mystique has failed missions before. Usually when she underestimated the environment or overestimated what she needed to bring along. Skills fail for the same reasons.

**Mistake 1: A description that's too generic**

```yaml
# Ruim
description: Ajuda com SQL e banco de dados.

# Bom
description: Otimiza queries SQL para Databricks Unity Catalog, focando em
performance de joins, particionamento e análise de plano de execução.
Use quando o usuário pedir otimização ou revisão de queries SQL.        
```

The bad description will trigger the skill in the wrong contexts or fail to trigger when it should. The good one is specific about the environment, the focus, and the trigger.

**Mistake 2: Telling Claude what it already knows**

Any instruction you'd write for a senior developer with no context on your project is an instruction that doesn't belong in the skill. It belongs to Claude by default.

**Mistake 3: A SKILL.md over 500 lines**

Anthropic's official documentation sets 500 lines as the limit for optimal performance. Beyond that, split it into files using progressive disclosure.

**Mistake 4: Unqualified tools in an MCP context**

```markdown
# Ruim
Use a ferramenta bigquery_schema para recuperar schemas.

# Bom
Use a ferramenta BigQuery:bigquery_schema para recuperar schemas.        
```

When multiple MCP servers are available, Claude may fail to find the tool without the server prefix. Always use the fully qualified name.

**Mistake 5: One skill for everything**

A skill that tries to cover SQL optimization, pipeline creation, documentation, and code review all at once is like Mystique trying to turn into five people simultaneously. None of the transformations will be convincing.

Each skill should have a single, well-defined purpose.

### Testing and Iterating: How Mystique Would Rehearse

Mystique doesn't go into the field without testing the transformation. Skills need the same rigor.

The recommended process has two actors: Claude A, which writes and refines the skill, and Claude B, a clean instance that runs it with no prior knowledge of what was in your head when you wrote it.

```markdown
## Protocolo de teste

1. Escreva a skill com Claude A
2. Abra uma nova sessão com Claude B, carregue apenas a skill
3. Execute 3 a 5 tarefas representativas do caso de uso real
4. Observe onde Claude B hesita, ignora instruções ou pede esclarecimentos
5. Cada hesitação é uma lacuna na skill. Volte ao Claude A e corrija.
6. Repita até Claude B executar sem ambiguidade        
```

If Claude B asks a question the skill should have answered, the skill is incomplete. If Claude B ignores part of the instructions, the skill is poorly structured. If Claude B executes perfectly on every test case, the skill is ready for production.

**Complete Example: A Code Review Skill for Microsoft Fabric**

```yaml
---
name: fabric-pipeline-review
description: Revisa pipelines de dados no Microsoft Fabric para qualidade,
performance e aderência aos padrões do projeto. Use quando o usuário pedir
revisão, auditoria ou feedback sobre código de pipeline Microsoft Fabric.
allowed-tools:
  - read
  - bash
---

## Contexto do projeto
- Ambiente: Microsoft Fabric com Lakehouse habilitado
- Linguagem: PySpark e SQL com type hints obrigatórios
- Arquitetura: Medallion (Bronze → Silver → Gold) via Fabric Lakehouses
- Namespace: `{workspace}.{lakehouse}.{camada}_{dominio}_{entidade}`

## Checklist de revisão obrigatória

### Performance
- [ ] Ausência de `collect()` fora de contextos de debug
- [ ] Joins com tabelas > 500GB usam broadcast hint ou salt
- [ ] Particionamento alinhado com padrão de leitura da camada
- [ ] Delta Lake V-Order habilitado nas tabelas Gold para otimização de leitura Power BI

### Qualidade
- [ ] Schema explícito definido na ingestão Bronze
- [ ] Regras de qualidade implementadas via Data Quality no Fabric ou Great Expectations
- [ ] Tratamento de registros nulos documentado por coluna crítica

### Padrões do projeto
- [ ] Nomenclatura de variáveis em snake_case
- [ ] Funções com docstring no padrão Google Style
- [ ] Sem credenciais hardcoded, usar Azure Key Vault via Fabric Linked Service

## Formato de saída
Para cada item encontrado, retorne:
- Severidade: [CRÍTICO | ALTO | MÉDIO | BAIXO]
- Localização: linha ou função específica
- Problema: descrição objetiva
- Sugestão: correção recomendada com exemplo de código

## Referências adicionais
- Padrões de nomenclatura detalhados: ver `naming-conventions.md`
- Exemplos de anti-padrões comuns: ver `anti-patterns.md`        
```

This skill has about 280 tokens in the main body. It covers the essentials of the project context, structures the process, and defines the output format without explaining to Claude what PySpark is or how Databricks works.

### Conclusion: The Perfect Transformation Leaves No Trace

What makes Mystique terrifying to her enemies isn't her ability to transform. It's that when she pulls off the perfect transformation, nobody notices anything happened. The mission is accomplished without friction, without noise, without waste.

A well-written skill has the same property. Claude loads it, executes it, and delivers the result. No tokens wasted on context it already had. No ambiguity forcing a clarifying question. No unnecessary files eating up the context window.

The difference between a mediocre skill and an excellent one isn't the number of instructions. It's the precision of each one.

Write the way Mystique operates: with the minimum needed for the perfect transformation.

### References

*Anthropic. Skill Authoring Best Practices.* [*https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

*Anthropic. Claude Code Best Practices.* [*https://code.claude.com/docs/en/best-practices*](https://code.claude.com/docs/en/best-practices)

*Anthropic. Skills Overview.* [*https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
