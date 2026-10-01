---
title: "A Arte da Transformação: Como Escrever Skills no Claude Code com a Precisão da Mystique"
date: 2026-04-14T12:50:00Z
summary: "Mystique não é a mutante mais forte. Não tem o adamantium de Wolverine, a telepatia de Xavier ou as rajadas de Ciclope. O que ela tem é algo mais raro: a capacidade de fazer o máximo com o mínimo."
tags: ["Claude", "Custos", "Agentes de IA"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/arte-da-transforma%C3%A7%C3%A3o-como-escrever-skills-claude-code-lopes-jxdlf"
cover:
  image: cover.jpg
  alt: "A Arte da Transformação: Como Escrever Skills no Claude Code com a Precisão da Mystique"
  relative: true
---

Mystique não é a mutante mais forte. Não tem o adamantium de Wolverine, a telepatia de Xavier ou as rajadas de Ciclope. O que ela tem é algo mais raro: a capacidade de fazer o máximo com o mínimo.

Para se transformar em qualquer pessoa, ela não precisa de equipamento, de preparação longa ou de recursos externos. Ela lê o ambiente, identifica exatamente o que precisa replicar e executa com precisão cirúrgica. Nenhum movimento desperdiçado. Nenhum detalhe desnecessário. Cada transformação consome exatamente a energia necessária para cumprir a missão.

Escrever uma skill no Claude Code da [Anthropic](https://www.linkedin.com/company/anthropicresearch/) exige exatamente essa mentalidade.

Uma skill mal escrita é como uma Mystique que transforma em dez pessoas ao mesmo tempo sem necessidade: consome energia, confunde o ambiente e entrega menos do que prometia. Uma skill bem escrita é a transformação perfeita: Claude lê, entende e executa sem desperdício.

Este é o manual que Mystique usaria se precisasse ensinar alguém a escrever skills.

### O Que é uma Skill e Como Claude a Carrega

Antes de escrever, é preciso entender o que acontece quando Claude carrega uma skill.

Uma skill no Claude Code é um arquivo SKILL.md armazenado em .claude/skills/ do seu projeto. Ela instrui Claude a executar um conjunto específico de tarefas de forma padronizada e reutilizável. Pense nela como um conjunto de instruções que transforma Claude em um especialista temporário para aquela tarefa.

O que a maioria dos desenvolvedores não percebe é como o carregamento funciona. Na inicialização da sessão, Claude carrega apenas os metadados de todas as skills disponíveis: nome e descrição. O corpo completo da skill só é carregado quando Claude determina que ela é relevante para a tarefa em execução. Arquivos adicionais referenciados na skill são carregados apenas quando necessários.

Isso tem uma implicação direta: **cada token no corpo da sua skill compete com a conversa, com o histórico e com outros arquivos de contexto.** Uma skill de 2.000 tokens desnecessários é 2.000 tokens subtraídos do que Claude precisa para raciocinar sobre o problema real.

Mystique não carrega uma mala antes de cada missão. Ela leva exatamente o que precisa.

### A Anatomia de uma Skill Bem Escrita

Uma skill eficiente tem três componentes: frontmatter, corpo e arquivos de referência opcionais.

O frontmatter é obrigatório e define como Claude vai descobrir e acionar a skill:

```yaml
---
name: sql-optimizer
description: Otimiza queries SQL para Databricks, incluindo análise de plano de execução, particionamento e uso de cache. Use quando o usuário pedir para otimizar, revisar ou melhorar performance de queries SQL.
allowed-tools:
  - bash
  - read
---        
```

A descrição é o elemento mais crítico do frontmatter. É ela que Claude usa para decidir se a skill é relevante. Uma descrição vaga faz Claude ignorar a skill. Uma descrição excessivamente longa desperdiça tokens que são carregados em cada sessão. O alvo é entre 20 e 40 palavras, específicas o suficiente para acionar nos casos certos e silenciosas nos casos errados.

Mystique sabe exatamente quando revelar sua identidade e quando permanecer na sombra. A descrição da skill funciona da mesma forma.

### Boas Práticas de Escrita: O Que Colocar no Corpo

O corpo da skill é onde a maioria dos desenvolvedores erra. O instinto natural é colocar tudo o que Claude pode precisar saber. O resultado é uma skill obesa que degrada performance e desperdiça contexto.

A regra de ouro é simples: **coloque apenas o que Claude não sabe por padrão.**

Claude já sabe o que é SQL, o que é Databricks, como funciona um plano de execução e quais são as melhores práticas gerais de otimização. Explicar isso na skill é como Mystique praticando no espelho antes de se transformar em alguém que ela já conhece de cor.

**Exemplo ruim:**

```markdown
## Otimização de SQL

SQL (Structured Query Language) é uma linguagem de consulta utilizada para
interagir com bancos de dados relacionais. Para otimizar queries SQL, é
importante entender como o banco de dados executa as consultas. O Databricks
utiliza Apache Spark por baixo, que tem características específicas de
performance. Sempre analise o plano de execução antes de otimizar...        
```

Esse bloco tem aproximadamente 150 tokens. Claude já sabe tudo isso. Zero valor adicionado.

**Exemplo bom:**

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

Esse bloco tem aproximadamente 120 tokens e entrega contexto que Claude genuinamente não tem: as especificidades do seu ambiente, suas convenções e suas restrições. É o que Mystique precisaria saber antes de se passar por alguém do seu time.

### Redução de Tokens: A Técnica da Transformação Progressiva

Mystique não se transforma em uma pessoa diferente para cada detalhe de uma missão. Ela assume uma identidade e extrai o que precisa de forma incremental, conforme a situação exige.

Skills bem arquitetadas funcionam da mesma forma, com uma técnica chamada **progressive disclosure**: o arquivo principal contém apenas o essencial, e detalhes adicionais ficam em arquivos separados carregados sob demanda.

**Estrutura recomendada:**

```
.claude/skills/
  sql-optimizer/
    SKILL.md          ← corpo principal, máximo 500 linhas
    patterns.md       ← padrões de otimização detalhados
    anti-patterns.md  ← erros comuns a evitar
    examples.md       ← exemplos de antes e depois        
```

No [SKILL.md](http://SKILL.md), você referencia os arquivos adicionais:

```markdown
## Referências
- Para padrões detalhados de otimização: ver `patterns.md`
- Para anti-padrões comuns: ver `anti-patterns.md`
- Para exemplos práticos: ver `examples.md`        
```

Claude carrega patterns.md apenas quando está trabalhando em um problema que exige aquele nível de detalhe. Os outros arquivos ficam no filesystem consumindo zero tokens de contexto até serem necessários.

O impacto é significativo. Uma skill monolítica de 3.000 tokens carregada integralmente consome contexto mesmo quando apenas 20% do conteúdo é relevante para a tarefa. A mesma skill estruturada em arquivos carrega em média 400 tokens no SKILL.md e acessa os demais somente quando necessário.

### Erros Mais Comuns e Como Evitar

Mystique já falhou em missões. Geralmente quando subestimou o ambiente ou superestimou o que precisava levar consigo. Skills falham pelos mesmos motivos.

**Erro 1: Descrição genérica demais**

```yaml
# Ruim
description: Ajuda com SQL e banco de dados.

# Bom
description: Otimiza queries SQL para Databricks Unity Catalog, focando em
performance de joins, particionamento e análise de plano de execução.
Use quando o usuário pedir otimização ou revisão de queries SQL.        
```

A descrição ruim vai acionar a skill em contextos errados ou não acionar quando deveria. A boa é específica sobre o ambiente, o foco e o gatilho.

**Erro 2: Instruir Claude sobre o que ele já sabe**

Qualquer instrução que você escreveria para um desenvolvedor sênior sem contexto do seu projeto é uma instrução que não pertence à skill. Pertence ao Claude por padrão.

**Erro 3: SKILL.md acima de 500 linhas**

A documentação oficial da Anthropic estabelece 500 linhas como limite para performance ótima. Acima disso, divida em arquivos usando progressive disclosure.

**Erro 4: Ferramentas não qualificadas em contexto MCP**

```markdown
# Ruim
Use a ferramenta bigquery_schema para recuperar schemas.

# Bom
Use a ferramenta BigQuery:bigquery_schema para recuperar schemas.        
```

Quando múltiplos servidores MCP estão disponíveis, Claude pode não localizar a ferramenta sem o prefixo do servidor. Sempre use o nome completamente qualificado.

**Erro 5: Uma skill para tudo**

Uma skill que tenta cobrir otimização SQL, criação de pipelines, documentação e revisão de código ao mesmo tempo é como Mystique tentando se transformar em cinco pessoas simultaneamente. Nenhuma das transformações vai ser convincente.

Cada skill deve ter um propósito único e bem definido.

### Testando e Iterando: Como Mystique Ensaiaria

Mystique não vai a campo sem testar a transformação. Skills precisam do mesmo rigor.

O processo recomendado tem dois atores: Claude A, que escreve e refina a skill, e Claude B, uma instância limpa que a executa sem conhecimento prévio do que estava na sua cabeça quando escreveu.

```markdown
## Protocolo de teste

1. Escreva a skill com Claude A
2. Abra uma nova sessão com Claude B, carregue apenas a skill
3. Execute 3 a 5 tarefas representativas do caso de uso real
4. Observe onde Claude B hesita, ignora instruções ou pede esclarecimentos
5. Cada hesitação é uma lacuna na skill. Volte ao Claude A e corrija.
6. Repita até Claude B executar sem ambiguidade        
```

Se Claude B faz uma pergunta que a skill deveria responder, a skill está incompleta. Se Claude B ignora parte das instruções, a skill está mal estruturada. Se Claude B executa perfeitamente em todos os casos de teste, a skill está pronta para produção.

**Exemplo Completo: Skill de Code Review para Microsoft Fabric**

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

Essa skill tem aproximadamente 280 tokens no corpo principal. Cobre o essencial do contexto do projeto, estrutura o processo e define o formato de saída sem explicar para Claude o que é PySpark ou como funciona o Databricks.

### Conclusão: A Transformação Perfeita Não Deixa Rastro

O que torna Mystique aterrorizante para seus inimigos não é a capacidade de se transformar. É que quando ela executa a transformação perfeita, ninguém percebe que aconteceu algo. A missão é cumprida sem fricção, sem ruído, sem desperdício.

Uma skill bem escrita tem a mesma propriedade. Claude a carrega, executa e entrega o resultado. Nenhum token desperdiçado em contexto que ele já tinha. Nenhuma ambiguidade que force uma pergunta de esclarecimento. Nenhum arquivo desnecessário consumindo janela de contexto.

A diferença entre uma skill mediana e uma skill excelente não está na quantidade de instruções. Está na precisão de cada uma delas.

Escreva como Mystique opera: com o mínimo necessário para a transformação perfeita.

### Referências

*Anthropic. Skill Authoring Best Practices.* [*https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

*Anthropic. Claude Code Best Practices.* [*https://code.claude.com/docs/en/best-practices*](https://code.claude.com/docs/en/best-practices)

*Anthropic. Skills Overview.* [*https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
