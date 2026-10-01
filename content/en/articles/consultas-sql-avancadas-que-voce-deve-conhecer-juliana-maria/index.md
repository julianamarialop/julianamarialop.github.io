---
title: "Advanced SQL Queries You Should Know"
slug: "advanced-sql-queries-you-should-know"
date: 2024-07-02T14:15:00Z
summary: "Today's article is about a subject I love and that never goes out of style. SQL!!"
tags: ["SQL"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/consultas-sql-avan%C3%A7adas-que-voc%C3%AA-deve-conhecer-juliana-maria-lopes-us3qf"
cover:
  image: cover.png
  alt: "Advanced SQL Queries You Should Know"
  relative: true
---

Today's article is about a subject I love and that never goes out of style. SQL!!

If you've been involved in Data Analysis for a while, you're probably already familiar with basic commands such as SELECT, INSERT, UPDATE and DELETE, etc. Although they are the most widely used, it's also good to know the queries below for deeper data analysis.

## 1. Window Functions

Window functions are used for calculations over a set of rows related to the current row. Let's look at an example where we calculate a running total of sales using the SUM( ) function with the OVER( ) clause. Imagine we have a sales data table called ‘Sales\_Data’ that records sales amounts on various dates. We want to calculate the running total of sales for each date, meaning the total sales up to and including each date.

```
SELECT 
    Date,
    Sales_Amount,
    SUM(Sales_Amount) OVER (ORDER BY Date) AS Running_Total
FROM 
    Sales_Data;        
```

In this example, the SUM(Sales\_Amount) OVER (ORDER BY Date) function calculates the running total of sales up to the current date for each row in the 'Sales\_Data' table.

Window functions can be used for many tasks, such as calculating running totals, moving averages, rankings and much more, without collapsing the result set into a single row per group.

## 2. Common Table Expressions (CTEs)

CTEs (Common Table Expressions) provide a way to create temporary result sets that can be referenced within a query. They improve readability and simplify complex queries. Here's how we can use a CTE to calculate the total revenue for each product category.

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

The query defines a CTE called ‘category\_revenue’. It calculates the total revenue for each category by summing the revenue from the sales table and grouping the results by the category column. The main query selects all columns from the ‘category\_revenue’ CTE, effectively displaying the calculated total revenue for each category.

## 3. Recursive Queries

Recursive queries let you traverse hierarchical data structures, such as org charts or bills of materials. Suppose we have a table representing employee relationships and we want to find all the subordinates of a given manager.

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

This recursive CTE finds every employee who reports directly or indirectly to a specific manager, 'manager\_id\_of\_interest'. It starts with the employees who report directly to the manager and then recursively finds their subordinates, building up the hierarchy.

## 4. Pivot Tables

Pivot tables turn rows into columns, summarizing data in a tabular format. Let's say we have a table containing sales data and we want to pivot the data to show the total sales of each product across different months.

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

This query aggregates the sales data for each product by month using conditional aggregation. It sums the sales for January, February and March separately for each product, producing a table that shows total sales per product for those months.

## 5.Analytic Functions

Analytic functions calculate aggregate values based on a group of rows. For example, we can use the ROW\_NUMBER() function to assign a unique row number to each record in a dataset.

```
SELECT 
    customer_id, 
    order_id, 
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS order_rank 
FROM 
    orders;        
```

This query assigns a unique rank to each order per customer based on the order date, using the ROW\_NUMBER() window function. The result shows the sequence of orders placed by each customer.

## 6. Unpivot

Unpivoting is the opposite of pivoting: columns are turned into rows. Let's say we have a table with sales data aggregated by month and we want to "unpivot" it to analyze trends over time.

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

This query turns the monthly sales columns into rows, making it easier to analyze trends over time by product. Each row represents a product's sales in a specific month.

## 7. Conditional Aggregation

Conditional aggregation involves applying aggregate functions conditionally based on specified criteria. For example, we might want to calculate the average sales amount only for orders placed by repeat customers.

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

This query calculates the average order total for customers who have placed more than one order. It aggregates the order count and the total order value for each customer, then calculates the average for repeat customers.

## 8. Date Functions

Date functions in SQL let you manipulate and extract date-related information. For example, we can use the DATE\_TRUNC() function to group sales data by month.

```
SELECT 
    DATE_TRUNC('month', order_date) AS month, 
    SUM(sales_amount) AS total_sales 
FROM 
    sales 
GROUP BY 
    DATE_TRUNC('month', order_date);        
```

This output shows the total sales amount (total\_sales) aggregated for each month as month, where each month is represented by its first day (for example, 2023-01-01 for January). Total sales are summed for each respective month.

## 9. MERGE or UPSERT Statement

MERGE statements (also known as UPSERT or ON DUPLICATE KEY UPDATE) let you insert, update or delete records in a target table based on the results of a join with a source table. Let's say we want to synchronize two tables containing customer data.

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

The MERGE statement updates the customers\_target table based on the customers\_source table. If a customer\_id in customers\_source matches one in customers\_target, the name and email are updated. If there's no match, a new row is inserted.

## 10. CASE Statements

CASE statements allow conditional logic inside SQL queries. For example, we can use a CASE statement to categorize customers based on their total purchase amount.

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

The query sorts customers into categories based on their total purchase amount. Customers with a total purchase amount of $1000 or more are labeled 'Platinum', those with $500 to $999 are labeled 'Gold' and those with less than $500 are labeled 'Silver'.

\*\*Explanation:\*\*

1. \*\*Customer 1:\*\* Total purchases = 200 + 300 = 500. Classified as 'Gold'.

2. \*\*Customer 2:\*\* Total purchases = 800. Classified as 'Gold'.

3. \*\*Customer 3:\*\* Total purchases = 150 + 400 = 550. Classified as 'Silver'.

4. \*\*Customer 4:\*\* Total purchases = 1200. Classified as 'Platinum'.

## 11. String Functions

String functions in SQL let you manipulate text data. For example, we can use the CONCAT() function to concatenate first and last names.

```
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name 
FROM 
    employees;        
```

Let's look at a sample dataset and explain the output.

\*\*Sample data in the employees table:\*\*

| first\_name | last\_name |

|------------|-----------|

| John | Doe |

| Jane | Smith |

| Alice | Johnson |

| Bob | Brown |

\*\*Output:\*\*

| full\_name |

|----------------|

| John Doe |

| Jane Smith |

| Alice Johnson |

| Bob Brown |

The query concatenates the first\_name and last\_name columns from the employees table with a space between them, creating a full\_name for each employee.

\*\*Explanation:\*\*

1. \*\*John Doe:\*\* The first\_name ("John") and last\_name ("Doe") columns are concatenated with a space between them, resulting in "John Doe".

2. \*\*Jane Smith:\*\* The first\_name ("Jane") and last\_name ("Smith") columns are concatenated, resulting in "Jane Smith".

3. \*\*Alice Johnson:\*\* The first\_name ("Alice") and last\_name ("Johnson") columns are concatenated, resulting in "Alice Johnson".

4. \*\*Bob Brown:\*\* The first\_name ("Bob") and last\_name ("Brown") columns are concatenated, resulting in "Bob Brown".

## 12. Grouping Sets

Grouping sets allow data to be aggregated at multiple levels of granularity in a single query. Let's say we want to calculate total sales revenue by month and year.

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

\*\*Sample data in the sales table:\*\*

| order\_date | sales\_amount |

|------------|--------------|

| 2023-01-15 | 1000 |

| 2023-01-20 | 1500 |

| 2023-02-10 | 2000 |

| 2023-03-05 | 2500 |

| 2024-01-10 | 3000 |

| 2024-01-20 | 3500 |

| 2024-02-25 | 4000 |

\*\*Output:\*\*

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

\*\*Explanation:\*\*

1. \*\*Grouping by year and month:\*\*

- 2023-01: 1000 + 1500 = 2500

- 2023-02: 2000

- 2023-03: 2500

- 2024-01: 3000 + 3500 = 6500

- 2024-02: 4000

2. \*\*Grouping by year:\*\*

- 2023: 2500 (Jan) + 2000 (Feb) + 2500 (Mar) = 7000

- 2024: 6500 (Jan) + 4000 (Feb) = 10500

3. \*\*Grouping by month:\*\*

- January (all years): 2500 (2023) + 6500 (2024) = 9000

- February (all years): 2000 (2023) + 4000 (2024) = 6000

- March (all years): 2500

This result provides subtotals for each month of each year, grand totals for each year and grand totals for each month across all years.

## 13. Cross Joins

Cross joins (CROSS JOIN) produce the Cartesian product of two tables, resulting in a combination of every row from each table. For example, we can use a CROSS JOIN to generate every possible combination of products and customers.

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

Let's look at a sample dataset for the products and customers tables.

\*\*products table:\*\*

| product\_id | product\_name |

|------------|--------------|

| 1 | Product A |

| 2 | Product B |

\*\*customers table:\*\*

| customer\_id | customer\_name |

|-------------|---------------|

| 101 | Customer X |

| 102 | Customer Y |

\*\*Output:\*\*

| product\_id | product\_name | customer\_id | customer\_name |

|------------|--------------|-------------|---------------|

| 1 | Product A | 101 | Customer X |

| 1 | Product A | 102 | Customer Y |

| 2 | Product B | 101 | Customer X |

| 2 | Product B | 102 | Customer Y |

The query performs a CROSS JOIN between the products and customers tables, resulting in a Cartesian product. This means each product is paired with each customer, generating every possible combination of products and customers.

\*\*Explanation:\*\*

1. \*\*Product A with Customer X:\*\* Combination of product\_id 1 and customer\_id 101.

2. \*\*Product A with Customer Y:\*\* Combination of product\_id 1 and customer\_id 102.

3. \*\*Product B with Customer X:\*\* Combination of product\_id 2 and customer\_id 101.

4. \*\*Product B with Customer Y:\*\* Combination of product\_id 2 and customer\_id 102.

The result is a complete set of combinations between products and customers, demonstrating the Cartesian product of the two tables.

## 14. Derived Tables

Inline views (also known as derived tables) let you create temporary result sets within a SQL query. Let's say we want to find customers who made purchases above the average order value.

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

\*\*orders table:\*\*

| customer\_id | order\_total |

|-------------|-------------|

| 1 | 100 |

| 1 | 200 |

| 2 | 500 |

| 3 | 300 |

| 3 | 200 |

| 4 | 700 |

\*\*Calculating the order total for each customer:\*\*

| customer\_id | order\_total |

|-------------|-------------|

| 1 | 300 |

| 2 | 500 |

| 3 | 500 |

| 4 | 700 |

\*\*Calculating the average order value:\*\*

To calculate the average order value, we add up all the order values and divide by the total number of orders:

(100 + 200 + 500 + 300 + 200 + 700) / 6 = 2000 / 6 ≈ 333.33

\*\*Filtering customers with total orders above the average:\*\*

| customer\_id | order\_total |

|-------------|-------------|

| 2 | 500 |

| 3 | 500 |

| 4 | 700 |

\*\*Explanation:\*\*

1. \*\*Calculating the order total for each customer:\*\* The subquery groups orders by customer\_id and sums the order\_total values for each customer.

2. \*\*Calculating the average order value:\*\* Another subquery calculates the average of the order values across the entire orders table.

3. \*\*Filtering customers:\*\* The outer query filters the customers whose order totals are greater than the average order value.

This way, the query finishes by displaying the customers whose order totals exceed the average, producing the correct output.

## 15. Set Operators

Set operators such as UNION, INTERSECT and EXCEPT let you combine the results of two or more queries. For example, we can use the UNION operator to merge the results of two queries into a single result set.

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

This query combines the results of the products and archived\_products tables, eliminating any duplicate entries, to create a unified list of product IDs and names. The UNION operator ensures each product appears only once in the final result.

\*\*Sample data:\*\*

\*\*products table:\*\*

| product\_id | product\_name |

|------------|-----------------|

| 1 | Chocolate Bar |

| 2 | Dark Chocolate |

| 3 | Milk Chocolate |

\*\*archived\_products table:\*\*

| product\_id | product\_name |

|------------|-----------------|

| 3 | Milk Chocolate |

| 4 | White Chocolate |

| 5 | Almond Chocolate|

\*\*Output:\*\*

| product\_id | product\_name |

|------------|-----------------|

| 1 | Chocolate Bar |

| 2 | Dark Chocolate |

| 3 | Milk Chocolate |

| 4 | White Chocolate |

| 5 | Almond Chocolate|

The query merges the results of the products and archived\_products tables, eliminating the duplicates (in this case, Milk Chocolate with product\_id 3), creating a unified list of products.

### That's all for today! If you enjoyed this article, help spread the word and subscribe to our newsletter for more interesting content. See you next time!
