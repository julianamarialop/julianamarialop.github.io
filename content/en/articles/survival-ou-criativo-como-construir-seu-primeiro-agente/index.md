---
title: "Survival or Creative: How to Build Your First AI Agent on Oracle Without Ever Having Opened the Console"
slug: "survival-or-creative-build-your-first-ai-agent-on-oracle"
date: 2026-09-08T15:55:00Z
summary: "Anyone who has played Minecraft knows the first decision in the game isn't about where to build. It's about which mode to play."
tags: ["AI Agents", "Oracle", "Copilot", "MCP", "Costs", "Microsoft Fabric"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/survival-ou-criativo-como-construir-seu-primeiro-agente-lopes-2shtf"
cover:
  image: cover.png
  alt: "Survival or Creative: How to Build Your First AI Agent on Oracle Without Ever Having Opened the Console"
  relative: true
---

Anyone who has played Minecraft knows the first decision in the game isn't about where to build. It's about which mode to play.

In Creative, your inventory comes full. You open the menu, drag in whatever block you want, and the house goes up in minutes. In Survival, you start empty-handed: you punch a tree to get wood, craft a workbench, then a pickaxe, then head down into the mine. The same house takes hours.

The Creative player builds faster. The Survival player knows where every block came from, what it cost, and what happens if they want to move to another biome.

That's exactly the difference between the two ways of building enterprise agents today. And if you've never opened an Oracle console in your life, this article is for you, because we're going to play Survival from start to finish, punching the first tree and making it all the way to the debug screen, with code that actually works.

On one side, OCI Enterprise AI, which went GA in March 2026. On the other, Copilot Studio, rebuilt at Build 2026. I'll spend most of the time on the first one, because it's the less known and the more poorly explained of the two.

### Why Oracle Decided to Sell Blocks

[Oracle](https://www.linkedin.com/company/oracle/) spent years with a perception problem. Everyone knew it had databases and ERP. Almost nobody associated its name with an AI platform.

OCI Enterprise AI was the answer, and it brings together in a single offering three layers that used to live apart.

The first is intelligence, meaning the models and inference. And here it's worth noticing something almost nobody expects from Oracle: the catalog is third-party. Grok from xAI, Gemini from Google, open gpt-oss, Cohere models, and the option to import your own.

The second is the ability to act, meaning the agents and the tools. Document search, a code interpreter in an isolated container, function calling, MCP server calls, and question-to-SQL conversion.

The third is control, which comes built in instead of being stitched on later. Identity through OCI IAM, zero data retention endpoints, tracing of every step executed, a sovereign AI option, and dedicated clusters for anyone who needs isolation.

The smartest decision this platform made was about the API. Instead of inventing its own dialect, Oracle adopted the OpenAI Responses API as its interface. You use the official OpenAI SDK, swap the base URL, the authentication, and the model name, and the rest of your code stays the same. LangChain, LlamaIndex, and the OpenAI Agents SDK work without refactoring.

Translating for anyone who has never seen Oracle: you don't need to learn Oracle to use Oracle. That's the whole point.

### Entering the World

Let's build for real. The scenario is an agent that answers questions about the internal reimbursement policy and queries the expense system when it needs a real number.

### 1. Permission to join the server

Nothing happens on OCI without an IAM policy. A compartment is the logical box where resources live, and the policy says who can do what inside it. Ask your administrator for:

```
allow group <seu-grupo>
to manage generative-ai-family
in compartment <seu-compartimento>        
```

This is a sandbox policy, the equivalent of joining the server with permission to build anywhere. In production you narrow it down, and in step 3 I'll show how to tie the permission to a specific key.

### 2. Generating the world, and the choices you can't take back

A project is the resource that organizes agents and related assets. You create it through the console, and on that screen there are three decisions a lot of people click through without reading.

Retention defines how long responses and conversations are kept, with a maximum of 720 hours, or 30 days.

Short-term memory compaction summarizes recent history to save tokens and latency. You choose the compaction model at creation time and can't change it afterward.

Long-term memory extracts and persists important information from conversations as embeddings, and requires choosing an extraction model and an embedding model at creation time.

In those last two cases, if you enabled it and want to undo it, the way out is to delete the project. It's like the world seed. Once you pick it, that's the one. Save the project's OCID; it goes into the code.

### 3. The pickaxe

Create a Generative AI API key through the console, grab its OCID, and tie the permission to that specific key:

```
allow group <grupo-dos-builders>
to manage generative-ai-response
in compartment <seu-compartimento>
where ALL {request.principal.type='generativeaiapikey',
request.principal.id='<ocid-da-chave>'}        
```

An API key is for testing and early development. For production, Oracle's recommendation is IAM authentication, with an instance or resource principal, which avoids long-lived credentials.

### 4. Punching the first tree

Install the OpenAI SDK, not the OCI SDK. That detail trips up a lot of people on day one.

```
pip install openai        
```

And the first agent:

```
from openai import OpenAI

client = OpenAI(
    base_url="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com/openai/v1",
    api_key="<sua-api-key>",
    project="ocid1.generativeaiproject.oc1.us-chicago-1.xxxxxxxx"
)

response = client.responses.create(
    model="xai.grok-4.3",
    input="Explique em uma frase o que é um banco de dados."
)

print(response.output_text)        
```

Three things to notice, because they explain the philosophy of the entire platform.

The base URL carries the region. Swap us-chicago-1 for yours and the traffic changes continents, which matters when there's a data residency requirement.

The model is a string, and Oracle hosts third-party models. Grok from xAI, Gemini from Google, open gpt-oss. Switching models means changing one line, and that's how you trade cost against quality without rewriting the application.

If you want dedicated capacity instead of on-demand, the model identifier becomes the OCID of the cluster endpoint. Same code, isolated infrastructure.

### 5. The workbench

An agent that only knows what the model already knew is useless for anything enterprise. It needs to answer based on your reimbursement policy, not based on the internet.

You upload the file, create a vector store, and declare the search tool right in the call:

```
response = client.responses.create(
    model="openai.gpt-oss-120b",
    input="Qual o prazo para solicitar reembolso de viagem?",
    tools=[
        {
            "type": "file_search",
            "vector_store_ids": ["<id-do-vector-store>"]
        }
    ]
)        
```

Notice that you didn't build a RAG pipeline. Retrieval is managed by the platform. It's the game's workbench, that moment when loose blocks become a tool.

### 6. Redstone, or the agent that acts

Looking things up in a document is nice, but a real agent executes. Function calling is the standard for that, and the mechanics matter: the model doesn't run your function. It returns the function's name and arguments, your application executes it, and you send the result back.

```
tools = [
    {
        "type": "function",
        "name": "consultar_despesas",
        "description": "Retorna as despesas lançadas por um colaborador em um período.",
        "parameters": {
            "type": "object",
            "properties": {
                "colaborador": {"type": "string"},
                "mes": {"type": "string", "description": "Formato 2026-08"}
            },
            "required": ["colaborador", "mes"],
        },
    },
]        
```

You're the one who executes. You're the one with access to the system. The model only asks. For enterprise architecture, that boundary is the difference between a proof of concept and something that passes a security review.

Count the round trips on that path: the application sends the prompt, the model returns the call, the application executes, the application returns the result, and only then does the model answer. That's two full trips between your application and the platform.

If the tool already exists on an MCP server, you cut that back-and-forth in half. Declare the server right in the call and the platform talks to it directly, without handing control back to your code midway. Three steps instead of five, one trip instead of two:

```
response = client.responses.create(
    model="openai.gpt-oss-120b",
    tools=[
        {
            "type": "mcp",
            "server_label": "despesas",
            "server_url": "https://interno.exemplo.com/mcp",
            "require_approval": "never",
            "allowed_tools": ["consultar_despesas"]
        }
    ],
    input="Quanto o time de dados gastou em viagem em agosto?"
)        
```

### 7. The treasure map

This is the most Oracle piece of all, and the one that matters most to anyone who works with data. Enterprise AI's NL2SQL converts a natural language question into validated SQL, using a semantic enrichment layer that maps business terms to tables, columns, and joins.

The security detail that deserves applause: NL2SQL generates the SQL and doesn't execute it. The one that executes is the Database Tools MCP Server, using the end user's identity. And the configuration requires two separate connections: an enrichment one, with higher privilege to read metadata and samples, and a query one, with lower privilege to run on the user's behalf.

If you come from data engineering, you recognize the pattern immediately. It's separation of duties applied to an agent.

### 8. Pressing F3

Every Minecraft player knows the debug screen. In the Responses API it comes for free: every response carries an output field that is the list of steps executed, with types like message, file\_search\_call, and mcp\_call.

```
for item in response.output:
    print(item.type)        
```

Native traceability, without instrumenting anything. And if you want full observability, with latency and cost, you can plug in Langfuse by swapping only the OpenAI client import.

### Creative Mode

On the other side, Copilot Studio solves the same problem with a full inventory.

You don't write code. You create the agent on a screen, turn on generative orchestration, and the model decides on its own which tool to call. Since Build 2026 the product has four surfaces plus one: Skills, which are reusable instructions in markdown, Tools, Knowledge, Connected agents, and Memory.

Its power isn't in those surfaces. It's in Microsoft IQ, the context layer with three sources: Work IQ, with email, chat, files, calendar, and people from Microsoft 365; Fabric IQ, with business data in Fabric; and Foundry IQ, with knowledge bases indexed by Azure AI Search. Connecting a source gives you read and action at the same time, within the signed-in user's permissions.

If your company lives in Microsoft 365, the inventory is already full and the house goes up in minutes. If it doesn't, you're in Creative mode in a world where the blocks that matter didn't come in the menu, and every connector is an attempt to import blocks from another world.

Putting the two side by side, the difference shows up in five points. You build either by writing code against an API or by clicking through screens with automatic orchestration. The agent runs in your OCI account, in the region you choose, or on Microsoft's platform. The context you get for free is your database and your files on one side, and Microsoft 365, Fabric, and Foundry on the other. The bill arrives either per character transaction and cluster commitment, or per credit consumed per action. And each one wins where the data already lives.

### The Cost of Each Block

Oracle charges for ore. On-demand inference is metered in transactions, and a transaction is one character, counting prompt and response together. A dedicated cluster requires a minimum commitment of 744 unit-hours, which is a full month. Imported models don't carry that requirement.

Microsoft charges for construction. Copilot Credits come in packs of 25,000 for 200 dollars a month, or pay-as-you-go on Azure at the same rate.

That changes who approves the bill inside the client. One goes to infrastructure, with capacity and a monthly commitment. The other goes to the business side, with credit per action. I've seen proposals get miscalibrated by missing this and end up in front of the wrong committee.

### In the End, the Same Build

Whoever plays Survival and whoever plays Creative end up with the same house on the screen. What changes is who carried the materials and how much each one knows about their own build.

And the two modes are converging faster than the sales pitch admits. Oracle and Microsoft both adopted MCP as the tool protocol. Both decided that an agent needs its own identity, one with IAM authentication on hosted endpoints, the other with an automatic Entra Agent ID on every new agent since July 2026. Both understood that reusable instructions need to be a versionable artifact, not text pasted into a field.

Coming from opposite starting points, they arrived at the same three conclusions. It's as if the two factories had agreed on the same fitting.

So the question isn't which mode is better. It's which side of the boundary holds the data that drives your business. If the answer is email, meetings, and files, the Creative inventory already has you covered. If it's a database, your own applications, or data that can't cross a geographic border, grab the pickaxe.

The code is up there, and it runs today.

### References

- Quick Start Guide, Enterprise AI Agents: <https://docs.oracle.com/en-us/iaas/Content/generative-ai/get-started-agents.htm>
- OCI OpenAI-Compatible Endpoints: <https://docs.oracle.com/en-us/iaas/Content/generative-ai/openai-compatible-api.htm>
- Announcing GA of OCI Enterprise AI: <https://blogs.oracle.com/ai-and-datascience/announcing-oci-enterprise-ai-ga>
- What's New in Oracle AI, August 2026: <https://blogs.oracle.com/ai-and-datascience/whats-new-in-ai-august-2026>
- Paying for Dedicated AI Clusters: <https://docs.oracle.com/en-us/iaas/Content/generative-ai/pay-dedicated.htm>
- Build an agent, Microsoft Copilot Studio: <https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/build-overview>
- What's new in Copilot Studio: <https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new>
