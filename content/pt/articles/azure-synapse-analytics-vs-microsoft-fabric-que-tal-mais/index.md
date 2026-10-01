---
title: "Azure Synapse Analytics vs Microsoft Fabric: Que tal mais um projeto de migração ?"
date: 2023-05-30T17:44:00Z
summary: "Em maio de 2023, a Microsoft anunciou o Microsoft Fabric . Essa nova solução amplia a promessa de integração feita no Azure Synapse Analytics para abranger todas as cargas de trabalho analíticas, podendo ser utilizada…"
tags: ["Microsoft Fabric", "Azure", "SQL", "Custos", "Power BI", "Engenharia de Dados"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/azure-synapse-analytics-vs-microsoft-fabric-que-tal-mais-lopes"
cover:
  image: cover.png
  alt: "Azure Synapse Analytics vs Microsoft Fabric: Que tal mais um projeto de migração ?"
  relative: true
---

Em maio de 2023, a Microsoft anunciou o [Microsoft Fabric](https://learn.microsoft.com/en-gb/fabric/). Essa nova solução amplia a promessa de integração feita no *Azure Synapse Analytics* para abranger todas as cargas de trabalho analíticas, podendo ser utilizada por engenheiros de dados até profissionais de negócios especializados em conhecimento. O Microsoft *Fabric* combina *Power BI, Data Factory e Data Lake* em uma nova geração da infraestrutura de dados *Synapse*. Disponibilizado como uma oferta SaaS unificada, seu objetivo é reduzir custos e tempo de implementação, ao mesmo tempo em que habilita recursos avançados de ciência de dados.

### **Mas, e agora? Como ficam as empresas que investiram na plataforma Azure ?**

O *Microsoft Fabric* é o sucessor natural do *Synapse*. No entanto, as organizações que assumiram um compromisso significativo com o *Azure Synapse Analytics* podem ficar desapontadas ao descobrir que **não há um caminho de atualização automática para suas cargas de trabalho.**

Dependendo da carga de trabalho, diferentes graus de esforço serão necessários para adaptá-los para execução no *Microsoft Fabric*. Para algumas organizações, os custos associados a esse esforço de migração (e os riscos inerentes a qualquer migração) podem atuar como uma barreira.

Esse artigo tem por objetivo ajudar as pessoas que estão familiarizadas com o *Azure Synapse Analytics* a entender o *Fabric* e explanar o custo/benefício de uma futura migração. Iremos descrever como os recursos da *Synapse* são equivalentes no *Fabric*, destacando as principais diferenças ao longo do caminho.

Para as empresas que optarem por uma migração, alguns fatores importantes deveram ser considerados, por exemplo, cargas de trabalho baseadas em *Spark* oferecem um caminho de migração mais direto do que aquelas baseadas em SQL. No entanto, existem lacunas significativas em que os recursos do *Synapse* não são transferidos para o *Fabric* (mais adiante desse artigo iremos detalhar). Essa complexidade torna a decisão mais desafiadora. Minha recomendação é que as organizações invistam em um "pico técnico" para avaliar como o *Fabric* pode suportar suas cargas de trabalho *Synapse* mais comuns, a fim de obter informações valiosas sobre os desafios de migração e as oportunidades de longo prazo oferecidas pela plataforma.

### Quais as principais lacunas para uma migração ?

A lista a seguir fornece um mapeamento para cada recurso do *Azure Synapse versus Fabric* com as principais questões a serem resolvidas:

1. **SQL Serverless (Synapse) versus SQL Endpoint (Fabric)** : Sintaxe OPENROWSET não suportada, isso significa que o SQL não pode ser usado para consultar arquivos no Data Lake. No entanto, os dados estruturados colocados na área “Tabelas” do OneLake permitirão que esses dados sejam consultados via SQL no “Default Warehouse”, portanto, isso fornece funcionalidade semelhante ao OPENROWSET.
2. **Apache Spark Pools (Synapse) versus Managed Spark Pools (Fabric) :** O *Fabric* é SaaS, portanto, não há necessidade de criar e gerenciar pools *Spark*. Será possível escolher qual versão do ambiente *Spark* você deseja usar e carregar pacotes específicos do *Python* em seu ambiente, incluindo a opção de fazer isso dinamicamente dentro de um notebook. As melhorias de desempenho significam que o ambiente *Spark* subjacente “gira” em segundos, em vez de minutos. Finalmente temos um concorrente digno para o *Databricks*.
3. **Notebooks Spark (Synapse) versus Notebooks (Fabric)** : Uma série de novos recursos foram adicionados como capacidade de adicionar comentários aos notebooks e coedição – vários usuários podem abrir e editar um Notebook simultaneamente assim como *Data Wrangler* – novos utilitários estão disponíveis em Notebooks para permitir que os dados sejam explorados.
4. **Synapse Studio versus Power BI Interfaces:** A experiência do usuário agora é organizada em torno de personas específicas “Data Engineering”, “Data Science”, “Data Warehousing” e “Real-time Analytics”, então você ainda tem *Power BI e Data Factory* como ferramentas independentes.
5. **Pipelines:** Algumas ações de pipeline foram removidas no *Fabric*. Por exemplo, a integração com recursos de *Machine Learning* agora é via notebooks.

### Vamos falar sobre melhorias..

Olhando para o ecossistema Microsoft mais amplo, o *Fabric* oferece integração "pronta para uso" com funcionalidades que, de outra forma, exigiriam a criação e configuração de recursos adicionais do Azure para integração com o *Synapse*, por exemplo:

- [Azure Machine Learning](https://azure.microsoft.com/en-gb/products/machine-learning) - não há necessidade de criar uma instância do Azure Machine Learning para registrar seus modelos de aprendizado de máquina e registrar experimentos, o *Fabric* fornece um ponto de extremidade MLFlow por padrão.
- [Power BI](https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)- embora houvesse integração entre o *Synapse* e o *Power BI*, isso é bastante aprimorado com o *Fabric*. Conjuntos de dados podem ser criados com facilidade diretamente no OneLake, modelos e medidas podem ser criados a partir do *Fabric UX*. Além disso, um conjunto de dados padrão é criado em qualquer Lakehouse no Fabric, simplificando ainda mais o processo. Por fim, a maneira como os conjuntos de dados são apresentados no Fabric não apenas como uma entrada para o *Power BI*, mas como um "produto de dados" que pode ser consumido por muitos outros meios parece um grande passo à frente.

### Modelo comercial e custos

O Microsoft *Fabric* adota um modelo comercial diferente do *Azure Synapse Analytics*. Para organizações pequenas (com cargas de trabalho menores e começando em sua jornada de dados) o modelo "pagamento por consulta" do SQL Serverless e a natureza "pagamento por minuto" dos Spark Pools são diferenciais com relação a outros fornecedores cloud.

No *Fabric* abandona em grande parte a abordagem "pague pelo que usar". Adota uma abordagem baseada na capacidade. **Isso forçará as organizações a se comprometerem com um gasto mínimo mensal na plataforma.** Embora existam níveis mais baixos disponíveis que permitirão que organizações com cargas de trabalho menores adotem o *Fabric*, a principal preocupação é que isso pode resultar em um impacto nos custos da Azure.

### Conclusões

As organizações que atualmente usam o Azure *Synapse Analytics* devem avaliar o Microsoft *Fabric* e determinar como ele se encaixa em seu roteiro de tecnologia. Os principais fatores a serem considerados incluem:

- Impacto em custos - como a mudança de PaaS (*Synapse*) para SaaS (*Fabric*) afeta o custo? Por exemplo, é possível economizar eliminando a necessidade de gerenciar os recursos do Azure?
- Prós e contras do SaaS - como uma plataforma SaaS, o *Fabric* adota uma abordagem opinativa para implantar, configurar e implementar tecnologias sobre as quais você tem mais controle com a natureza PaaS do *Synapse* (e os recursos mais amplos do Azure que geralmente o acompanham).
- Bloqueio do fornecedor - mudar para o *Fabric* torna mais difícil mudar para um fornecedor diferente no futuro? Este é um problema significativo em sua empresa?
- Tempo para valorizar - a experiência do desenvolvedor e os recursos de produtividade no *Fabric* (por exemplo, a nova experiência de notebooks) abrem oportunidades para simplificar o ciclo de vida de desenvolvimento de ponta a ponta?
- Minimizando a dívida técnica - o *Fabric* simplificará sua base de código e, portanto, reduzirá o esforço de manutenção? Por exemplo, conectividade direta do *Power BI* para tabelas Delta no OneLake significa que uma camada SQL (e os scripts associados para criar as exibições SQL) não precisa mais ser mantida.
- Custos da Azure - *Fabric* adota um modelo de cobrança diferente do *Synapse*, como isso afetará seu Azure OpEx mensal?
- Novos recursos - olhando além da migração "like for like" da funcionalidade existente, quais oportunidades os novos recursos do *Fabric* oferecem, eles desbloqueiam casos de uso que estão em sua lista de pendências?
- Estratégia - como o *Fabric* se encaixa em sua estratégia de análise e dados de longo prazo?

Se você acredita que há oportunidades, como próximo passo, recomendo que você faça um pequeno investimento direcionado em um "pico técnico" para avaliar o quão bem o *Fabric* pode suportar sua visão de dados e análises.

**Referências**

<https://azure.microsoft.com/en-us/blog/introducing-microsoft-fabric-data-analytics-for-the-era-of-ai/>
