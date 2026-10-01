---
title: "May the Analytical Force Be with You: Exploring Databricks Star Wars Style"
slug: "may-the-analytical-force-be-with-you-exploring-databricks-star-wars-style"
date: 2024-09-23T15:56:00Z
summary: "In recent years, Databricks has established itself as a powerful platform, much like the Force that guides the Jedi on their missions, helping companies accelerate their data and analytics projects. Just as the union between the…"
tags: ["Databricks", "Security", "Costs", "Azure", "Data Governance", "Data Engineering"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/que-for%C3%A7a-anal%C3%ADtica-esteja-com-voc%C3%AA-explorando-o-databricks-lopes-kkcvf"
cover:
  image: cover.jpg
  alt: "May the Analytical Force Be with You: Exploring Databricks Star Wars Style"
  relative: true
---

In recent years, Databricks has established itself as a powerful platform, much like the Force that guides the Jedi on their missions, helping companies accelerate their data and analytics projects. Just as the union between the Force and the Jedi creates harmony, Databricks brings the *data warehouse* and the *data lake* together in one balanced, powerful solution: the **lakehouse**.

But how, exactly, can we **structure** and configure a Databricks platform efficiently so it's as precise as a lightsaber in the hands of a Jedi? Just as the Jedi follow their code of honor, we also need a set of best practices to make sure Databricks runs in perfect harmony, protecting our data as if it were the Resistance's greatest secret.

In this article, we'll set off on our galactic journey and explore the main **pillars** that make up a well-architected Databricks platform. From **data governance** (our organizing "Force") to **cost optimization** (the fuel that keeps the ride across the galaxy smooth), we'll cover everything you need to master this powerful tool.

So, ready for the mission? May **governance** be with you! 🌌

To kick off our best practices journey, let's break the topics down as follows:

## 1. Data Governance

The first step toward a solid architecture is making sure the data truly adds value to the business and supports the company's strategy. Data governance involves overseeing policies and processes to ensure data is reliable, secure, and used efficiently.

**Data governance** in Databricks goes beyond simply storing and accessing information. It involves a set of **best practices** to make sure data is always secure, high quality, and compliant with the organization's policies and regulations. Let's look at how to apply these concepts clearly and effectively:

### 🔍 1.1. Data Classification and Tagging

First of all, it's essential to **classify and understand** the sensitivity and importance of the data. This helps you identify data that requires more protection, such as confidential or restricted data, and also define who owns the data within the company.

- **Data Classification**: Categorize data into levels such as public, confidential, or restricted. Also define the data owner, that is, who is responsible for it within the organization.
- **Tags and Comments**: Use **consistent tags** to mark tables with important information, such as the data owner, its origin, and its sensitivity level. This makes it easier to manage and monitor data usage. Adding **comments** to tables and columns also helps document important details, and they can even be generated automatically with the help of AI.
- **Data Masking**: For test or development environments, implement **data masking** techniques that protect sensitive information, making sure that data isn't improperly exposed.

### ✅ 1.2. Data Quality

Data quality is essential to make sure the decisions based on it are reliable.

- **Data Validation**: Automate consistency checks, using features such as **ADD CONSTRAINT**, to make sure data always complies with the established rules.
- **Error Handling**: Implement robust mechanisms to identify and fix data errors quickly.
- **Automated Tests**: Add automated tests to your processes to make sure everything works as expected.
- **Standardization**: Use standardized data formats, such as consistent naming conventions, unified date formats, and clear units of measurement, avoiding confusion and discrepancies.

### 🗂 1.3. Unity Catalog

**Unity Catalog** is a powerful tool for managing and organizing data securely and efficiently.

- **Data Segregation**: Use catalogs to segment data by team, business unit, or specific environment.
- **Access Control**: Implement **Role-Based Access Control (RBAC)** or **Attribute-Based Access Control (ABAC)** to make sure each user has access only to the data they need for their job.
- **Fine-Grained Permissions**: Apply detailed permissions at the database, table, row, and column level, enforcing the principle of "least privilege."
- **Audit Logs**: Enable audit logging to track access to and changes made to the data, making monitoring and regulatory compliance easier.

### 🛡️ 1.4. Data Policies

Finally, it's essential that governance practices are established and followed rigorously.

- **Data Retention Policies**: Define and enforce clear policies for the data lifecycle, using features such as **Databricks VACUUM** to ensure compliance with legal requirements.
- **Regulatory Compliance**: Make sure governance practices are aligned with regulations such as **GDPR, CCPA, HIPAA**, among others.
- **Third-Party Tools**: Take advantage of Databricks integrations with catalog and governance tools, such as **Azure Purview**, to strengthen your data control capabilities.
- **Policies and Procedures**: Create clear policies and procedures that define responsibilities, roles, and processes.
- **Regular Reports**: Produce periodic reports on governance metrics, such as access logs, data quality, and compliance status.
- **Data Lineage**: Use **data lineage** tools to trace where data comes from and how it is transformed along the pipelines, ensuring full transparency and control.

---

## 2. Interoperability and Usability

A good *lakehouse* should be able to interact easily with both **users** and other **systems**. This means its architecture must support multiple tools and technologies, ensuring a smooth, frictionless experience for everyone involved.

### 📋 2.1. General

Managing a Databricks platform requires best practices to ensure **security**, **efficiency**, and ongoing **maintenance**. Here are some guidelines that can help you structure your environment in an organized, secure way:

- **Service Principals**: When setting up accounts that need to interact with Databricks, such as accounts used by Terraform, it's essential to use **Service Principals**. This gives each service its own account, making auditing and access control easier. That way, you'll know exactly who has access and which permissions are in effect.
- **Infrastructure as Code (IaC)**: To automate the deployment and maintenance of Databricks, use **Infrastructure as Code (IaC)**. The Databricks provider for Terraform is a great solution for this, since it lets you manage the environment in a repeatable, secure way.
- **Secrets Management**: Make sure all secrets and credentials used to access other services are stored securely. Use **Databricks Secret Scopes**, which can be integrated with tools such as Azure KeyVault, to make sure this information is protected from unauthorized access.
- **CI/CD**: Deploy changes to the Databricks environment through **CI/CD (Continuous Integration/Continuous Delivery)** pipelines. All source code should be stored in a Git repository, enabling version control, change tracking, and safer development.

### 🔄 2.2. Data Sharing

Data sharing in Databricks requires following best practices to ensure **security** and **privacy**, especially when multiple partners or business units are involved:

- **Delta Sharing**: When it comes to sharing data securely, **Delta Sharing** is an ideal solution. It lets you share data with external partners or business units while keeping control over access. For extra security, set up **IP access lists** to restrict who can access the data, and implement **token rotation** to keep control tight.
- **Databricks Clean Rooms**: Use Databricks **Clean Rooms** when you need collaborative analysis across organizations without sharing the raw data. This ensures data privacy is preserved, while also complying with privacy regulations such as GDPR.
- **Marketplace**: If you need access to commercial or open data, consider the **Databricks Marketplace**, which offers a wide range of data to meet different business needs.
- **Lakehouse Federation**: **Data federation** is useful when you need to access information from several systems without migrating the data to a central location. However, consider the impact on query performance and the data ingress/egress costs when adopting this approach.

---

## 3. Operational Excellence

A cutting-edge architecture is no use if operations can't keep up. **Operational excellence** covers all the processes that keep the Databricks platform running efficiently and stably in a production environment, minimizing downtime and ensuring continuity.

### 🚀 Processing (Clusters)

Cluster management in Databricks is essential for good performance, security, and cost optimization. Here are some recommended practices:

### 3.1. General

- **Cluster Policies**: Define cluster policies to limit size and resources, or even to create "T-shirt-size clusters" (small, medium, large), tailored to the needs of different workloads.
- **Databricks Runtime**: **Databricks Runtime** is constantly evolving, with improvements in usability, performance, and security. Whenever possible, use the latest version to make sure you have access to the best features.
- **Restart Long-Running Clusters**: Clusters that run for long periods can miss critical security and operating system updates. Make sure they're restarted periodically to avoid performance and security issues.
- **Use SSD Volumes**: Clusters with workers that use SSD volumes are automatically configured with disk caching, speeding up queries and improving the performance of your environment.
- **Cluster Pre-warming**: If your queries are slow because of cluster cold starts, consider using **Databricks pools**, which let you pre-warm clusters to cut down wait times.

### ⚙️ Orchestration (Jobs)

Configuring and managing jobs in Databricks can be optimized to ensure efficiency and scalability.

### 3.2. Job Configuration

- **Job Clusters**: When configuring jobs, use **job-specific clusters**, sized correctly for the workload. Using **autoscaling** lets you handle variations in demand efficiently.
- **Job Retries**: Set an appropriate number of retries for critical jobs, taking transient failures into account. To avoid overload, implement **exponential backoff** logic in the code, adjusting the retry frequency when errors occur.
- **Service Principals**: Make sure jobs are configured with a **Service Principal** as owner, which avoids continuity problems if the job's original creator leaves the team.
- **Using Parameters**: In multi-stage jobs, use parameters to **share information** between stages, making integration and process control easier.
- **Event-Driven Jobs**: Whenever possible, choose **event-driven jobs**, which are more efficient in terms of time and cost. For one-off ingestions, consider using the COPY INTO command as an alternative.

### 3.3. Code Management

- **Version Control**: Store your code in a version control system such as Git. Use **Databricks Repos** to sync notebooks and files with the repository, making it easier to manage and track changes.
- **Modular Code**: Write **modular, reusable code** so it can be shared across different jobs and notebooks, promoting efficiency and standardization.
- **Automated Tests**: Implement **unit, integration, and E2E tests** to make sure the code works as expected, from the simplest functions to the most complex flows.
- **Databricks Asset Bundles (DAB)**: Use **Databricks Asset Bundles** to make developing and deploying jobs easier, ensuring consistency and automation.
- **CI/CD Pipelines**: Set up **CI/CD** pipelines to automate workflows in Databricks, using tools such as **Azure DevOps**, **GitLab**, or **GitHub Actions**.

### 3.4. Error Handling and Logging

- **Error Handling**: Implement robust error handling with **try-catch** blocks, making sure exceptions are handled properly without abrupt interruptions.
- **Logging**: Use **structured logging** to record events, metrics, and errors. Databricks integrates with logging tools such as **Azure Log Analytics**, which makes monitoring and diagnosis easier.

### 🧑💻 People and Processes

Beyond the technical side, it's essential to set up a dedicated team and create well-documented, standardized processes.

### 3.5. General

- **Operations Team**: Put together an **operations team** dedicated to the Lakehouse, responsible for upholding best practices, ensuring security, and monitoring the tools in use.
- **Managing Service Limits**: When designing the architecture, take into account the service limits and quotas of Databricks, the cloud provider, and **Unity Catalog**, to avoid disruptions from exceeding limits.
- **Naming Standards**: Consider creating a document with **naming standards** for Databricks objects, such as catalogs, which can follow conventions like <sigla\_do\_ambiente>-<nome\_do\_projeto>. This standardization can be enforced through CI/CD pipelines.

### 3.6. Collaboration and Documentation

- **Complete Documentation**: Fully document your workflows, code, and configurations. Use features such as **comments**, **Markdown**, and **visualizations** inside notebooks to make sure everything is clear to the team.
- **Code Reviews**: Implement a **code review** process to ensure quality and promote knowledge sharing among team members.
- **Resource Tagging**: Use consistent **tags** to mark resources according to company policies. This makes monitoring, cost management, and finding important information easier.

---

## 4. Security, Privacy, and Compliance

Protecting data and systems is essential. That's why a good Databricks setup must have robust mechanisms for **security**, **privacy**, and **compliance** with standards and regulations. Keeping the environment safe from threats is a priority for protecting the value of the data and customers' trust.

### 🛡️ 4.1. General Security

- **Security Analysis Tool (SAT)**: Databricks offers the **Security Analysis Tool (SAT)**, which helps you check whether your workspaces follow security best practices. This tool is available on [GitHub](https://github.com/databricks-industry-solutions/security-analysis-tool).
- **Multi-Factor Authentication (MFA)**: Make sure every account that uses Databricks is set up with **multi-factor authentication (MFA)**, using an appropriate identity provider. For Azure Databricks, the default identity provider is **Entra**, while for GCP or AWS you can configure **SSO**.
- **Role-Based Access Control (RBAC)**: Use **Azure AD** groups and **Databricks SCIM** to manage permissions based on the principle of **least privilege**, making sure each user has only the access they need.
- **Service Principals**: When providing automated or programmatic access to Databricks, use Azure AD **Service Principals**, making sure these identities have the minimum permissions needed to do their jobs.
- **Enhanced Security and Compliance**: If your company needs to meet compliance standards such as **PCI-DSS or HIPAA**, consider using the **Enhanced Security and Compliance** add-on to make sure the specific requirements are met.

### 👨💻 4.2. Code Management

- **Secrets**: All secrets, such as access credentials, should be stored in **secret scopes** with the appropriate permissions to protect them from unauthorized access.
- **DBFS Root**: Avoid storing data in the **DBFS root**. That's because when data is stored in the root, every user can access it, compromising security.
- **Static Code Analysis (IaC)**: Consider using tools such as **checkov**, **tfsec**, and **terrascan** to run static analysis on Infrastructure as Code (IaC), identifying vulnerabilities and compliance issues.
- **Static Code Analysis (Python)**: For Python code, use tools such as **Pylint** to check code quality and security.
- **Code Reviews**: Hold regular code reviews to make sure notebooks and jobs follow coding best practices and that no confidential information is exposed.
- **Dependency Management**: Keep dependencies up to date, applying patches regularly. Tools such as **Snyk** help identify vulnerabilities in third-party libraries and tools, which is essential for maintaining operational security.

### 🌐 4.3. Network Security (Azure)

- **Deploy Databricks in a VNet**: Use Azure **VNet injection** to deploy Databricks inside a **private virtual network (VNet)**, making sure your cluster and workspace are isolated from the public internet.
- **Private Endpoints**: Configure **Azure Private Link** to create private endpoints, enabling secure communication between Databricks and other Azure services, such as storage accounts and databases.
- **Network Security Groups (NSGs)**: Use **NSGs** to control inbound and outbound traffic on the Databricks subnets, making sure only the necessary traffic is allowed.
- **Secure Cluster Connectivity**: Configure clusters to run with **secure connectivity**, that is, with no public IP, preventing direct access from the internet.
- **IP Access Lists**: Consider implementing **IP access lists** to restrict workspace access to allowed IP addresses only.

### 🔐 4.4. Data Protection (Azure)

- **Encryption at Rest**: Make sure all data stored in services such as **Azure Data Lake Storage (ADLS)** is encrypted at rest, using Azure storage service encryption.
- **Encryption in Transit**: Enable **HTTPS and SSL/TLS** to encrypt data in transit, securing communications between Databricks and external systems.
- **Managed Identity for Azure Resources**: Use **managed identities** to give Databricks secure access to **Azure Key Vault** and other resources, without having to expose credentials.
- **Customer-Managed Keys (CMK)**: Configure **CMKs** to manage data encryption in Databricks, implementing key rotation and usage monitoring to detect unauthorized access.

### 📚 4.5. Documentation and Training

- **Disaster Recovery (DR) Plan Documentation**: Document your **disaster recovery (DR)** strategy, including backup procedures, recovery steps, and assignment of responsibilities.
- **Runbooks**: Create **runbooks** with step-by-step instructions for disaster recovery scenarios, making sure your team knows how to act quickly in case of incidents.
- **Knowledge Sharing**: Promote knowledge sharing about the DR plan across the whole organization, making sure everyone is prepared.

### 💾 4.6. Operational Security

- **Backups**: Use cross-region storage to protect your critical data, or implement backup jobs that write the data to a local region or storage account.
- **Git**: Store all Infrastructure as Code (IaC), cluster configuration, jobs, and notebooks in Git repositories. This makes recovery easier in case of incidents and promotes version control.
- **Disaster Recovery (DR) Plan**: Develop and regularly test a **disaster recovery plan**, ensuring business continuity in case of serious incidents.

### ⚙️ 4.7. Workspace Configuration

- **Credential Passthrough**: Starting with **Databricks Runtime 15.0**, Credential Passthrough will be deprecated. Instead, use **Unity Catalog (UC)** to manage identities and permissions more efficiently.
- **Environment Isolation**: Set up different workspaces for **development, stage, and production environments**, or for different business units. This isolation enables better resource management and security.
- **Data Separation**: Logically and physically separate your **confidential data** from non-confidential data, making sure sensitive information is protected.

---

## 5. Performance Efficiency

With demand for data analytics and processing growing exponentially, **performance efficiency** is crucial. Your platform must be able to adapt to changes in workload without compromising the speed and quality of results.

### 🔎 Queries

Query optimization in Databricks is essential for efficient performance and for avoiding unnecessary bottlenecks. Here are some recommended practices to maximize the performance of your queries:

### 5.1. General

- **Liquid Clustering**: Configure **liquid clustering** on the columns most often used in queries. This technique is preferable to **Z-ordering** or partitioning, since it improves lookup performance without the risk of over-partitioning.
- **Efficient File Formats**: Use file formats such as **Parquet** or **ORC**, which offer better performance and data compression. For even more efficiency, store the data in **managed tables** in the lakehouse.
- **Bigger Clusters**: When your workload grows linearly, plan for **bigger clusters**. A bigger cluster usually processes the same load faster and, in many cases, doesn't cost more, it just runs faster.
- **Data Skipping**: Databricks automatically collects statistics on the first **32 columns** defined (including nested columns). To improve query performance, make sure the most frequently queried columns are within those first 32 columns.
- **Avoid Partitioning**: With the arrival of **liquid clustering**, partitioning has become less necessary. In many cases, partitioning the data can lead to **over-partitioning**, where each partition should be at least 1 GB, which can hurt performance.

### 5.2. Performance

- **Predicate Pushdown**: Use **predicate pushdown** to filter data right at the start of query execution. This reduces the amount of data moved around and improves overall performance. When reading from an RDBMS, combine options such as **partitionColumn**, **lowerBound**, and **upperBound** to parallelize the read operation.
- **Broadcast Joins**: For smaller tables, use **broadcast joins**, sending the smaller table to all executors. This improves join performance in complex queries.
- **Skew Handling**: Identify and manage skewed data (**skew**) to make sure data partitions are distributed evenly. Techniques such as **salting** can help mitigate data skew.
- **Persistence (Cache)**: Use the .persist command to store subquery results and data in formats other than Parquet. However, avoid overusing persistence unless you know exactly what impact it will have on performance.
- **Speculative Execution**: Turn on **speculative execution** to re-run slow tasks on other nodes, which helps mitigate the impact of long-running tasks and improves total execution time.
- **Compaction**: Use the **OPTIMIZE** command to manually optimize tables in **Delta Lake**. For continuous optimization, enable **AUTO OPTIMIZE** and **AUTO COMPACT** when writing to tables, improving performance over the long run.
- **ANALYZE TABLE**: The **ANALYZE TABLE** statement collects statistics about tables within a specified schema, helping improve query performance.

### 💻 Code

Well-structured, optimized code can significantly improve query performance and the overall efficiency of the system.

### 5.3. Code

- **Avoid Wide Transformations**: Minimize the use of wide transformations, such as **groupBy** and **join**, which require shuffling large amounts of data across the network. When these operations are necessary, optimize them to reduce the impact on performance.
- **Prefer DataFrames and Datasets**: Use **DataFrames** and **Datasets** instead of RDDs, since they offer automatic optimizations and are easier to use. Take advantage of the **Catalyst optimizer** and the **Tungsten engine** to get better performance from your operations.
- **Code Profiling**: **Profile your code** regularly to identify and resolve performance bottlenecks. Use tools such as the **Spark UI** to gain insight into execution and improve efficiency.
- **MERGE Statements**: When possible, use **partition pruning** during MERGE operations, optimizing how these operations run.

### 5.4. Timestamps

- **Timestamps**: In Databricks, **timestamps** are stored as floating-point numbers, representing the number of seconds (and fractions of a second) since the Unix epoch.
- **Notebooks and Time Zones**: The value of timestamps displayed in notebooks is adjusted to the current session's time zone, which is usually **UTC**. If the data in the file doesn't contain a time zone indicator, timestamp parsing may depend on the session's time zone.
- **SQL Warehouses**: In **SQL warehouses**, the default time zone is also **UTC**, unless configured otherwise. However, there is no time zone offset or indicator.

---

## 6. Cost Optimization

Finally, a good architecture can't forget about **cost optimization**. Managing resources smartly and effectively ensures the company maximizes its return on investment, delivering value without waste.

Controlling costs in Databricks is essential to make sure you're getting the most out of the platform without going over budget. Here are some practices to help you manage costs effectively:

### 💰 6.1. Cost Monitoring

- **Regular Monitoring**: It's essential to constantly monitor usage and costs in Databricks. Use the **Cost Analysis** available in Databricks or third-party tools to get a clear view of your consumption. In the **Databricks account console**, there's a dedicated page for analyzing **DBU** (Databricks Units) usage, although it doesn't include VM or storage costs.
- **Budgets and Notifications**: Databricks offers a **budget setting** feature, where you can set up notifications to be alerted if usage exceeds the set amount, helping keep spending under control.

### 💰 6.2 Optimized Clusters

- **Cost-Efficient Cluster Configurations**: Use cluster configurations that offer a good cost-benefit ratio. For **non-critical** workloads, consider using **spot instances**, which are cheaper but can be interrupted at any time. To ensure resilience, implement a retry policy when using these instances.
- **Auto-Termination Policies**: Configure **auto-termination** policies for idle clusters, keeping unnecessary clusters from running and racking up costs.
- **Graviton Clusters (AWS)**: If you're running on AWS, consider using **Graviton clusters**, which offer a better price/performance ratio than other instance types.

### 💰 6.3 Photon and Query Optimization

- **Photon Runtime**: The Databricks **Photon Runtime** offers a significant performance boost compared with traditional Spark, while also being more cost-efficient. It's ideal if you're looking to optimize performance without raising spending.
- **Query Optimization**: Regularly review and optimize your Spark queries. Use the **Spark Query Profile** and analyze the **execution plans** to identify performance bottlenecks. Making queries more efficient reduces execution time and, as a result, costs.

### 💰 6.4 Serverless Instances

- **Serverless Options**: When appropriate, consider using **serverless SQL warehouses**, **workflows**, and **notebooks**. These options can be more economical, since you pay only for the time you use, without having to keep dedicated clusters running.

---

## 🔄 7. Reliability

Failures happen. But the question is: how does your platform react to them? The **reliability** of a Databricks system involves the ability to recover quickly from failures and keep operating without affecting critical business processes.

### 📊 7.1. Monitoring and Logging

Keeping a Databricks environment running efficiently requires a solid monitoring and logging strategy. Here are some recommended practices to ensure the integrity, performance, and security of your environment:

- **Enable Audit Logs:** Turn on **audit logs** in Databricks to capture detailed information about activity, such as login events, data access, and administrative actions. These logs help keep a history of operations and can be configured with **audit filters** to prevent data leakage between different environments.
- **Azure Monitor:** Use **Azure Monitor** to track the health and performance of your Databricks environment, making sure operations are running as expected and spotting potential problems before they get worse.
- **Integration with Monitoring Tools:** When needed, integrate Databricks with monitoring tools such as **Datadog, Prometheus, Splunk**, or **Azure Monitor** itself, to improve visibility into the environment and the tracking of critical metrics.
- **Cluster Monitoring:** **Regularly monitor** your clusters, checking their health, performance, and logs. Set up **automatic alerts** for important metrics, such as CPU usage, memory, or job duration, to avoid unexpected outages. Integrating with platforms such as **Slack** or **PagerDuty** can be useful for getting immediate notifications.
- **Resource Management:** Monitor cluster resource usage with tools such as **Ganglia** or the **Databricks Cluster UI**, making sure resources are being used efficiently.
- **Auto Loader Monitoring:** **Auto Loader** lets you inspect the state of a data stream through a **SQL API** and the **Spark Streaming Query Listener**, providing detailed insight into the files processed and the state of queries in real time.
- **Job Monitoring:** Use the **Databricks Jobs** interface to monitor job status and performance. You can also implement **custom monitoring** for specific metrics, making bottlenecks easier to spot.
- **Delta Live Tables Monitoring:** Every pipeline in **Delta Live Tables** produces an **event log** that includes audit logs, data quality checks, pipeline progress, and data lineage information. This makes it easier to keep track of pipelines continuously.
- **Streaming Monitoring:** With the **Structured Streaming** interface, you can monitor input rates, processing rates, and latency for your streaming queries. The **StreamingQuery.progress** method provides detailed reports in JSON format for deeper analysis.
- **ML and AI Monitoring:** For **monitoring Machine Learning and AI models**, use inference tables that continuously record model inputs and outputs in a **Delta table**. This lets you monitor, debug, and optimize models with the help of SQL queries, notebooks, and Lakehouse monitoring tools.
- **Security and Cost Monitoring:** Security monitoring should be implemented to ensure compliance and privacy. On top of that, monitor and control costs regularly to avoid budget surprises.

### 📦 7.2. Other Important Aspects

- **Default Workspace Storage:** Avoid using the workspace's **default storage** for production data. Instead, create dedicated storage locations, configured and tuned to your specific needs, ensuring greater security and flexibility.
- **Resilience to Availability Zone (AZ) Failures:** Databricks is already **resilient to AZ failures** by default. Make sure clusters are configured for **Auto-Scaling** and have a retry policy for jobs. Control plane functionality should be restored about 15 minutes after an AZ failure.
- **Regional Failure:** Although an **active-active** multi-region deployment in Databricks is usually not very financially viable, it's recommended to use **Infrastructure as Code (IaC)** to create a secondary deployment in a backup region. Use replicated cloud storage to ensure continuity of operations.

### 🛠️ 7.3. Infrastructure on Azure

- **GRS (Geo-Redundant Storage):** In most cases, GRS (Geo-Redundant Storage) offers an economical storage option while still guaranteeing 16 nines of durability. However, if regional recovery time is critical, consider using GZRS (Zone-Redundant Storage).

---

That wraps up our galactic journey through Databricks, exploring the main pillars for setting up this powerful platform strategically and efficiently.

Just as a Jedi masters the Force, mastering Databricks requires best practices that keep data governance, cost optimization, and performance in balance. These guidelines are like the Jedi code, offering guidance but always flexible enough to adapt to the needs and realities of each organization.

May the power of data be with you as you build a successful platform!

Thank you for reading, and be sure to follow the other articles in the newsletter.

## References

Databricks SAT: <https://github.com/databricks-industry-solutions/security-análise-t>

Data Lakehouse: <https://learn.microsoft.com/en-us/azure/databricks/lakehouse-arch>

Best practices: <https://learn.microsoft.com/en-us/azure/databricks/data-governan>

Protection: <https://www.databricks.com/blog/data-exfiltration-protection-with->

Cluster connectivity: <https://learn.microsoft.com/en-us/azure/databricks/security/netw>

Databricks budgets API: <https://www.databricks.com/blog/best-practices-cost-management-databricks#:~:text=Warehouse%20creation%20permissions.-,Monitoring%20usage,-Along%20with%20controlling>

Databricks Photon: <https://www.databricks.com/product/photon#:~:text=no%20rewrite%20required.-,Por> [que%20Photon%3F,-Desempenho%20da%20consulta](https://www.databricks.com/product/photon#:~:text=no%20rewrite%20required.-,Why%20Photon%3F,-Query%20performance%20on)
