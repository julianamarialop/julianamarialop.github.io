---
title: "O Que os Protocolos do Batman Me Ensinaram Sobre Business Intelligence dentro do Claude"
date: 2026-07-13T18:20:00Z
summary: "Em 2000, no arco Torre de Babel, Ra's al Ghul derrubou a Liga da Justiça inteira sem disparar um único raio. Ele roubou os arquivos secretos da Batcaverna: os protocolos de contingência que o próprio Batman havia…"
tags: ["Claude", "SQL", "Agentes de IA"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/o-que-os-protocolos-do-batman-me-ensinaram-sobre-business-lopes-bjidf"
cover:
  image: cover.png
  alt: "O Que os Protocolos do Batman Me Ensinaram Sobre Business Intelligence dentro do Claude"
  relative: true
---

### O Homem Sem Superpoderes

Em 2000, no arco Torre de Babel, Ra's al Ghul derrubou a Liga da Justiça inteira sem disparar um único raio. Ele roubou os arquivos secretos da Batcaverna: os protocolos de contingência que o próprio Batman havia escrito para neutralizar cada herói, caso algum saísse do controle. Superman, Mulher Maravilha, Flash. Todos caíram diante de documentos.

Essa história me acompanha porque ela revela o verdadeiro poder do Batman. Ele não voa, não tem super força, não corre mais rápido que o som. Ele escreve. Para cada cenário possível, existe um protocolo documentado antes do cenário acontecer. O cinto de utilidades é ridiculamente simples, mas nunca foi o cinto. O poder sempre foi o protocolo que diz qual ferramenta usar, quando e em que ordem.

Construir um projeto de Business Intelligence de ponta a ponta dentro do Claude funciona exatamente assim. Você não precisa de superpoderes: nem plataforma dedicada, nem cluster, nem pipeline. Precisa de três coisas simples: um protocolo escrito em markdown, SQL básico e os seus dados. Neste artigo eu mostro como montar esse projeto, passo a passo.

### Antes de Começar: As Três Peças

A arquitetura inteira se resume a isto:

- A **skill** é o seu protocolo. Uma pasta com um arquivo chamado SKILL.md, escrito em markdown puro, onde você registra as regras do seu BI: como cada KPI é calculado, quais validações rodam antes de qualquer entrega, qual o formato do resultado. A Anthropic lançou as Agent Skills em outubro de 2025 e publicou o formato como padrão aberto em dezembro do mesmo ano, em agentskills.io. O mesmo arquivo funciona hoje no Claude, no Codex CLI e no Gemini CLI.
- O **ambiente de execução de código** é a sua Batcaverna. O Claude possui um sandbox onde escreve e executa Python de verdade, e é aí que mora o segredo da confiabilidade: o modelo escreve o código, e o código calcula os números. Nenhum número da sua análise sai da "cabeça" do modelo. Todos saem de queries executadas, com resultado determinístico.
- O **SQL simples** é o batarangue. Dentro do sandbox, o DuckDB executa SQL analítico diretamente sobre arquivos CSV, em memória, sem servidor. SELECT, JOIN, GROUP BY e CTEs resolvem o trajeto completo do dado bruto ao KPI.

### Passo 1: Escreva o Protocolo

Abra qualquer editor de texto e crie um arquivo chamado SKILL.md. Ele tem duas partes: um cabeçalho YAML entre traços, com nome e descrição, e o corpo em markdown com as instruções. A descrição é o gatilho: é por ela que o Claude decide quando ativar o protocolo, então seja específica. Este é um protocolo completo e funcional para BI de vendas:

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

Leia de novo com calma, porque cada bloco resolve um problema clássico de BI. As definições de KPI acabam com o "cada área calcula de um jeito". As validações de chegada matam a análise sobre dado sujo. As regras de transformação garantem rastreabilidade. E a entrega padroniza o resultado independente de quem pediu. Isso é um protocolo do Batman em forma de arquivo. Escrito uma vez, executado sempre igual.

### Passo 2: Instale o Protocolo na Batcaverna

No Claude, as skills ficam nas configurações da conta, na seção de capacidades. Ali você habilita o recurso e envia a sua skill como uma pasta compactada contendo o SKILL.md. Nos planos Team e Enterprise, o administrador controla centralmente quais skills ficam disponíveis para a organização, o que transforma o seu protocolo em padrão do time inteiro.

Um detalhe elegante do formato: o mecanismo de progressive disclosure. O Claude carrega só o nome e a descrição de cada skill instalada. As instruções completas entram no contexto apenas quando a tarefa corresponde à descrição. Você pode manter dezenas de protocolos instalados sem custo relevante de contexto. O Batman não carrega todos os planos no cinto; ele sabe onde cada um está guardado.

### Passo 3: Entregue os Dados

Abra uma conversa nova e arraste os arquivos. O ambiente aceita CSV, TSV e Excel, com limite de 30 MB por arquivo e até 20 arquivos por conversa. Depois, um prompt direto:

> "Analise as vendas do primeiro semestre usando o protocolo de BI de vendas. Quero receita líquida por mês, ticket médio por região e os 10 produtos com maior queda."

A skill ativa pela descrição e a primeira coisa que acontece não é a análise. É a validação, porque o protocolo mandou validar antes. O Claude imprime colunas, tipos, contagem de linhas e range de datas. Se o arquivo tem pedidos duplicados ou datas de 2019 num recorte de 2026, ele para e pergunta, em vez de produzir um dashboard bonito sobre dado errado.

### Passo 4: Deixe o SQL Trabalhar

Com o dado validado, o Claude escreve as transformações. Dá para pensar nisso como uma arquitetura medallion em miniatura: bronze é o CSV bruto, silver é a limpeza, gold é a agregação final. Em DuckDB, a etapa silver e gold de receita mensal fica assim:

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

Você não precisa escrever essa query. O Claude escreve, seguindo as definições do protocolo, e executa no sandbox. Mas você consegue ler, e isso importa: SQL simples é auditável por qualquer pessoa do time. A cada etapa, ele reporta as contagens: entraram 48.210 linhas, saíram 1.432 duplicadas, restaram 46.778. Se a cadeia não reconcilia, o protocolo manda parar.

### Passo 5: Peça a Entrega no Formato do Público

O mesmo ambiente que executa SQL gera a entrega final, e aqui você escolhe conforme a audiência:

> "Gere o dashboard interativo com esses resultados."

E sai um artifact navegável para exploração. Ou:

> "Monte uma apresentação executiva de 5 slides com esses números para o comitê."

E sai um .pptx. O ambiente também produz .xlsx com fórmulas funcionais e .docx, todos para download. Feche pedindo a documentação: as queries executadas em markdown, junto do resultado. Análise sem rastreabilidade é número solto.

### Passo 6: Repita, Porque Agora É Repetível

No mês seguinte, chega o arquivo novo. Você abre outra conversa, arrasta o CSV e usa o mesmo prompt. O protocolo é o mesmo, as definições são as mesmas, o resultado é comparável. E quando a regra de negócio mudar, você não reeduca o time: edita o SKILL.md, versiona no Git com pull request e dono, e todo mundo herda a regra nova na próxima conversa. Governança deixou de ser tradição oral. Virou arquivo auditável.

### O Que Muda Para Times de Dados

A pergunta desconfortável: se isso resolve, para que serve a plataforma de BI?

Serve para o que sempre serviu, e a honestidade importa. Volumes acima de 30 MB, refresh agendado, row-level security, catálogo corporativo e centenas de usuários simultâneos são território de plataforma. O Claude não substitui o Fabric nem o Power BI, e quem vender essa história está fabricando o desastre de governança de 2027.

O que muda é a camada anterior. A fase exploratória, que hoje leva semanas entre pedido, fila e primeira entrega, comprime para uma sessão. A pessoa de negócio valida a hipótese antes de qualquer investimento em plataforma, dentro de regras que o time de dados escreveu. O medo clássico do self-service nunca foi o acesso ao dado; foi cada um calculando o KPI do seu jeito. Com o protocolo carregado, existe autonomia com fronteira.

### Disponibilidade e Acesso

A execução de código e a criação de arquivos estão disponíveis para todos os usuários do Claude, incluindo o plano gratuito, na web, no desktop e no mobile. As skills são habilitadas nas configurações, e administradores de Team e Enterprise controlam centralmente o que fica provisionado para a organização. Em contas Enterprise novas, o ambiente vem habilitado com egress de rede desligado por padrão, mantendo o sandbox isolado.

### Conclusão: Preparação Vence Poder Bruto

Na Torre de Babel, a Liga não caiu diante de alguém mais forte. Caiu diante de conhecimento tático documentado com rigor suficiente para ser executável por qualquer um. Essa sempre foi a arma real da Batcaverna: não os gadgets, os arquivos.

O seu projeto de BI dentro do Claude segue a mesma lógica. O poder não está no modelo. Está no protocolo que você escreveu no Passo 1: as definições, as validações, o formato de entrega. Markdown é a linguagem dos protocolos. SQL simples é o batarangue. E o analista que documenta suas regras é o Batman da sala: sem nenhum superpoder, preparado para todos os cenários.

Escreva o seu primeiro SKILL.md esta semana. Comece com um KPI e três validações. Os deuses e as plataformas continuam necessários, mas quem decide o rumo da batalha é quem chegou com o plano escrito.

### Referências

- Anthropic. Equipping agents for the real world with Agent Skills. <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills>
- Agent Skills. Especificação do padrão aberto. <https://agentskills.io>
- Anthropic. Create and edit files with Claude. <https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude>
- Anthropic. Repositório oficial de skills. <https://github.com/anthropics/skills>
