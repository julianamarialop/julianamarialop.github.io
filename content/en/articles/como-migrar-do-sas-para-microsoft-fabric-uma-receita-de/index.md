---
title: "How to Migrate from SAS to Microsoft Fabric: An Irresistible 2-Layer Banoffee Recipe"
slug: "how-to-migrate-from-sas-to-microsoft-fabric-2-layer-banoffee-recipe"
date: 2025-04-19T16:13:00Z
summary: "Migrating an established platform like SAS can look like a complex challenge. But, just like making an irresistible Banoffee, if we follow the steps calmly and methodically, the result will be delicious! Inspired…"
tags: ["Microsoft Fabric", "Copilot", "Data Engineering", "Data Architecture"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/como-migrar-do-sas-para-microsoft-fabric-uma-receita-de-lopes-csh5f"
cover:
  image: cover.png
  alt: "How to Migrate from SAS to Microsoft Fabric: An Irresistible 2-Layer Banoffee Recipe"
  relative: true
---

Migrating an established platform like SAS can look like a complex challenge. But, just like making an irresistible Banoffee, if we follow the steps calmly and methodically, the result will be delicious! Inspired by a previous article where I walked through [a migration from SAS to Azure Databricks](https://www.linkedin.com/pulse/como-migrar-do-sas-para-databricks-uma-receita-de-bolo-lopes-0lrnf/) using a cake recipe, today I want to share a new and improved recipe: **Migrating from SAS to Microsoft Fabric in just 2 layers.**

In this article, I'll break down each layer in a simple, practical way, so you can implement it smoothly at your company. And, of course, there will be a **finishing touch** that makes all the difference!

Shall we begin?

### Ingredients you'll need for this migration

Before you roll up your sleeves, make sure you have all the right ingredients:

### 🗂️ Understanding the Current Environment:

- **Complete mapping of the SAS tables:**
- **Identification of the existing projects:**

### 🛠️ The Right Tools:

- The **Microsoft Fabric** platform:
- **Fabric Copilot** (AI assistant for automatically converting SAS scripts).

### 👩‍💻 A prepared team:

- Solutions Architect (defines the strategy).
- Data Engineers and Data Analysts (technical execution).
- Data Scientists (ensure the quality of analyses after the migration).

---

### 🥧 Layer 1 – Migrating the data (The Banoffee's crunchy base)

With Banoffee, we always start with the base, that firm layer of cookies that will hold up all the delicious layers on top. In the same way, when migrating from SAS to
[Microsoft Fabric](https://www.linkedin.com/company/microsoft-fabric-world?trk=article-ssr-frontend-pulse_little-mention)
, it's essential to start by securing a solid, safe base: your **data**.

### Detailed steps for migrating the data:

**1. Survey and document the SAS tables:**

- Take an inventory of the existing tables in SAS.
- Document essential metadata such as name, format, schema, volume, and refresh frequency.
- This survey is the foundation for an organized migration.

**2. Set up the Lakehouse in Fabric:**

- Create a Lakehouse in Microsoft Fabric using OneLake as the centralized repository.
- Define areas to receive raw data (bronze) and refined data (silver/gold).

**3. Set up automation with pipelines:**

- In Microsoft Fabric, use pipelines to automate the extract and load process (ETL).
- Configure direct connections between your SAS environment and the Lakehouse, enabling a fast and secure migration.

**4. Run and monitor the migration:**

- Use the pipeline you created to automatically load the SAS tables in Delta Lake format.
- Track the run through Fabric's built-in monitoring, spotting and fixing any failures quickly.

**5. Validate the integrity of the migrated data:**

- Run comparison tests to make sure every migrated table is identical to the original in content and structure.
- Use Fabric's analytics tools to validate consistency and integrity.

---

### 🍯🍌 Layer 2 – Migrating the SAS projects (Caramel and bananas)

Once we have a solid data base, it's time to fill our Banoffee: transforming the existing SAS scripts and projects so they run inside Microsoft Fabric. This layer is the heart of the migration, bringing real analytical intelligence to your new platform.

### Detailed steps for migrating the projects:

**1. Inventory and prioritize the SAS projects:**

- Document in detail every SAS script currently in use.
- Rank them by business relevance and technical complexity.
- Prioritize the migration by starting with the most important scripts, the ones critical to operations.

**2. Automatic conversion with Fabric Copilot:**

- Use Fabric Copilot to automate the conversion of SAS code into Spark notebooks (PySpark or SQL).
- Copy and paste the original code into Fabric Copilot and ask it to generate the initial conversion automatically.

A practical example of using Fabric Copilot:

```
/* Exemplo original de código SAS */
PROC SQL;
  CREATE TABLE clientes_vip AS
  SELECT id, nome, SUM(compras) AS total
  FROM vendas
  WHERE compras > 1000
  GROUP BY id, nome;
QUIT;        
```

Fabric Copilot automatically turns it into an equivalent Spark notebook:

```
# Código convertido automaticamente pelo Fabric Copilot
clientes_vip = spark.sql("""
  SELECT id, nome, SUM(compras) AS total
  FROM vendas
  WHERE compras > 1000
  GROUP BY id, nome
""")

clientes_vip.write.format("delta").save("Tables/clientes_vip")        
```

**3. Review and final adjustments:**

- Review the converted code and make sure the results are consistent.
- Make any small adaptations needed for the specifics of the original processes.

**4. Final testing and validation of the processes:**

- Run each migrated project in parallel with the original SAS ones, validating results and performance.
- Make sure the results you get are exactly the ones expected.

---

### 🍦 Finishing touch – Special whipped cream: a notebook ready for your migration!

To finish this recipe, there's nothing better than a special whipped cream that makes everything even tastier and easier. I've prepared a **parameterizable** notebook that you can copy straight into your Microsoft Fabric environment, making your journey much easier:

```
# Parâmetros iniciais – Defina seu diretório e Lakehouse
sas_file_dir = "/Lakehouse/SASFiles/"
destino_delta = "Tables/"

# Função para carregar arquivos SAS diretamente para Delta Lake
def migrar_tabelas_sas(sas_file_path, table_name):
    df = spark.read.format("com.github.saurfang.sas.spark").load(sas_file_path)
    delta_path = f"{destino_delta}{table_name}"
    df.write.format("delta").mode("overwrite").save(delta_path)
    print(f"✅ Tabela '{table_name}' migrada com sucesso para '{delta_path}'")

# Automatize a migração de todos os arquivos no diretório
files = mssparkutils.fs.ls(sas_file_dir)
sas_files = [f.path for f in files if f.name.endswith(".sas7bdat")]

for sas_file in sas_files:
    nome_tabela = sas_file.split("/")[-1].replace(".sas7bdat", "")
    migrar_tabelas_sas(sas_file, nome_tabela)        
```

Remember: a successful migration, just like a delicious Banoffee, depends on good planning, patience, and, of course, good ingredients!

What about you, have you worked with Fabric yet? Did you run into sweet or bitter challenges during your migration? Share your experience in the comments! Let's savor these stories together.

See you next time!
