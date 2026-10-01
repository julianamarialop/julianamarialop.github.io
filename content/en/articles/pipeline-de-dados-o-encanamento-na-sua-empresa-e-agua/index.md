---
title: "Data Pipelines - Is Your Company's Plumbing Carrying Clean Water or Sewage?"
slug: "data-pipelines-is-your-company-plumbing-clean-water-or-sewage"
date: 2020-06-12T20:21:00Z
summary: "Pipeline is an English term that can be translated into Portuguese as “tubagem” or “canalização” (piping or plumbing). In our language, the concept is used to refer to a computing architecture. These virtual pipes are created…"
tags: ["Data Engineering"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/pipeline-de-dados-o-encanamento-na-sua-empresa-%C3%A9-%C3%A1gua-lopes"
cover:
  image: cover.jpg
  alt: "Data Pipelines - Is Your Company's Plumbing Carrying Clean Water or Sewage?"
  relative: true
---

### Introduction - What are data pipelines?

Pipeline is an English term that can be translated into Portuguese as “tubagem” or “canalização” (piping or plumbing). In our language, the concept is used to refer to a computing architecture. These virtual pipes are created to segment data and, in doing so, increase the throughput of a digital system.

A data flow pipeline is a series of components, or data flow blocks, and each one performs a specific task that contributes to a larger goal.

Its set of resources brings together the end-to-end operation of collecting the data, transforming it, training a model, delivering insights, and applying the model when and where action needs to be taken to reach the business goal.

Scalable, efficient data pipelines are as important to the success of analytics, data science and machine learning as an army's front-line strategies are to winning a war.

Roughly 50% of the effort in designing this orchestra goes into preparing data for analysis and *Machine Learning*. The remaining effort is split: 25% goes into making model insights and inferences easily consumable at scale, and 25% into training.

A big data pipeline ties everything together. It is the railroad on which heavy, fast freight cars run. Long-term success depends on building and deploying the services correctly.

### Perspectives - A View by Area

There are three stakeholders involved in building data analytics or machine learning applications: data scientists, engineers and business managers.

From the data science perspective, the goal is to find the most robust and computationally cheapest model for a given problem using the available data.

From the engineering point of view, the goal is to build things others can rely on; to innovate by creating new things or finding better ways to build existing things that run 24x7 without much human intervention.

As for the business perspective, the goal is to add value for customers; science and engineering are means to that end.

Looking more closely through the engineering lens, we can name the following pillars as the main characteristics for success:

- **Accessibility**: data easily accessible to data scientists for hypothesis evaluation and model experimentation, preferably through a query language.
- **Scalability**: the ability to scale as the volume of ingested data grows, while keeping cost low.
- **Efficiency**: data and machine learning results are ready within the specified latency to meet business objectives.
- **Monitoring**: automatic alerts on the health of the data and the pipeline, needed for a proactive response to potential business risks.

### Building Stages

A data pipeline has five stages, grouped into three phases in its construction:

- **Phase I** - Data engineering: collection, ingestion, preparation (~ 50% of the effort)
- **Phase II** - Analytics / Machine Learning: computation (~ 25% of the effort)
- **Phase III** - Delivery: presentation (~ 25% of the effort)

**Collection**: Data sources (mobile apps, websites, web applications, microservices, IoT devices, etc.) are instrumented to collect relevant data.

**Ingestion**: The instrumented sources pump data into various entry points (HTTP, MQTT, message queues, etc.). There may also be jobs that import data from services such as Google Analytics. Data can come in two forms: blobs and streams. All of this data is collected in a Data Lake.

**Preparation**: This is the extract, transform, load (ETL) operation that cleans, conforms, shapes, transforms and catalogs the data blobs and streams in the data lake, preparing the data for ML and storing it in a Data Warehouse.

**Computation**: this is where analytics, data science and machine learning happen. Computation can be a combination of batch and stream processing. Models and insights (structured data and streams) are stored back in the Data Warehouse.

**Presentation**: information is delivered through dashboards, emails, text messages and push notifications. ML model inferences are exposed as microservices.

![No alt text was provided for this image](img-01.png)

### Conclusion

As you have seen, a data pipeline is like an “orchestra” that performs defined tasks sequentially or in parallel within a given period of time.

The more aligned your pipeline is with the expectations of data scientists and business managers, the easier it will be to obtain insights that deliver positive results for the company.

Pipeline development also needs to be thought out and designed in an optimized way, preferably on a robust Big Data environment.

**Now think about it: at your company, are the orchestration processes and data loads robust and fast enough to meet your business demand?**

Thank you and see you next time!
