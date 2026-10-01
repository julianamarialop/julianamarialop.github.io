---
title: "Como modernizar processos COBOL com Azure Databricks: Uma receita de pavê com exemplo de JCL usando PCICDIT e arquivo de entrada VSAM"
date: 2025-01-10T19:12:00Z
summary: "Depois de escrever o artigo anterior sobre migração de SAS para Databricks em formato de receita de bolo , gostei tanto da experiência que decidi repetir a ideia, mas desta vez com COBOL! Como o COBOL é uma linguagem…"
tags: ["Databricks", "Azure"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/como-modernizar-processos-cobol-com-databricks-uma-receita-lopes-pqtcf"
cover:
  image: cover.jpg
  alt: "Como modernizar processos COBOL com Azure Databricks: Uma receita de pavê com exemplo de JCL usando PCICDIT e arquivo de entrada VSAM"
  relative: true
---

Depois de escrever o [artigo anterior sobre migração de SAS para Databricks](https://www.linkedin.com/pulse/como-migrar-do-sas-para-databricks-uma-receita-de-bolo-lopes-0lrnf/) em formato de **receita de bolo**, gostei tanto da experiência que decidi repetir a ideia, mas desta vez com COBOL! Como o **COBOL** é uma linguagem tão antiga quanto aquelas receitas de família que passam de geração em geração, achei que seria mais divertido fazer uma **receita de pavê**. Afinal, COBOL e pavê são clássicos que resistem ao tempo!

Você já ouviu falar em **COBOL**? Se nunca ouviu, não se preocupe, vou te explicar! O **COBOL** (“Common Business-Oriented Language”) é uma das linguagens de programação mais antigas e ainda muito importantes no mundo corporativo. Criada em **1959**, ela foi projetada para ser simples e eficiente em soluções de negócios, e acabou se tornando a principal escolha para sistemas de grande porte, principalmente em setores como **bancos**, **seguros** e **governos**.

Apesar de sua idade, o COBOL ainda roda em muitos sistemas críticos pelo mundo. Pense em sistemas que processam transações bancárias, pagamentos e registros financeiros: é bem provável que tenha um programa COBOL por trás disso. Mas, com o passar do tempo, as empresas precisam modernizar essas soluções para acompanhar novas tecnologias e demandas.

Neste artigo, vou mostrar como você pode modernizar processos COBOL em um formato bem divertido: uma **receita de pavê**! Vamos ver o passo a passo, incluindo um exemplo prático de **JCL** e também como usar o [Databricks](https://www.linkedin.com/company/databricks/) para dar um toque moderno a tudo isso. Bora preparar esse pavê?

---

### 🍰 Ingredientes da nossa receita:

1. **Levantamento dos processos COBOL existentes:**
2. **Ferramentas essenciais:**
3. **Equipe especializada:**

---

### 👩🍳 Modo de preparo: Passo 1 - Entendimento e preparação do ambiente

Antes de modernizar, é importante entender bem o processo atual.

1. **Levante os arquivos de entrada e saída:**
2. **Entenda o fluxo do JCL:**
3. **Verifique o programa COBOL:**

---

### 👩🍳 Modo de preparo: Passo 2 - Exemplo prático de JCL com PCICDIT e VSAM

Agora, vamos preparar o pavê com um exemplo prático.

### Exemplo de JCL:

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

### Explicação do JCL:

1. **//JOBNAME JOB**: Define o nome do job, a conta e as classes de execução e mensagens.
2. **//STEP1 EXEC PGM=PCICDIT**: Executa o programa **PCICDIT**.
3. **//INFILE DD DSN=INPUT.VSAM.FILE**: Especifica o arquivo de entrada, que é um arquivo VSAM.
4. **//OUTFILE DD DSN=OUTPUT.FLAT.FILE**: Define o arquivo de saída como um flat file, com especificações de espaço e formato de registro.
5. **//SYSPRINT DD SYSOUT=**\*: Direciona a saída de log para o console.
6. **//SYSIN DD**: Contém os comandos do PCICDIT, onde é especificado que o arquivo de entrada será copiado para o arquivo de saída.

---

### 👩🍳 Modo de preparo: Passo 3 - Conversão do arquivo VSAM usando Databricks

Com os dados do arquivo VSAM já identificados, podemos criar um notebook Databricks para realizar a conversão desses dados para um formato moderno, como **Delta Lake**. Abaixo está um exemplo de código PySpark que faz essa conversão:

### Exemplo de código PySpark puro:

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

### Explicação do código:

1. **Criamos uma SparkSession:** é necessária para utilizar as funcionalidades do Spark.
2. **Leitura do arquivo VSAM:** aqui consideramos um arquivo de texto simulado como entrada.
3. **Definimos o esquema do DataFrame:** renomeando as colunas para refletir a estrutura do VSAM.
4. **Escrita no formato Delta:** o arquivo é gravado em um diretório no formato Delta Lake.

### Utilizando o Databricks Assistant:

Você pode usar o **Databricks Assistant** para gerar automaticamente um notebook semelhante a este. Basta fornecer um prompt claro, como:

**Prompt sugerido:** “Crie um notebook PySpark para ler um arquivo VSAM, converter para um DataFrame e gravar no formato Delta.”

O Databricks Assistant será capaz de entender a solicitação e gerar um código base, que você pode ajustar conforme suas necessidades.

Tenho um presente: [Faça o download do notebook que criei aqui !](https://github.com/julianamarialop/databricks-solutions/blob/main/Notebook%3A%20Migra%C3%A7%C3%A3o%20COBOL%20para%20Tabelas%20Delta.py)

---

### Conclusão

Seguindo essa receita de pavê, você conseguirá modernizar seus processos COBOL de forma estruturada, garantindo a continuidade dos negócios e abrindo caminho para novas soluções tecnológicas. E você, já participou de uma modernização como essa? Compartilhe nos comentários suas experiências!

Gostou do conteúdo? Deixe um like e compartilhe com quem pode estar passando por esse desafio!

#COBOL #JCL #VSAM #Mainframe #Modernização #TransformaçãoDigital #DataEngineering
