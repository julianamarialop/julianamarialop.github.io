---
title: "NoSQL Databases: What Do You Mean There's No Query?"
slug: "nosql-databases-what-do-you-mean-there-is-no-query"
date: 2017-02-17T15:42:00Z
summary: "Continuing the series of articles on Big Data, let's talk a bit about non-relational databases."
tags: []
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/bancos-nosql-como-assim-n%C3%A3o-tem-query-juliana-maria-lopes"
cover:
  image: cover.jpg
  alt: "NoSQL Databases: What Do You Mean There's No Query?"
  relative: true
---

Continuing the series of articles on Big Data, let's talk a bit about non-relational databases.

Personally, when I first started hearing the term "NoSQL", my head would tie itself in knots. "**NOSQL** databases, what do you mean there's no query?", "How do you store the data?", "How do you retrieve the information?".

To start building our understanding, I'll go back to the topic of ***MapReduce*** covered in the previous article. As mentioned, in ***Hadoop*** the way to check, for example, how many times a given term showed up on social media is to use the Reduce framework.

![](img-01.jpg)

When a job starts on a node, the ***<key,value>*** pairs are transferred in chunks to the mapping nodes. A new mapping instance is created for each input record. These pairs are collected locally on the mapping node through a function on a reduce node.

So, how do you store these Key/Value pairs? With **NoSQL** databases. Basically, the big advantage of this kind of storage is how flexibly the data is structured. Notice below that we no longer have tables, rows and columns.

![](img-02.jpg)

Fine, but how do you run a simple query on this database if it can't be done with SQL? That's exactly where programming languages come into the picture. ***Python, Java, R*** and so many others help us search and cross-reference this data.

![](img-03.jpg)

Yes, I know, this image is pretty scary and makes "Selects" look like child's play. But don't panic, there are already IDEs on the market that help you build these queries.

So what happens to the names Rows, Tables and Columns? See below.

![](img-04.jpg)

Keep in mind that Key/Value databases are the simplest in the NoSQL category; there are other types based on ***Columns, Documents and Graphs***.

![](img-05.jpg)

***Column-Based (Column Stores)***: Hbase, Cassandra, Hypertable, Accumulo, Amazon SimpleDB, Cloudata, Cloudera, SciDB, HPCC, Stratosphere;

***Document-Based (Document Stores):*** MongoDB, CouchDB, BigCouch, RavenDB, Clusterpoint Server, ThruDB, TerraStore, RaptorDB, JasDB, SisoDB, SDB, SchemaFreeDB, djondb;

***Graph-Based (Graph-Based Stores):*** Neo4J, Infinite Graph, Sones, InfoGrid, HyperGraphDB, DEX, Trinity, AllegroGraph, BrightStarDB, BigData, Meronymy, OpenLink Virtuoso, VertexDB, FlockDB;

***Key-Value-Based (Key-Value Stores):*** Dynamo, Azure Table Storage, Couchbase Server, Riak, Redis, LevelDB, Chordless, GenieDB, Scalaris, Tokyo, Cabinet/Tyrant, GT.M, Scalien, Berkeley DB, Voldemort, Dynomite, KAI, MemcacheDB, Faircom C-Tree, HamsterDB, STSdb, Tarantool/Box, Maxtable, Pincaster, RaptorDB, TIBCO Active Spaces, allegro-C, nessDB, HyperDex, Mnesia, LightCloud, Hibari, BangDB.

If you missed the beginning of this series and want to learn more about Big Data, also read [**What You Need to Know About Big Data So You Don't Embarrass Yourself at the Coffee Machine**](http://www.linkedin.com/pulse/o-que-voc%C3%AA-precisa-saber-sobre-big-data-e-n%C3%A3o-passar-vergonha-lopes?trk=pulse_spock-articles)

In the next post I'll talk about ***Apache Spark***.

Thank you.
