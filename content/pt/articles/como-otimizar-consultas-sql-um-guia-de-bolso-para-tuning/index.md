---
title: "Como otimizar consultas SQL: Um guia de bolso para \"tuning\"​ de dados"
date: 2020-06-26T16:17:00Z
summary: "O tempo passa, novas técnicas, linguagens e ferramentas de ingestão de dados surgem, mas é uma verdade universal. SQL nunca sai de moda !"
tags: ["SQL"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/como-otimizar-consultas-sql-um-guia-de-bolso-para-tuning-lopes"
cover:
  image: cover.jpg
  alt: "Como otimizar consultas SQL: Um guia de bolso para \"tuning\"​ de dados"
  relative: true
---

## Este artigo descreve algumas técnicas especiais para otimizar consultas SQL

O tempo passa, novas técnicas, linguagens e ferramentas de ingestão de dados surgem, mas é uma verdade universal. SQL nunca sai de moda !

Neste guia, incluí várias sugestões para otimizar instruções SQL. Espero que seja útil para todos.

Vamos lá !

## 1. Tente não usar SELECT \* para consultar o SQL, mas selecione campos específicos.

Exemplo negativo:

```
SELECT * FROM funcionário;
```

Exemplo positivo:

```
SELECT id,nome FROM funcionário;
```

**Justificativa**:

- Usando apenas os campos obrigatórios, podemos economizar nossos recursos e reduzir a sobrecarga da rede.
- Com \* nenhum índice da tabela é utilizado

## 2. Se você sabe que existe apenas um resultado da consulta, é recomendável usar o LIMIT 1

Suponha que exista uma tabela de funcionários e você queira encontrar uma pessoa chamada Maria.

```
CREATE TABLE employee ( 
id int (11) NOT NULL, 
nome varchar (50) DEFAULT NULL, 
idade int (2) DEFAULT NULL, 
data datetime DEFAULT NULL, 
sex int (1) DEFAULT NULL, 
PRIMARY KEY (id));
```

Exemplo negativo:

```
SELECT id,nome FROM funcionário WHERE LOWER(name) = 'Maria';
```

Exemplo positivo:

```
SELECT id,nome FROM funcionário WHERE LOWER(name) = 'Maria' LIMIT 1;

SELECT TOP 1 id,nome FROM funcionário WHERE LOWER(name) = 'Maria';
```

**Justificativa** :

- Após adicionar o LIMIT 1, quando um registro correspondente for encontrado, **ele não continuará a varredura** e a eficiência será bastante aprimorada.

## 3. Tente evitar o uso da condição OR para unir condições

Crie uma nova tabela de usuário com índice na coluna idx\_userId

```
CREATE TABLE user ( 
  id int (11) NOT NULL AUTO_INCREMENT, 
  userId int (11) NOT NULL, 
  age int (11) NOT NULL, 
  name varchar (255) NOT NULL, 
  PRIMARY KEY (id), 
  KEY idx_userId (userId))
```

Suponha que agora você precise consultar usuários com userid1 ou 18 anos de idade, é fácil ter o seguinte SQL.

Exemplo negativo:

```
SELECT * FROM usuário WHERE userid = 1 OR age = 18;
```

Exemplo positivo:

```
// Use union all 

SELECT * FROM usuário WHERE userid = 1 
UNION ALL 
SELECT * FROM usuário WHERE idade = 18; 

// Ou escreva dois SQL separados

SELECT * FROM usuário WHERE userid = 1;

SELECT * FROM usuário WHERE idade = 18; 
```

**Justificativa** :

- O uso de OR pode invalidar o índice e, portanto, requer uma verificação completa da tabela.

## 4. Otimize sua declaração like

No desenvolvimento diário, se você usar consultas de palavras-chave difusas, é fácil pensar em LIKE como alternativa, mas provavelmente invalidará seu índice.

Exemplo negativo:

```
SELECT userId,nome FROM usuário WHERE userId LIKE '%123';
```

Exemplo positivo:

```
SELECT userId,nome FROM usuário WHERE userId LIKE '123%';
```

**Justificativa** :

- Quando o % é utilizado no inicio a consulta irá varrer a tabela toda, quando utilizado no final a busca acontece somente nos valores iniciados em 1.

## 5. Você deve evitar usar o operador ! = ou <> na cláusula WHERE, tanto quanto possível, caso contrário, o mecanismo deixará de usar o índice e executará uma verificação completa da tabela

Exemplo negativo:

```
SELECT idade,nome FROM usuário WHERE idade <> 18;
```

Exemplo positivo:

```
// Você pode considerar duas gravações sql separadas ou UNION ALL

SELECT idade, nome do usuário WHERE idade < 18; 

SELECT idade, nome do usuário WHERE idade > 18;
```

**Motivo** : o uso de ! = ou <> provavelmente invalidará o índice

## 6. Use a palavra-chave DISTINCT com cuidado

A palavra-chave DISTINCT geralmente é usada para filtrar registros duplicados para retornar registros exclusivos. Quando usado no caso de consultar um campo ou alguns campos, traz efeito de otimização para a consulta.

**No entanto, quando existem muitos campos, isso reduz bastante a eficiência da consulta.**

Exemplo negativo:

```
SELECT DISTINCT * FROM usuário;
```

Exemplo positivo:

```
SELECT DISTINCT nome FROM usuário;
```

**Justificativa** :

- o tempo da CPU e o tempo de ocupação da instrução com distintos são maiores que a instrução sem distintos.
- Porque, ao consultar muitos campos, se você usar distintos, o mecanismo de banco de dados comparará os dados e filtrará os dados duplicados. *No entanto, esse processo de comparação e filtragem consumirá recursos do sistema e tempo de CPU.*

## 7. Remova índices redundantes e duplicados

Exemplo negativo:

```
KEY idx_userId (userId)   

KEY idx_userId_age (userId,age)
```

Exemplo positivo:

```
// Exclua o índice userId, porque o índice combinado (A, B) é equivalente à 
criação dos índices (A) e (A, B)

KEY idx_userId_age (userId,age)
```

**Justificativa** :

- Índices duplicados precisam ser mantidos, e o otimizador também precisa considerá-los um por um ao otimizar consultas, o que afetará o desempenho.

## 8. Se a quantidade de dados for grande, otimize seu DELETE

Evite modificar ou excluir muitos dados ao mesmo tempo, porque isso causará alta utilização da CPU, o que afetará o acesso de outras pessoas ao banco de dados.

Exemplo negativo:

```
// Excluir 100.000 ou mais 1 milhão de cada vez
DELETE FROM usuário WHERE id < 100000;
```

Exemplo positivo:

```
// Excluir em lotes

DELETE FROM usuário WHERE < 500; 

DELETE FROM produto WHERE id > = 500 AND id < 1000 ；
```

**Justificativa** :

- para excluir muitos dados ao mesmo tempo, pode haver um erro de tempo limite de espera de bloqueio excedido, portanto, é recomendável operar em lotes.

## 9. Considere usar valores padrão em vez de NULL na cláusula where

Exemplo positivo:

```
SELECT * FROM usuário WHERE idade IS NOT NULL;
```

Exemplo positivo:

```
SELECT * FROM usuário WHERE idade > 0; // Defina 0 como padrão
```

**Justificativa:**

- Se você substituir o valor nulo pelo valor padrão, geralmente torna possível a indexação e, ao mesmo tempo, a expressão será relativamente clara.

## 10. Tente substituir UNION por UNION ALL

**Se não houver registros duplicados nos resultados da pesquisa** , é recomendável substituir a união pela união de todos.

Exemplo negativo:

```
SELECT * FROM usuário WHERE userid = 1
UNION 
SELECT * FROM usuário WHERE idade = 10
```

Exemplo positivo:

```
SELECT * FROM usuário WHERE userid = 1
UNION ALL
SELECT * FROM usuário WHERE idade = 10
```

**Justificativa** :

- Se você usar UNION, independentemente de os resultados da pesquisa serem repetidos, ele tentará mesclar e classificá-los antes de produzir os resultados finais.
- Se os resultados da pesquisa não tiverem registros duplicados, use UNION ALL em vez da união, o que aumentará a eficiência.

## 11. Use os campos numéricos o máximo possível. Se os campos contiverem apenas informações numéricas, tente não projetá-los como VARCHAR.

Exemplo negativo:

```
king_id varchar(20）NOT NULL;
```

Exemplo positivo:

```
king_id int(20）NOT NULL;
```

**Justificativa** :

- em comparação com os campos numéricos, os tipos de caracteres reduzirão o desempenho da consulta e da conexão e aumentarão a sobrecarga de armazenamento.

## 12. Use em VARCHAR/NVARCHAR vez de CHAR/NCHAR sempre que possível

Exemplo negativo:

```
deptName char(100) DEFAULT NULL
```

Exemplo positivo:

```
deptName varchar(100) DEFAULT NULL
```

**Justificativa** :

- Primeiro, como o espaço de armazenamento do campo de tamanho variável é pequeno, portanto, o espaço de armazenamento pode ser salvo.
- Em segundo lugar, para consultas, a pesquisa em um campo relativamente pequeno é mais eficiente.

## Bônus: Use o EXPLAIN para analisar seu plano SQL

Ao escrever SQL no desenvolvimento diário, tente desenvolver um hábito. Use o EXPLAIN para analisar o SQL que você escreveu, especialmente o índice.

```
EXPLAIN SELECT * FROM user WHERE userid = 10086 AND age =18;
```

---

Sim, chegamos ao fim. Espero que você goste e tenha uma ideia sobre como otimizar e acelerar suas consultas SQL.

Não deixe de conferir os outros artigos que escrevi ! Aqui no final da página encontram-se os links..

Obrigada e até a próxima !
