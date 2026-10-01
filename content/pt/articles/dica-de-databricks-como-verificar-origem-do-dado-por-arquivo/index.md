---
title: "Dica de Databricks: Como verificar a origem do dado por arquivo - input_file_name()"
date: 2023-06-22T13:24:00Z
summary: "Não seria um sonho tem uma coluna na sua tabela Bronze (ou Landing como quiser chamar) que informe de qual arquivo o dado foi originado ?"
tags: ["Databricks"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/dica-de-databricks-como-verificar-origem-do-dado-por-arquivo-lopes"
cover:
  image: cover.png
  alt: "Dica de Databricks: Como verificar a origem do dado por arquivo - input_file_name()"
  relative: true
---

**Não seria um sonho tem uma coluna na sua tabela Bronze (ou Landing como quiser chamar) que informe de qual arquivo o dado foi originado ?**

**Confira a seguir como fazer isso:**

Abaixo temos um conjunto de arquivos JSON para carga.

![](img-01.png)

Vamos realizar a leitura dos arquivos para um dataframe

![](img-02.png)

Agora, salvando o dataframe em Tabela Delta

![](img-03.png)

**Agora vem minha pergunta, como saber de qual arquivo cada pessoa veio?**

![](img-04.png)

O segredo está na função **input\_file\_name()**, essa função pode ser utilizada tanto com SQL ou com Python, ela retorna o nome do arquivo **lido**, no exemplo abaixo estou usando a função no **select** da minha tabela Bronze no formato Delta.

![](img-05.png)

Porém, se utilizarmos essa função após a criação da tabela o que será exibido são os arquivos parquet e não os arquivos de origem em si.

Para resolver esse problema, vamos adicionar a coluna "nomeArquivo" na criação da Tabela Delta.

![](img-06.png)

Agora sim !!

![](img-07.png)

Por hoje é isso pessoal, espero que tenha agregado.

Até a próxima.
