---
title: "Azure Databricks Delta Sharing and the Data Buffet: Pick, Serve Yourself, and Analyze!"
slug: "azure-databricks-delta-sharing-and-the-data-buffet"
date: 2025-02-06T15:11:00Z
summary: "Imagine a world where sharing data between companies is as simple as opening a delivery app and ordering your favorite meal. Instead of complicated processes, slow transfers, and worries…"
tags: ["Databricks", "Costs", "Data Governance", "Security", "Azure"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/databricks-delta-sharing-e-o-buffet-de-dados-escolha-sirva-se-lopes-z52jf"
cover:
  image: cover.jpg
  alt: "Azure Databricks Delta Sharing and the Data Buffet: Pick, Serve Yourself, and Analyze!"
  relative: true
---

Imagine a world where sharing data between companies is as simple as opening a delivery app and ordering your favorite meal. Instead of complicated processes, slow transfers, and security worries, you get instant access to reliable, up-to-date data. That's the future Databricks Delta Sharing offers: an open, secure, and efficient system for sharing data across organizations and platforms, with no headaches.

### What Is Databricks Delta Sharing?

Databricks Delta Sharing works like a big data buffet restaurant. Instead of every user having to cook their own dishes (that is, copy and replicate data), they can simply grab what they need from the self-service station, with no waste and guaranteed quality. And the best part: no endless lines or mystery dishes!

Built on the Delta Lake architecture, it lets organizations share governed data from their Lakehouses with any consumer, whether or not they're on the Databricks platform. This open protocol ensures recipients can access shared data through tools such as Python, R, SQL, and BI platforms, promoting interoperability and efficiency.

![Databricks Delta Sharing](img-01.png)

\_Databricks Delta Sharing\_

Now that you've got the concept of Delta Sharing, let's explore how it can transform the way your company shares information.

### Why Should My Company Adopt Delta Sharing?

Many companies struggle to share data securely and efficiently. Legacy processes require excessive replication, high operating costs, and security risks. Delta Sharing solves these problems by bringing:

✅ Lower costs: No need for data replication or manual transfers.

✅ Secure access: Centralized governance and fine-grained control over who accesses the data.

✅ Interoperability: Works with a wide range of tools and languages, with no lock-in to a single vendor.

✅ Real-time updates: Data is always current, without unnecessary ETL pipelines.

✅ Easy integration: Data is accessible directly by consumers in their own work environments.

Now that we know the benefits, let's look at the different types of sharing available.

### Types of Sharing in Delta Sharing

Just as a buffet restaurant offers different kinds of dishes to suit different tastes and dietary restrictions, Delta Sharing provides three distinct ways to share data, depending on your company's needs:

- **Databricks-to-Databricks Protocol:** Share data and AI assets across Databricks workspaces, with governance built into Unity Catalog.
- **Open Sharing Protocol:** Lets any consumer, even without Databricks, access shared data through open APIs.
- **Open Source Implementation:** Share data across any platform, without depending on Databricks.

Whatever method you choose, making sure recipients have efficient and secure access is essential.

### What Is a Recipient?

In Delta Sharing, the Recipient is like a buffet customer who can access the available dishes (data) as needed, without having to cook from scratch. The Recipient can be a business partner, a customer, or an internal team. Recipients don't need to be on Databricks, since Delta Sharing supports access from popular tools such as Python, SQL, Pandas, Apache Spark, Power BI, and many others.

Each Recipient receives a secure access token or a credentials file, ensuring that only authorized users can access the data.

Now that you know how the data is accessed, let's see how to set up Delta Sharing in your company.

### How to Set Up Delta Sharing in Your Account

Before you start sharing or consuming data through Delta Sharing, your company needs to set up Databricks Unity Catalog, ensuring full governance and security over the data. The setup includes:

- **Enabling Unity Catalog** in your Databricks workspace.
- **Defining Access Policies**, configuring security rules for granular control.
- **Turning on Audit Logs** to track data access and sharing.
- **Registering Recipients**, making sure only authorized users receive access permissions.

Now that your account is set up, let's see how to create and share data in practice.

### Clean Rooms: Secure, Collaborative Data Sharing

An advanced approach within Delta Sharing is the concept of Clean Rooms, a secure environment that lets different companies collaborate on data analysis without directly sharing their raw information. This is especially useful for sectors such as healthcare, finance, and retail, where data privacy is a priority.

![](img-02.png)

With Clean Rooms, companies can define rules that let partners analyze aggregated, anonymized data, ensuring compliance with regulations such as GDPR and LGPD (Brazil's data protection law). This capability lets multiple partners extract insights from the same dataset without compromising security.

### Companies Already Using Delta Sharing

Several global companies have already adopted Delta Sharing to improve the efficiency and security of their data sharing:

- **Shell**: Uses Delta Sharing to share operational insights with partners in the energy sector, ensuring efficient collaboration.
- **HSBC**: Implemented Delta Sharing to streamline compliance processes and financial risk analysis.
- **Adobe**: Uses the platform to share marketing and customer engagement data with strategic partners.
- **Nasdaq**: Uses Delta Sharing to provide secure access to market data and analytical reports for investors and regulators.

### Delta Sharing Costs

Although Delta Sharing removes the need for data replication, it can generate costs related to transferring data across different regions and platforms. The costs may include:

- **Data egress (egress fees):** When data is shared across cloud regions, the transfer may be billed.
- **Query processing:** Depending on the infrastructure used, there are costs associated with running queries on the shared data.
- **Permission and log management:** Unity Catalog lets you track access and manage permissions, which can affect usage costs.

### Cost Calculation Example

Let's walk through a practical example to estimate Delta Sharing costs:

Volume of shared data: **10 TB per month**

Data egress cost (egress fees): **$0.09 per GB**

Query processing cost: **$0.02 per query** (assuming 100,000 queries)

Log management cost: **$0.005 per log operation** (assuming 500,000 operations)

Total calculation:

- Data egress cost: **$921.60**
- Processing cost: **$2,000.00**
- Log management cost: **$2,500.00**
- Estimated total monthly cost: **$5,421.60**

Companies that share large volumes of data should consider strategies to optimize these costs, such as storing data in regions close to consumers or using data compression.

### Conclusion: Delta Sharing Is the Future of Data Sharing

With Databricks Delta Sharing, your company can finally leave behind manual, slow, and insecure data sharing processes. This shift not only increases operational efficiency but also enables a smoother, more trustworthy culture of collaboration, letting different teams and partners access critical information instantly and securely.

On top of that, adopting Delta Sharing provides a solid foundation for future innovation. With data accessible in real time and robust governance, organizations can accelerate their artificial intelligence and analytics initiatives, producing more accurate and strategic insights. This lets companies make informed decisions quickly, responding nimbly to market changes.

💡 If your company wants to collaborate efficiently, cut costs, and drive innovation, it's time to adopt Delta Sharing! 🚀 Instead of relying on transfers, copies, and replications, the data is accessible wherever and whenever it's needed, with full control and security.
