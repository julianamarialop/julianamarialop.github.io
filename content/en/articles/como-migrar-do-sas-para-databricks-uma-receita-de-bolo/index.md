---
title: "How to migrate from SAS to Azure Databricks: A foolproof two-step recipe"
slug: "how-to-migrate-from-sas-to-azure-databricks-a-foolproof-two-step-recipe"
date: 2025-01-09T13:17:00Z
summary: "Migrating a well-established platform like SAS to Databricks can be challenging, but when we follow a well-structured recipe, everything becomes simpler and more efficient. In this recipe, we'll split the process into…"
tags: ["Databricks", "Azure"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/como-migrar-do-sas-para-databricks-uma-receita-de-bolo-lopes-0lrnf"
cover:
  image: cover.jpg
  alt: "How to migrate from SAS to Azure Databricks: A foolproof two-step recipe"
  relative: true
---

Migrating a well-established platform like **SAS** to Databricks can be challenging, but when we follow a well-structured recipe, everything becomes simpler and more efficient. In this recipe, we'll split the process into two main steps: table migration and SAS project migration. And, as a grand finale, there's a special gift at the end to make your journey even easier!

---

### 🍰 Ingredients for our migration recipe:

**Understanding the current environment:**

- Survey every table, process and project in SAS that needs to be migrated.
- Identify the dependencies between tables and projects.

**The right tools:**

- Databricks (with support for the Delta Lake format).
- Connectors for the databases in use.
- The Databricks Assistant (it'll be our sous-chef in this kitchen!).

**A prepared team:**

- Solutions Architect.
- Data Engineers.
- Data Scientists.

---

### 👩🍳 Directions: Step 1 - Table migration

Just like baking a cake, we start with the basic ingredients: the tables. In this step, the goal is to migrate the tables from SAS to Databricks using the Delta format, ensuring scalable and efficient storage.

**Steps:**

**Survey all the tables to be migrated:**

List the existing tables in SAS and identify their characteristics (schema, data volume, update frequency).

**Use the parameterized notebook:**

To make the migration easier, I prepared a special notebook that automatically migrates tables from SAS to the Delta format in Databricks.

This notebook is fully parameterized and lets you easily configure connections, table names and target directories.

**Validate the migration:**

Compare the migrated data with the original data in SAS to ensure consistency and integrity.

---

### 👩🍳 Directions: Step 2 - SAS project migration

Now that the tables are ready, it's time to migrate the SAS projects. This step is like adding the frosting to the cake: this is where the ETL processes and SAS code get converted and adapted to Databricks.

**Steps:**

**List the SAS projects:**

Identify every SAS process and piece of code that needs to be migrated. Prioritize the most critical ones.

**Use the Databricks Assistant to convert the code:**

Take the existing SAS code and paste it into the Databricks Assistant.

Ask the Assistant to convert the code to SQL or PySpark, depending on your needs.

This feature lets you quickly turn SAS code into a format Databricks understands, drastically reducing migration time.

**Deploy and test the migrated projects:**

Run the converted code and validate the results.

Make sure the new processes are producing the same results expected in SAS.

---

### 🎂 Grand Finale: A special gift!

To help even more on this migration journey, I prepared a **ready-to-use, fully parameterized notebook** to migrate SAS tables to the Delta format. This notebook lets you:

- Quickly configure the SAS data source and the destination in Databricks.
- Run the migration automatically and efficiently.
- Make sure every table is in Delta format, ready to be used in the new projects.

**Want the notebook?** Just copy the Python code below!

If you prefer, download the [notebook](https://github.com/julianamarialop/databricks-solutions/blob/main/Notebook%3A%20Migra%C3%A7%C3%A3o%20SAS%20para%20Tabelas%20Delta.py).

```
# Cell 1: Criar widgets de comando para os parâmetros de entrada
dbutils.widgets.text("sas_file_dir", "/caminho/para/seu/diretorio", "SAS File Directory")
dbutils.widgets.text("sas_file_name", "", "SAS File Name (optional)")
dbutils.widgets.text("catalog", "seu_catalogo", "Catalog")
dbutils.widgets.text("schema", "seu_schema", "Schema")
dbutils.widgets.text("table_name", "", "Table Name (optional)")        
```
```
# Cell 2: Obter os valores dos widgets
sas_file_dir = dbutils.widgets.get("sas_file_dir")
sas_file_name = dbutils.widgets.get("sas_file_name")
catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
table_name = dbutils.widgets.get("table_name")

# Função para carregar e salvar um arquivo SAS como tabela Delta
def load_and_save_sas_file(sas_file_path, catalog, schema, table_name):
    # Carregar o arquivo SAS em um DataFrame
    df = spark.read.format("com.github.saurfang.sas.spark") \
        .load(sas_file_path)

    # Exibir o DataFrame carregado
    display(df)

    # Especificar o caminho Delta
    delta_path = f"/mnt/delta/{catalog}/{schema}/{table_name}"

    # Escrever o DataFrame como uma tabela Delta
    df.write.format("delta") \
        .mode("overwrite") \
        .save(delta_path)

    # Criar a tabela Delta no catálogo especificado
    spark.sql(f"""
        CREATE TABLE {catalog}.{schema}.{table_name}
        USING DELTA
        LOCATION '{delta_path}'
    """)

# Verificar se um nome de arquivo específico foi fornecido
if sas_file_name:
    # Construir o caminho completo do arquivo SAS
    sas_file_path = f"{sas_file_dir}/{sas_file_name}"
    # Usar o nome da tabela fornecido ou derivar do nome do arquivo
    table_name = table_name if table_name else sas_file_name.split(".")[0]
    # Carregar e salvar o arquivo SAS
    load_and_save_sas_file(sas_file_path, catalog, schema, table_name)
else:
    # Listar todos os arquivos SAS no diretório
    files = dbutils.fs.ls(sas_file_dir)
    sas_files = [f.path for f in files if f.path.endswith(".sas7bdat")]

    # Carregar e salvar cada arquivo SAS
    for sas_file_path in sas_files:
        # Derivar o nome da tabela do nome do arquivo
        table_name = sas_file_path.split("/")[-1].split(".")[0]
        load_and_save_sas_file(sas_file_path, catalog, schema, table_name)        
```

---

### Conclusion

By following this recipe, you'll have a smooth and efficient migration, with a modern, scalable platform ready to meet your business's new demands. Remember: the secret to a good migration is planning each step carefully and having the right tools at hand.

What about you, have you taken part in a migration like this? What were the main challenges? Share in the comments! Let's swap experiences!
