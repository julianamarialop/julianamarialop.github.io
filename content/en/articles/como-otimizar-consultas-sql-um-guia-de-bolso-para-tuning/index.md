---
title: "How to Optimize SQL Queries: A Pocket Guide to Data \"Tuning\""
slug: "how-to-optimize-sql-queries-a-pocket-guide-to-data-tuning"
date: 2020-06-26T16:17:00Z
summary: "Time goes by, new data ingestion techniques, languages and tools come along, but one thing is a universal truth. SQL never goes out of style!"
tags: ["SQL"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/como-otimizar-consultas-sql-um-guia-de-bolso-para-tuning-lopes"
cover:
  image: cover.jpg
  alt: "How to Optimize SQL Queries: A Pocket Guide to Data \"Tuning\""
  relative: true
---

## This article describes some special techniques for optimizing SQL queries

Time goes by, new data ingestion techniques, languages and tools come along, but one thing is a universal truth. SQL never goes out of style!

In this guide, I've included several suggestions for optimizing SQL statements. I hope it's useful for everyone.

Let's go!

## 1. Try not to use SELECT \* to query SQL; select specific fields instead.

Bad example:

```
SELECT * FROM funcionário;
```

Good example:

```
SELECT id,nome FROM funcionário;
```

**Rationale**:

- By using only the fields we need, we save resources and reduce network overhead.
- With \* no index on the table is used

## 2. If you know the query has only one result, it's recommended to use LIMIT 1

Suppose there's an employee table and you want to find a person named Maria.

```
CREATE TABLE employee ( 
id int (11) NOT NULL, 
nome varchar (50) DEFAULT NULL, 
idade int (2) DEFAULT NULL, 
data datetime DEFAULT NULL, 
sex int (1) DEFAULT NULL, 
PRIMARY KEY (id));
```

Bad example:

```
SELECT id,nome FROM funcionário WHERE LOWER(name) = 'Maria';
```

Good example:

```
SELECT id,nome FROM funcionário WHERE LOWER(name) = 'Maria' LIMIT 1;

SELECT TOP 1 id,nome FROM funcionário WHERE LOWER(name) = 'Maria';
```

**Rationale** :

- After adding LIMIT 1, once a matching record is found, **it won't keep scanning**, and efficiency improves considerably.

## 3. Try to avoid using the OR condition to join conditions

Create a new user table with an index on the idx\_userId column

```
CREATE TABLE user ( 
  id int (11) NOT NULL AUTO_INCREMENT, 
  userId int (11) NOT NULL, 
  age int (11) NOT NULL, 
  name varchar (255) NOT NULL, 
  PRIMARY KEY (id), 
  KEY idx_userId (userId))
```

Suppose you now need to query users with userid 1 or who are 18 years old; it's easy to end up with the following SQL.

Bad example:

```
SELECT * FROM usuário WHERE userid = 1 OR age = 18;
```

Good example:

```
// Use union all 

SELECT * FROM usuário WHERE userid = 1 
UNION ALL 
SELECT * FROM usuário WHERE idade = 18; 

// Ou escreva dois SQL separados

SELECT * FROM usuário WHERE userid = 1;

SELECT * FROM usuário WHERE idade = 18; 
```

**Rationale** :

- Using OR can invalidate the index and therefore requires a full table scan.

## 4. Optimize your LIKE statement

In day-to-day development, if you use fuzzy keyword queries, it's easy to reach for LIKE, but it will probably invalidate your index.

Bad example:

```
SELECT userId,nome FROM usuário WHERE userId LIKE '%123';
```

Good example:

```
SELECT userId,nome FROM usuário WHERE userId LIKE '123%';
```

**Rationale** :

- When % is used at the beginning, the query scans the whole table; when it's used at the end, the search only touches values starting with 1.

## 5. You should avoid using the ! = or <> operator in the WHERE clause as much as possible; otherwise the engine will stop using the index and perform a full table scan

Bad example:

```
SELECT idade,nome FROM usuário WHERE idade <> 18;
```

Good example:

```
// Você pode considerar duas gravações sql separadas ou UNION ALL

SELECT idade, nome do usuário WHERE idade < 18; 

SELECT idade, nome do usuário WHERE idade > 18;
```

**Reason** : using ! = or <> will probably invalidate the index

## 6. Use the DISTINCT keyword carefully

The DISTINCT keyword is usually used to filter out duplicate records and return unique ones. When used to query one field or a few fields, it has an optimizing effect on the query.

**However, when there are many fields, it greatly reduces query efficiency.**

Bad example:

```
SELECT DISTINCT * FROM usuário;
```

Good example:

```
SELECT DISTINCT nome FROM usuário;
```

**Rationale** :

- the CPU time and occupancy time of a statement with distinct are higher than those of a statement without it.
- Because, when querying many fields, if you use distinct, the database engine will compare the data and filter out the duplicates. *However, this comparison and filtering process consumes system resources and CPU time.*

## 7. Remove redundant and duplicate indexes

Bad example:

```
KEY idx_userId (userId)   

KEY idx_userId_age (userId,age)
```

Good example:

```
// Exclua o índice userId, porque o índice combinado (A, B) é equivalente à 
criação dos índices (A) e (A, B)

KEY idx_userId_age (userId,age)
```

**Rationale** :

- Duplicate indexes have to be maintained, and the optimizer also has to consider them one by one when optimizing queries, which hurts performance.

## 8. If the data volume is large, optimize your DELETE

Avoid modifying or deleting a lot of data at once, because it will cause high CPU usage, which will affect other people's access to the database.

Bad example:

```
// Excluir 100.000 ou mais 1 milhão de cada vez
DELETE FROM usuário WHERE id < 100000;
```

Good example:

```
// Excluir em lotes

DELETE FROM usuário WHERE < 500; 

DELETE FROM produto WHERE id > = 500 AND id < 1000 ；
```

**Rationale** :

- when deleting a lot of data at once, you may hit a lock wait timeout exceeded error, so it's recommended to work in batches.

## 9. Consider using default values instead of NULL in the where clause

Good example:

```
SELECT * FROM usuário WHERE idade IS NOT NULL;
```

Good example:

```
SELECT * FROM usuário WHERE idade > 0; // Defina 0 como padrão
```

**Rationale:**

- If you replace the null value with a default value, it usually makes indexing possible and, at the same time, the expression will be relatively clear.

## 10. Try replacing UNION with UNION ALL

**If there are no duplicate records in the search results**, it's recommended to replace union with union all.

Bad example:

```
SELECT * FROM usuário WHERE userid = 1
UNION 
SELECT * FROM usuário WHERE idade = 10
```

Good example:

```
SELECT * FROM usuário WHERE userid = 1
UNION ALL
SELECT * FROM usuário WHERE idade = 10
```

**Rationale** :

- If you use UNION, regardless of whether the search results repeat, it will try to merge and sort them before producing the final results.
- If the search results have no duplicate records, use UNION ALL instead of union, which will increase efficiency.

## 11. Use numeric fields as much as possible. If fields contain only numeric information, try not to design them as VARCHAR.

Bad example:

```
king_id varchar(20）NOT NULL;
```

Good example:

```
king_id int(20）NOT NULL;
```

**Rationale** :

- compared with numeric fields, character types reduce query and join performance and increase storage overhead.

## 12. Use VARCHAR/NVARCHAR instead of CHAR/NCHAR whenever possible

Bad example:

```
deptName char(100) DEFAULT NULL
```

Good example:

```
deptName varchar(100) DEFAULT NULL
```

**Rationale** :

- First, since a variable-length field takes up little storage space, storage space can be saved.
- Second, for queries, searching a relatively small field is more efficient.

## Bonus: Use EXPLAIN to analyze your SQL plan

When writing SQL in day-to-day development, try to build a habit. Use EXPLAIN to analyze the SQL you've written, especially the index.

```
EXPLAIN SELECT * FROM user WHERE userid = 10086 AND age =18;
```

---

Yes, we've reached the end. I hope you enjoyed it and got an idea of how to optimize and speed up your SQL queries.

Be sure to check out the other articles I've written! The links are here at the bottom of the page..

Thank you and see you next time!
