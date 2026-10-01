---
title: "Como migrar do SAS para Azure Databricks: Uma receita de bolo infalível em 2 etapas"
date: 2025-01-09T13:17:00Z
summary: "Migrar uma plataforma consolidada como o SAS para o Databricks pode ser desafiador, mas quando seguimos uma receita de bolo bem estruturada, tudo fica mais simples e eficiente. Nesta receita, vamos dividir o processo em…"
tags: ["Databricks", "Azure"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/como-migrar-do-sas-para-databricks-uma-receita-de-bolo-lopes-0lrnf"
cover:
  image: cover.jpg
  alt: "Como migrar do SAS para Azure Databricks: Uma receita de bolo infalível em 2 etapas"
  relative: true
---

Migrar uma plataforma consolidada como o **SAS** para o Databricks pode ser desafiador, mas quando seguimos uma receita de bolo bem estruturada, tudo fica mais simples e eficiente. Nesta receita, vamos dividir o processo em duas etapas principais: migração de tabelas e migração de projetos SAS. E, como gran finale, tem um presente especial ao final para facilitar ainda mais sua jornada!

---

### 🍰 Ingredientes da nossa receita de migração:

**Entendimento do ambiente atual:**

- Levante todas as tabelas, processos e projetos no SAS que precisam ser migrados.
- Identifique as dependências entre tabelas e projetos.

**Ferramentas certas:**

- Databricks (com suporte ao formato Delta Lake).
- Conectores para os bancos de dados utilizados.
- O Databricks Assistant (vai ser nosso assistente nessa cozinha!).

**Equipe preparada:**

- Arquiteto de Soluções.
- Engenheiros de Dados.
- Cientistas de Dados.

---

### 👩🍳 Modo de preparo: Etapa 1 - Migração de tabelas

Assim como na preparação de um bolo, começamos pelos ingredientes básicos: as tabelas. Nesta etapa, o objetivo é migrar as tabelas do SAS para o Databricks utilizando o formato Delta, garantindo um armazenamento escalável e eficiente.

**Passos:**

**Levante todas as tabelas que serão migradas:**

Liste as tabelas existentes no SAS e identifique suas características (esquema, volume de dados, periodicidade de atualização).

**Utilize o notebook parametrizado:**

Para facilitar a migração, preparei um notebook especial que realiza a migração automática das tabelas do SAS para o formato Delta no Databricks.

Este notebook está totalmente parametrizado e permite configurar facilmente as conexões, nomes de tabelas e diretórios de destino.

**Valide a migração:**

Compare os dados migrados com os dados originais no SAS para garantir consistência e integridade.

---

### 👩🍳 Modo de preparo: Etapa 2 - Migração de projetos SAS

Agora que as tabelas estão prontas, é hora de migrar os projetos SAS. Esse passo é como adicionar a cobertura ao bolo: é aqui que os processos de ETL e os códigos SAS serão convertidos e adaptados para o Databricks.

**Passos:**

**Liste os projetos SAS:**

Identifique todos os processos e códigos SAS que precisam ser migrados. Priorize os mais críticos.

**Use o Databricks Assistant para converter o código:**

Pegue os códigos SAS já prontos e insira-os no Databricks Assistant.

Solicite ao Assistant que converta os códigos para SQL ou PySpark, dependendo da necessidade.

Essa funcionalidade permite transformar rapidamente o código SAS em um formato que o Databricks compreenda, reduzindo drasticamente o tempo de migração.

**Implemente e teste os projetos migrados:**

Execute os códigos convertidos e valide os resultados.

Certifique-se de que os novos processos estão produzindo os mesmos resultados esperados no SAS.

---

### 🎂 Gran Finale: Presente especial!

Para ajudar ainda mais nessa jornada de migração, preparei um **notebook pronto e totalmente parametrizado** para migrar as tabelas do SAS para o formato Delta. Esse notebook permite:

- Configurar rapidamente a fonte de dados SAS e o destino no Databricks.
- Executar a migração de forma automática e eficiente.
- Garantir que todas as tabelas estejam no formato Delta, prontas para serem utilizadas nos novos projetos.

**Quer o notebook?** Basta copiar esse código python abaixo !

Se você preferir faça o download do [notebook](https://github.com/julianamarialop/databricks-solutions/blob/main/Notebook%3A%20Migra%C3%A7%C3%A3o%20SAS%20para%20Tabelas%20Delta.py).

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

### Conclusão

Seguindo essa receita de bolo, você terá uma migração tranquila e eficiente, com uma plataforma moderna e escalável pronta para atender às novas demandas do seu negócio. Lembre-se: o segredo de uma boa migração está em planejar bem cada etapa e contar com as ferramentas certas.

E você, já participou de uma migração como essa? Quais foram os principais desafios? Compartilhe nos comentários! Vamos trocar experiências!
