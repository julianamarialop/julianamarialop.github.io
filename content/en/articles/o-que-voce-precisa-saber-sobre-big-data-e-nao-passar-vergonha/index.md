---
title: "What you need to know about Big Data so you don't embarrass yourself at the coffee machine?"
slug: "what-you-need-to-know-about-big-data-so-you-dont-embarrass-yourself"
date: 2017-02-14T22:35:00Z
summary: "Picture this: a director at the company you work for starts asking the following questions:"
tags: []
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/o-que-voc%C3%AA-precisa-saber-sobre-big-data-e-n%C3%A3o-passar-vergonha-lopes"
cover:
  image: cover.jpg
  alt: "What you need to know about Big Data so you don't embarrass yourself at the coffee machine?"
  relative: true
---

Picture this: a director at the company you work for starts asking the following questions:

***"How many times is my company's name mentioned on Twitter?" or "What are the biggest questions or complaints from customers on our Facebook page?"***

As an IT analyst, how would you organize this data coming from social networks and produce a report or dashboard that makes sense to the leadership team?

It's precisely to answer questions like these that Big Data platforms are becoming more and more famous and talked about.

### **But what is Big Data?**

![](img-01.jpg)

These days the acronyms **Hadoop, Hive, Spark, NoSQL** and so many others are all the rage. But do you really understand what all this "alphabet soup" means?

I'm also trying to understand what this whole ecosystem means, and in an attempt to organize my ideas and studies on such a fascinating subject, I'm starting a series of articles.

What exactly is this pile of acronyms that everyone is talking about and chasing as if it were the last oil well discovered on the planet?

As almost always happens, creativity shows up in the face of a problem that needs solving. What do we do with this immense amount of data generated every second by computers and phones?

Photos, videos, posts: how can I use this information to better understand my customer's profile and make more money? How do I organize, store and cross-reference these different forms of data?

![](img-02.jpg)

With that in mind, brilliant minds started developing organization and storage models, the famous **MapReduce and NoSQL Databases**. The first ecosystem to gain fame, which you've surely heard of, was **Hadoop**.

Written in **Java**, the goal of this framework, broadly speaking, is to map information as if it were a dictionary, count which items are similar, and store the data in reduced form in a database built for that purpose (**NoSQL**). For each type of data there are different databases. I'll go into more detail on this in the next article.

To keep it simple, **Hadoop** is the whole thing, the ecosystem. It has a MapReduce layer called **YARN** that stores data in the databases designed for each type of data. **Cassandra, Hive, HBase**: those are the ones.

![](img-03.jpg)

You're probably wondering, **"Imagine how powerful a machine you need to run this enormous volume!"** Well, that's why a file system was created, **HDFS**, which splits everything into ***nodes and clusters***. In other words, the amount of processing and hardware can grow or shrink as needed.

**Hadoop** has been around for more than 10 years and has proven to be the best solution for processing large data sets. **MapReduce** is a great solution for single-pass computations, but not very efficient for use cases that require computations and algorithms with multiple iterations

![](img-04.jpg)

To solve this other data complexity problem, **Spark** enters the scene.

I hope this post has contributed to your learning and helps you put together the pieces of today's puzzle.

References:

<http://spark.apache.org/>

<http://hadoop.apache.org/>
