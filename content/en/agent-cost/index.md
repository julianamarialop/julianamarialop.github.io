---
title: "Agent Cost Calculator"
sobretitulo: "Microsoft Ignite 2026 · Table Talk TT1759"
summary: "Price an agent architecture before you build it: from its structure, not its volume, against the vendors' own prices. The same Python engine as the repository, running in your browser."
lab: true
ShowToc: false
ShowReadingTime: false
ShowBreadCrumbs: false
ShowPostNavLinks: false
depois: |
  ## Run it on your machine

  Python 3.8 or newer and nothing else: no `pip install`, no API key, no cloud account.

  ```bash
  git clone https://github.com/julianamarialop/agent-cost-math
  cd agent-cost-math
  python agent_cost.py --architecture architecture.example.json
  python agent_cost.py --architecture architecture.example.json --live
  python live_prices.py --check
  ```

  `--live` reads the prices at that moment from the Anthropic pricing page and from the Azure Retail Prices API. `live_prices.py --check` compares the hand table in the repository with those sources and exits with an error when they disagree. To price your own system, edit `architecture.example.json`: one entry per component, with its role, monthly volume, model and, for loops, the iteration ceiling.

  ## At Microsoft Ignite 2026

  This page is the companion to the Table Talk **TT1759, "Agent Cost Is an Architecture Decision, Not a Token Count"** (Agent Platform, level 300), in person in San Francisco. A Table Talk is a conversation, not a lecture: bring your own architecture and we price it at the table.
---

Most agent cost estimates multiply requests by a price per request. That number is wrong in a predictable direction, because volume is not what sets the bill. Orchestration is: which components exist, what role each one plays, how many turns its loop takes, which model it runs and how much context it rereads on every turn.

The example below is a claims triage with five components. The router handles four times more requests than the claim specialist and costs thirty six times less. Change any input and the calculator prices it again, or refuses when the architecture is missing something it needs, because a line that enters an estimate at zero disappears from the proposal and nobody notices.

Nothing on this page is computed in JavaScript. Your browser runs the same Python file that is in the repository, so the numbers here are the numbers on the command line. The calculator calls no model: it is arithmetic over prices read from the vendors' public sources.
