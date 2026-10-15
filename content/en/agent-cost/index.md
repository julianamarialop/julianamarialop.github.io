---
title: "Agent Cost Calculator"
summary: "An estimate of what an AI agent costs, derived from its architecture rather than its request volume, using the prices the vendors themselves publish."
lab: true
ShowToc: false
ShowReadingTime: false
ShowBreadCrumbs: false
ShowPostNavLinks: false
depois: |
  ## Running it locally

  Requires only Python 3.8 or later. There are no packages to install, no API key and no cloud account.

  ```bash
  git clone https://github.com/julianamarialop/agent-cost-math
  cd agent-cost-math
  python agent_cost.py --architecture architecture.example.json
  python agent_cost.py --architecture architecture.example.json --live
  python live_prices.py --check
  ```

  The `--live` option retrieves prices at execution time from the Anthropic pricing page and the Azure Retail Prices API. The `live_prices.py --check` command compares the repository's price table with those sources and exits with an error when they diverge. To estimate a different architecture, edit `architecture.example.json`, with one entry per component: role, monthly volume, model and, for iterative components, the iteration limit.

  ## About the calculator

  The calculations on this page are performed by the same Python code published in the repository, loaded in the browser, so the results on the page and on the command line are identical. The calculator does not invoke any model: it performs calculations only, over the prices published by the vendors and refreshed daily.
---

What does an artificial intelligence agent cost? The most common estimate multiplies the number of requests by the price of one model call. That method underestimates cost, because an agent does not execute a single call: it executes several iterations before it answers, and each iteration processes more text than the previous one.

An agent's cost is determined by its architecture: how many iterations it executes, which model each step uses, and how much context is reprocessed on every iteration. This page presents that reasoning in four steps, with a single example: an online store's customer service assistant answering the question "Where is my order?". Each step introduces one concept, and the values can be changed to observe their effect on cost.
