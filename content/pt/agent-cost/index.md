---
title: "Calculadora de custo de agentes"
slug: "custo-de-agentes"
sobretitulo: "Microsoft Ignite 2026 · Table Talk TT1759"
summary: "Precifique a arquitetura de um agente antes de construí-lo: pela estrutura, não pelo volume, com os preços dos próprios fornecedores. O mesmo motor Python do repositório, rodando no seu navegador."
lab: true
ShowToc: false
ShowReadingTime: false
ShowBreadCrumbs: false
ShowPostNavLinks: false
depois: |
  ## Rode na sua máquina

  Basta Python 3.8 ou mais novo: sem `pip install`, sem chave de API, sem conta de nuvem.

  ```bash
  git clone https://github.com/julianamarialop/agent-cost-math
  cd agent-cost-math
  python agent_cost.py --architecture architecture.example.json
  python agent_cost.py --architecture architecture.example.json --live
  python live_prices.py --check
  ```

  O `--live` lê os preços naquele momento na página de preços da Anthropic e na Azure Retail Prices API. O `live_prices.py --check` compara a tabela manual do repositório com essas fontes e termina com erro quando elas divergem. Para precificar o seu próprio sistema, edite o `architecture.example.json`: uma entrada por componente, com o papel, o volume mensal, o modelo e, nos loops, o teto de iterações.

  ## No Microsoft Ignite 2026

  Esta página acompanha a Table Talk **TT1759, "Agent Cost Is an Architecture Decision, Not a Token Count"** (Agent Platform, nível 300), presencial, em San Francisco. Table Talk é conversa, não palestra: traga a sua arquitetura e a gente precifica na mesa.
---

A maioria das estimativas de custo de agentes multiplica requisições por um preço por requisição. Esse número erra numa direção previsível, porque não é o volume que define a conta. É a orquestração: quais componentes existem, que papel cada um cumpre, quantas voltas o loop dá, que modelo ele usa e quanto contexto ele relê a cada volta.

O exemplo abaixo é uma triagem de sinistros com cinco componentes. O roteador atende quatro vezes mais pedidos que o especialista e custa trinta e seis vezes menos. Mude qualquer entrada e a calculadora refaz a conta, ou recusa quando falta algo de que ela precisa, porque uma linha que entra na estimativa com valor zero some da proposta e ninguém percebe.

Nenhuma conta desta página é feita em JavaScript. O seu navegador roda o mesmo arquivo Python que está no repositório, então os números daqui são os números da linha de comando. A calculadora não chama modelo nenhum: é aritmética sobre preços lidos das fontes públicas dos fornecedores.
