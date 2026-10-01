---
title: "Databricks Tip: How to Track Where Each Record Came From, File by File - input_file_name()"
slug: "databricks-tip-track-data-source-by-file-input-file-name"
date: 2023-06-22T13:24:00Z
summary: "Wouldn't it be a dream to have a column in your Bronze table (or Landing, whatever you prefer to call it) telling you which file each record came from?"
tags: ["Databricks"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/dica-de-databricks-como-verificar-origem-do-dado-por-arquivo-lopes"
cover:
  image: cover.png
  alt: "Databricks Tip: How to Track Where Each Record Came From, File by File - input_file_name()"
  relative: true
---

**Wouldn't it be a dream to have a column in your Bronze table (or Landing, whatever you prefer to call it) telling you which file each record came from?**

**Here's how to do it:**

Below we have a set of JSON files to load.

![](img-01.png)

Let's read the files into a dataframe.

![](img-02.png)

Now, let's save the dataframe as a Delta table.

![](img-03.png)

**Now here's my question: how do we know which file each person came from?**

![](img-04.png)

The secret is the **input\_file\_name()** function. You can use it with either SQL or Python, and it returns the name of the file that was **read**. In the example below, I'm using the function in the **select** on my Bronze table in Delta format.

![](img-05.png)

However, if we use this function after the table has been created, what we get back are the parquet files, not the original source files.

To solve this, let's add the "nomeArquivo" (file name) column when we create the Delta table.

![](img-06.png)

Now we're talking!!

![](img-07.png)

That's it for today, folks. I hope this was useful.

See you next time.
