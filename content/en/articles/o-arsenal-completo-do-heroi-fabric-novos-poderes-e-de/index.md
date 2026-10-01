---
title: "The Fabric Hero's Complete Arsenal: New Powers and Gear for July 2025"
slug: "fabric-hero-complete-arsenal-new-powers-and-gear-july-2025"
date: 2025-07-16T14:19:00Z
summary: "July 2025 arrived with a shower of updates that turned Microsoft Fabric into an even more powerful superhero. Like any self-respecting hero, Fabric never stops evolving, picking up new powers and…"
tags: ["Microsoft Fabric", "Data Governance", "Security", "Azure", "SQL", "Databricks"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/o-arsenal-completo-do-her%C3%B3i-fabric-novos-poderes-e-de-lopes-gx1pf"
cover:
  image: cover.jpg
  alt: "The Fabric Hero's Complete Arsenal: New Powers and Gear for July 2025"
  relative: true
---

July 2025 arrived with a shower of updates that turned [Microsoft Fabric](https://www.linkedin.com/company/microsoft-fabric-world/) into an even more powerful superhero. Like any self-respecting hero, Fabric never stops evolving, picking up new powers and gear to face the increasingly complex challenges of the data world.

This month was especially notable, with six major updates that significantly expanded the platform's capabilities. From a new cosmic armor to real-time gadgets, by way of custom shields and interdimensional bridges, our hero's arsenal has never been so complete.

Let's explore each of these new powers and see how they can transform the way we work with data, making our missions more efficient, secure and powerful.

### The New Cosmic Armor: Cosmos DB in Fabric

Imagine Tony Stark developing a new version of the Iron Man armor, but this time with advanced cosmic technology. That's exactly what the launch of Cosmos DB in Microsoft Fabric represents. This new "armor" isn't just an addition to the arsenal: it's a fundamental transformation that lets our hero operate in entirely new dimensions.

Cosmos DB in Fabric brings the power of Azure Cosmos DB directly into the platform, combining high availability, dynamic scalability and AI-optimized performance in a fully managed experience. It's as if Fabric gained the ability to process NoSQL data natively, while keeping all the flexibility and power we already know.

The big revolution of this cosmic armor is automatic mirroring to OneLake. As soon as you create a Cosmos DB database in your workspace, Fabric automatically starts replicating all the data to OneLake in Delta format, in near real time. It's like having a smart backup system that doesn't just protect your data, but makes it instantly available for advanced analytics.

But this armor's powers go further. With native support for vector search and full-text search, Cosmos DB in Fabric lets you run similarity searches using vector embeddings, finding results based on the meaning and context of the data, not just keywords. It's like having a radar that detects not only objects, but also their intentions and relationships.

For teams working on modern applications, this new armor offers powerful use cases. Imagine a smart knowledge assistant that accesses manuals, support documents and chat logs stored as JSON in Cosmos DB. With vector indexing, the assistant delivers semantically relevant results for user queries, while the data replicated in OneLake enables ongoing analytics to refine the content.

### The Custom Shield: Customer Managed Keys in OneLake

Every superhero needs a reliable shield, and Captain America always knew it. Now Microsoft Fabric has its own custom shield with the launch of Customer Managed Keys (CMK) in OneLake. But unlike Captain America's vibranium, this shield can be forged exactly to your security specifications.

Customer Managed Keys are one of the most requested features among Fabric's enterprise users. By default, Microsoft already encrypts all data at rest in OneLake using Microsoft-managed keys. But for organizations in regulated industries such as finance, healthcare and government, having full control over encryption keys isn't just desirable: it's essential.

With CMK, you can use your own keys, stored in Azure Key Vault, to encrypt data in OneLake. It's like having a personal safe where only you know the combination. Imagine a financial services company that needs to demonstrate full control over data encryption to auditors. With CMK, they can show that only their security team has access to the encryption key, and that revoking the key will immediately block access to sensitive data.

The power of this custom shield goes beyond simple encryption. It offers granular control at the workspace level, letting organizations selectively encrypt only the workspaces that require enhanced data protection. It's a flexible approach that doesn't force a one-size-fits-all solution on every scenario.

The feature also supports key rotation and revocation. If a healthcare organization needs to rotate encryption keys every 90 days to stay compliant, it can automate rotation policies in Azure Key Vault without disrupting analytics workflows. And if access needs to be revoked, OneLake automatically blocks read and write operations within an hour, ensuring the data stays secure.

### The Interdimensional Bridge: Unity Catalog Mirroring

Doctor Strange always impressed with his ability to open portals between dimensions, connecting worlds that once seemed impossible to reach. Microsoft Fabric has just gained a similar power with the launch of Azure Databricks Unity Catalog Mirroring, now generally available.

This interdimensional bridge lets tables governed in Unity Catalog be accessed directly by Microsoft Fabric, creating a unified, governed experience across both platforms with no data duplication. It's as if Fabric gained the ability to "see" across dimensions, accessing data that lives in the Databricks universe as if it were native.

The magic of this bridge is its transparency. Datasets managed by Databricks become instantly usable in Fabric, keeping all the governance and access control established in Unity Catalog. It's an integration that respects existing security policies while dramatically expanding the possibilities for analytics and collaboration.

For teams working with both platforms, this interdimensional bridge removes the need for complex synchronization or data duplication processes. Data scientists can keep working in Databricks with their preferred tools, while business analysts access the same data through Power BI and other Fabric tools, all while keeping a single source of truth.

The impact of this feature goes beyond technical convenience. It represents a fundamental shift in how we think about data ecosystems, letting organizations take advantage of the best of both worlds without compromises or added complexity.

### The Real-Time Gadget: SQL Operator in Eventstream

Batman has always been known for his ingenious gadgets, specialized tools he develops for specific situations. Microsoft Fabric has just added a new gadget to its utility belt: the SQL Operator in Eventstream, a powerful tool for missions that require real-time data processing.

The SQL Operator is a significant evolution in Eventstream, offering full control over real-time data transformations using familiar SQL. While Eventstream already offered a rich no-code experience with built-in operators like Filter, Aggregate and Join, the SQL Operator lets you package all your data transformation logic in one place.

This gadget really shines in complex scenarios that require conditional logic, nested expressions, string manipulation and advanced aggregations. It's like having a multi-tool that adapts to any situation, letting you write custom transformations with a surgeon's precision and an artist's flexibility.

The development experience is intuitive and powerful. You can test your queries on real-time data before publishing, making sure the logic is right. IntelliSense support boosts productivity and minimizes errors with syntax highlighting and autocomplete. It's like having a personal assistant who knows every available function and syntax.

For teams already working with Azure Stream Analytics, this gadget offers a smooth transition, letting you bring your existing transformation logic straight into Fabric Eventstream. It's a bridge that connects existing knowledge with new possibilities, speeding up adoption and shortening the learning curve.

### The Advanced Security System: Workspace Access Limits

Just as Superman's Fortress of Solitude has advanced security systems to protect dangerous knowledge and technology, Microsoft Fabric is rolling out a new protection system: Workspace Access Limits, to be introduced in August 2025.

This advanced security system is designed to improve quality of service and reliability, and to encourage proper access control over workspaces. It's a proactive measure meant to protect both individual users and the ecosystem as a whole, making sure resources are used efficiently and responsibly.

The access limits work like a smart monitoring system that watches usage patterns and applies controls when needed. It's like having a digital guardian who understands when usage is within normal parameters and when it may be affecting the platform's overall performance.

This feature strikes a careful balance between flexibility and control. While keeping the ease of use that characterizes Fabric, it introduces safeguards that protect every user's experience. It's an approach that prioritizes the platform's long-term sustainability.

For administrators and governance teams, this system offers greater visibility and control over how resources are used, enabling more effective planning and proactive capacity management.

### The Universal Communicator: Improved SAP Connectivity

The Starfleet Federation has always relied on universal communicators to connect different species and cultures. Microsoft Fabric has just upgraded its own universal communicator with significant improvements to SAP connectivity, making it easier to integrate with one of the most important enterprise ecosystems in the world.

The new options for integrating data from SAP sources are an important step forward for organizations that depend on these systems for critical business operations. With more than 170 connectors available in Data Factory, Fabric keeps expanding its ability to talk to practically any enterprise system.

This improved connectivity is especially valuable for companies that need to unify SAP data with other sources for comprehensive analytics and AI use cases. It's like having a universal translator that not only understands different data "languages", but also harmonizes them into a common language the whole organization can use.

The improvements include more robust options for extracting, transforming and loading SAP data, letting organizations make better use of their existing SAP investments while modernizing their analytics capabilities.

### Conclusion

Each of these features doesn't just add technical capabilities; it represents an evolution in how we think about data integration, security, governance and processing. Together, they create a more robust, flexible and powerful ecosystem that can adapt to the ever-changing needs of modern organizations.

See you in the next article!
