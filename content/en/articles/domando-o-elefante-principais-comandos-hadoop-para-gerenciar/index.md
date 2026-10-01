---
title: "Taming the Elephant - Key Hadoop Commands for Managing HDFS"
slug: "taming-the-elephant-key-hadoop-commands-for-managing-hdfs"
date: 2017-08-24T15:51:00Z
summary: "In this article, I'll walk through the main Hadoop operations for working with HDFS through shell commands. To try them out, you can run these commands on one of the VMs from Cloudera, Hortonworks, HDInsight, or…"
tags: []
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/domando-o-elefante-principais-comandos-hadoop-para-gerenciar-lopes"
cover:
  image: cover.jpg
  alt: "Taming the Elephant - Key Hadoop Commands for Managing HDFS"
  relative: true
---

In this article, I'll walk through the main Hadoop operations for working with HDFS through shell commands. To try them out, you can run these commands on one of the VMs from Cloudera, Hortonworks, HDInsight, or on your own cluster setup if you have one.

### **1 - Create a directory in HDFS**

```
hadoop fs -mkdir <pastas>

Exemplo:
hadoop fs -mkdir /home/user/diretorio_1 /home/user/diretorio_2
```

### **2 - List the contents of a directory**

```
hadoop fs -ls <pastas>
﻿
Examplo:
hadoop fs -ls /home/user/diretorio_1
```

### 3 - Upload and download a file in HDFS

*Upload - Copy a single file or several files from the local file system to Hadoop*

```
hadoop fs -put <pasta de origem> ... <pasta de destino HDFS>

Exemplo:

hadoop fs -put /home/user/ArquivoExemplo.txt  /user/HDFS/diretorio_1/
```

*Download - Copy files to local directories*

```
hadoop fs -get <pasta de Origem HDFS> <pasta de destino>

Exemplo:

hadoop fs -get /user/HDFS/diretorio_1/ArquivoExemplo.txt /home/
```

### 4. View the contents of a file

```
hadoop fs -cat <pastas e nome de arquivo>

Exemplo:

hadoop fs -cat /user/HDFS/diretorio_1/ArquivoExemplo.txt
```

### 5. Copy files between HDFS directories

```
hadoop fs -cp <pasta de origem> <pasta de destino>

Exemplo:

hadoop fs -cp /user/HDFS/diretorio_1/ArquivoExemplo.txt /user/HDFS/dir_2
```

*This command also lets you copy multiple files; to do that, use only the folder structure in the source reference.*

### 6. Move files

```
hadoop fs -mv <pasta de origem> <pasta de destino>

Exemplo:

hadoop fs -mv /user/HDFS/diretorio_1/Arquivo.txt /user/HDFS/dir_2
```

### 7. Remove a file or directory from HDFS

```
hadoop fs -rm <pasta ou arquivo>

Exemplo:

hadoop fs -rm /user/HDFS/diretorio_1/ArquivoExemplo.txt
```

### 8. Show the last lines of a file

```
hadoop fs -tail <nome de arquivo>

Exemplo:
```
```
hadoop fs -tail /user/HDFS/diretorio_1/ArquivoExemplo.txt
```

I hope this post has added to your learning and helps you in your day-to-day work handling files.

See also:
