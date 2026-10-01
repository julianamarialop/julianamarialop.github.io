---
title: "Databricks Lakebase: O Guia Definitivo para a Nova Era de Dados Operacionais e Agentes de IA"
date: 2026-03-03T12:31:00Z
summary: "O Databricks Lakebase representa uma evolução significativa na arquitetura de dados, especificamente no domínio dos bancos de dados OLTP (Online Transactional Processing). Não se trata apenas de mais um banco de dados…"
tags: ["Agentes de IA", "Arquitetura de Dados", "Governança de Dados", "Databricks", "Engenharia de Dados", "Custos"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/databricks-lakebase-o-guia-definitivo-para-nova-era-de-lopes-qcg0f"
cover:
  image: cover.png
  alt: "Databricks Lakebase: O Guia Definitivo para a Nova Era de Dados Operacionais e Agentes de IA"
  relative: true
---

O **Databricks Lakebase** representa uma evolução significativa na arquitetura de dados, especificamente no domínio dos bancos de dados OLTP (Online Transactional Processing). Não se trata apenas de mais um banco de dados na nuvem, mas de uma redefinição fundamental de como os dados transacionais são armazenados, processados e integrados com ecossistemas analíticos e de inteligência artificial. Esta nova arquitetura visa eliminar o abismo histórico entre as necessidades operacionais de baixa latência e as demandas de escala e flexibilidade dos data lakes.

Tradicionalmente, bancos de dados OLTP e sistemas analíticos operam em silos distintos, exigindo pipelines ETL complexos e frágeis para mover dados entre eles. O Lakebase propõe uma solução unificada, combinando a robustez de um banco de dados relacional com a escalabilidade e a economia do armazenamento em nuvem. Seu design é intrinsecamente otimizado para a era dos agentes de IA, oferecendo capacidades que os sistemas legados não conseguem prover.

Para compreender o impacto do Lakebase, é essencial analisar seus pilares técnicos e como eles resolvem desafios de longa data na engenharia de dados. A inovação reside na forma como ele gerencia latência, isolamento de dados e integração, tudo isso enquanto suporta cargas de trabalho operacionais intensivas e as demandas emergentes da inteligência artificial.

### Engenharia de Baixa Latência em Object Storage

Um dos maiores desafios ao desacoplar armazenamento e computação em bancos de dados OLTP, utilizando *object storage* (como S3 ou ADLS), é a latência. O Lakebase aborda isso com uma arquitetura sofisticada que emprega camadas de estado (soft-state) e mecanismos de cache inteligente. Embora os dados frios residam no armazenamento de objetos de baixo custo, as páginas ativas do Postgres são mantidas em camadas intermediárias de alta performance. Essa abordagem permite que o Lakebase entregue latência de milissegundos de um dígito e suporte milhões de transações por segundo, uma performance antes considerada inatingível para arquiteturas baseadas puramente em data lakes. É a combinação da eficiência do armazenamento em nuvem com a performance necessária para aplicações transacionais críticas.

### Ramificação Instantânea: O "Git Checkout" para Dados Operacionais

O mecanismo de ramificação (branching) do Lakebase, baseado em copy-on-write, é uma funcionalidade transformadora. Ele permite a criação de réplicas exatas de um banco de dados de produção, incluindo esquema e dados, de forma instantânea e com custo marginal. Isso é viável porque o Lakebase isola os metadados. Ao criar um novo branch, ele inicialmente aponta para os mesmos arquivos de dados originais. As alterações são gravadas apenas em novos blocos, garantindo isolamento total para:

- **Testes de alta fidelidade:** Desenvolvedores podem testar novas funcionalidades em um ambiente idêntico ao de produção sem riscos.
- **Migrações de esquema complexas:** Alterações no esquema podem ser testadas e validadas em um ambiente isolado antes de serem aplicadas à produção.
- **Experimentação de agentes de IA:** Agentes podem operar em suas próprias instâncias isoladas para experimentação e validação, sem afetar a produção ou outros agentes.

Essa capacidade elimina a necessidade de ambientes de staging caros e demorados, acelerando o ciclo de desenvolvimento e garantindo a integridade dos dados de produção.

### Otimização para Agentes de IA: Por que o Lakebase é Essencial

A verdadeira força motriz por trás do design do Lakebase é o suporte robusto a agentes de IA autônomos. Não é apenas o branching que o torna ideal, mas uma combinação de características que atendem às demandas intrínsecas da inteligência artificial operacional:

1. **Estado Persistente de Baixa Latência:** Agentes de IA, especialmente em cenários de tempo real como recomendação de produtos ou detecção de fraudes, precisam de acesso a dados operacionais com latência de milissegundos. O Lakebase oferece isso ao manter as páginas ativas do Postgres em camadas de alta performance, mesmo com o armazenamento subjacente em object storage. Isso significa que os agentes podem tomar decisões rápidas baseadas nos dados mais recentes, sem gargalos de performance que limitariam sistemas tradicionais.
2. **Escalabilidade Elástica (Serverless):** Agentes de IA podem ter picos de demanda imprevisíveis. Um banco de dados tradicional exigiria provisionamento excessivo para lidar com esses picos, resultando em custos elevados. O Lakebase, com sua arquitetura serverless, escala elasticamente até zero quando não está em uso e expande-se instantaneamente para atender a milhões de transações por segundo. Isso otimiza custos e garante que os agentes sempre tenham os recursos necessários, sem intervenção manual.
3. **Unificação Nativa com o Unity Catalog:** A governança de dados é crucial para agentes de IA. O Lakebase se integra nativamente ao Unity Catalog, estendendo as mesmas permissões e políticas de segurança do Lakehouse para os dados operacionais. Isso simplifica a gestão de acesso e garante que os agentes operem dentro dos limites de conformidade, além de permitir que os dados operacionais sejam imediatamente visíveis para o treinamento e monitoramento de modelos de IA no Lakehouse, sem a necessidade de pipelines ETL complexos.

Esses pilares, combinados com o *branching* para experimentação segura, tornam o Lakebase a infraestrutura de estado ideal para a segurança, a confiabilidade e a agilidade da inteligência artificial autônoma. Ele fornece a base para que agentes de IA possam experimentar, aprender e operar em produção com confiança.

### Unificação Real: O Fim do Abismo entre OLTP e OLAP

Historicamente, a movimentação de dados de bancos de dados operacionais para sistemas analíticos (Lakehouse) era um processo árduo, envolvendo pipelines ETL frágeis, gerenciamento manual de esquemas e latência significativa. O Lakebase, com sua integração nativa ao Unity Catalog, elimina essa complexidade.

Os dados operacionais são sincronizados quase em tempo real com a camada analítica, sem a necessidade de infraestrutura duplicada ou custos de saída de dados. A governança é unificada: as mesmas permissões e políticas de segurança definidas no Unity Catalog para o Lakehouse são estendidas ao Lakebase. Isso resulta em uma plataforma de dados verdadeiramente unificada, onde os dados operacionais estão imediatamente disponíveis para análise e treinamento de modelos de IA, sem atrito.

### Arquitetura de Referência: Integrando Lakebase com Ecossistemas Existentes

Para entender como o Lakebase se encaixa em uma arquitetura de dados moderna, é crucial visualizar sua integração com sistemas legados e o Lakehouse. A abordagem não é de um ETL tradicional, mas sim de uma **integração Zero-ETL** ou **acesso federado**, que minimiza a movimentação de dados e a complexidade.

Imagine o seguinte cenário:

1. **Sistemas OLTP Legados (Fontes de Dados):** Sua organização possui bancos de dados transacionais existentes (PostgreSQL, MySQL, SQL Server, Oracle, etc.) que contêm dados operacionais críticos. Esses sistemas continuam a ser a fonte primária de verdade para suas aplicações legadas.
2. **Lakehouse (Camada Analítica Unificada):** O Databricks Lakehouse, construído sobre Delta Lake e Unity Catalog, atua como sua plataforma unificada para dados analíticos, data warehousing, BI e Machine Learning. Ele ingere dados de diversas fontes, incluindo os sistemas OLTP legados, através de mecanismos como o Lakehouse Federation ou streaming de dados (ex: Kafka, Change Data Capture - CDC) para o Delta Live Tables.
3. **Lakebase (Camada de Serviço Operacional para Agentes de IA):** Aqui é onde o Lakebase entra. Ele serve como a camada de dados operacional de alta performance e baixa latência especificamente otimizada para agentes de IA. O Lakebase pode ser alimentado de duas formas principais: **Novos Dados Operacionais:** Para novas aplicações ou microsserviços que exigem as capacidades únicas do Lakebase (baixa latência em object storage, branching, escalabilidade serverless), os dados podem ser escritos diretamente no Lakebase e **Dados Sincronizados do Lakehouse:** Para dados que se originam em sistemas legados e são ingeridos no Lakehouse, o Lakebase pode consumir esses dados de forma otimizada. Graças à integração nativa com o Unity Catalog, as tabelas do Lakehouse podem ser facilmente acessadas e, se necessário, materializadas ou referenciadas no Lakebase para que os agentes de IA tenham acesso operacional de baixa latência. Isso cria um fluxo de dados bidirecional ou de consumo, onde o Lakebase atua como um cache operacional inteligente ou um datastore primário para as operações dos agentes.

**O Papel do Lakebase para Agentes de IA:**

Nesta arquitetura, o Lakebase não substitui o Lakehouse, mas o complementa, fornecendo a **velocidade e a agilidade transacional** que os agentes de IA exigem. Ele é a "memória de curto prazo" e o "ambiente de trabalho" dos agentes, onde eles podem:

- **Ler dados operacionais em tempo real:** Para tomar decisões instantâneas (ex: recomendação, detecção de fraude).
- **Escrever e atualizar dados:** Para executar ações (ex: ajustar estoque, processar um pedido).
- **Experimentar com segurança:** Utilizar o *branching* para testar novas lógicas ou modelos de agentes sem impactar a produção.

Essa arquitetura permite que a organização mantenha seus sistemas legados funcionando, enquanto moderniza sua camada de dados para suportar a próxima geração de aplicações e agentes de IA, tudo isso dentro de uma estrutura unificada e governada pelo Unity Catalog.

### Estratégia de Modelagem e Retenção de Dados no Lakebase

A modelagem de dados e a estratégia de retenção são aspectos cruciais para otimizar o Lakebase para agentes de IA e garantir sua eficiência no ecossistema Lakehouse. A abordagem aqui difere dos bancos de dados analíticos tradicionais.

### 1. Modelagem de Dados: Relacional Puro para Operações de Agentes

Sim, a indicação é um **modelo relacional puro**, similar ao PostgreSQL, para as tabelas dentro do Lakebase. Isso se deve a:

- **Familiaridade e Maturidade:** O modelo relacional é amplamente compreendido e otimizado para operações transacionais (OLTP), que são o foco dos agentes de IA que precisam ler e escrever dados rapidamente.
- **Integridade Referencial:** A capacidade de impor chaves primárias e estrangeiras garante a consistência dos dados, essencial para a confiabilidade das decisões dos agentes.
- **Consultas Pontuais Otimizadas:** Agentes frequentemente realizam consultas pontuais ou transações específicas (ex: "qual o estoque do produto X?", "atualizar status do pedido Y?"). O modelo relacional é altamente eficiente para esses tipos de operações.

É importante ressaltar que, enquanto o Lakebase mantém o modelo relacional para a camada operacional, o Lakehouse (Delta Lake) continua sendo o local ideal para modelos de dados dimensionais (Star Schema, Snowflake Schema) otimizados para análises complexas e BI.

### 2. Matriz de Decisão de Ingestão: O que vai para o Lakebase?

A decisão sobre quais dados devem ser materializados no Lakebase não é arbitrária, mas sim guiada pela criticidade operacional para os agentes de IA. Não se trata de uma cópia indiscriminada de todos os dados legados, mas de uma seleção estratégica baseada em três critérios principais:

**Frequência de Escrita e Atualização (Volatilidade):**

- **Pergunta:** O agente de IA precisa atualizar este dado em milissegundos ou segundos? A informação muda tão rapidamente que uma replicação assíncrona ou um cache de maior latência no Lakehouse seria insuficiente para a consistência operacional?
- **Exemplo:** O **estoque de produtos** em um e-commerce é um dado altamente volátil e crítico. Um agente de recomendação ou de gestão de pedidos precisa saber o estoque exato agora para evitar vender um produto indisponível. Dados como o **endereço de entrega do cliente**, embora importantes, não exigem a mesma frequência de atualização por um agente e podem ser acessados com maior latência do Lakehouse.

**Dependência de Estado para Decisão Imediata:**

- **Pergunta:** O agente de IA precisa desse dado para tomar uma decisão imediata e crítica no seu fluxo de trabalho? A ausência ou desatualização dessa informação impediria o agente de completar sua tarefa ou levaria a uma decisão incorreta?
- **Exemplo:** Para um agente de detecção de fraude, o **histórico recente de transações** de um usuário é crucial para identificar padrões anômalos *no momento da transação*. Já o **histórico completo de compras** para análise de tendências pode residir no Lakehouse, pois não é necessário para a decisão imediata de aprovar ou negar uma transação.

**Volume e Granularidade de Acesso:**

- **Pergunta:** O agente acessa esse dado em alta granularidade (registros individuais) e em grande volume de requisições pontuais? Ou o acesso é mais para análises agregadas ou em lote?
- **Exemplo:** Um agente de personalização pode precisar acessar o **perfil de preferência individual** de um usuário (alta granularidade, muitas requisições pontuais). Dados de **campanhas de marketing passadas** (baixa granularidade, acesso em lote para análise) seriam mais adequados para o Lakehouse.

**Como o Unity Catalog Ajuda na Decisão:**

O Unity Catalog atua como o ponto central de governança. Ele permite que você defina e gerencie o acesso aos dados, independentemente de estarem no Lakebase ou no Lakehouse. Para dados que precisam ser materializados no Lakebase, você pode usar mecanismos de **sincronização de dados** (como CDC) que levam apenas as tabelas ou colunas críticas do Lakehouse para o Lakebase, mantendo a linhagem e a governança unificadas. Alternativamente, para novas aplicações, o Lakebase pode ser o destino primário para esses dados operacionais críticos.

Em resumo, a decisão de "copiar" (ou materializar) dados para o Lakebase é um exercício de engenharia de dados focado em performance e criticidade operacional. Apenas os dados que são verdadeiramente o "estado ativo" e que exigem a latência de milissegundos para as operações dos agentes devem residir no Lakebase, enquanto o vasto histórico e os dados menos voláteis permanecem no Lakehouse.

### 3. Armazenamento: Otimização para Baixa Latência e Eficiência

O Lakebase não "copia" indiscriminadamente todos os dados do legado. A estratégia de armazenamento é mais inteligente e focada no "estado ativo" necessário para os agentes:

- **Dados Operacionais Ativos:** O Lakebase é projetado para armazenar o subconjunto de dados operacionais que os agentes de IA precisam acessar e modificar em tempo real. Isso pode ser uma replicação de tabelas específicas de sistemas legados (via CDC ou *streaming* para o Lakehouse e, em seguida, para o Lakebase) ou dados gerados diretamente por novas aplicações que utilizam o Lakebase como seu banco de dados primário.
- **Materialização Seletiva:** Para dados que residem primariamente no Lakehouse (originados de sistemas legados), o Lakebase pode materializar visões ou tabelas específicas que são relevantes para as operações dos agentes. Isso significa que apenas os dados necessários para as decisões em tempo real dos agentes são mantidos na camada de baixa latência do Lakebase, enquanto o histórico completo e os dados frios permanecem no Lakehouse.
- **Armazenamento em Object Storage com Cache Inteligente:** Embora os dados sejam armazenados em *object storage* de baixo custo, o Lakebase utiliza camadas de cache e *soft-state* para garantir que os dados mais acessados pelos agentes estejam disponíveis com latência de milissegundos. Isso evita a duplicação massiva de dados e otimiza os custos de armazenamento.

### Recomendação de Retenção: Estado Ativo vs. Histórico Frio

A estratégia de retenção no Lakebase deve ser orientada pela necessidade operacional dos agentes de IA:

- **Lakebase: Retenção de Curto Prazo (Estado Ativo):** O Lakebase deve reter apenas o estado ativo e relevante para as operações em tempo real dos agentes. Isso significa dados que são frequentemente lidos e modificados pelos agentes. Por exemplo, para um agente de recomendação, o estoque atual de produtos, o histórico recente de interações do usuário e o status de pedidos em andamento. Períodos de retenção podem variar de dias a poucas semanas, dependendo da volatilidade e da criticidade dos dados para as decisões do agente.
- **Lakehouse: Retenção de Longo Prazo (Histórico Frio):** O histórico completo e os dados frios (que não são mais necessários para decisões em tempo real, mas são valiosos para análises retrospectivas, treinamento de modelos e conformidade) devem ser descarregados para o Lakehouse (Delta Lake). A integração nativa do Lakebase com o Unity Catalog facilita esse processo, permitindo que os dados sejam movidos ou sincronizados para o Lakehouse de forma eficiente e governada.

Essa divisão clara de responsabilidades garante que o Lakebase permaneça ágil e de baixa latência para os agentes, enquanto o Lakehouse oferece escalabilidade e economia para o armazenamento de longo prazo e análises complexas. É uma abordagem que equilibra performance operacional com eficiência de custos e governança de dados.

### Caso de Uso: Recomendação de Produtos em Tempo Real com Agentes de IA em E-commerce

Imagine uma grande plataforma de e-commerce que deseja oferecer recomendações de produtos hiper-personalizadas e em tempo real, adaptando-se instantaneamente ao comportamento do usuário e às mudanças de estoque/preço. Os sistemas tradicionais lutam com a latência e a complexidade de gerenciar dados transacionais e analíticos para essa finalidade.

**Desafio:**

- **Latência:** Atrasos na ingestão de dados de cliques, visualizações e compras resultam em recomendações desatualizadas.
- **Experimentação:** Testar novos algoritmos de recomendação ou estratégias de precificação em produção é arriscado e lento.
- **Escalabilidade:** Lidar com milhões de eventos por segundo e manter a performance do banco de dados transacional.
- **Agentes de IA:** Treinar e operar agentes de IA que precisam de acesso rápido e consistente a dados operacionais para tomar decisões em milissegundos.

**Solução com Databricks Lakebase:**

1. **Dados Operacionais em Lakebase:** Todos os eventos de usuário (cliques, visualizações, adições ao carrinho, compras) e dados de catálogo de produtos (preço, estoque) são armazenados no Lakebase. A baixa latência garante que esses dados estejam disponíveis quase instantaneamente.
2. **Agentes de IA para Recomendação:** Agentes de IA são desenvolvidos para monitorar o comportamento do usuário em tempo real. Eles acessam os dados do Lakebase para identificar padrões e gerar recomendações personalizadas.
3. **Branching para Experimentação Segura:** Antes de lançar um novo algoritmo de recomendação, um branch do banco de dados do Lakebase é criado. Agentes de IA podem ser treinados e testados nesse ambiente isolado, simulando cenários de produção sem impactar os clientes reais. Se o novo algoritmo gerar hallucinations ou recomendações inadequadas, o branch é simplesmente descartado.
4. **Integração com Lakehouse:** Os dados do Lakebase são sincronizados em tempo real com o Lakehouse via Unity Catalog. Isso permite que equipes de Data Science usem o histórico completo de interações para treinar modelos de IA mais complexos e realizar análises de negócio aprofundadas, enquanto os agentes operam com os dados mais recentes.

**Benefícios:**

- **Recomendações em Tempo Real:** A baixa latência do Lakebase garante que as recomendações sejam sempre baseadas nos dados mais atuais.
- **Inovação Acelerada:** O branching permite testar e iterar rapidamente em novos algoritmos de IA sem risco à produção.
- **Experiência do Cliente Aprimorada:** Recomendações mais precisas e personalizadas levam a maior engajamento e vendas.
- **Governança Unificada:** O Unity Catalog garante que todos os dados, do operacional ao analítico, estejam sob o mesmo guarda-chuva de segurança e conformidade.

### Guia de Implementação Passo a Passo: Agentes de IA com Agent Bricks e Lakebase

Para demonstrar a capacidade do Lakebase em conjunto com o Agent Bricks para construir agentes de IA robustos, vamos detalhar um fluxo de trabalho técnico. O foco será na criação de um agente de recomendação que interage com dados operacionais no Lakebase e utiliza o branching para experimentação segura.

### 1. Configuração Inicial no Databricks e Lakebase

Primeiro, certifique-se de que seu ambiente Databricks esteja configurado com o Unity Catalog e o Agent Bricks Preview habilitado. Você precisará de um workspace Databricks e permissões para criar catálogos, esquemas e utilizar o Agent Bricks.

```
-- Criar um catálogo no Unity Catalog para o Lakebase
CREATE CATALOG IF NOT EXISTS ecommerce_catalog;
USE CATALOG ecommerce_catalog;

-- Criar um esquema (database) para os dados operacionais do e-commerce
CREATE SCHEMA IF NOT EXISTS operational_db;
USE SCHEMA operational_db;

-- Tabela de Pedidos (OLTP) no Lakebase
CREATE TABLE orders (
    order_id STRING NOT NULL PRIMARY KEY,
    user_id STRING NOT NULL,
    product_id STRING NOT NULL,
    quantity INT NOT NULL,
    order_timestamp TIMESTAMP NOT NULL,
    status STRING NOT NULL
) USING LAKEBASE;

-- Tabela de Produtos (OLTP) no Lakebase
CREATE TABLE products (
    product_id STRING NOT NULL PRIMARY KEY,
    product_name STRING NOT NULL,
    category STRING NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL
) USING LAKEBASE;

-- Inserir dados de exemplo
INSERT INTO products VALUES
(\'prod_001\', \'Laptop Gamer\', \'Eletronicos\', 1500.00, 100),
(\'prod_002\', \'Mouse Sem Fio\', \'Acessorios\', 50.00, 500),
(\'prod_003\', \'Teclado Mecanico\', \'Acessorios\', 120.00, 200);

INSERT INTO orders VALUES
(\'order_001\', \'user_a\', \'prod_001\', 1, \'2026-02-27 10:00:00\', \'completed\'),
(\'order_002\', \'user_b\', \'prod_002\', 2, \'2026-02-27 10:05:00\', \'pending\'),
(\'order_003\', \'user_a\', \'prod_003\', 1, \'2026-02-27 10:15:00\', \'completed\');        
```

### 2. Desenvolvendo um Agente de Recomendação com Agent Bricks

Vamos criar um agente simples que, dado um user\_id, recomenda produtos baseados em compras anteriores e no estoque atual. O Agent Bricks permite definir agentes de forma declarativa. Este exemplo simula a lógica dentro de um notebook Databricks, que seria a base para um agente Agent Bricks.

```
# Exemplo de código Python em um notebook Databricks para um agente de recomendação
# Este código simula a lógica que seria encapsulada por um Agent Bricks

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.sql import Statement

# Inicializar o cliente do Workspace (assumindo autenticação configurada)
w = WorkspaceClient()

def get_user_orders(user_id: str, branch: str = "main"):
    # Conectar ao Lakebase usando o branch especificado
    # Em um ambiente real, o Agent Bricks gerencia a conexão e o contexto do branch
    query = f"USE BRANCH {branch}; SELECT product_id FROM orders WHERE user_id = \'{user_id}\'"
    result = w.statement_execution.execute_statement(
        statement=query,
        warehouse_id="<seu_warehouse_id>", # Substitua pelo ID do seu SQL Warehouse
        catalog="ecommerce_catalog",
        schema="operational_db"
    ).result.data_array
    return [row[0] for row in result]

def get_product_stock(product_id: str, branch: str = "main"):
    query = f"USE BRANCH {branch}; SELECT stock_quantity FROM products WHERE product_id = \'{product_id}\'"
    result = w.statement_execution.execute_statement(
        statement=query,
        warehouse_id="<seu_warehouse_id>",
        catalog="ecommerce_catalog",
        schema="operational_db"
    ).result.data_array
    return result[0][0] if result else 0

def recommend_products(user_id: str, branch: str = "main"):
    purchased_products = get_user_orders(user_id, branch)
    recommendations = []
    # Lógica de recomendação simplificada: recomendar produtos com estoque > 0 que não foram comprados
    all_products_query = f"USE BRANCH {branch}; SELECT product_id, product_name FROM products WHERE stock_quantity > 0"
    all_products_result = w.statement_execution.execute_statement(
        statement=all_products_query,
        warehouse_id="<seu_warehouse_id>",
        catalog="ecommerce_catalog",
        schema="operational_db"
    ).result.data_array

    for prod_id, prod_name in all_products_result:
        if prod_id not in purchased_products:
            recommendations.append(prod_name)
    return recommendations

# Exemplo de uso do agente (simulado)
user_to_recommend = "user_a"
print(f"Recomendações para {user_to_recommend} (branch main): {recommend_products(user_to_recommend)}")        
```

### 3. Experimentação Segura com Branching e Agent Bricks

Agora, vamos usar o branching do Lakebase para testar uma nova estratégia de recomendação que envolve uma promoção agressiva em um produto específico, o que pode impactar o estoque. O Agent Bricks pode ser configurado para operar em branches específicos para testes.

```
-- Criar um novo branch para testar a promoção
CREATE BRANCH promo_test ON TABLE orders;
CREATE BRANCH promo_test ON TABLE products;        
```

Um agente de IA configurado para o branch promo\_test pode agora simular as alterações. No Agent Bricks, você especificaria o branch no contexto de execução do agente.

```
# Simulação de um agente de IA operando no branch \'promo_test\'
# O Agent Bricks abstrairia a gestão do branch para o desenvolvedor do agente

# Agente de IA decide aplicar um desconto e vender um Laptop Gamer
# Esta operação ocorre APENAS no branch \'promo_test\'
update_query = "UPDATE products SET stock_quantity = stock_quantity - 1 WHERE product_id = \'prod_001\'"
w.statement_execution.execute_statement(
    statement=update_query,
    warehouse_id="<seu_warehouse_id>",
    catalog="ecommerce_catalog",
    schema="operational_db",
    branch="promo_test" # Especifica o branch para a operação
)

# O agente verifica o estoque no branch de teste
print(f"Estoque de Laptop Gamer no branch promo_test: {get_product_stock(\'prod_001\', branch=\'promo_test\')}")

# O estoque no branch principal permanece inalterado
print(f"Estoque de Laptop Gamer no branch main: {get_product_stock(\'prod_001\', branch=\'main\')}")        
```

Se o resultado da simulação no promo\_test for positivo (por exemplo, aumento de vendas simuladas sem esgotar o estoque de forma prejudicial), as alterações podem ser mescladas para o branch main. Caso contrário, o branch promo\_test pode ser descartado sem afetar a produção.

```
-- Se os testes forem bem-sucedidos, mesclar as alterações (exemplo conceitual, a mesclagem pode ser mais complexa)
-- MERGE BRANCH promo_test INTO main ON TABLE orders;
-- MERGE BRANCH promo_test INTO main ON TABLE products;

-- Descartar o branch de teste após a conclusão (seja mesclado ou não)
DROP BRANCH promo_test ON TABLE orders;
DROP BRANCH promo_test ON TABLE products;        
```

### 4. Integração Contínua com o Lakehouse (Unity Catalog)

Independentemente dos branches operacionais, os dados do Lakebase são continuamente sincronizados com o Lakehouse via Unity Catalog. Isso permite que equipes de Data Science e Analytics continuem a treinar modelos de IA mais complexos e realizar análises de negócio aprofundadas sobre o histórico completo de interações, enquanto os agentes operam com os dados mais recentes e em seus branches isolados.

```
-- Exemplo de como uma equipe de Data Science pode consultar dados operacionais
-- diretamente do Lakehouse via Unity Catalog para treinamento de modelos
SELECT
    o.user_id,
    p.product_name,
    o.quantity,
    o.order_timestamp,
    p.category
FROM
    ecommerce_catalog.operational_db.orders AS o
JOIN
    ecommerce_catalog.operational_db.products AS p
ON
    o.product_id = p.product_id
WHERE
    o.order_timestamp >= current_date() - INTERVAL \'30 days\';        
```

### Conclusão

O Databricks Lakebase, em conjunto com o Agent Bricks, oferece uma plataforma poderosa para a construção e operação de aplicações inteligentes e agentes de IA. A capacidade de fornecer baixa latência em object storage, o mecanismo de branching para experimentação segura e a integração perfeita com o Unity Catalog para governança unificada, posicionam o Lakebase como a fundação técnica ideal para a próxima geração de sistemas transacionais e analíticos. Para organizações que buscam inovar rapidamente com IA, o Lakebase e o Agent Bricks fornecem as ferramentas necessárias para transformar dados operacionais em inteligência acionável de forma segura e escalável.

### Referências

- [Lakebase Postgres | Databricks on AWS](https://docs.databricks.com/aws/en/oltp/)
- [What is Lakebase Provisioned? | Databricks on AWS](https://docs.databricks.com/aws/en/oltp/instances/about)
- [Tutorial: Branch-based development workflow | Databricks on AWS](https://docs.databricks.com/aws/en/oltp/projects/dev-workflow-tutorial)
- [Agent Bricks | Databricks on AWS](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/)
- [Databricks documentation | Databricks on AWS](https://docs.databricks.com/aws/en/)
