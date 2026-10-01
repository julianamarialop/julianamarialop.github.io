---
title: "Construindo um Arranha-Céu de Dados: Como Garantir Qualidade no seu BI"
date: 2025-09-18T17:14:00Z
summary: "Imagine que você foi contratado para construir o maior arranha-céu da cidade. Seria um projeto incrível, não é mesmo? Mas e se eu te dissesse que você precisa usar tijolos rachados, cimento vencido e vigas de ferro…"
tags: ["Databricks", "Microsoft Fabric"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/construindo-um-arranha-c%C3%A9u-de-dados-como-garantir-qualidade-lopes-vortf"
cover:
  image: cover.jpg
  alt: "Construindo um Arranha-Céu de Dados: Como Garantir Qualidade no seu BI"
  relative: true
---

Imagine que você foi contratado para construir o maior arranha-céu da cidade. Seria um projeto incrível, não é mesmo? Mas e se eu te dissesse que você precisa usar tijolos rachados, cimento vencido e vigas de ferro enferrujadas? Provavelmente você pensaria duas vezes antes de aceitar o projeto, certo?

Pois é exatamente isso que acontece quando tentamos construir um sistema de Business Intelligence (BI) com dados de baixa qualidade. Assim como um prédio precisa de materiais confiáveis, nossos relatórios e dashboards precisam de dados limpos e organizados. Valores nulos, duplicados ou inconsistentes são como rachaduras na fundação - podem não parecer perigosos no início, mas com o tempo podem derrubar toda a estrutura.

Neste artigo, vamos aprender como ser um "engenheiro de qualidade de dados", garantindo que nosso arranha-céu de BI seja construído sobre bases sólidas. E o melhor: vou mostrar exemplos práticos de como fazer isso no
[Microsoft Fabric](https://www.linkedin.com/company/microsoft-fabric-world?trk=article-ssr-frontend-pulse_little-mention)
e no
[Databricks](https://www.linkedin.com/company/databricks?trk=article-ssr-frontend-pulse_little-mention)
!

### O Projeto do Arranha-Céu: Entendendo a Qualidade de Dados

Antes de começar a construção, todo bom engenheiro precisa de um projeto bem detalhado. No mundo dos dados, esse projeto é o que chamamos de framework de qualidade de dados [1]. É como ter a planta baixa, as especificações técnicas e o cronograma da obra.

### Os Materiais de Construção (Dados Brutos)

Os dados brutos que chegam dos sistemas da empresa são como os materiais que chegam no canteiro de obras:

- Alguns vêm sujos (com caracteres especiais ou espaços extras)
- Outros vêm quebrados (valores nulos ou incompletos)
- Alguns chegam no formato errado (datas como texto, números como string)
- E às vezes chegam materiais duplicados (o mesmo cliente cadastrado duas vezes)

### O Canteiro de Obras (Processo ETL)

O processo de ETL (Extração, Transformação e Carga) é nosso canteiro de obras. É aqui que:

- Extraímos os materiais dos fornecedores (sistemas origem)
- Transformamos e limpamos os materiais (tratamos os dados)
- Carregamos os materiais tratados na estrutura (Data Warehouse)

### O Engenheiro de Qualidade (Data Steward)

Todo canteiro de obras precisa de um engenheiro de qualidade que inspeciona cada material antes dele ser usado na construção. No mundo dos dados, essa pessoa é o Data Steward - o profissional responsável por garantir que apenas dados de boa qualidade entrem no nosso "arranha-céu" [2].

### As 6 Inspeções Obrigatórias: As Dimensões da Qualidade

Assim como um engenheiro faz diferentes tipos de inspeção nos materiais, precisamos verificar nossos dados em 6 aspectos fundamentais [3]:

### 1. Completude: "Chegaram todos os materiais?"

O que é: Verificar se todos os dados necessários estão presentes. Exemplo prático: Um cadastro de cliente sem e-mail é como tentar construir uma parede sem todos os tijolos.

Como implementar no Fabric:

```
-- Verificar completude no Fabric

SELECT COUNT(*) as total_registros
     , COUNT(email) as emails_preenchidos
     , (COUNT(email)  100.0 / COUNT()) as percentual_completude 
FROM clientes;        
```

Como implementar no Databricks:

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

### 2. Precisão: "Os materiais têm as medidas certas?"

O que é: Os dados refletem corretamente a realidade. Exemplo prático: Uma viga que deveria ter 10 metros mas tem 9,5 metros pode comprometer toda a estrutura.

Como implementar no Fabric:

```
-- Validar formato de CPF no Fabric
SELECT *
FROM clientes
WHERE LEN(REPLACE(REPLACE(cpf, '.', ''), '-', '')) != 11
   OR cpf NOT LIKE '[0-9][0-9][0-9].[0-9][0-9][0-9].[0-9][0-9][0-9]-[0-9][0-9]';        
```

### 3. Consistência: "As plantas estão alinhadas?"

O que é: Os mesmos dados devem ser iguais em diferentes lugares. Exemplo prático: A planta do arquiteto e a do engenheiro devem mostrar a mesma parede no mesmo lugar.

Como implementar no Databricks:

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

### 4. Conformidade: "Os materiais seguem as normas técnicas?"

O que é: Os dados seguem os padrões e formatos definidos. Exemplo prático: Todos os parafusos devem ser do tipo especificado na norma ABNT.

### 5. Integridade: "As conexões estão firmes?"

O que é: As relações entre diferentes dados são válidas. Exemplo prático: Cada coluna do 5º andar deve estar conectada à fundação correspondente.

### 6. Atualidade: "Estamos usando a planta mais recente?"

O que é: Os dados são recentes o suficiente para serem úteis. Exemplo prático: Usar uma planta de 2020 para construir em 2024 pode gerar problemas.

### O Maior Vilão: Os Valores Nulos (Materiais Faltando)

Imagine que você está construindo uma parede e, de repente, percebe que faltam alguns tijolos. O que fazer? Deixar o buraco? Improvisar com outro material? Parar a obra até os tijolos chegarem?

No mundo dos dados, os valores nulos são exatamente esses "tijolos faltando". E a forma como lidamos com eles pode fazer a diferença entre um prédio seguro e um desastre [4].

### Cenário 1: Falta Material na Decoração (Atributos de Dimensão)

Situação: Um cliente não tem o campo "estado" preenchido porque mora no exterior. Solução: Em vez de deixar em branco, colocamos "Não se Aplica" ou "Internacional".

Implementação no Fabric:

```
-- Tratar nulos em dimensões no Fabric
UPDATE dim_clientes 
SET estado = CASE 
    WHEN estado IS NULL AND pais != 'Brasil' THEN 'Internacional'
    WHEN estado IS NULL AND pais = 'Brasil' THEN 'Não Informado'
    ELSE estado 
END;        
```

Implementação no Databricks:

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

### Cenário 2: Falta Material na Estrutura (Chaves Estrangeiras)

Situação: Uma venda foi registrada, mas o produto ainda não existe no cadastro. Solução: Criamos um "produto temporário" até o cadastro correto chegar.

Implementação no Databricks com Delta Lake:

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

### Automatizando a Inspeção: Ferramentas do Engenheiro

### No Microsoft Fabric: Data Quality Rules

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

### No Databricks: Great Expectations

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

### Monitoramento Contínuo: A Manutenção do Prédio

Assim como um prédio precisa de manutenção regular, nossos dados precisam de monitoramento contínuo.

### Dashboard de Qualidade no Fabric:

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

### Alertas Automáticos no Databricks:

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

### Conclusão: Seu Arranha-Céu Está Pronto!

Construir um sistema de BI com dados de qualidade é como erguer um arranha-céu: exige planejamento, materiais de qualidade, inspeções rigorosas e manutenção constante. Mas quando tudo está funcionando bem, você tem uma estrutura sólida que pode suportar qualquer decisão de negócio.

Lembre-se sempre:

- **Planeje antes de construir:** Defina seu framework de qualidade
- **Inspecione todos os materiais:** Implemente as 6 dimensões de qualidade
- **Trate os problemas na origem:** Não deixe valores nulos se acumularem
- **Monitore constantemente:** Use ferramentas automáticas de validação
- **Mantenha a estrutura:** Qualidade de dados é um processo contínuo

Com essas práticas e as ferramentas do Fabric e Databricks, você estará pronto para construir o arranha-céu de dados mais confiável da sua empresa! Até a próxima !

---

### Referências

[1] LakeFS. (2025). Data Quality Framework: Best Practices & Tools. <https://lakefs.io/data-quality/data-quality-framework/>

[2] Hauskrecht, A. (s.d.). Building a Data Warehouse Data Quality Process. Toptal. <https://www.toptal.com/database/data-warehouse-data-quality-process>

[3] Data Science Academy. (2023). As 6 Dimensões da Qualidade de Dados (Data Quality). <https://blog.dsacademy.com.br/as-6-dimensoes-da-qualidade-de-dados-data-quality/>

[4] Iverson, H. K., & Oates, J. (2016). How to Manage Null Values in Your Data Warehouse. [TDAN.com](http://TDAN.com).
