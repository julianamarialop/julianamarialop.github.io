---
title: "Consultas SQL avançadas que você deve conhecer"
date: 2024-07-02T14:15:00Z
summary: "O artigo de hoje é sobre um assunto que adoro e nunca sai de moda. SQL !!"
tags: ["SQL"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/consultas-sql-avan%C3%A7adas-que-voc%C3%AA-deve-conhecer-juliana-maria-lopes-us3qf"
cover:
  image: cover.png
  alt: "Consultas SQL avançadas que você deve conhecer"
  relative: true
---

O artigo de hoje é sobre um assunto que adoro e nunca sai de moda. SQL !!

Se você já está envolvido em Análise de Dados há algum tempo, já deve estar familiarizado com os comandos básicos como SELECT, INSERT, UPDATE e DELETE, etc. Embora sejam os mais utilizados, também é bom conhecer as consultas abaixo para uma análise mais profunda dos dados.

## 1. Window Functions

Funções de janela são usadas para cálculos em um conjunto de linhas relacionadas à linha atual. Vamos considerar um exemplo onde calculamos o total acumulado de vendas usando a função SUM( ) com a cláusula OVER( ). Imagine que temos uma tabela de dados de vendas chamada ‘Sales\_Data’ que registra os valores de vendas em várias datas. Queremos calcular o total acumulado de vendas para cada data, o que significa o total de vendas até e incluindo cada data.

```
SELECT 
    Date,
    Sales_Amount,
    SUM(Sales_Amount) OVER (ORDER BY Date) AS Running_Total
FROM 
    Sales_Data;        
```

Neste exemplo, a função SUM(Sales\_Amount) OVER (ORDER BY Date) calcula o total acumulado de vendas até a data atual para cada linha na tabela 'Sales\_Data'.

Funções de janela podem ser usadas para várias tarefas, como calcular totais acumulados, médias móveis, classificações e muito mais, sem colapsar o conjunto de resultados em uma única linha por grupo.

## 2. Common Table Expressions (CTEs)

CTEs (Common Table Expressions) fornecem uma maneira de criar conjuntos de resultados temporários que podem ser referenciados dentro de uma consulta. Eles melhoram a legibilidade e simplificam consultas complexas. Aqui está como podemos usar um CTE para calcular a receita total para cada categoria de produto.

```
WITH category_revenue AS (
    SELECT 
        category, 
        SUM(revenue) AS total_revenue 
    FROM 
        sales 
    GROUP BY 
        category
)
SELECT 
    * 
FROM 
    category_revenue;        
```

A consulta define um CTE chamado ‘category\_revenue’. Ele calcula a receita total para cada categoria somando a receita da tabela de vendas e agrupando os resultados pela coluna de categoria. A consulta principal seleciona todas as colunas do CTE ‘category\_revenue’, exibindo efetivamente a receita total calculada para cada categoria.

## 3. Consultas Recursivas

Consultas recursivas permitem percorrer estruturas de dados hierárquicas, como organogramas ou listas de materiais. Suponha que temos uma tabela que representa os relacionamentos de funcionários e queremos encontrar todos os subordinados de um determinado gerente.

```
WITH RECURSIVE subordinates AS (
    SELECT 
        employee_id, 
        name, 
        manager_id 
    FROM 
        employees 
    WHERE 
        manager_id = 'manager_id_of_interest'
    
    UNION ALL
    
    SELECT 
        e.employee_id, 
        e.name, 
        e.manager_id 
    FROM 
        employees e 
    JOIN 
        subordinates s 
    ON 
        e.manager_id = s.employee_id
)
SELECT 
    * 
FROM 
    subordinates;        
```

Este CTE recursivo encontra todos os funcionários que se reportam direta ou indiretamente a um gerente específico 'manager\_id\_of\_interest'. Ele começa com os funcionários que se reportam diretamente ao gerente e, em seguida, encontra recursivamente seus subordinados, construindo a hierarquia.

## 4. Tabelas Dinâmicas

Tabelas dinâmicas transformam linhas em colunas, resumindo dados em um formato tabular. Digamos que temos uma tabela contendo dados de vendas e queremos dinamizar os dados para exibir as vendas totais de cada produto em diferentes meses.

```
SELECT 
    product, 
    SUM(CASE WHEN month = 'Jan' THEN sales ELSE 0 END) AS Jan, 
    SUM(CASE WHEN month = 'Feb' THEN sales ELSE 0 END) AS Feb, 
    SUM(CASE WHEN month = 'Mar' THEN sales ELSE 0 END) AS Mar 
FROM 
    sales_data 
GROUP BY 
    product;        
```

Esta consulta agrega os dados de vendas para cada produto por mês usando agregação condicional. Ela soma as vendas de janeiro, fevereiro e março separadamente para cada produto, resultando em uma tabela que mostra as vendas totais por produto para esses meses.

## 5.Funções Analíticas

Funções analíticas calculam valores agregados com base em um grupo de linhas. Por exemplo, podemos usar a função ROW\_NUMBER() para atribuir um número de linha único a cada registro em um conjunto de dados.

```
SELECT 
    customer_id, 
    order_id, 
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS order_rank 
FROM 
    orders;        
```

Esta consulta atribui uma classificação única a cada pedido por cliente com base na data do pedido, usando a função de janela ROW\_NUMBER(). O resultado mostra a sequência de pedidos feitos por cada cliente.

## 6. Unpivot

Unpivoting é o oposto de pivotar, onde colunas são transformadas em linhas. Digamos que temos uma tabela com dados de vendas agregados por mês e queremos "despivotar" para analisar as tendências ao longo do tempo.

```
SELECT 
    product, 
    month, 
    sales 
FROM 
    sales_data 
UNPIVOT (
    sales FOR month IN (sales_jan AS 'Jan', sales_feb AS 'Feb', sales_mar AS 'Mar')
) AS unpivoted_sales;        
```

Esta consulta transforma as colunas de vendas mensais em linhas, facilitando a análise de tendências ao longo do tempo por produto. Cada linha representa as vendas de um produto em um mês específico.

## 7. Agregação Condicional

A agregação condicional envolve a aplicação de funções de agregação condicionalmente com base em critérios especificados. Por exemplo, podemos querer calcular o valor médio de vendas apenas para pedidos feitos por clientes recorrentes.

```
SELECT 
    customer_id, 
    AVG(CASE WHEN order_count > 1 THEN order_total ELSE NULL END) AS avg_sales_repeat_customers 
FROM (
    SELECT 
        customer_id, 
        COUNT(*) AS order_count, 
        SUM(order_total) AS order_total 
    FROM 
        orders 
    GROUP BY 
        customer_id
) AS customer_orders;        
```

Esta consulta calcula o total médio de pedidos para clientes que fizeram mais de um pedido. Ela agrega a contagem de pedidos e o valor total dos pedidos para cada cliente, em seguida, calcula a média para os clientes recorrentes.

## 8. Funções de Data

Funções de data em SQL permitem a manipulação e extração de informações relacionadas a datas. Por exemplo, podemos usar a função DATE\_TRUNC() para agrupar dados de vendas por mês.

```
SELECT 
    DATE_TRUNC('month', order_date) AS month, 
    SUM(sales_amount) AS total_sales 
FROM 
    sales 
GROUP BY 
    DATE_TRUNC('month', order_date);        
```

Esta saída mostra o valor total de vendas (total\_sales) agregado para cada mês como month, onde cada mês é representado pelo primeiro dia daquele mês (por exemplo, 2023-01-01 para janeiro). As vendas totais são somadas para cada respectivo mês.

## 9. Instrução MERGE ou UPSERT

As instruções MERGE (também conhecidas como UPSERT ou ON DUPLICATE KEY UPDATE) permitem inserir, atualizar ou excluir registros em uma tabela de destino com base nos resultados de uma junção com uma tabela de origem. Vamos supor que queremos sincronizar duas tabelas contendo dados de clientes.

```
MERGE INTO customers_target t
USING customers_source s
ON t.customer_id = s.customer_id
WHEN MATCHED THEN 
    UPDATE SET 
        t.name = s.name, 
        t.email = s.email
WHEN NOT MATCHED THEN 
    INSERT (customer_id, name, email) 
    VALUES (s.customer_id, s.name, s.email);        
```

A instrução MERGE atualiza a tabela customers\_target com base na tabela customers\_source. Se um customer\_id em customers\_source corresponder a um em customers\_target, o nome e o email são atualizados. Se não houver correspondência, uma nova linha é inserida.

## 10. Instruções CASE

Instruções CASE permitem lógica condicional dentro de consultas SQL. Por exemplo, podemos usar uma instrução CASE para categorizar clientes com base no seu valor total de compra.

```
SELECT 
    customer_id, 
    CASE 
        WHEN total_purchase_amount >= 1000 THEN 'Platinum' 
        WHEN total_purchase_amount >= 500 THEN 'Gold' 
        ELSE 'Silver' 
    END AS customer_category 
FROM (
    SELECT 
        customer_id, 
        SUM(order_total) AS total_purchase_amount 
    FROM 
        orders 
    GROUP BY 
        customer_id
) AS customer_purchases;        
```

A consulta classifica os clientes em categorias com base no seu valor total de compra. Clientes com um valor total de compra de $1000 ou mais são rotulados como 'Platinum', aqueles com $500 a $999 são rotulados como 'Gold' e aqueles com menos de $500 são rotulados como 'Silver'.

\*\*Explicação:\*\*

1. \*\*Customer 1:\*\* Total de compras = 200 + 300 = 500. Classificado como 'Gold'.

2. \*\*Customer 2:\*\* Total de compras = 800. Classificado como 'Gold'.

3. \*\*Customer 3:\*\* Total de compras = 150 + 400 = 550. Classificado como 'Silver'.

4. \*\*Customer 4:\*\* Total de compras = 1200. Classificado como 'Platinum'.

## 11. Funções de String

Funções de string em SQL permitem a manipulação de dados textuais. Por exemplo, podemos usar a função CONCAT() para concatenar nomes e sobrenomes.

```
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name 
FROM 
    employees;        
```

Vamos considerar um conjunto de dados de exemplo e explicar a saída.

\*\*Dados de exemplo na tabela employees:\*\*

| first\_name | last\_name |

|------------|-----------|

| John | Doe |

| Jane | Smith |

| Alice | Johnson |

| Bob | Brown |

\*\*Saída:\*\*

| full\_name |

|----------------|

| John Doe |

| Jane Smith |

| Alice Johnson |

| Bob Brown |

A consulta concatena as colunas first\_name e last\_name da tabela employees com um espaço entre elas, criando um full\_name para cada funcionário.

\*\*Explicação:\*\*

1. \*\*John Doe:\*\* As colunas first\_name ("John") e last\_name ("Doe") são concatenadas com um espaço entre elas, resultando em "John Doe".

2. \*\*Jane Smith:\*\* As colunas first\_name ("Jane") e last\_name ("Smith") são concatenadas, resultando em "Jane Smith".

3. \*\*Alice Johnson:\*\* As colunas first\_name ("Alice") e last\_name ("Johnson") são concatenadas, resultando em "Alice Johnson".

4. \*\*Bob Brown:\*\* As colunas first\_name ("Bob") e last\_name ("Brown") são concatenadas, resultando em "Bob Brown".

## 12. Conjuntos de Agrupamento

Os conjuntos de agrupamento (Grouping Sets) permitem a agregação de dados em múltiplos níveis de granularidade em uma única consulta. Vamos supor que queremos calcular a receita total de vendas por mês e ano.

```
SELECT 
    YEAR(order_date) AS year, 
    MONTH(order_date) AS month, 
    SUM(sales_amount) AS total_revenue 
FROM 
    sales 
GROUP BY 
    GROUPING SETS (
        (YEAR(order_date), MONTH(order_date)), 
        YEAR(order_date), 
        MONTH(order_date)
    );        
```

\*\*Dados de exemplo na tabela sales:\*\*

| order\_date | sales\_amount |

|------------|--------------|

| 2023-01-15 | 1000 |

| 2023-01-20 | 1500 |

| 2023-02-10 | 2000 |

| 2023-03-05 | 2500 |

| 2024-01-10 | 3000 |

| 2024-01-20 | 3500 |

| 2024-02-25 | 4000 |

\*\*Saída:\*\*

| year | month | total\_revenue |

|------|-------|---------------|

| 2023 | 1 | 2500 |

| 2023 | 2 | 2000 |

| 2023 | 3 | 2500 |

| 2024 | 1 | 6500 |

| 2024 | 2 | 4000 |

| 2023 | NULL | 7000 |

| 2024 | NULL | 10500 |

| NULL | 1 | 9000 |

| NULL | 2 | 6000 |

| NULL | 3 | 2500 |

\*\*Explicação:\*\*

1. \*\*Agrupamento por ano e mês:\*\*

- 2023-01: 1000 + 1500 = 2500

- 2023-02: 2000

- 2023-03: 2500

- 2024-01: 3000 + 3500 = 6500

- 2024-02: 4000

2. \*\*Agrupamento por ano:\*\*

- 2023: 2500 (Jan) + 2000 (Fev) + 2500 (Mar) = 7000

- 2024: 6500 (Jan) + 4000 (Fev) = 10500

3. \*\*Agrupamento por mês:\*\*

- Janeiro (todos os anos): 2500 (2023) + 6500 (2024) = 9000

- Fevereiro (todos os anos): 2000 (2023) + 4000 (2024) = 6000

- Março (todos os anos): 2500

Este resultado fornece subtotais para cada mês de cada ano, totais gerais para cada ano e totais gerais para cada mês em todos os anos.

## 13. Cross Joins

Os joins cruzados (CROSS JOIN) produzem o produto cartesiano de duas tabelas, resultando em uma combinação de cada linha de cada tabela. Por exemplo, podemos usar um CROSS JOIN para gerar todas as possíveis combinações de produtos e clientes.

```
SELECT 
    p.product_id, 
    p.product_name, 
    c.customer_id, 
    c.customer_name 
FROM 
    products p 
CROSS JOIN 
    customers c;        
```

Vamos considerar um conjunto de dados de exemplo para as tabelas products e customers.

\*\*Tabela products:\*\*

| product\_id | product\_name |

|------------|--------------|

| 1 | Product A |

| 2 | Product B |

\*\*Tabela customers:\*\*

| customer\_id | customer\_name |

|-------------|---------------|

| 101 | Customer X |

| 102 | Customer Y |

\*\*Saída:\*\*

| product\_id | product\_name | customer\_id | customer\_name |

|------------|--------------|-------------|---------------|

| 1 | Product A | 101 | Customer X |

| 1 | Product A | 102 | Customer Y |

| 2 | Product B | 101 | Customer X |

| 2 | Product B | 102 | Customer Y |

A consulta realiza um CROSS JOIN entre as tabelas products e customers, resultando em um produto cartesiano. Isso significa que cada produto é emparelhado com cada cliente, gerando todas as possíveis combinações de produtos e clientes.

\*\*Explicação:\*\*

1. \*\*Product A com Customer X:\*\* Combinação de product\_id 1 e customer\_id 101.

2. \*\*Product A com Customer Y:\*\* Combinação de product\_id 1 e customer\_id 102.

3. \*\*Product B com Customer X:\*\* Combinação de product\_id 2 e customer\_id 101.

4. \*\*Product B com Customer Y:\*\* Combinação de product\_id 2 e customer\_id 102.

O resultado é um conjunto completo de combinações entre produtos e clientes, demonstrando o produto cartesiano das duas tabelas.

## 14. Tabelas Derivadas

As visualizações inline (também conhecidas como tabelas derivadas) permitem a criação de conjuntos de resultados temporários dentro de uma consulta SQL. Vamos supor que queremos encontrar clientes que fizeram compras acima do valor médio dos pedidos.

```
SELECT 
    customer_id, 
    order_total 
FROM (
    SELECT 
        customer_id, 
        SUM(order_total) AS order_total 
    FROM 
        orders 
    GROUP BY 
        customer_id
) AS customer_orders 
WHERE 
    order_total > (
        SELECT 
            AVG(order_total) 
        FROM 
            orders
    );        
```

\*\*Tabela orders:\*\*

| customer\_id | order\_total |

|-------------|-------------|

| 1 | 100 |

| 1 | 200 |

| 2 | 500 |

| 3 | 300 |

| 3 | 200 |

| 4 | 700 |

\*\*Cálculo do total de pedidos para cada cliente:\*\*

| customer\_id | order\_total |

|-------------|-------------|

| 1 | 300 |

| 2 | 500 |

| 3 | 500 |

| 4 | 700 |

\*\*Cálculo do valor médio dos pedidos:\*\*

Para calcular o valor médio dos pedidos, somamos todos os valores de pedidos e dividimos pelo número total de pedidos:

(100 + 200 + 500 + 300 + 200 + 700) / 6 = 2000 / 6 ≈ 333.33

\*\*Filtragem de clientes com pedidos totais acima da média:\*\*

| customer\_id | order\_total |

|-------------|-------------|

| 2 | 500 |

| 3 | 500 |

| 4 | 700 |

\*\*Explicação:\*\*

1. \*\*Cálculo do total de pedidos para cada cliente:\*\* A subconsulta agrupa os pedidos por customer\_id e soma os valores de order\_total para cada cliente.

2. \*\*Cálculo do valor médio dos pedidos:\*\* Outra subconsulta calcula a média dos valores dos pedidos em toda a tabela orders.

3. \*\*Filtragem de clientes:\*\* A consulta externa filtra os clientes cujos totais de pedidos são maiores que o valor médio dos pedidos.

Dessa forma, a consulta finaliza exibindo os clientes cujos totais de pedidos excedem a média, resultando na saída correta.

## 15. Operadores de Conjunto

Operadores de conjunto como UNION, INTERSECT e EXCEPT permitem combinar os resultados de duas ou mais consultas. Por exemplo, podemos usar o operador UNION para mesclar os resultados de duas consultas em um único conjunto de resultados.

```
SELECT 
    product_id, 
    product_name 
FROM 
    products 
UNION 
SELECT 
    product_id, 
    product_name 
FROM 
    archived_products;        
```

Esta consulta combina os resultados das tabelas products e archived\_products, eliminando quaisquer entradas duplicadas, para criar uma lista unificada de IDs e nomes de produtos. O operador UNION garante que cada produto apareça apenas uma vez no resultado final.

\*\*Dados de exemplo:\*\*

\*\*Tabela products:\*\*

| product\_id | product\_name |

|------------|-----------------|

| 1 | Chocolate Bar |

| 2 | Dark Chocolate |

| 3 | Milk Chocolate |

\*\*Tabela archived\_products:\*\*

| product\_id | product\_name |

|------------|-----------------|

| 3 | Milk Chocolate |

| 4 | White Chocolate |

| 5 | Almond Chocolate|

\*\*Saída:\*\*

| product\_id | product\_name |

|------------|-----------------|

| 1 | Chocolate Bar |

| 2 | Dark Chocolate |

| 3 | Milk Chocolate |

| 4 | White Chocolate |

| 5 | Almond Chocolate|

A consulta mescla os resultados das tabelas products e archived\_products, eliminando os duplicados (no caso, Milk Chocolate com product\_id 3), criando uma lista unificada de produtos.

### Por hoje é só! Se você gostou deste artigo, ajude na divulgação e assine a nossa newsletter para receber mais conteúdos interessantes. Até a próxima!
