---
title: "What Tony Stark's Hall of Armor Taught Me About the Math Nobody Does: Tokens per Claude Subscription"
slug: "tony-stark-hall-of-armor-tokens-per-claude-subscription"
date: 2026-08-17T21:10:00Z
summary: "Beneath the Malibu mansion, Tony Stark keeps a gallery that tells his story better than any biography. The Mark III, gold and red, built for everyday use. The Mark XLIV, the Hulkbuster, designed for a…"
tags: ["Claude", "Costs", "Prompt Engineering"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/o-que-sala-de-armaduras-do-tony-stark-me-ensinou-sobre-lopes-z9sof"
cover:
  image: cover.jpg
  alt: "What Tony Stark's Hall of Armor Taught Me About the Math Nobody Does: Tokens per Claude Subscription"
  relative: true
---

### The Hall of Armor

Beneath the Malibu mansion, Tony Stark keeps a gallery that tells his story better than any biography. The Mark III, gold and red, built for everyday use. The Mark XLIV, the Hulkbuster, designed for a single extreme scenario. What defines Tony was never having the most powerful armor. It's knowing which armor each mission calls for. He doesn't fly to a gala inside the Hulkbuster, and when he picks wrong, the story makes him pay: too little armor means scrambling in the middle of the battle, too much armor means cost sitting idle in the hangar.

Choosing an Anthropic Claude plan is that same problem, with a twist Tony never had: the armor manuals don't publish the power output. Anthropic doesn't disclose how many tokens each plan delivers. That's why every comparison making the rounds repeats the same prices and the same adjectives without answering the only question that matters: does your workday fit inside the limit?

In this article I do the math nobody does. A simulation of tokens, windows and prompts, cross-referenced with the real usage of two kinds of people, so you can find your plan in a table row instead of finding out the hard way, with the "you've reached your limit" screen in the middle of a delivery.

### What Anthropic Publishes (and What It Doesn't)

The official numbers are prices and multipliers. Every paid plan expresses its capacity as multiples of the Pro plan per session, and each plan family structures its limits in its own way:

![](img-01.png)

What Anthropic doesn't publish is the absolute value behind the 1x. The official documentation only says that consumption varies with conversation length, the model and the features used. That opacity is a product decision, not an oversight: it gives the company flexibility to adjust allocations without breaking published commitments.

But you can simulate it. User tests estimate that Pro delivers about 44 thousand tokens per five-hour window, and the support documentation points to up to 45 messages per window on Pro, dropping to somewhere between 10 and 40 prompts in real Claude Code use. Applying the official multipliers to that baseline, the whole hall of armor becomes measurable.

### The Simulation Assumptions

The whole simulation below uses these assumptions, stated so you can disagree with them and redo the math. Baseline: Pro at roughly 44 thousand tokens per 5-hour window, other plans projected using the official multipliers. A chat prompt consumes about a thousand tokens. A coding prompt consumes from one thousand to 4.4 thousand, because it carries repository context along with it. The month has 44 windows: two per business day, 22 business days.

And the two kinds of people, with the math out in the open:

Light use, the analyst who looks things up: 15 chat prompts times a thousand tokens, plus 2 coding tasks times 2.5 thousand. Total: about 20 thousand tokens per window.

Heavy use, the dev on a project with Claude Code open all day: 10 chat prompts times a thousand, plus 25 coding prompts times 2.5 thousand. Total: about 72 thousand tokens per window.

Important: these are directional estimates, not guaranteed numbers. They're meant to size the order of magnitude, and that's exactly what a purchasing decision needs.

### The Simulation: Individual Plans

![](img-02.png)

The reading is straightforward: find your profile column and scroll down. The light user lives comfortably on Pro, using less than half the window. The heavy user blows past Pro at 164%, which is the mathematical translation of that lockout screen before lunch. On Max 5x, the same heavy day uses a third of the window. The Max 20x Hulkbuster is only justified for people who run heavier than our heavy profile: long agent sessions, large repositories, near-continuous use.

### The Simulation: Business Plans

![](img-03.png)

Here lies the nuance almost every comparison ignores. In the individual table, the bottleneck is the five-hour window, which renews on its own. In the business table, Team seats add weekly caps per person, which reset at a fixed time. Premium has the largest window in the house, 6.25 times Pro, larger even than Max 5x. But the heavy user who repeats 72 thousand tokens a day, every day, piles up against the weekly cap. Intense bursts with breaks favor Premium. A continuous marathon favors Max 20x, which knows nothing about weeks.

On the Enterprise row, honesty is mandatory: price and capacity are negotiated case by case, so there's no number to publish. What's public are the differentiators: a 500 thousand token context window in chat, audit logs, configurable data retention and SCIM provisioning. You don't read the Enterprise column; you ask about it at the negotiating table.

### The Finding Hidden in the Math

Divide each plan's price by the simulated monthly tokens and the insight the price list hides shows up. Pro, Team Standard, Max 5x and Team Premium cost practically the same per token: around 10 dollars per million. Pricing is linear; you pay in proportion to what you can consume. The exception is Max 20x: about 5 dollars per million, half the unit cost of all the others.

In other words: the only volume discount in the hall of armor is at the very top. For people who really consume, the Hulkbuster isn't a luxury, it's the best unit price in the catalog. For people who don't, it's still the most expensive armor in the hangar.

### What the Price Doesn't Show: Governance

If the decision were only about capacity, the conversation would end at the tables. But the Team plan exists for another reason, and it doesn't show up in any token column: the control layer. SSO and domain capture, role-based permissions, spending controls per organization and per person, enterprise search, connectors to work tools, and the data processing agreement that passes the client's security review. When someone leaves the team, access is revoked centrally.

Team requires a minimum of two members, goes up to 150 seats and lets you mix seat types freely: a Premium for whoever does the heavy lifting, Standards for everyone else. Every seat, Standard included, has access to Claude Code and Cowork. And the admin can enable prepaid usage credits, so the team keeps working past the included limit, with a defined spending cap. Delivery week isn't a typical week, and it's cheaper to pay for occasional overage than to size the fleet for the peak.

### Conclusion: The Mission Chooses the Armor

At the end of Iron Man 3, Tony blows up the suits he's accumulated. The gesture says what the whole hall always knew: the suits were never the power. The power was the judgment.

With AI plans, that judgment is now in your hands: count the prompts in a normal day of yours, multiply by the cost of each type, and find your row in the tables. If your day fits in 44 thousand tokens, Pro is the Mark III that gets it done. If it blows past at 164%, the upgrade isn't vanity, it's math. And if your company needs telemetry on the fleet, the conversation is no longer about tokens and has become about governance.

The question was never which armor is the strongest. It's: what is your mission, and what does it consume per five-hour window?

### References

- Anthropic. What is the Team plan? <https://support.claude.com/en/articles/9266767-what-is-the-team-plan>
- Anthropic. Using Claude Code with your Pro or Max plan. <https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan>
- Anthropic. Claude plans and pricing. <https://claude.com/pricing>
- Jamie Lord. Claude Team Premium vs Max plans. <https://lord.technology/2026/03/28/claude-team-premium-vs-max-plans-usage-limits-pricing-and-which-to-choose.html>
- Layer3Labs. Claude Pro vs Max vs Team. <https://www.layer3labs.io/guides/claude-pro-vs-max-for-teams>
- BrainGrid. Claude Code Pricing 2026. <https://www.braingrid.ai/blog/claude-code-pricing>
