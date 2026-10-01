---
title: "Building a Data Skyscraper: How to Ensure Quality in Your BI"
slug: "building-a-data-skyscraper-how-to-ensure-quality-in-your-bi"
date: 2025-09-18T17:14:00Z
summary: "Imagine you've been hired to build the tallest skyscraper in the city. It would be an incredible project, right? But what if I told you that you had to use cracked bricks, expired cement and rusty iron…"
tags: ["Databricks", "Microsoft Fabric"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/construindo-um-arranha-c%C3%A9u-de-dados-como-garantir-qualidade-lopes-vortf"
cover:
  image: cover.jpg
  alt: "Building a Data Skyscraper: How to Ensure Quality in Your BI"
  relative: true
---

Imagine you've been hired to build the tallest skyscraper in the city. It would be an incredible project, right? But what if I told you that you had to use cracked bricks, expired cement and rusty iron beams? You'd probably think twice before accepting the project, wouldn't you?

Well, that's exactly what happens when we try to build a Business Intelligence (BI) system on low-quality data. Just as a building needs reliable materials, our reports and dashboards need clean, organized data. Null, duplicate or inconsistent values are like cracks in the foundation: they may not seem dangerous at first, but over time they can bring down the whole structure.

In this article, we'll learn how to be a "data quality engineer," making sure our BI skyscraper is built on solid ground. And the best part: I'll show you hands-on examples of how to do this in
[Microsoft Fabric](https://www.linkedin.com/company/microsoft-fabric-world?trk=article-ssr-frontend-pulse_little-mention)
and in
[Databricks](https://www.linkedin.com/company/databricks?trk=article-ssr-frontend-pulse_little-mention)
!

### The Skyscraper Blueprint: Understanding Data Quality

Before construction begins, every good engineer needs a detailed plan. In the data world, that plan is what we call a data quality framework [1]. It's like having the floor plan, the technical specifications and the construction schedule.

### The Building Materials (Raw Data)

The raw data coming in from the company's systems is like the materials arriving at the construction site:

- Some arrive dirty (with special characters or extra spaces)
- Others arrive broken (null or incomplete values)
- Some come in the wrong format (dates as text, numbers as strings)
- And sometimes duplicate materials show up (the same customer registered twice)

### The Construction Site (ETL Process)

The ETL (Extract, Transform, Load) process is our construction site. This is where:

- We extract the materials from the suppliers (source systems)
- We transform and clean the materials (process the data)
- We load the treated materials into the structure (Data Warehouse)

### The Quality Engineer (Data Steward)

Every construction site needs a quality engineer who inspects each material before it's used in the building. In the data world, that person is the Data Steward: the professional responsible for making sure only good-quality data gets into our "skyscraper" [2].

### The 6 Mandatory Inspections: The Dimensions of Quality

Just as an engineer runs different types of inspections on materials, we need to check our data on 6 fundamental aspects [3]:

### 1. Completeness: "Did all the materials arrive?"

What it is: Checking that all the necessary data is present. Practical example: A customer record without an email is like trying to build a wall without all the bricks.

How to implement it in Fabric:

```
-- Verificar completude no Fabric

SELECT COUNT(*) as total_registros
     , COUNT(email) as emails_preenchidos
     , (COUNT(email)  100.0 / COUNT()) as percentual_completude 
FROM clientes;        
```

How to implement it in Databricks:

```
# Verificar completude no Databricks
from pyspark.sql.functions import col, count, when, isnan, isnull

df_clientes = spark.table("clientes")
completude_email = df_clientes.select(
    count("*").alias("total"),
    count(when(col("email").isNotNull(), 1)).alias("emails_validos")
).collect()[0]

percentual = (completude_email.emails_validos / completude_email.total) * 100
print(f"Completude do email: {percentual:.2f}%")        
```

### 2. Accuracy: "Do the materials have the right measurements?"

What it is: The data correctly reflects reality. Practical example: A beam that should be 10 meters long but is 9.5 meters can compromise the entire structure.

How to implement it in Fabric:

```
-- Validar formato de CPF no Fabric
SELECT *
FROM clientes
WHERE LEN(REPLACE(REPLACE(cpf, '.', ''), '-', '')) != 11
   OR cpf NOT LIKE '[0-9][0-9][0-9].[0-9][0-9][0-9].[0-9][0-9][0-9]-[0-9][0-9]';        
```

### 3. Consistency: "Are the blueprints aligned?"

What it is: The same data must be identical in different places. Practical example: The architect's blueprint and the engineer's must show the same wall in the same place.

How to implement it in Databricks:

```
# Verificar consistência entre tabelas no Databricks
vendas_total = spark.sql("""
    SELECT cliente_id, SUM(valor) as total_vendas
    FROM vendas 
    GROUP BY cliente_id
""")

clientes_total = spark.sql("""
    SELECT cliente_id, total_compras
    FROM clientes
""")

inconsistencias = vendas_total.join(
    clientes_total, "cliente_id", "inner"
).filter(
    col("total_vendas") != col("total_compras")
)

inconsistencias.show()        
```

### 4. Conformity: "Do the materials follow the technical standards?"

What it is: The data follows the defined standards and formats. Practical example: Every screw must be of the type specified in the ABNT standard (Brazil's national standards body).

### 5. Integrity: "Are the connections secure?"

What it is: The relationships between different pieces of data are valid. Practical example: Every column on the 5th floor must be connected to its corresponding foundation.

### 6. Timeliness: "Are we using the latest blueprint?"

What it is: The data is recent enough to be useful. Practical example: Using a 2020 blueprint to build in 2024 can cause problems.

### The Biggest Villain: Null Values (Missing Materials)

Imagine you're building a wall and suddenly realize some bricks are missing. What do you do? Leave the hole? Improvise with another material? Stop the work until the bricks arrive?

In the data world, null values are exactly those "missing bricks." And how we handle them can make the difference between a safe building and a disaster [4].

### Scenario 1: Missing Material in the Finishes (Dimension Attributes)

Situation: A customer doesn't have the "state" field filled in because they live abroad. Solution: Instead of leaving it blank, we put "Not Applicable" or "International."

Implementation in Fabric:

```
-- Tratar nulos em dimensões no Fabric
UPDATE dim_clientes 
SET estado = CASE 
    WHEN estado IS NULL AND pais != 'Brasil' THEN 'Internacional'
    WHEN estado IS NULL AND pais = 'Brasil' THEN 'Não Informado'
    ELSE estado 
END;        
```

Implementation in Databricks:

```
# Tratar nulos em dimensões no Databricks
from pyspark.sql.functions import when, col

df_clientes_tratado = df_clientes.withColumn(
    "estado_tratado",
    when(col("estado").isNull() & (col("pais") != "Brasil"), "Internacional")
    .when(col("estado").isNull() & (col("pais") == "Brasil"), "Não Informado")
    .otherwise(col("estado"))
)        
```

### Scenario 2: Missing Material in the Structure (Foreign Keys)

Situation: A sale was recorded, but the product doesn't exist in the catalog yet. Solution: We create a "temporary product" until the correct record arrives.

Implementation in Databricks with Delta Lake:

```
# Implementar "Inferred Members" no Databricks
def tratar_produto_inexistente(df_vendas, df_produtos):
    # Identificar produtos que não existem
    produtos_faltando = df_vendas.select("produto_id").distinct() \
        .join(df_produtos.select("produto_id"), "produto_id", "left_anti")
    
    # Criar registros temporários
    produtos_temporarios = produtos_faltando.withColumn(
        "nome_produto", lit("Produto Pendente")
    ).withColumn(
        "categoria", lit("Aguardando Cadastro")
    ).withColumn(
        "status", lit("Temporário")
    )
    
    # Adicionar à tabela de produtos
    df_produtos_completo = df_produtos.union(produtos_temporarios)
    
    return df_produtos_completo        
```

### Automating the Inspection: The Engineer's Tools

### In Microsoft Fabric: Data Quality Rules

```
-- Criar regra de qualidade no Fabric
CREATE OR ALTER PROCEDURE sp_validar_qualidade_clientes
AS
BEGIN
    -- Verificar completude
    DECLARE @completude_email FLOAT = (
        SELECT COUNT(email) * 100.0 / COUNT(*) 
        FROM clientes
    );
    
    -- Verificar duplicatas
    DECLARE @duplicatas INT = (
        SELECT COUNT(*) - COUNT(DISTINCT cpf) 
        FROM clientes
    );
    
    -- Alertar se qualidade baixa
    IF @completude_email < 90 OR @duplicatas > 0
    BEGIN
        PRINT 'ALERTA: Qualidade dos dados abaixo do esperado!';
        PRINT 'Completude email: ' + CAST(@completude_email AS VARCHAR(10)) + '%';
        PRINT 'Duplicatas encontradas: ' + CAST(@duplicatas AS VARCHAR(10));
    END
END;        
```

### In Databricks: Great Expectations

```
# Implementar validação automática no Databricks
import great_expectations as ge

# Criar expectativas de qualidade
df_ge = ge.from_pandas(df_clientes.toPandas())

# Definir regras
df_ge.expect_column_to_exist("email")
df_ge.expect_column_values_to_not_be_null("email", mostly=0.9)
df_ge.expect_column_values_to_be_unique("cpf")
df_ge.expect_column_values_to_match_regex("cpf", r"^\d{3}\.\d{3}\.\d{3}-\d{2}$")

# Executar validação
resultado = df_ge.validate()
print(f"Validação passou: {resultado.success}")        
```

### Continuous Monitoring: Building Maintenance

Just as a building needs regular maintenance, our data needs continuous monitoring.

### Quality Dashboard in Fabric:

```
-- Métricas de qualidade para dashboard
SELECT 
    'Clientes' as tabela,
    COUNT(*) as total_registros,
    COUNT(email) * 100.0 / COUNT(*) as completude_email,
    COUNT(DISTINCT cpf) * 100.0 / COUNT(*) as unicidade_cpf,
    GETDATE() as data_verificacao
FROM clientes

UNION ALL

SELECT 
    'Produtos' as tabela,
    COUNT(*) as total_registros,
    COUNT(nome) * 100.0 / COUNT(*) as completude_nome,
    COUNT(DISTINCT codigo) * 100.0 / COUNT(*) as unicidade_codigo,
    GETDATE() as data_verificacao
FROM produtos;        
```

### Automatic Alerts in Databricks:

```
# Sistema de alertas no Databricks
def verificar_qualidade_e_alertar():
    # Verificar qualidade
    qualidade = calcular_metricas_qualidade()
    
    # Definir thresholds
    thresholds = {
        'completude_minima': 95,
        'duplicatas_maximas': 0,
        'precisao_minima': 98
    }
    
    # Verificar alertas
    alertas = []
    for metrica, valor in qualidade.items():
        if metrica in thresholds:
            if valor < thresholds[metrica]:
                alertas.append(f" {metrica}: {valor}% (esperado: {thresholds[metrica]}%)")
    
    # Enviar alertas se necessário
    if alertas:
        enviar_notificacao_slack(alertas)
        
# Agendar execução
dbutils.jobs.taskValues.set("alertas_qualidade", verificar_qualidade_e_alertar())        
```

### Conclusion: Your Skyscraper Is Ready!

Building a BI system on quality data is like raising a skyscraper: it takes planning, quality materials, rigorous inspections and constant maintenance. But when everything is working well, you have a solid structure that can support any business decision.

Always remember:

- **Plan before you build:** Define your quality framework
- **Inspect every material:** Implement the 6 dimensions of quality
- **Fix problems at the source:** Don't let null values pile up
- **Monitor constantly:** Use automated validation tools
- **Maintain the structure:** Data quality is an ongoing process

With these practices and the tools in Fabric and Databricks, you'll be ready to build the most reliable data skyscraper in your company! See you next time!

---

### References

[1] LakeFS. (2025). Data Quality Framework: Best Practices & Tools. <https://lakefs.io/data-quality/data-quality-framework/>

[2] Hauskrecht, A. (n.d.). Building a Data Warehouse Data Quality Process. Toptal. <https://www.toptal.com/database/data-warehouse-data-quality-process>

[3] Data Science Academy. (2023). As 6 Dimensões da Qualidade de Dados (The 6 Dimensions of Data Quality). <https://blog.dsacademy.com.br/as-6-dimensoes-da-qualidade-de-dados-data-quality/>

[4] Iverson, H. K., & Oates, J. (2016). How to Manage Null Values in Your Data Warehouse. [TDAN.com](http://TDAN.com).
