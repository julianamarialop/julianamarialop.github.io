---
title: "Exploring New Horizons: Transform Your Organization with Data Mesh on Microsoft Fabric"
slug: "exploring-new-horizons-transform-your-organization-data-mesh-fabric"
date: 2024-07-12T13:16:00Z
summary: "Microsoft Fabric is the complete solution for all of your company's analytics needs, unifying the whole process in a single platform. From ingesting data into the data lake to delivering information to…"
tags: ["Data Architecture", "Microsoft Fabric", "Azure", "Data Governance"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/desbravando-horizontes-transforme-sua-organiza%C3%A7%C3%A3o-com-lopes-9zuaf"
cover:
  image: cover.png
  alt: "Exploring New Horizons: Transform Your Organization with Data Mesh on Microsoft Fabric"
  relative: true
---

Microsoft Fabric is the complete solution for all of your company's analytics needs, unifying the whole process in a single platform. From ingesting data into the data lake to delivering information to business users, everything can be done in Microsoft Fabric. With the ability to integrate data from many sources, such as Amazon AWS and Azure, it brings all the information together in one place.

As a SaaS (Software as a Service), Microsoft Fabric combines the power of Power BI with many capabilities from Synapse and other areas of Azure, with no need to install or configure software.

![](img-01.png)

One of the main features of Microsoft Fabric is the separation of storage and compute, which lets different compute workloads run over the same datasets. OneLake is the storage layer built on ADLS (Azure Data Lake Storage) Gen2, providing a single place for an organization to store all of its data, both structured and unstructured. This eliminates data silos and simplifies security, governance and data discovery, allowing every user and application to access the data they need.

Data Mesh is a domain-oriented decentralization of data access. The Data Mesh architecture shifts responsibility for data access from technology teams to business teams.

The four principles of Data Mesh are:

1. **Domain ownership:** Domain teams take responsibility for their data, owning both analytical and operational data.
2. **Data as a product:** Each team defines not only the data it owns, but also the data it produces and consumes from other teams. Domain teams are responsible for providing high-quality data that meets the needs of other domains.
3. **Self-service data infrastructure:** A dedicated team provides domain-agnostic capabilities, tools and systems, enabling domain teams to consume and create data products in an integrated way.
4. **Federated data governance:** Promotes standardization and interoperability of all data products across the entire Data Mesh, creating a data ecosystem that follows organizational rules and industry regulations.

Adopting the Data Mesh pattern lets business groups work independently with multiple data lakes organized around business domains.

Data is organized by domain and control sits directly over the data, providing easy access and complete governance at the data level rather than at the application level.

### Enabling Data Mesh with OneLake in Microsoft Fabric

![](img-02.png)

OneLake offers a true data mesh as a service.

An organization can have many data domains (SALES, FINANCE, MARKETING, HUMAN RESOURCES, etc.). A single dataset can be used across different domains, clouds and engines. A single data product can span multiple domains. "Shortcuts" provide the connections between domains, allowing data to be virtualized into a single data product.

Every engine can access the same data without needing to import or export it. You can choose the right engine for the right job. The engines work with data optimized in Delta Parquet as the native format.

That's all for today, folks! Thanks for reading!
