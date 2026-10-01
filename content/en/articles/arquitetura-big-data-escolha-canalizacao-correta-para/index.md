---
title: "Big Data Architecture: Choose the Right Plumbing for Your Pipelines"
slug: "big-data-architecture-choose-the-right-plumbing-for-your-pipelines"
date: 2020-06-15T16:40:00Z
summary: "Last week, I wrote an article about data pipelines (check it out here) covering the main characteristics of a robust and optimized build, ideally using a…"
tags: ["Data Engineering", "Azure", "Costs"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/arquitetura-big-data-escolha-canaliza%C3%A7%C3%A3o-correta-para-lopes"
cover:
  image: cover.jpg
  alt: "Big Data Architecture: Choose the Right Plumbing for Your Pipelines"
  relative: true
---

Last week, I wrote an article about data pipelines [(check it out here)](https://www.linkedin.com/pulse/pipeline-de-dados-o-encanamento-na-sua-empresa-%C3%A9-%C3%A1gua-lopes/ ) covering the main characteristics of a robust and optimized build, ideally using a Big Data environment.

Continuing on that theme, let's look at the main components for building a highly scalable environment.

The figure below shows an architecture that uses open source technologies to implement every stage of the big data pipeline. The preparation and compute stages are often merged to optimize compute costs.

![On-premises Big Data environment](img-01.png)

The main components of big data architecture and technology are the following:

- **HTTP / MQTT endpoints** for data ingestion and for serving results. There are several frameworks and technologies for this.
- **Pub/sub message queue** for ingesting high-volume streaming data. Kafka is currently the most common choice in on-premises environments.
- **High-volume, low-cost data storage** for the data lake (and data warehouse): Hadoop HDFS or cloud blob storage such as AWS S3 or Azure Blob.
- **Query and data catalog infrastructure** to turn a data lake into a data warehouse. Apache Hive is a popular query language option.
- **MapReduce batch compute engine** for high-throughput processing, for example Hadoop MapReduce and Apache Spark.
- **Data streaming**, for example Apache Storm and Apache Flink. Apache Beam has also emerged as an option for data flows.
- **Machine learning frameworks** for data science and ML. Scikit-Learn, TensorFlow and PyTorch are popular options for building and training models.
- Deployment **orchestration** options include Hadoop YARN and Kubernetes / Kubeflow.

### Big Data Architecture in the Cloud

With the rise of computing as a service, you can stand up your environment faster and get more out of your money. Several components in the architecture can be replaced by equivalent services from the cloud provider.

Typical big data pipeline architectures on *Amazon Web Services, Microsoft Azure and Google Cloud Platform (GCP)* are shown below. Each one maps closely to the general big data architecture discussed in the previous section. You can use them as a reference to shortlist the technologies that fit your needs.

### AWS Big Data Environment

![AWS Big Data environment](img-02.png)

### **Azure Big Data Environment**

![No alt text was provided for this image](img-03.png)

### Google Big Data Environment

![Google Big Data environment](img-04.png)

### Conclusion

This article covered the main components for deploying a Big Data environment. There are basically two main kinds of "infrastructure", on-premises and cloud, and either way it starts with adopting storage, processing and queuing services.

Choosing the best environment depends on a few pillars to analyze, such as cost, the complexity of the service or technology to be deployed, and the infrastructure the company already has.

Thank you, and see you next time.
