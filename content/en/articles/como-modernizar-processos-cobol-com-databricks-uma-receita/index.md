---
title: "How to Modernize COBOL Processes with Azure Databricks: A Pavê Recipe with a JCL Example Using PCICDIT and a VSAM Input File"
slug: "modernize-cobol-processes-azure-databricks-pave-recipe-jcl-vsam"
date: 2025-01-10T19:12:00Z
summary: "After writing my previous article on migrating from SAS to Databricks as a cake recipe, I enjoyed the experience so much that I decided to repeat the idea, but this time with COBOL! Since COBOL is a language…"
tags: ["Databricks", "Azure"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/como-modernizar-processos-cobol-com-databricks-uma-receita-lopes-pqtcf"
cover:
  image: cover.jpg
  alt: "How to Modernize COBOL Processes with Azure Databricks: A Pavê Recipe with a JCL Example Using PCICDIT and a VSAM Input File"
  relative: true
---

After writing my [previous article on migrating from SAS to Databricks](https://www.linkedin.com/pulse/como-migrar-do-sas-para-databricks-uma-receita-de-bolo-lopes-0lrnf/) as a **cake recipe**, I enjoyed the experience so much that I decided to repeat the idea, but this time with COBOL! Since **COBOL** is a language as old as those family recipes handed down from generation to generation, I thought it would be more fun to make a **pavê recipe** (pavê is a classic Brazilian layered dessert, a cousin of the trifle). After all, COBOL and pavê are classics that stand the test of time!

Have you ever heard of **COBOL**? If you haven't, don't worry, I'll explain! **COBOL** ("Common Business-Oriented Language") is one of the oldest programming languages and is still very important in the corporate world. Created in **1959**, it was designed to be simple and efficient for business solutions, and it ended up becoming the main choice for large-scale systems, especially in sectors such as **banking**, **insurance** and **government**.

Despite its age, COBOL still runs many critical systems around the world. Think of systems that process bank transactions, payments and financial records: there is a good chance a COBOL program is behind them. But over time, companies need to modernize these solutions to keep up with new technologies and demands.

In this article, I'll show you how to modernize COBOL processes in a really fun format: a **pavê recipe**! We'll go step by step, including a hands-on **JCL** example and how to use [Databricks](https://www.linkedin.com/company/databricks/) to give all of it a modern touch. Shall we make this pavê?

---

### 🍰 Ingredients for our recipe:

1. **Survey of the existing COBOL processes:**
2. **Essential tools:**
3. **Specialized team:**

---

### 👩🍳 Directions: Step 1 - Understanding and preparing the environment

Before modernizing, it's important to understand the current process well.

1. **Gather the input and output files:**
2. **Understand the JCL flow:**
3. **Check the COBOL program:**

---

### 👩🍳 Directions: Step 2 - Hands-on JCL example with PCICDIT and VSAM

Now let's make the pavê with a hands-on example.

### JCL example:

```
//JOBNAME  JOB  (ACCT),'COBOL MIGRATION',CLASS=A,MSGCLASS=X
//STEP1    EXEC PGM=PCICDIT
//INFILE   DD   DSN=INPUT.VSAM.FILE,DISP=SHR
//OUTFILE  DD   DSN=OUTPUT.FLAT.FILE,DISP=(NEW,CATLG,DELETE),
//             SPACE=(CYL,(5,5),RLSE),
//             DCB=(RECFM=FB,LRECL=80,BLKSIZE=800)
//SYSPRINT DD   SYSOUT=*
//SYSIN    DD   *
   COMMAND=COPY
   INPUT=INFILE
   OUTPUT=OUTFILE
/*        
```

### JCL explanation:

1. **//JOBNAME JOB**: Defines the job name, the account, and the execution and message classes.
2. **//STEP1 EXEC PGM=PCICDIT**: Runs the **PCICDIT** program.
3. **//INFILE DD DSN=INPUT.VSAM.FILE**: Specifies the input file, which is a VSAM file.
4. **//OUTFILE DD DSN=OUTPUT.FLAT.FILE**: Defines the output file as a flat file, with space and record format specifications.
5. **//SYSPRINT DD SYSOUT=**\*: Sends the log output to the console.
6. **//SYSIN DD**: Holds the PCICDIT commands, which specify that the input file will be copied to the output file.

---

### 👩🍳 Directions: Step 3 - Converting the VSAM file with Databricks

With the VSAM file data already identified, we can create a Databricks notebook to convert that data into a modern format such as **Delta Lake**. Below is an example of PySpark code that performs this conversion:

### Plain PySpark code example:

```
from pyspark.sql import SparkSession

# Criando a sessão Spark
spark = SparkSession.builder.appName("VSAM_to_Delta").getOrCreate()

# Lendo o arquivo VSAM (simulado como um arquivo sequencial)
vsam_df = spark.read.format("csv").option("header", "false").load("/mnt/input/vsam-file.txt")

# Definindo o esquema do arquivo VSAM
vsam_df = vsam_df.withColumnRenamed("_c0", "key").withColumnRenamed("_c1", "value")

# Gravando no formato Delta
vsam_df.write.format("delta").mode("overwrite").save("/mnt/output/delta-vsam")

print("Conversão concluída com sucesso!")        
```

### Code explanation:

1. **We create a SparkSession:** it is required to use Spark's features.
2. **Reading the VSAM file:** here we take a simulated text file as input.
3. **We define the DataFrame schema:** renaming the columns to reflect the VSAM structure.
4. **Writing in Delta format:** the file is saved to a directory in Delta Lake format.

### Using Databricks Assistant:

You can use **Databricks Assistant** to automatically generate a notebook similar to this one. Just give it a clear prompt, such as:

**Suggested prompt:** "Create a PySpark notebook to read a VSAM file, convert it to a DataFrame and write it in Delta format."

Databricks Assistant will understand the request and generate base code that you can adjust to your needs.

I have a gift for you: [Download the notebook I created here!](https://github.com/julianamarialop/databricks-solutions/blob/main/Notebook%3A%20Migra%C3%A7%C3%A3o%20COBOL%20para%20Tabelas%20Delta.py)

---

### Conclusion

By following this pavê recipe, you'll be able to modernize your COBOL processes in a structured way, ensuring business continuity and paving the way for new technology solutions. What about you, have you ever taken part in a modernization like this? Share your experiences in the comments!

Did you like this content? Leave a like and share it with someone who may be facing this challenge!

#COBOL #JCL #VSAM #Mainframe #Modernization #DigitalTransformation #DataEngineering
