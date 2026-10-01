---
title: "Domando o Elefante - Principais Comandos Hadoop para gerenciar o HDFS"
date: 2017-08-24T15:51:00Z
summary: "Neste artigo, apresentarei as principais operações Hadoop para manipular o HDFS por meio de comandos shell. Para testar, você pode utilizar esses comandos usando algumas das VMs da Cloudera, Hortonworks, HDInsight, ou…"
tags: []
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/domando-o-elefante-principais-comandos-hadoop-para-gerenciar-lopes"
cover:
  image: cover.jpg
  alt: "Domando o Elefante - Principais Comandos Hadoop para gerenciar o HDFS"
  relative: true
---

Neste artigo, apresentarei as principais operações Hadoop para manipular o HDFS por meio de comandos shell. Para testar, você pode utilizar esses comandos usando algumas das VMs da Cloudera, Hortonworks, HDInsight, ou se você possui sua própria configuração de cluster.

### **1 - Criar um diretório no HDFS**

```
hadoop fs -mkdir <pastas>

Exemplo:
hadoop fs -mkdir /home/user/diretorio_1 /home/user/diretorio_2
```

### **2 - Listar o conteúdo de um diretório**

```
hadoop fs -ls <pastas>
﻿
Examplo:
hadoop fs -ls /home/user/diretorio_1
```

### 3 - Upload e download de um arquivo no HDFS

*Upload - Copie um único arquivo ou vários do sistema de arquivos local para o Hadoop*

```
hadoop fs -put <pasta de origem> ... <pasta de destino HDFS>

Exemplo:

hadoop fs -put /home/user/ArquivoExemplo.txt  /user/HDFS/diretorio_1/
```

*Download - Copie arquivos para os diretórios locais*

```
hadoop fs -get <pasta de Origem HDFS> <pasta de destino>

Exemplo:

hadoop fs -get /user/HDFS/diretorio_1/ArquivoExemplo.txt /home/
```

### 4. Ver o conteúdo do Arquivo

```
hadoop fs -cat <pastas e nome de arquivo>

Exemplo:

hadoop fs -cat /user/HDFS/diretorio_1/ArquivoExemplo.txt
```

### 5. Copiar arquivos entre diretórios do HDFS

```
hadoop fs -cp <pasta de origem> <pasta de destino>

Exemplo:

hadoop fs -cp /user/HDFS/diretorio_1/ArquivoExemplo.txt /user/HDFS/dir_2
```

*Este comando também permite a cópia de vários arquivos, para isso utilize somente a estrutura de pasta na referência da origem.*

### 6. Mover os arquivos

```
hadoop fs -mv <pasta de origem> <pasta de destino>

Exemplo:

hadoop fs -mv /user/HDFS/diretorio_1/Arquivo.txt /user/HDFS/dir_2
```

### 7. Remover um Arquivo ou Diretório do HDFS

```
hadoop fs -rm <pasta ou arquivo>

Exemplo:

hadoop fs -rm /user/HDFS/diretorio_1/ArquivoExemplo.txt
```

### 8. Exibir as Últimas Linhas do Arquivo

```
hadoop fs -tail <nome de arquivo>

Exemplo:
```
```
hadoop fs -tail /user/HDFS/diretorio_1/ArquivoExemplo.txt
```

Espero que essa publicação tenha contribuído para seu aprendizado e ajude no seu cotidiano de manipulação de arquivos.

Veja também:
