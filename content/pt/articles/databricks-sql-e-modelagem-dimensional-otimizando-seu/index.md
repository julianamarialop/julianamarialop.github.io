---
title: "Databricks SQL e Modelagem Dimensional: Otimizando seu Data Warehouse"
date: 2024-05-23T14:06:00Z
summary: "No dinâmico cenário do armazenamento de informações, as metodologias utilizadas para estruturar dados desempenham um papel crucial na descoberta de insights valiosos para a tomada de decisões informadas. Desde as…"
tags: ["Databricks", "SQL", "Engenharia de Dados", "Governança de Dados"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/databricks-sql-e-modelagem-dimensional-otimizando-seu-lopes-lirdf"
cover:
  image: cover.png
  alt: "Databricks SQL e Modelagem Dimensional: Otimizando seu Data Warehouse"
  relative: true
---

### Introdução

No dinâmico cenário do armazenamento de informações, as metodologias utilizadas para estruturar dados desempenham um papel crucial na descoberta de insights valiosos para a tomada de decisões informadas. Desde as teorias fundamentais das décadas de 1990 e 2000, propostas por especialistas como Inmon (Inmon WH, Building the Data Warehouse, 1990), Kimball (Kimball R, The Data Warehouse Toolkit, 1996) e mais tarde Linstedt (Linstedt D, Data Vault Series 1 — Data Vault Overview, 2002), diversas técnicas de modelagem para armazenamento de dados tradicionais têm evoluído e sido amplamente discutidas. Neste artigo, abordaremos a Modelagem Dimensional. Vamos explorar os pontos fortes e os desafios dessa abordagem, além de discutir as melhores práticas para implementá-la no Databricks.

Para projetar um modelo de dados dimensional, é essencial compreender profundamente os requisitos de negócios e ter um bom conhecimento das fontes de dados. A implementação mais comum da Modelagem Dimensional é o Star Schema, amplamente adotado como camada de apresentação na maioria dos data warehouses nas últimas décadas. Este método organiza os dados de maneira desnormalizada em torno de eventos mensuráveis, conhecidos como Fatos, e dos detalhes contextuais que cercam esses eventos, chamados de Dimensões.

### O sucesso da modelagem dimensional: Por que ela se tornou o padrão Ouro

A Modelagem Dimensional foi introduzida para otimizar o modelo de dados para análise na camada lógica dos Sistemas de Gerenciamento de Bancos de Dados Relacionais (RDBMS) sem a necessidade de redesenhar a camada física. Enquanto as camadas lógica e física do RDBMS foram projetadas especificamente para Processamento de Transações Online (OLTP), facilitando a entrada eficiente de dados orientados a linhas e garantindo propriedades ACID (Atomicidade, Consistência, Isolamento, Durabilidade) em dados normalizados, a Modelagem Dimensional foca no processamento analítico online (OLAP). Essa abordagem permite o processamento e a agregação de dados históricos com melhor desempenho.

### Benefícios da Modelagem Dimensional

**Usabilidade Simplificada dos Dados**: A modelagem dimensional torna a compreensão dos dados mais fácil ao estruturá-los em tabelas factuais e dimensionais. Isso facilita para os usuários finais a correspondência entre os processos do mundo real e o modelo de dados. Além disso, ela suporta a agregação eficiente de dados, servindo como uma camada semântica para ferramentas de Business Intelligence (BI).

**Desempenho de Consulta**: Uma das principais vantagens da modelagem dimensional é a otimização do desempenho das consultas sem comprometer a profundidade da análise histórica. O esquema Star, uma implementação comum dessa modelagem, desnormaliza os dados em fatos e dimensões granulares de negócios, melhorando significativamente o desempenho das consultas e a agregação de dados.

**Escalabilidade e Consistência**: Os modelos dimensionais são altamente escaláveis, acomodando volumes crescentes de dados e adaptando-se a requisitos de negócios em constante mudança. O esquema em estrela permite ajustes nas dimensões e nos fatos, facilita a gestão de dimensões de mudança lenta e a integração de dados incrementais. Outras abordagens, como o esquema Snowflake ou o uso de chaves substitutas nas tabelas de dimensão, ajudam a reduzir a redundância dos dados.

Com esses benefícios, a Modelagem Dimensional se consolidou como o padrão ouro para a análise de dados em ambientes de data warehousing, oferecendo uma estrutura robusta e flexível que atende às necessidades modernas de negócios.

### Mas, nem tudo são flores...

A Modelagem Dimensional atingiu um alto nível de otimização na camada lógica, equilibrando efetivamente a redundância e o desempenho das consultas. Isso era essencial quando os recursos de armazenamento e computação eram caros e os bancos de dados orientados a linhas não conseguiam lidar adequadamente com o processamento analítico. Com o avanço das tecnologias de dados, surgiram novas considerações sobre a modelagem dimensional tradicional.

**Limitações Operacionais e de Design:** A Modelagem Dimensional exige um investimento inicial significativo no design de esquemas, além de manutenção contínua dos pipelines de dados, geralmente gerenciados por ferramentas ETL. Esta abordagem envolve uma sobrecarga operacional e enfrenta desafios de design, como a complexidade no gerenciamento de dimensões que mudam lentamente e as junções de fato a fato. No passado, esses desafios eram aceitos como compensações necessárias para melhorar o desempenho das consultas. No entanto, com as tecnologias de dados modernas, esses problemas podem ser mitigados, reduzindo a necessidade de esquemas complexos e a sobrecarga operacional.

**Evolução Tecnológica em Armazenamento e Processamento de Dados:** As tecnologias modernas de armazenamento de dados proporcionam flexibilidade e escalabilidade ao desacoplar armazenamento e processamento. Essas tecnologias utilizam processamento paralelo massivo (MPP) e armazenamento físico em colunas, otimizando a agregação e análise de dados históricos por padrão. Com a redução significativa dos custos de armazenamento ao longo do tempo, as desvantagens da desnormalização foram minimizadas. Avanços como a compactação de dados na camada de armazenamento e clustering superam a complexidade de manter os dados normalizados.

Com esses avanços tecnológicos, é possível reavaliar a necessidade de designs de esquemas complexos e explorar alternativas que ofereçam simplicidade e eficiência operacional.

## Certo, se você optar por seguir com um modelo multidimensional, aqui estão algumas recomendações práticas para o Databricks...

Considerando os recursos avançados de Data Warehousing do Databricks, aderir estritamente à Modelagem Dimensional, por exemplo, Star Schema, não é mais uma necessidade; no entanto possível e muito bem apoiado. Analisaremos aqui várias tecnologias Databricks que tornam possível implementar e otimizar a técnica de Modelagem Dimensional.

- **Propriedades ACID:** Databricks [Delta Lake](https://www.databricks.com/product/delta-lake-on-databricks) suporta transações ACID em tabelas Delta, simplificando a manutenção e a qualidade dos modelos dimensionais.
- **Camadas de dados** : O Star Schema pode ser implantado em uma Gold Layer da [arquitetura medalhão](https://docs.databricks.com/en/lakehouse/medallion.html) em Databricks para potencializar a análise e a rápida tomada de decisões.
- **Pipelines ELT** : O pipeline para transformar os dados transacionais em modelos de dados dimensionais é suportado pelo Databricks SQL e [Delta Live Tables (DLT)](https://www.databricks.com/product/delta-live-tables) .
- **Restrições relacionais** : Ao contrário dos data lakes usuais, o Databricks oferece suporte [ao aprimoramento de esquema](https://docs.databricks.com/en/tables/constraints.html) , como restrições relacionais, por exemplo, chaves primárias, chaves estrangeiras e colunas de identidade no [SQL do Databricks](https://www.databricks.com/product/databricks-sql) como chaves substitutas e restrições CHECK impostas para qualidade de dados. As restrições físicas e virtuais podem existir como metaobjetos no [Catálogo do Unity](https://www.databricks.com/product/unity-catalog) **.**
- **Governança unificada** : todos os modelos de dados, tabelas de dimensões, tabelas de fatos e suas relações são registrados centralmente no Catálogo do Unity. Com o Unity Catalog como camada de governança unificada, Dimensões e Fatos podem ser descobertos e compartilhados entre organizações sem a necessidade de duplicá-los.
- **Otimização** : Databricks suporta [Liquid Clustering](https://docs.databricks.com/en/delta/clustering.html) , que otimiza incrementalmente o layout dos dados sem reescrever os dados, o que pode ser aplicado a tabelas de fatos, bem como a tabelas de dimensões.

Espero que essas dicas simples te ajude na implementação de seu modelo. Boa Sorte !
