---
title: "A DW on Hadoop? How to model your Star Schema for HDFS"
slug: "a-dw-on-hadoop-how-to-model-your-star-schema-for-hdfs"
date: 2017-04-07T16:42:00Z
summary: "Over the years, data warehouses have been the main tool for company decision-making and analysis. These include conventional OLAP and ETL tools supplied by countless hardware and…"
tags: []
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/dw-com-hadoop-como-modelar-seu-star-schema-para-o-hdfs-lopes"
cover:
  image: cover.jpg
  alt: "A DW on Hadoop? How to model your Star Schema for HDFS"
  relative: true
---

Over the years, data warehouses have been the main tool for company decision-making and analysis. These include conventional *OLAP and ETL* tools supplied by countless hardware and software vendors, *DW* appliances built by combining databases and servers, in-memory databases and virtualization tools.

But how do you accommodate and process an ever-growing amount of data at an acceptable speed for analysis and for finding information that's crucial to the business?

In Brazil, we're still at a very early stage when it comes to Big Data. I believe that companies will soon start their projects to "migrate" conventional *DW* databases to *HDFS*.

> In my opinion, the BI professional of today who invests in learning
> *Hadoop, Spark* and
> *Fast Data loading methods* will be one step ahead in the job market.

The *Hadoop* ecosystem, which is evolving alongside large data environments, also has a set of technologies for building a data warehouse. For example, Apache *Hive* is a data warehouse option within the *Hadoop* ecosystem that can process large data sets stored in distributed storage environments using SQL.

![](img-01.jpg)

**So, is there a recipe or a magic formula for migrating the data? Unfortunately not, but we can follow a few guidelines.**

### **1 - Denormalize**

Denormalization is commonly used to improve performance when implementing a Star Schema model on top of the Hadoop distributed file system (HDFS). Unlike an *RDBMS*, *Hadoop* tolerates the data overlap caused by denormalization thanks to relatively cheap hardware and software.

Therefore, the decision to denormalize data sets that change frequently should be made carefully, weighing the trade-off between query performance and deployment. The following is an example of the denormalization method that can be used to build a *Hadoop*-based data warehouse.

### 1.1 - Merge Dimensions

Several dimensions with a small number of rows are bundled and turned into a single dimension data set, so the number of fact data sets and joins can be reduced. It's hard to optimize the system with a large number of joins between dimension data sets and fact data sets when using *Hadoop*.

> A small number of large files is better than a large number of small files for optimal performance with
> *Hadoop*; one large dimension is processed faster than several small dimensions.

![](img-02.jpg)

### 1.2 - Merge Facts with Dimensions

Dimension and fact data sets that are queried together are organized into a single set by applying the join during the deployment process instead of at query time on the user side.

> The data sets are joined at data load time to reduce the number of joins. It's similar to the dimension merging process, except that the merge is fact-to-dimension.

![](img-03.jpg)

### 1.3 - Generate Historical and Current Data Sets Together for Loading

Since it's usually faster to regenerate the entire data set than to update a single event, given how *HDFS* works, the data sets needed for the loading process are appended according to their temporal and business characteristics.

> It's better to reload all the current content together with the history than to run multiple updates.

![](img-04.jpg)

### 2 - Organize Fact tables in a "Columnar" way

It may sound strange, but it's much better to have hundreds of columns than millions of rows. Especially when users build a data warehouse that extracts and uses part of a dataset's columns, a columnar format that allows partial column extraction greatly improves query performance.

As an example, we can have a Sales fact organized by "Month/Year" that expands its columns with each new period.

### 3 - Compress the Data

Compression helps improve processing performance by reducing not only the size of the stored data but also the amount of disk I/O. It's better to use a compression codec that supports splittable processing so the nodes can be processed in parallel in a distributed environment.

If compression isn't feasible, additional splittable file storage formats, such as *Avro*, are needed. As with file storage, different compression methods can be used for each partition within a single data set.

### 4 - Partition the Data

Data sets are partitioned according to data query patterns, so results can be found without scanning the entire data set. Partitioning helps improve performance, since it reduces the objects a query has to scan and reduces I/O.

Once a data set is split into partitions according to some criterion, such as dates that reflect user query patterns, only one daily partition needs to be scanned when extracting data for a given date, which makes it far more efficient than a full scan of the whole data set.

> The partitioning method is similar to building a data warehouse based on an
> *RDBMS*. One difference is that, unlike an
> *RDBMS* that defines how a data set is partitioned, Hadoop creates several partitioning strategies according to a user's query patterns.

Hadoop copies the original dataset and creates several data sets, and each data set is strategically partitioned. In other words, Hadoop uses much more disk space, copying and multiplying a data set to improve performance.

### 5 - Bucketing

*Bucketing* is a process by which a dataset is split into *buckets*, groups of clustered data, using the values of a given column. Each block can have several column values as criteria, but a given value among the criteria column's values is included in only one block.

![](img-05.jpg)

Another benefit of *bucketing* is that it makes data sets small enough to use a map-side join, which loads that block into memory for fast processing.

### 6 - Index the Data

In Apache *Hive*, you can generate indexes that play roles similar to *RDBMS* indexes. *Hive* supports compact indexes, bitmap indexes and so on. It's important to first analyze user query patterns in order to generate indexes that reflect those patterns (as in an *RDBMS* indexing strategy).

> When using an index, statistics should be collected regularly to help the optimizer find the best route.

### Conclusion

The fundamental value of a data warehouse is the same, even when it's built as an application within a Hadoop ecosystem. Fortunately, data warehouse building methodology can be used without much change when building *Hadoop*-based databases.

![](img-06.jpg)

As long as the characteristics of *Hadoop* ecosystems are reflected in your physical modeling process, the data warehouse will be ready for the era of big data, where structured and unstructured data will be integrated.

*References*

- *Ralph Kimball and Matt Brandwein – Hadoop 101 for EDW Professionals*
- *Hadoop 101 for EDW Professionals – Dr. Ralph Kimball Answers Your Questions*
- *Ralph Kimball and Eli Collins – EDW 101 for Hadoop Professionals*
- *Ralph Kimball – Newly Emerging Best Practices for Big Data*
- *Ralph Kimball – The Evolving Role of the Enterprise Data Warehouse in the Era of Big Data Analytics*
- *Josh Wills - What Comes After The Star Schema?*

See also:

[NoSQL databases: what do you mean there's no Query?](https://www.linkedin.com/pulse/bancos-nosql-como-assim-n%C3%A3o-tem-query-juliana-maria-lopes)

[What you need to know about Big Data so you don't embarrass yourself at the coffee machine?](https://www.linkedin.com/pulse/o-que-voc%C3%AA-precisa-saber-sobre-big-data-e-n%C3%A3o-passar-vergonha-lopes)
