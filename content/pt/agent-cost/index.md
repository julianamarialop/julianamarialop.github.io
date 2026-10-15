---
title: "Calculadora de custo de agentes"
slug: "custo-de-agentes"
sobretitulo: "Microsoft Ignite 2026 · Table Talk TT1759"
summary: "Estimativa do custo de um agente de IA a partir da sua arquitetura, e não do volume de requisições, com os preços publicados pelos próprios fornecedores."
lab: true
ShowToc: false
ShowReadingTime: false
ShowBreadCrumbs: false
ShowPostNavLinks: false
depois: |
  ## Execução local

  Requer apenas Python 3.8 ou superior. Não há pacotes a instalar, chave de API ou conta de nuvem.

  ```bash
  git clone https://github.com/julianamarialop/agent-cost-math
  cd agent-cost-math
  python agent_cost.py --architecture architecture.example.json
  python agent_cost.py --architecture architecture.example.json --live
  python live_prices.py --check
  ```

  A opção `--live` consulta os preços no momento da execução, na página de preços da Anthropic e na Azure Retail Prices API. O comando `live_prices.py --check` compara a tabela de preços do repositório com essas fontes e encerra com erro quando há divergência. Para estimar outra arquitetura, edite o arquivo `architecture.example.json`, com uma entrada por componente: papel, volume mensal, modelo e, nos componentes iterativos, o limite de iterações.

  ## Sobre a calculadora

  Os cálculos desta página são executados pelo mesmo código Python publicado no repositório, carregado no navegador. Os resultados da página e da linha de comando são, portanto, idênticos. A calculadora não invoca nenhum modelo: realiza apenas cálculos sobre os preços publicados pelos fornecedores, atualizados diariamente.

  ## No Microsoft Ignite 2026

  Esta página acompanha a Table Talk **TT1759, "Agent Cost Is an Architecture Decision, Not a Token Count"** (Agent Platform, nível 300), sessão presencial em San Francisco. O formato Table Talk é uma discussão em grupo, e não uma apresentação: os participantes podem trazer a própria arquitetura para que o custo seja estimado durante a sessão.
---

Quanto custa um agente de inteligência artificial? A estimativa mais comum multiplica o número de solicitações pelo preço de uma chamada ao modelo. Esse método subestima o custo, porque um agente não executa uma única chamada: ele executa várias iterações antes de responder, e cada iteração processa mais texto que a anterior.

O custo de um agente é determinado pela sua arquitetura: quantas iterações ele executa, qual modelo cada etapa utiliza e quanto contexto é reprocessado a cada iteração. Esta página apresenta esse raciocínio em quatro etapas, com um único exemplo: o assistente de atendimento de uma loja online que responde à pergunta "Onde está o meu pedido?". Cada etapa introduz um conceito, e os valores podem ser alterados para observar o efeito no custo.
