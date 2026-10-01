---
title: "Integrating Azure Databricks and Microsoft Fabric: A Meeting of Giants! - Part IV - Extending with V-ORDERED"
slug: "integrating-azure-databricks-and-microsoft-fabric-part-4-v-order"
date: 2024-07-08T16:55:00Z
summary: "We've reached the end of the \"Integrating Azure Databricks and Microsoft Fabric\" series. Throughout this journey, we explored how these two powerful tools can be combined to optimize data analytics processes…"
tags: ["Microsoft Fabric", "Databricks", "Azure", "Power BI"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/integrando-azure-databricks-e-microsoft-fabric-um-encontro-lopes-5hvbf"
cover:
  image: cover.png
  alt: "Integrating Azure Databricks and Microsoft Fabric: A Meeting of Giants! - Part IV - Extending with V-ORDERED"
  relative: true
---

We've reached the end of the "Integrating Azure Databricks and Microsoft Fabric" series. Throughout this journey, we explored how these two powerful tools can be combined to optimize data analytics, storage, and visualization processes. If you haven't read the previous articles yet, start [here](https://www.linkedin.com/pulse/integrando-azure-databricks-e-microsoft-fabric-um-encontro-lopes-fb1af/).

The next design consideration focuses on the importance of using Microsoft Fabric and the V-Order feature. This feature is a write-time optimization for the parquet file format that enables fast data reads in Microsoft Fabric compute engines such as Power BI.

Both Databricks and Microsoft chose to adopt Delta Lake, an open-source columnar file format. However, Microsoft added an extra V-Order compression layer that delivers up to 50% more compression. V-Order is fully compatible with the open-source parquet format; every parquet engine can read it as regular parquet files.

It's worth noting that you can apply V-Ordering to tables that don't have it by using Fabric's maintenance feature.

V-Order brings notable benefits to Microsoft Fabric, especially for components like Power BI and SQL endpoints. For example, it lets Power BI connect directly to real-time data using Direct Lake mode while keeping data queries highly performant. Since there's no import process, changes in the data source show up in Power BI instantly, with no waiting for a refresh.

![](img-01.png)

It's essential to point out that using V-Order optimized tables is, for now, exclusive to Microsoft Fabric. Databricks hasn't implemented this feature yet. So, until it does, you'll need to use a service inside Microsoft Fabric to take advantage of V-Order optimized tables.

It's also worth noting that, if V-Order optimization isn't essential, the Databricks processing step between the Silver and Gold stages can still be relevant. Although this may seem redundant, it's a viable option for continuing to process data with Databricks.

Another significant reason organizations choose this design is transactional consistency across multiple tables. Maintaining that consistency, especially in the Gold stage, is crucial. Currently, Spark only supports transactions on individual tables. So, if there are data inconsistencies across tables, they have to be resolved through compensating measures. For example, you can commit inserts to several tables, or to none of them if an error occurs. If you're changing the details of a purchase order that affect three tables, you can group those changes into a single transaction. That means that when you query those tables, they'll have all the changes or none of them. This concern for integrity highlights the importance of an environment that can manage complex transactions across multiple tables. Microsoft Fabric Warehouse is the only platform that supports this on top of Delta Lake. To learn more, click here.

In the updated architecture, shown in the image above, Synapse Engineering now acts as the processing engine from the Silver stage to Gold. This approach ensures that all tables are V-Order optimized. In addition, Synapse Warehouse was added for use cases that require transactional capabilities. However, these architectural changes require data engineers to navigate across different data processing services. So it's essential to provide clear guidance to every team. For example, you can set guidelines for the Bronze and Silver stages using native Databricks features, such as ingestion tracking with AutoLoader and validations with Delta Live Tables to ensure data quality. And, for the Gold stage, focus on building integration logic specific to consumption, exclusively with Microsoft Fabric.

### Conclusion

Integrating Azure Databricks with Microsoft Fabric offers organizations a wide range of benefits and possibilities. Combining the flexibility and scalability of Azure Databricks with the simplicity and intuitive features of Microsoft Fabric can considerably improve how data is used and managed across every layer. There are several architectural design options, from enhancing a Databricks-centric architecture with a Microsoft Fabric layer to incorporating a OneLake gold layer into the architecture to improve performance and security.

In addition, the introduction of V-Order optimization in Microsoft Fabric and the use of additional components can significantly simplify data processing and increase its efficiency. However, these combinations or integrations require careful consideration, since they may involve moving between services and balancing flexibility, data security, and isolation.

And that wraps up our series of articles exploring the integration between Databricks and Microsoft Fabric! Thanks for reading!
