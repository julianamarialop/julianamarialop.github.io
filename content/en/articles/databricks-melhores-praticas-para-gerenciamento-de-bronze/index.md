---
title: "Databricks: Best Practices for Managing Bronze, Silver and Gold (Medallion Architecture)"
slug: "databricks-best-practices-managing-bronze-silver-gold-medallion"
date: 2023-10-05T13:00:00Z
summary: "Many of the clients I work with implement a Medallion architecture to logically organize their data in a Lakehouse. As data flows, it moves through several stages or layers. The best-known design…"
tags: ["Data Architecture", "Databricks"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/databricks-melhores-pr%C3%A1ticas-para-gerenciamento-de-bronze-lopes"
cover:
  image: cover.png
  alt: "Databricks: Best Practices for Managing Bronze, Silver and Gold (Medallion Architecture)"
  relative: true
---

Many of the clients I work with implement a [Medallion architecture](https://www.databricks.com/glossary/medallion-architecture) to logically organize their data in a Lakehouse. As data flows, it moves through several stages or layers. The best-known design, as seen below, uses a Bronze, Silver and Gold layer. Hence the term "medallion".

Although the three-layer design is common and widely recognized, I've noticed a lot of discussion about the scope, purpose and best practices of each of these layers. I've also observed that there's a big difference between theory and practice.

### Data Platform Strategy

The most important consideration when layering your architecture is determining how your data platform will be used. A centralized, shared data platform will have a different structure from a federated, multi-platform setup used by several domains. The layers also vary depending on whether you align your platforms with the source-system side or the consumption side of your architecture. A source-aligned platform is usually easier to standardize in terms of layers and structure than a consumer-aligned platform, because of the diversity of data uses on the consumption side.

With these considerations in mind, let's explore layer by layer. For each layer, I'll start with some abstract, high-level goals and then dig deeper with practical observations.

### Landing Area

An optional layer often seen in organizations implementing a data platform is a landing area or landing zone. This is an intermediate location where data from various source systems is stored before being moved into the Bronze layer. This layer is often needed in situations where it's hard to extract data from the target source system, such as when working with external clients or SaaS vendors. In those situations, there's a dependency, or sometimes the data is delivered in a non-preferred format or structure.

The design of a landing zone varies from organization to organization. Often it's simply a blob storage account. In other cases, the landing zone is part of the data lake services, such as a specific container, bucket or folder where data is ingested. Data in landing zones tends to be highly diverse in terms of file formats, which can include CSV, JSON, XML, Parquet, Delta and others.

### Bronze Layer

The Bronze layer is usually a reservoir that stores data in its natural, original state. It contains unvalidated data (there's no need to define schemas first). In this layer, data is obtained using full loads or delta loads. Data stored in the Bronze layer usually has the following characteristics:

- It keeps the raw state of the data source in its "as is" structure.
- The data is immutable (read-only).
- It's managed using range-partitioned tables, for example using a YYYYMMDD or date/time folder structure.
- It keeps the complete (unprocessed) history of each dataset in an efficient storage format, such as Parquet or Delta.
- For transactional data, it can be appended incrementally and grow over time.
- It provides the ability to recreate any state of a given data system.
- It can be a combination of streaming and batch transactions.
- It can include additional metadata, such as schema information, source file names or a record of when the data was processed.

A common question is: "What's the best file format? Should I use Delta or Parquet?" Delta is faster, but since the data already has versioning or history through a folder structure, I don't see any compelling benefit in keeping a transaction log or applying versioning. Data in the Bronze layer is usually new data or is being appended. So if you prefer to use Parquet, that's fine. Alternatively, you can use Delta to stay aligned with all the other layers.

Some people argue that data in the Bronze layer can be useful for ad hoc queries or analysis by business users. In my experience working with clients, I rarely see raw data used as input for running ad hoc queries or analysis. Working with raw data requires a deep understanding of how the source system was designed and the crafting of complex business logic that is encapsulated in the data itself. This data usually contains many small tables and is hard to secure. In short, the Bronze layer is an intermediate layer and serves as the entry point for other layers, accessed mainly by technical teams.

### Silver Layer

The Silver layer provides a refined structure for the data that has been ingested. It represents a validated, enriched version of the data that can be trusted for downstream workloads, both operational and analytical. The Silver layer usually has the following characteristics:

- It uses data quality rules for data validation and processing.
- It normally contains only functional data, filtering out technical or irrelevant data coming from the Bronze layer.
- It applies historization, usually using type 2 or type 4 slowly changing dimension (SCD) techniques. This involves adding columns such as start, end and current.
- It stores data in an efficient storage format, preferably Delta or Parquet.
- It uses versioning to roll back processing errors.
- It handles missing data and standardizes empty or dirty fields.
- It's often enriched with reference and/or master data.
- The data is often organized around specific subject areas.
- The data is usually aligned and organized with the source system.

For the Silver layer, some points to watch include:

The Silver layer can act as a temporary storage layer in some cases, where older data can be deleted or storage accounts can be created on demand. This depends on the intended use of the data. If you don't plan to use the data in its original context for operational reporting or operational analytics, the Silver layer can be used temporarily. However, if you plan to retain history and use this data for operational reporting and analytics, it's recommended to make the Silver layer persistent.

Data in the Silver layer can be queried. So, in terms of data modeling, it's recommended to follow a more denormalized data model. That's because this design makes better use of distributed, column-based storage that is separated from compute. Although it's possible to implement a more normalized design, there are no convincing arguments for doing so, since the Delta layer already offers isolation and protection, such as schema merging to handle changes and the history available in the Bronze layer. So adding extra complexity and reducing performance is generally not recommended.

Another discussion that comes up is whether there should be data joining or integration across applications and source systems in the Silver layer. The answer depends on the scenario. If you plan to use the Silver layer for operational reporting or operational analytics, it's generally recommended not to combine or integrate data across source systems, to avoid unnecessary coupling between applications. However, if you want a more isolated design, data integration across sources can happen in a higher layer.

The same argument mentioned above also applies when you align your Lakehouses with the source-system side of your architecture. If you plan to build data products and strongly want to align data ownership, it's not advisable for your engineers to join data across applications from other domains. That would create unnecessary coupling points.

As for enrichments, such as calculations, if you plan to support operational reporting that requires enrichments, it's recommended to enrich the data in the Silver layer. This may result in some extra calibration when combining data at a later stage in the Gold layer, but it takes advantage of the benefits of flexibility.

### Gold Layer

Data in the Gold layer, according to the principles of a Lakehouse architecture, is usually organized into "project-specific" databases ready for consumption. In this context, data ownership can be considered changed, since the data is no longer aligned between source and system. Instead, it has been integrated and combined with other data.

In the Gold layer, depending on the use cases, a more denormalized, read-optimized data model with fewer joins is recommended. So a Kimball-style star schema may be appropriate. In addition, expect the following characteristics:

- Gold tables represent data that has been transformed for consumption or use cases.
- The data is stored in an efficient storage format, preferably Delta.
- The Gold layer uses versioning to roll back processing errors.
- Historization is applied only for the set of use cases or consumers, so the Gold layer can be a selection or aggregation of data found in the Silver layer.
- In the Gold layer, complex business rules are applied, which includes post-processing activities, calculations, enrichments and use-case-specific optimizations.
- The data is highly governed and well documented.

The Gold layer is usually the most complex, because its design depends on the scope of the architecture. In the simplest scenario, where your Lakehouses are aligned only with the source-system side, the data in the Gold layer will represent "data product" data. This data is generic and can be used for wide distribution across several domains after distribution. In this case, the data is expected to meet the precise needs of analytical consumers after distribution to another platform, which may also be a Lakehouse. So the data is modeled with a structure specific to the use case.

If the Lakehouse's scope is larger and covers both sides, additional layers will be needed. Some organizations call these additional layers workspace or presentation layers. In this design, the data in the Gold layer is more generic and serves as an integration layer from which data marts or subsets can be populated. Some companies also use these layers to share data with other platforms or teams, making selections and/or pre-filtering for specific use cases.

I hope you found this article useful. To everyone building a next-generation data platform, enjoy the journey!
