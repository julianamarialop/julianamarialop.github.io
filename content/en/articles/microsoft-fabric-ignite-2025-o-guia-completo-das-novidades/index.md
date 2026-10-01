---
title: "Microsoft Fabric at Ignite 2025: The Complete Guide to What's New"
slug: "microsoft-fabric-at-ignite-2025-the-complete-guide-to-whats-new"
date: 2025-11-25T15:53:00Z
summary: "Microsoft Ignite 2025 wasn't an event about future promises; it was about concrete deliveries that mark the maturity of Microsoft Fabric. The platform stopped being a collection of promising tools and became…"
tags: ["Microsoft Fabric", "Data Engineering", "AI Agents", "Databricks", "SQL", "Azure"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/microsoft-fabric-ignite-2025-o-guia-completo-das-novidades-lopes-2cp4f"
cover:
  image: cover.png
  alt: "Microsoft Fabric at Ignite 2025: The Complete Guide to What's New"
  relative: true
---

Microsoft Ignite 2025 wasn't an event about future promises; it was about concrete deliveries that mark the maturity of
[Microsoft Fabric](https://www.linkedin.com/company/microsoft-fabric-world?trk=article-ssr-frontend-pulse_little-mention)
. The platform stopped being a collection of promising tools and became a cohesive operating system for data and intelligence, where each new piece fits in to solve chronic problems we've faced for years in the data world.

The vision presented was clear: end the era of "gluing" services together with fragile pipelines and make way for an approach where business context flows natively across every layer. For anyone dealing with the complexity of enterprise data, the announcements are direct solutions to real pains: inconsistent metrics, the difficulty of integrating AI in a governed way and the barriers between transactional and analytical systems.

To understand the real impact of these changes, you have to go beyond the names and the presentations. You need to dissect each new feature, understand how it works technically and, more importantly, how it fits into the bigger puzzle. That's exactly what we'll do next: a complete, no-nonsense guide to what really matters in the Fabric announcements at Ignite 2025.

### 1. Fabric IQ: The Central Library of Business Definitions

Imagine your company is like a big professional kitchen. Each chef (department) had their own recipe for the "house special sauce", and nobody agreed on the ingredients. Fabric IQ is like creating a single, official recipe book, approved by the executive chef, that everyone has to follow. Now, when someone orders the "special sauce", everyone makes exactly the same thing.

Fabric IQ is Microsoft Fabric's semantic intelligence layer. Its main goal is to end the mess of having multiple definitions of business metrics and entities scattered across dozens of Power BI models, Analysis Services cubes and other sources. It does this through a new item called Ontology, which is where you define, in a centralized and governed way, what your business entities are (customer, product, sale), how they relate to each other and what the rules and hierarchies are.

![Fabric IQ](img-01.gif)

\_Fabric IQ\_

Fabric IQ is made up of five components that work together:

- **Ontology:** Defines the business entities, their relationships and hierarchies. It's the conceptual model of the business.
- **Semantic Model:** Adds the metrics, calculations and BI logic (DAX) on top of the ontology. It's the analysis layer.
- **Graph:** A native graph engine that enables complex queries over the relationships defined in the ontology.
- **Data Agent:** AI agents that use the ontology to understand natural language questions and answer based on the data.
- **Operations Agent:** Autonomous agents that monitor, learn and act in real time based on business context.

Before, if you had 10 different reports, you probably had 10 different definitions of "net revenue". With Fabric IQ, you define "net revenue" once in the Ontology, and that definition is reused across every report, dashboard, AI agent and even operational application. This solves three critical problems:

1. **Consistency:** All the numbers match, because everyone uses the same logic.
2. **Governance:** There's a single point of control and auditing for business logic.
3. **Agility:** New data or AI projects are born with the business "dictionary" already in place, speeding up development.

Architecturally, this changes everything. You no longer need to replicate business logic in every model. The Ontology becomes the source of truth, and you build everything on top of it. That simplifies the architecture, reduces redundancy and makes maintenance easier. It's the consolidation of the semantic layer we always dreamed of.

### 2. Fabric Data Agents: Intelligent Assistants That Understand Your Business

Think of Data Agents as specialized personal assistants. Each one is trained in a specific area of the company (sales, logistics, finance). You ask a question in plain language, and the assistant doesn't just search the organized files (structured data); it also digs through emails, contracts and documents (unstructured data) to give you the most complete answer possible.

Fabric Data Agents are conversational AI agents that reason over the data in OneLake. They work like "virtual analysts" you can query in natural language. The big evolution announced at Ignite 2025 was the expansion of these agents' power on two fronts:

1. **Reasoning over unstructured data:** Through integration with Azure AI Search, Data Agents can now be configured to query search indexes containing documents (PDFs, Word, emails, etc.). That means that when you ask a question, the agent can combine information from structured tables in the lakehouse with insights from unstructured documents.
2. **Using the Ontology as a knowledge source:** Data Agents now use the Fabric IQ Ontology as their "instruction manual". That means they already know what an "active customer", a "premium product" or a "canceled sale" is, because those definitions are centralized. This makes answers more accurate and aligned with the language of the business.

On top of that, Data Agents now integrate directly with Microsoft 365 Copilot, letting users reach them from inside Teams, Word or Excel without leaving their work environment.

Building a question-and-answer system over data has always been complex. You need to build a RAG (Retrieval-Augmented Generation) system, connect data sources, deal with security, and so on. Data Agents abstract away all that complexity. You create an agent, point it at the data sources (structured and unstructured), and it just works, automatically respecting security permissions (RLS and CLS).

![](img-02.png)

You can create a layer of reusable, governed "virtual analysts". Each Data Agent is an asset that can be shared across teams. Security is granular and native. And best of all: since the agents use the Ontology, they always speak the business's "language", reducing misunderstandings and increasing trust in the answers.

### 3. Data Factory: Modernizing Data Engineering

Data Factory received three important updates that modernize the way we build data pipelines in Fabric:

### 3.1. Native Integration with dbt

Imagine you're building a house. Before, you cut every wooden board on the spot, from scratch. Now, you buy prefabricated, certified pieces (dbt models) that fit together perfectly. Construction gets faster, more standardized and less error-prone.

dbt (Data Build Tool) has become a market standard for data transformation as code. It lets data engineers write SQL transformations in a modular, testable and versioned way. The news is that Fabric now supports running dbt projects natively as a pipeline activity in Data Factory. That means you can orchestrate your dbt jobs directly in Fabric, without external tools.

In addition, Microsoft announced a partnership with dbt Labs to bring dbt Fusion to Fabric in 2026, which promises next-generation performance.

If your team already uses dbt, you can migrate those projects to Fabric without rewriting code. If you don't use it yet, you now have one more reason to adopt it, since it's a modern data engineering practice. Native integration means fewer tools to manage and better integration with the Fabric ecosystem.

You can adopt CI/CD (continuous integration and delivery) practices for your data pipelines. Transformations become versioned, testable and reusable code. That raises the maturity of data engineering and makes collaboration between teams easier.

### 3.2. Mirroring for SAP

Think of SAP as a neighboring factory that holds valuable information. Before, to access that data, you had to send a truck, load everything, bring it to your warehouse and unload it (traditional ETL). Now, with Mirroring, it's like having a live camera pointed at the neighboring factory's inventory. You see everything in real time on your monitor (OneLake), without moving anything.

Mirroring for SAP lets you replicate data from SAP systems (such as SAP Datasphere) into OneLake in real time, with a zero-ETL approach. That means SAP data is automatically mirrored in Delta Lake format inside Fabric, available for analysis without building complex extract, transform and load pipelines.

There are two offerings:

1. **Mirroring for SAP with SAP Datasphere (GA):** Available today.
2. **SAP Business Data Cloud Connect for Microsoft Fabric:** Expected in 2026, it will enable bidirectional data sharing between SAP and Fabric.

Integration with SAP has always been one of the most complex and expensive in enterprise environments. Mirroring removes the need to build and maintain dedicated ETL pipelines, drastically cutting development time and operating costs. The data is available for analysis in near real time.

You can create a unified data architecture that includes SAP data without the traditional complexity. That opens the door to integrated analysis between SAP transactional data and the rest of the company's data, all in the same lakehouse 3.

### 3.3. AI Function Transforms for Dataflow Gen2

Imagine a production line where you need to sort products by color, size and quality. Before, that required manual inspection. Now, you've installed smart sensors on the conveyor belt that do it automatically, without stopping production.

Dataflow Gen2 now lets you apply AI-based transformations directly in the data flow, through a low-code interface. The available functions include:

- **Sentiment analysis:** Classifying text as positive, negative or neutral.
- **Entity extraction:** Identifying names of people, companies, places, etc. in text.
- **Language detection:** Automatically identifying the language of a text.

These transformations are applied at scale, with no need to write Python code or call external APIs by hand.

Enriching data with AI has always required a data scientist's intervention. Now, a data engineer or analyst can do it directly in the transformation flow, democratizing the use of AI in the data pipeline.

You can build smarter data pipelines that don't just move and transform data, but also enrich it with AI insights. This is especially useful for customer feedback analysis, document classification and other text-related tasks.

### 4. SQL Database in Fabric (GA): The Integrated Operational Database

Imagine you're building a house. Before, you had to hire an architect to design the foundation, an engineer to calculate the structure and a foreman to carry out the work. Now, you get the house move-in ready, with all the infrastructure already installed, tested and approved. You only need to worry about the decor (your application).

SQL Database in Fabric is a fully managed relational (OLTP) database, built on the Azure SQL Database engine but offered as a native SaaS experience inside Fabric. Reaching General Availability (GA) means it's ready for production workloads, with a defined SLA and full support.

The main technical characteristics are:

- **Provisioning in seconds:** Creating a database takes seconds, not hours.
- **Automatic scalability:** Compute and storage scale automatically with demand.
- **Replication to OneLake:** Transactional data is automatically replicated to OneLake in Delta Lake format, available for near real-time analysis through the SQL Analytics Endpoint.
- **Vector support:** The database natively supports creating and querying vector embeddings, essential for generative AI applications that use semantic search and RAG.
- **Security:** Includes SQL Auditing (preview) and workspace-level Customer Managed Keys (CMK) (preview) for advanced compliance.

Traditionally, you needed an operational database (Azure SQL DB) for your application and a data warehouse (Synapse, Fabric Warehouse) for analysis, with an ETL pipeline in between. SQL Database in Fabric removes that separation. You write to the operational database, and the data is already ready for analysis in OneLake, with no ETL.

This is a game changer for "translytical" (transactional + analytical) architectures. You can design simpler solutions where the application and the analytics share the same data source, reducing latency, costs and complexity. It's ideal for AI applications that need fresh transactional data and analytical context at the same time.

### 5. User Data Functions: Reusable, Governed Logic

Think of User Data Functions as specialized tools in your toolbox. Instead of improvising a different solution every time you need to tighten a screw (run some logic), you have a professional screwdriver that works perfectly and can be used on any project.

User Data Functions let you create fully managed Python functions that can be reused across different Fabric items (Pipelines, Notebooks, Power BI, etc.). The news announced at Ignite 2025 was four important integrations:

- **Fabric Activator:** Lets you invoke functions from event rules in Activator, processing events in real time.
- **Variable Library:** Integration with the Variable Library item to store settings, constants and environment variables the functions can access.
- **Azure Key Vault:** Support for securely accessing secrets (API keys, passwords) stored in Azure Key Vault.
- **Cosmos DB:** Support for reading and writing data in Cosmos DB databases (Fabric and Azure) directly from the functions.

Instead of having business logic scattered and duplicated across dozens of notebooks and pipelines, you centralize that logic in reusable functions. That makes maintenance easier (you update it in one place), improves governance (you know where each piece of logic lives) and speeds up development (you reuse instead of rewriting).

You can build a library of corporate functions used across the whole organization. That promotes standardization, reduces redundancy and makes collaboration between teams easier. The integrations with Key Vault and Variable Library make sure the logic is secure and configurable.

### 6. Partnership with Databricks: Real Interoperability with OneLake

Imagine your company (Fabric) and the company next door (Databricks) always had to exchange documents by mail, which was slow and expensive. Now, you've built a direct door between the two offices. You can just walk through and grab the document you need, with no red tape.

The partnership between Microsoft and Databricks has been deepened to enable native interoperability with OneLake. This comes in three phases:

- **Databricks Mirroring to OneLake (GA):** Available now. Data from the Databricks Unity Catalog can be mirrored into Fabric.
- **Native OneLake reads from Databricks (Preview by the end of 2025):** Databricks will be able to read data from OneLake directly through Unity Catalog, without copying it. A Databricks notebook will be able to query a Fabric lakehouse as if it were a local table.
- **Native OneLake writes from Databricks (2026):** Databricks will be able to write data directly to OneLake, with no additional storage needed.

Many organizations use both Fabric and Databricks. Before, that meant duplicating data, building sync pipelines and dealing with data egress costs. Now, both can operate on the same copy of the data in OneLake, eliminating duplication and simplifying the architecture.

You have total freedom to choose the best tool for each job. You can use Databricks Spark for a heavy transformation and, the next minute, use Power BI in Fabric to visualize that data, without creating copies. That reduces storage costs, simplifies governance and speeds up development. It's the fulfillment of the promise of a truly open data lakehouse.

### Conclusion

Microsoft Ignite 2025 delivered concrete new features that solve real problems. For us, data and AI architects, these updates are an opportunity to simplify our architectures, reduce redundancy and build smarter, more integrated solutions. Fabric is maturing quickly, and the vision of a unified intelligence platform is becoming reality.

### References

- [[1] From Data Platform to Intelligence Platform: Introducing Microsoft Fabric IQ](https://blog.fabric.microsoft.com/en-us/blog/from-data-platform-to-intelligence-platform-introducing-microsoft-fabric-iq?ft=All)
- [[2] What's New for Fabric Data Agents at Ignite 2025](https://blog.fabric.microsoft.com/en-us/blog/whats-new-for-fabric-data-agents-at-ignite-2025-unlocking-deeper-data-reasoning-and-seamless-ai-interoperability/)
- [[3] Advancing Data Integration: Innovation in Data Factory in MS Fabric at Ignite 2025](https://blog.fabric.microsoft.com/en-us/blog/advancing-data-integration-innovations-in-data-factory-in-ms-fabric-at-ignite-2025?ft=All)
- [[4] Announcing SQL database in Fabric (Generally Available)](https://blog.fabric.microsoft.com/en-us/blog/announcing-sql-database-in-fabric-is-now-generally-available-ga/)
- [[5] What's new in Fabric User Data Functions? Ignite 2025 edition](https://blog.fabric.microsoft.com/en-US/blog/whats-new-in-fabric-user-data-functions-ignite-2025-edition/)
- [[6] Microsoft and Databricks: Advancing Openness and Interoperability with OneLake](https://blog.fabric.microsoft.com/en-us/blog/microsoft-and-databricks-advancing-openness-and-interoperability-with-onelake?ft=All)
