---
title: "Databricks - Melhores Práticas para Gerenciamento de Bronze, Prata e Ouro (Arquitetura Medalhão)"
date: 2023-10-05T13:00:00Z
summary: "Muitos clientes com os quais trabalho implementam uma arquitetura Medallion para organizar logicamente seus dados em um Lakehouse. À medida que os dados fluem, eles passam por vários estágios ou camadas. O design mais…"
tags: ["Arquitetura de Dados", "Databricks"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/databricks-melhores-pr%C3%A1ticas-para-gerenciamento-de-bronze-lopes"
cover:
  image: cover.png
  alt: "Databricks - Melhores Práticas para Gerenciamento de Bronze, Prata e Ouro (Arquitetura Medalhão)"
  relative: true
---

Muitos clientes com os quais trabalho implementam uma [arquitetura Medallion](https://www.databricks.com/glossary/medallion-architecture) para organizar logicamente seus dados em um Lakehouse. À medida que os dados fluem, eles passam por vários estágios ou camadas. O design mais conhecido, como visto abaixo, utiliza uma camada Bronze, Prata e Ouro. Daí o termo "medalhão".

Embora o design de três camadas seja comum e amplamente reconhecido, tenho notado muitas discussões sobre o escopo, o propósito e as melhores práticas de cada uma dessas camadas. Também observei que há uma grande diferença entre teoria e prática.

### Estratégia da Plataforma de Dados

A consideração mais importante ao estratificar sua arquitetura em camadas é determinar como sua plataforma de dados será utilizada. Uma plataforma de dados centralizada e compartilhada terá uma estrutura diferente daquela de uma plataforma federada multiplataforma utilizada por diversos domínios. As camadas também variam dependendo se você alinha suas plataformas com o lado da origem dos sistemas ou com o lado do consumo de sua arquitetura. Uma plataforma alinhada à origem geralmente é mais fácil de padronizar em termos de camadas e estrutura do que uma plataforma alinhada ao consumidor, devido à diversidade de usos de dados no lado do consumo.

Levando essas considerações em conta, vamos explorar camada por camada. Para cada camada, começarei com alguns objetivos abstratos e de alto nível e, em seguida, aprofundarei com observações práticas.

### Área de Aterrissagem (Landing)

Uma camada opcional vista frequentemente em organizações que implementam uma plataforma de dados é uma área de aterrissagem ou zona de aterrissagem. Esta é uma localização intermediária na qual os dados de diversos sistemas de origem são armazenados antes de serem movidos para a camada Bronze. Essa camada é frequentemente necessária em situações em que é difícil extrair dados do sistema de origem alvo, como quando se trabalha com clientes externos ou fornecedores de SaaS. Nessas situações, há uma dependência ou, por vezes, os dados são fornecidos em um formato ou estrutura não preferencial.

O design de uma zona de destino varia de organização para organização. Muitas vezes, é simplesmente uma conta de armazenamento de blobs. Em outros casos, a zona de destino faz parte dos serviços do datalake, como um contêiner, bucket ou pasta específica onde os dados são ingeridos. Os dados nas zonas de destino costumam ser altamente diversificados em termos de formatos de arquivo, que podem incluir CSV, JSON, XML, Parquet, Delta e outros.

### Camada Bronze

A camada Bronze é geralmente um reservatório que armazena dados em seu estado natural e original. Ela contém dados não validados (não é necessário definir esquemas primeiro). Nessa camada, os dados são obtidos usando cargas completas ou cargas delta. Os dados armazenados na camada Bronze geralmente possuem as seguintes características:

- Mantêm o estado bruto da fonte de dados na sua estrutura "como está".
- Os dados são imutáveis (apenas leitura).
- Gerenciados usando tabelas particionadas por intervalo, por exemplo, usando uma estrutura de pasta AAAAMMDD ou data/hora.
- Mantêm o histórico completo (não processado) de cada conjunto de dados em um formato de armazenamento eficiente, como Parquet ou Delta.
- Para dados transacionais, podem ser acrescentados de forma incremental e crescer com o tempo.
- Fornecem a capacidade de recriar qualquer estado de um determinado sistema de dados.
- Podem ser uma combinação de streaming e transações em lote.
- Podem incluir metadados adicionais, como informações de esquema, nomes de arquivos de origem ou registro da hora em que os dados foram processados.

Uma pergunta comum é: "Qual é o melhor formato de arquivo? Devo usar Delta ou Parquet?" Delta é mais rápido, mas, como os dados já possuem controle de versão ou histórico usando uma estrutura de pastas, não vejo nenhum benefício atraente em manter um log de transações ou aplicar controle de versão. Os dados na camada Bronze geralmente são dados novos ou estão sendo anexados. Portanto, se você preferir usar Parquet, está tudo bem. Alternativamente, você pode usar Delta em alinhamento com todas as outras camadas.

Algumas pessoas argumentam que os dados na camada Bronze podem ser úteis para consultas ou análises ad hoc por parte dos usuários corporativos. Na minha experiência, trabalhando com clientes, raramente vejo dados brutos sendo usados como entrada para executar consultas ou análises ad hoc. Trabalhar com dados brutos exige um profundo entendimento de como o sistema de origem foi projetado e a elaboração de lógica de negócios complexa que está encapsulada nos próprios dados. Geralmente, esses dados contêm muitas tabelas pequenas e é difícil protegê-los. Em resumo, a camada Bronze é uma camada intermediária e serve como ponto de entrada para outras camadas, sendo acessada principalmente por equipes técnicas.

### Camada Prata

A camada Prata fornece uma estrutura refinada para os dados que foram ingeridos. Ela representa uma versão validada e enriquecida dos dados que pode ser confiável para cargas de trabalho posteriores, tanto operacionais quanto analíticas. A camada Prata geralmente possui as seguintes características:

- Utiliza regras de qualidade de dados para validação e processamento de dados.
- Normalmente contém apenas dados funcionais, filtrando dados técnicos ou irrelevantes provenientes da camada Bronze.
- Aplica historização, geralmente usando técnicas de dimensões de alteração lenta (SCD) do tipo 2 ou tipo 4. Isso envolve a adição de colunas como início, fim e atual.
- Armazena dados em um formato de armazenamento eficiente, preferencialmente Delta ou Parquet.
- Usa controle de versão para reverter erros de processamento.
- Lida com dados ausentes, padroniza campos vazios ou sujos.
- É frequentemente enriquecida com dados de referência e/ou mestres.
- Os dados muitas vezes são organizados em torno de áreas temáticas específicas.
- Os dados geralmente estão alinhados e organizados com o sistema de origem.

Para a camada Prata, alguns pontos de atenção incluem:

A camada Prata pode atuar como uma camada de armazenamento temporário em alguns casos, onde dados mais antigos podem ser excluídos ou contas de armazenamento podem ser criadas sob demanda. Isso depende do uso pretendido dos dados. Se você não planeja usar os dados em seu contexto original para relatórios operacionais ou análises operacionais, a camada Prata pode ser usada temporariamente. No entanto, se você planeja reter o histórico e usar esses dados para relatórios e análises operacionais, é recomendável tornar a camada Prata persistente.

Os dados na camada Prata podem ser consultados. Portanto, em termos de modelagem de dados, é recomendável seguir um modelo de dados mais desnormalizado. Isso ocorre porque esse design utiliza melhor o armazenamento distribuído baseado em colunas que é separado da computação. Embora seja possível implementar um design mais normalizado, não há argumentos convincentes para fazê-lo, uma vez que a camada Delta já oferece isolamento e proteção, como o esquema de mesclagem para lidar com alterações e o histórico disponível na camada Bronze. Portanto, adicionar complexidade extra e diminuir o desempenho não é geralmente recomendado.

Outra discussão que surge é se deve haver uma junção ou integração de dados entre aplicativos e sistemas de origem na camada Prata. A resposta depende do cenário. Se você planeja usar a camada Prata para relatórios operacionais ou análises operacionais, é geralmente recomendável não combinar ou integrar dados entre sistemas de origem, a fim de evitar acoplamentos desnecessários entre aplicativos. No entanto, se você deseja um design mais isolado, a integração de dados entre fontes pode ocorrer em uma camada superior.

O mesmo argumento mencionado acima também se aplica quando você alinha suas Lakehouses com o lado do sistema de origem de sua arquitetura. Se você planeja criar produtos de dados e deseja fortemente alinhar a propriedade dos dados, não é aconselhável que seus engenheiros façam a junção de dados entre aplicativos de outros domínios. Isso criaria pontos de acoplamento desnecessários.

Quanto a enriquecimentos, como cálculos, se você planeja facilitar relatórios operacionais que exigem enriquecimentos, é recomendável enriquecer os dados na camada Prata. Isso pode resultar em alguma calibração adicional ao combinar dados em um estágio posterior na camada Ouro, mas aproveita os benefícios da flexibilidade.

### Camada Ouro

Os dados na camada Ouro, de acordo com os princípios de uma arquitetura Lakehouse, geralmente são organizados em bancos de dados "específicos do projeto" prontos para consumo. Nesse contexto, a propriedade dos dados pode ser considerada alterada, uma vez que os dados não estão mais alinhados entre a origem e o sistema. Em vez disso, foram integrados e combinados com outros dados.

Na camada Ouro, dependendo dos casos de uso, é recomendável um modelo de dados mais desnormalizado e otimizado para leitura, com menos junções. Portanto, um esquema em estrela no estilo Kimball pode ser apropriado. Além disso, espere as seguintes características:

- As tabelas de Ouro representam dados que foram transformados para consumo ou casos de uso.
- Os dados são armazenados em um formato de armazenamento eficiente, de preferência Delta.
- A camada Ouro utiliza controle de versão para reverter erros de processamento.
- A historização é aplicada apenas para o conjunto de casos de uso ou consumidores, de modo que a camada Ouro pode ser uma seleção ou agregação de dados encontrados na camada Prata.
- Na camada Ouro, regras de negócios complexas são aplicadas, o que inclui atividades de pós-processamento, cálculos, enriquecimentos e otimizações específicas dos casos de uso.
- Os dados são altamente governados e bem documentados.

A camada Ouro costuma ser a mais complexa, pois seu design depende do escopo da arquitetura. No cenário mais simples, em que seus Lakehouses estão alinhados apenas com o lado do sistema de origem, os dados na camada Ouro representarão dados de "produtos de dados". Esses dados são genéricos e podem ser usados para uma ampla distribuição em diversos domínios após a distribuição. Nesse caso, espera-se que os dados atendam às necessidades precisas dos consumidores analíticos após a distribuição em outra plataforma, que também pode ser uma Lakehouse. Assim, os dados são modelados com uma estrutura específica para o caso de uso.

Se o escopo da Lakehouse for maior e abranger ambos os lados, camadas adicionais serão necessárias. Algumas organizações chamam essas camadas adicionais de espaço de trabalho ou camadas de apresentação. Nesse design, os dados na camada Ouro são mais genéricos e servem como camada de integração a partir da qual data marts ou subconjuntos podem ser preenchidos. Algumas empresas também usam essas camadas para compartilhar dados com outras plataformas ou equipes, fazendo seleções e/ou pré-filtragens para casos de uso específicos.

Espero que você tenha achado este artigo útil. Para todos que estão construindo uma plataforma de dados de próxima geração, aproveitem a jornada!
