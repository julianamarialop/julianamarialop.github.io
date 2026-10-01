---
title: "Que a Força Analítica Esteja com Você: Explorando o Databricks no Estilo Star Wars"
date: 2024-09-23T15:56:00Z
summary: "Nos últimos anos, Databricks se consolidou como uma plataforma poderosa, semelhante à força que guia os Jedi em suas missões, ajudando empresas a acelerar seus projetos de dados e análises. Assim como a união entre a…"
tags: ["Databricks", "Segurança", "Custos", "Azure", "Governança de Dados", "Engenharia de Dados"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/que-for%C3%A7a-anal%C3%ADtica-esteja-com-voc%C3%AA-explorando-o-databricks-lopes-kkcvf"
cover:
  image: cover.jpg
  alt: "Que a Força Analítica Esteja com Você: Explorando o Databricks no Estilo Star Wars"
  relative: true
---

Nos últimos anos, Databricks se consolidou como uma plataforma poderosa, semelhante à força que guia os Jedi em suas missões, ajudando empresas a acelerar seus projetos de dados e análises. Assim como a união entre a Força e os Jedi cria harmonia, o Databricks reúne o *data warehouse* e o *data lake* em uma solução equilibrada e poderosa – o **lakehouse**.

Mas, afinal, como podemos **estruturar** e configurar uma plataforma Databricks de forma eficiente para que ela seja tão precisa quanto um sabre de luz nas mãos de um Jedi? Assim como os Jedi seguem seu código de honra, nós também precisamos de uma série de boas práticas para garantir que o Databricks funcione em perfeita harmonia, protegendo nossos dados como se fossem o segredo da Resistência.

Neste artigo, embarcaremos em nossa jornada galáctica e exploraremos os principais **pilares** que compõem uma plataforma Databricks bem arquitetada. De **governança de dados** (a nossa "Força" organizadora) à **otimização de custos** (o combustível que mantém a navegação suave pela galáxia), abordaremos tudo o que você precisa para dominar essa poderosa ferramenta.

Então, preparado(a) para a missão? Que a **governança** esteja com você! 🌌

Para iniciarmos nossa jornada de boas práticas, vamos dividir os temas da seguinte forma:

## 1. Governança de Dados

O primeiro passo para uma arquitetura sólida é garantir que os dados realmente agreguem valor ao negócio e sustentem a estratégia da empresa. A governança de dados envolve a supervisão de políticas e processos para assegurar que os dados sejam confiáveis, seguros e utilizados de forma eficiente.

A **governança de dados** no Databricks vai além de simplesmente armazenar e acessar informações. Ela envolve um conjunto de **práticas recomendadas** para garantir que os dados estejam sempre seguros, com qualidade e em conformidade com as políticas e regulamentações da organização. Vamos entender como aplicar esses conceitos de maneira didática e eficaz:

### 🔍 1.1. Classificação e Marcação de Dados

Antes de tudo, é fundamental **classificar e entender** a sensibilidade e importância dos dados. Isso ajuda a identificar dados que exigem mais proteção, como os confidenciais ou restritos, e também a definir a quem pertencem os dados dentro da empresa.

- **Classificação de Dados**: Categorize os dados em níveis como público, confidencial ou restrito. Defina também o proprietário dos dados, ou seja, quem é responsável por eles dentro da organização.
- **Tags e Comentários**: Utilize **tags consistentes** para marcar tabelas com informações importantes, como o proprietário dos dados, sua origem e nível de sensibilidade. Isso facilita o gerenciamento e o monitoramento do uso dos dados. Adicionar **comentários** a tabelas e colunas também ajuda a documentar detalhes importantes, podendo inclusive ser gerados automaticamente com a ajuda de IA.
- **Mascaramento de Dados**: Para ambientes de teste ou desenvolvimento, implemente técnicas de **mascaramento de dados** que protejam informações sensíveis, garantindo que esses dados não sejam expostos indevidamente.

### ✅ 1.2. Qualidade dos Dados

A qualidade dos dados é essencial para garantir que as decisões baseadas neles sejam confiáveis.

- **Validação de Dados**: Automatize verificações de consistência, usando recursos como o **ADD CONSTRAINT**, para garantir que os dados estejam sempre em conformidade com as regras estabelecidas.
- **Tratamento de Erros**: Implemente mecanismos robustos para identificar e corrigir erros nos dados de forma ágil.
- **Testes Automatizados**: Adicione testes automáticos aos seus processos para garantir que tudo esteja funcionando como esperado.
- **Padronização**: Use formatos padronizados de dados, como convenções de nomenclatura consistentes, formatos de data unificados e unidades de medida claras, evitando confusões e discrepâncias.

### 🗂 1.3. Catálogo Unity

O **Catálogo Unity** é uma ferramenta poderosa para gerenciar e organizar os dados de forma segura e eficiente.

- **Segregação de Dados**: Use catálogos para segmentar os dados de acordo com equipes, unidades de negócios ou ambientes específicos.
- **Controle de Acesso**: Implemente o **Controle de Acesso Baseado em Função (RBAC)** ou **Atributo (ABAC)** para garantir que cada usuário tenha acesso apenas aos dados necessários para suas funções.
- **Permissões Refinadas**: Aplique permissões detalhadas em níveis de banco de dados, tabela, linha e coluna, garantindo o princípio de "mínimo privilégio".
- **Registros de Auditoria**: Habilite o registro de auditoria para acompanhar o acesso e as modificações feitas nos dados, facilitando o monitoramento e a conformidade com normas.

### 🛡️ 1.4. Políticas de Dados

Por fim, é essencial que as práticas de governança sejam estabelecidas e seguidas rigorosamente.

- **Políticas de Retenção de Dados**: Defina e aplique políticas claras para o ciclo de vida dos dados, usando funcionalidades como o **Databricks VACUUM** para garantir a conformidade com requisitos legais.
- **Conformidade Regulatória**: Assegure-se de que as práticas de governança estejam alinhadas com regulamentações como **GDPR, CCPA, HIPAA**, entre outras.
- **Ferramentas de Terceiros**: Aproveite as integrações do Databricks com ferramentas de catálogo e governança, como **Azure Purview**, para aprimorar suas capacidades de controle de dados.
- **Políticas e Procedimentos**: Crie políticas e procedimentos claros que definam responsabilidades, papéis e processos.
- **Relatórios Regulares**: Gere relatórios periódicos sobre métricas de governança, como registros de acesso, qualidade dos dados e status de conformidade.
- **Linhagem de Dados**: Utilize ferramentas de **linhagem de dados** para rastrear a origem dos dados e suas transformações ao longo dos pipelines, garantindo total transparência e controle.

---

## 2. Interoperabilidade e Usabilidade

Um bom *lakehouse* deve ser capaz de interagir facilmente tanto com os **usuários** quanto com outros **sistemas**. Isso significa que sua arquitetura deve suportar múltiplas ferramentas e tecnologias, garantindo uma experiência fluida e sem atritos para todos os envolvidos.

### 📋 2.1. Geral

A gestão de uma plataforma Databricks requer boas práticas para garantir **segurança**, **eficiência** e **manutenção** contínua. Aqui estão algumas orientações que podem ajudar a estruturar seu ambiente de forma organizada e segura:

- **Princípios de Serviço**: Ao configurar contas que precisam interagir com o Databricks, como contas para o uso do Terraform, é fundamental utilizar **Princípios de Serviço**. Isso permite que cada serviço tenha sua própria conta, facilitando a auditoria e o controle de acesso. Dessa forma, você saberá exatamente quem tem acesso e quais permissões estão em vigor.
- **Infraestrutura como Código (IaC)**: Para automatizar a implantação e manutenção do Databricks, utilize **Infraestrutura como Código (IaC)**. O provedor Databricks para o Terraform é uma ótima solução para isso, pois permite gerenciar o ambiente de forma replicável e segura.
- **Gerenciamento de Segredos**: Certifique-se de que todos os segredos e credenciais usados para acessar outros serviços estejam armazenados de forma segura. Utilize os **Escopos Secretos do Databricks**, que podem ser integrados a ferramentas como o Azure KeyVault, para garantir que essas informações estejam protegidas contra acessos não autorizados.
- **CI/CD**: Implemente mudanças no ambiente Databricks através de pipelines de **CI/CD (Integração Contínua/Entrega Contínua)**. Todo o código-fonte deve ser armazenado em um repositório Git, permitindo controle de versão, rastreamento de alterações e maior segurança no desenvolvimento.

### 🔄 2.2. Compartilhamento de Dados

O compartilhamento de dados no Databricks exige que sejam seguidas boas práticas para garantir **segurança** e **privacidade**, especialmente quando envolve múltiplos parceiros ou unidades de negócios:

- **Compartilhamento Delta**: Ao compartilhar dados com segurança, o **Delta Sharing** é uma solução ideal. Ele permite compartilhar dados com parceiros externos ou unidades de negócios, mantendo o controle sobre o acesso. Para maior segurança, configure **listas de acesso por IP** para restringir quem pode acessar os dados e implemente a **rotação de tokens** para manter o controle constante.
- **Databricks Clean Rooms**: Utilize os **Clean Rooms** do Databricks quando for necessária uma análise colaborativa entre organizações, mas sem compartilhar os dados brutos. Isso garante que a privacidade dos dados seja mantida, além de estar em conformidade com regulamentações de privacidade, como a GDPR.
- **Marketplace**: Caso precise acessar dados comerciais ou abertos, considere o **Databricks Marketplace**, que oferece uma vasta gama de dados para atender a diversas necessidades de negócios.
- **Lakehouse Federation**: A **federação de dados** é útil quando você precisa acessar informações de vários sistemas sem migrar os dados para um local central. Contudo, considere o impacto no desempenho das consultas e os custos de entrada/saída de dados ao adotar essa abordagem.

---

## 3. Excelência Operacional

Não adianta ter uma arquitetura de ponta se o operacional não acompanha. A **excelência operacional** diz respeito a todos os processos que mantêm a plataforma Databricks rodando de forma eficiente e estável em um ambiente de produção, minimizando paradas e garantindo continuidade.

### 🚀 Processamento (Clusters)

A gestão de clusters no Databricks é essencial para garantir o bom desempenho, segurança e otimização de custos. Aqui estão algumas práticas recomendadas:

### 3.1. Geral

- **Políticas de Cluster**: Defina políticas de cluster para limitar o tamanho e os recursos, ou mesmo para criar "clusters do tamanho de camiseta" (pequeno, médio, grande), ajustando-se às necessidades de diferentes cargas de trabalho.
- **Databricks Runtime**: O **Databricks Runtime** está em constante evolução, com melhorias em usabilidade, desempenho e segurança. Sempre que possível, utilize a versão mais recente para garantir que você tenha acesso às melhores funcionalidades.
- **Reiniciar Clusters de Longa Duração**: Clusters que ficam rodando por longos períodos podem perder atualizações críticas de segurança e sistema operacional. Garanta que eles sejam reiniciados periodicamente para evitar problemas de desempenho e segurança.
- **Usar Volumes SSD**: Clusters com workers que utilizam volumes SSD são automaticamente configurados com cache de disco, acelerando as consultas e melhorando a performance do seu ambiente.
- **Pré-aquecimento de Clusters**: Se suas consultas estiverem lentas devido à inicialização a frio dos clusters, considere utilizar os **pools do Databricks**, que permitem pré-aquecer clusters para reduzir o tempo de espera.

### ⚙️ Orquestração (Jobs)

A configuração e gerenciamento de trabalhos no Databricks podem ser otimizados para garantir eficiência e escalabilidade.

### 3.2. Configuração do Trabalho

- **Job Clusters**: Ao configurar trabalhos, utilize **clusters específicos para jobs**, dimensionados corretamente de acordo com a carga de trabalho. O uso de **dimensionamento automático** permite lidar com variações na demanda de forma eficiente.
- **Tentativas de Trabalho**: Defina um número adequado de tentativas para trabalhos críticos, considerando falhas transitórias. Para evitar sobrecarga, implemente uma lógica de **backoff exponencial** no código, ajustando a frequência das tentativas em caso de erros.
- **Princípios de Serviço**: Certifique-se de que os trabalhos estejam configurados com um **Princípio de Serviço** como proprietário, o que evita problemas de continuidade caso o criador original do job deixe a equipe.
- **Uso de Parâmetros**: Em trabalhos com múltiplos estágios, utilize parâmetros para **compartilhar informações** entre esses estágios, facilitando a integração e o controle do processo.
- **Trabalhos Orientados por Eventos**: Sempre que possível, opte por **trabalhos orientados por eventos**, que são mais eficientes em termos de tempo e custos. Para ingestões únicas, considere usar o comando COPY INTO como alternativa.

### 3.3. Gerenciamento de Código

- **Controle de Versão**: Armazene seu código em um sistema de controle de versão, como o Git. Utilize o **Databricks Repos** para sincronizar notebooks e arquivos com o repositório, facilitando o gerenciamento e o rastreamento de alterações.
- **Código Modular**: Escreva **código modular e reutilizável**, permitindo que ele seja compartilhado entre diferentes trabalhos e notebooks, promovendo eficiência e padronização.
- **Testes Automatizados**: Implemente **testes unitários, de integração e E2E** para garantir que o código funcione conforme esperado, desde as funções mais simples até os fluxos mais complexos.
- **Databricks Asset Bundles (DAB)**: Utilize o **Databricks Asset Bundles** para facilitar o desenvolvimento e a implantação de trabalhos, garantindo consistência e automação.
- **Pipelines de CI/CD**: Configure pipelines de **CI/CD** para automação dos fluxos de trabalho no Databricks, utilizando ferramentas como **Azure DevOps**, **GitLab** ou **GitHub Actions**.

### 3.4. Tratamento e Registro de Erros

- **Tratamento de Erros**: Implemente um tratamento de erros robusto com blocos **try-catch**, garantindo que exceções sejam tratadas de forma apropriada e sem interrupções bruscas.
- **Logging**: Utilize **log estruturado** para registrar eventos, métricas e erros. O Databricks oferece integração com ferramentas de logging, como **Azure Log Analytics**, o que facilita o monitoramento e diagnóstico.

### 🧑💻 Pessoas e Processos

Além da parte técnica, é fundamental estruturar uma equipe dedicada e criar processos bem documentados e padronizados.

### 3.5. Geral

- **Equipe de Operações**: Monte uma **equipe de operações** dedicada ao Lakehouse, responsável por manter as melhores práticas, garantir a segurança e monitorar as ferramentas usadas.
- **Gerenciamento de Limites de Serviço**: Ao projetar a arquitetura, considere os limites e cotas de serviço do Databricks, do provedor de nuvem e do **Unity Catalog**, para evitar interrupções por ultrapassagem de limites.
- **Padronização de Nomeação**: Considere criar um documento com **padrões de nomenclatura** para objetos Databricks, como catálogos, que podem seguir convenções como <sigla\_do\_ambiente>-<nome\_do\_projeto>. Essa padronização pode ser imposta através de pipelines de CI/CD.

### 3.6. Colaboração e Documentação

- **Documentação Completa**: Documente completamente seus fluxos de trabalho, código e configurações. Utilize recursos como **comentários**, **Markdown** e **visualizações** dentro dos notebooks para garantir que tudo esteja claro para a equipe.
- **Revisões de Código**: Implemente um processo de **revisão de código** para garantir a qualidade e promover o compartilhamento de conhecimento entre os membros da equipe.
- **Marcação de Recursos**: Utilize **tags** consistentes para marcar recursos de acordo com as políticas da empresa. Isso facilita o monitoramento, gestão de custos e localização de informações importantes.

---

## 4. Segurança, Privacidade e Conformidade

Proteger dados e sistemas é fundamental. Por isso, um bom setup de Databricks deve contar com mecanismos robustos de **segurança**, **privacidade** e **conformidade** com normas e regulamentações. Manter o ambiente seguro contra ameaças é prioridade para proteger o valor dos dados e a confiança dos clientes.

### 🛡️ 4.1. Segurança Geral

- **Security Analysis Tool (SAT)**: O Databricks oferece a ferramenta **Security Analysis Tool (SAT)**, que ajuda a verificar se seus espaços de trabalho seguem as práticas recomendadas de segurança. Essa ferramenta pode ser acessada no [GitHub](https://github.com/databricks-industry-solutions/security-analysis-tool).
- **Autenticação Multifator (MFA)**: Certifique-se de que todas as contas que usam o Databricks estejam configuradas com **autenticação multifator (MFA)**, utilizando um provedor de identidade adequado. No caso do Azure Databricks, o provedor de identidade padrão é o **Entra**, enquanto para GCP ou AWS você pode configurar o **SSO**.
- **Controle de Acesso Baseado em Função (RBAC)**: Utilize grupos do **Azure AD** e o **Databricks SCIM** para gerenciar permissões com base no princípio do **menor privilégio**, garantindo que cada usuário tenha apenas o acesso necessário.
- **Principais de Serviço**: Ao fornecer acesso automatizado ou programático ao Databricks, utilize os **Principais de Serviço** do Azure AD, assegurando que essas identidades tenham permissões mínimas para realizar suas funções.
- **Segurança e Conformidade Aprimoradas**: Se a sua empresa precisa atender a padrões de conformidade como **PCI-DSS ou HIPAA**, considere usar o complemento de **Segurança e Conformidade Aprimoradas** para garantir que os requisitos específicos sejam cumpridos.

### 👨💻 4.2. Gerenciamento de Código

- **Segredos**: Todos os segredos, como credenciais de acesso, devem ser armazenados dentro de **escopos secretos** com as permissões adequadas para protegê-los de acessos não autorizados.
- **Raiz do DBFS**: Evite armazenar dados na **raiz do DBFS**. Isso porque, quando os dados são armazenados na raiz, todos os usuários podem acessá-los, comprometendo a segurança.
- **Análise de Código Estático (IaC)**: Considere usar ferramentas como **checkov**, **tfsec** e **terrascan** para realizar análises estáticas em código de Infraestrutura como Código (IaC), identificando vulnerabilidades e problemas de conformidade.
- **Análise de Código Estático (Python)**: Para código Python, utilize ferramentas como **Pylint** para verificar a qualidade e segurança do código.
- **Revisões de Código**: Realize revisões de código regulares para garantir que notebooks e jobs sigam as melhores práticas de codificação e que não haja exposição de informações confidenciais.
- **Gerenciamento de Dependências**: Mantenha as dependências sempre atualizadas, aplicando patches regularmente. Ferramentas como **Snyk** ajudam a identificar vulnerabilidades em bibliotecas e ferramentas de terceiros, essenciais para manter a segurança operacional.

### 🌐 4.3. Segurança de Rede (Azure)

- **Implantar Databricks em uma VNet**: Utilize a **injeção de VNet** do Azure para implantar o Databricks dentro de uma **rede virtual privada (VNet)**, garantindo que seu cluster e workspace estejam isolados da internet pública.
- **Pontos de Extremidade Privados**: Configure **Azure Private Link** para criar pontos de extremidade privados, permitindo comunicação segura entre o Databricks e outros serviços do Azure, como contas de armazenamento e bancos de dados.
- **Grupos de Segurança de Rede (NSGs)**: Use **NSGs** para controlar o tráfego de entrada e saída nas sub-redes do Databricks, garantindo que apenas o tráfego necessário seja permitido.
- **Conectividade Segura do Cluster**: Configure os clusters para que eles operem com **conectividade segura**, ou seja, sem IP público, prevenindo o acesso direto pela internet.
- **Listas de Acesso IP**: Considere implementar **listas de acesso IP** para restringir o acesso ao workspace apenas a endereços IP permitidos.

### 🔐 4.4. Proteção de Dados (Azure)

- **Criptografia em Repouso**: Certifique-se de que todos os dados armazenados em serviços como **Azure Data Lake Storage (ADLS)** estejam criptografados em repouso, utilizando a criptografia do serviço de armazenamento do Azure.
- **Criptografia em Trânsito**: Habilite **HTTPS e SSL/TLS** para criptografar dados em trânsito, garantindo a segurança das comunicações entre o Databricks e sistemas externos.
- **Identidade Gerenciada para Recursos do Azure**: Utilize **identidades gerenciadas** para conceder ao Databricks acesso seguro ao **Azure Key Vault** e outros recursos, sem a necessidade de expor credenciais.
- **Chaves Gerenciadas pelo Cliente (CMK)**: Configure **CMKs** para gerenciar a criptografia de dados no Databricks, implementando rotação de chaves e monitoramento de uso para detectar acessos não autorizados.

### 📚 4.5. Documentação e Treinamento

- **Documentação do Plano de Recuperação de Desastres (DR)**: Documente sua estratégia de **recuperação de desastres (DR)**, incluindo procedimentos de backup, etapas de recuperação e atribuições de responsabilidades.
- **Runbooks**: Crie **runbooks** com instruções passo a passo para cenários de recuperação de desastres, assegurando que sua equipe saiba como agir rapidamente em caso de incidentes.
- **Compartilhamento de Conhecimento**: Promova o compartilhamento de conhecimento sobre o plano de DR em toda a organização, garantindo que todos estejam preparados.

### 💾 4.6. Segurança Operacional

- **Backups**: Use armazenamento entre regiões para proteger seus dados críticos ou implemente tarefas de backup que gravem os dados em uma região ou conta de armazenamento local.
- **Git**: Armazene todo o código de Infraestrutura como Código (IaC), configuração de cluster, jobs e notebooks em repositórios Git. Isso facilita a recuperação em caso de incidentes e promove o controle de versão.
- **Plano de Recuperação de Desastres (DR)**: Desenvolva e teste regularmente um **plano de recuperação de desastres**, garantindo a continuidade dos negócios em caso de incidentes graves.

### ⚙️ 4.7. Configuração do Espaço de Trabalho

- **Credential Passthrough**: A partir do **Databricks Runtime 15.0**, o Credential Passthrough será descontinuado. Em vez disso, utilize o **Unity Catalog (UC)** para gerenciar identidades e permissões de maneira mais eficiente.
- **Isolamento de Ambiente**: Defina diferentes workspaces para **ambientes de desenvolvimento, stage e produção**, ou para diferentes unidades de negócios. Esse isolamento permite uma melhor gestão de recursos e segurança.
- **Separação de Dados**: Separe logicamente e fisicamente seus **dados confidenciais** dos não confidenciais, garantindo que informações sensíveis estejam protegidas.

---

## 5. Eficiência de Desempenho

Com a demanda por análises e processamento de dados crescendo exponencialmente, a **eficiência de desempenho** é crucial. Sua plataforma deve ser capaz de se adaptar a mudanças na carga de trabalho sem comprometer a velocidade e a qualidade dos resultados.

### 🔎 Consultas

A otimização de consultas no Databricks é essencial para garantir um desempenho eficiente e evitar gargalos desnecessários. Aqui estão algumas práticas recomendadas para maximizar a performance das suas consultas:

### 5.1. Geral

- **Agrupamento Líquido (Liquid Clustering)**: Configure **agrupamento líquido** nas colunas frequentemente utilizadas nas consultas. Essa técnica é preferível ao uso de **ordenação Z** ou particionamento, já que melhora a performance de busca sem o risco de particionamento excessivo.
- **Formatos de Arquivo Eficientes**: Utilize formatos de arquivo como **Parquet** ou **ORC**, que oferecem melhor desempenho e compactação dos dados. Para ainda mais eficiência, armazene os dados dentro de **tabelas gerenciadas** no lakehouse.
- **Clusters Maiores**: Quando sua carga de trabalho aumenta linearmente, planeje o uso de **clusters maiores**. Um cluster maior geralmente processa a mesma carga mais rapidamente e, em muitos casos, não resulta em maior custo, apenas em maior velocidade.
- **Ignorância de Dados**: O Databricks coleta estatísticas automaticamente nas primeiras **32 colunas** definidas (incluindo colunas aninhadas). Para melhorar o desempenho das consultas, certifique-se de que as colunas mais frequentemente consultadas estejam dentro dessas primeiras 32 colunas.
- **Evite Particionamento**: Com o advento do **agrupamento líquido**, o particionamento tornou-se menos necessário. Em muitos casos, particionar os dados pode causar **particionamento excessivo**, onde cada partição precisa ter pelo menos 1 GB, o que pode prejudicar o desempenho.

### 5.2. Desempenho

- **Predicate Pushdown**: Use **predicate pushdown** para filtrar os dados logo no início da execução da consulta. Isso reduz a quantidade de dados movimentados e melhora o desempenho geral. Quando estiver lendo de um RDBMS, combine opções como **partitionColumn**, **lowerBound** e **upperBound** para paralelizar a operação de leitura.
- **Junções de Transmissão**: Para tabelas menores, utilize **junções de transmissão**, enviando a tabela menor para todos os executores. Isso melhora o desempenho das junções em consultas complexas.
- **Skew Handling**: Identifique e gerencie dados distorcidos (**skew**) para garantir que as partições de dados sejam distribuídas de maneira uniforme. Técnicas como **salting** podem ajudar a mitigar o skew de dados.
- **Persistência (Cache)**: Utilize o comando .persist para armazenar resultados de subconsultas e dados em formatos diferentes de Parquet. No entanto, evite o uso excessivo de persistência a menos que você saiba exatamente o impacto que isso terá no desempenho.
- **Execução Especulativa**: Ative a **execução especulativa** para executar novamente tarefas lentas em outros nós, o que ajuda a mitigar o impacto de tarefas demoradas e melhora o tempo total de execução.
- **Compactação (Compaction)**: Use o comando **OPTIMIZE** para otimizar manualmente tabelas no **Delta Lake**. Para uma otimização contínua, habilite **AUTO OPTIMIZE** e **AUTO COMPACT** ao gravar em tabelas, melhorando o desempenho a longo prazo.
- **ANALYZE TABLE**: A instrução **ANALYZE TABLE** coleta estatísticas sobre tabelas dentro de um esquema especificado, ajudando a melhorar o desempenho das consultas.

### 💻 Código

Um código bem estruturado e otimizado pode melhorar significativamente o desempenho das consultas e a eficiência geral do sistema.

### 5.3. Código

- **Evite Transformações Amplas**: Minimize o uso de transformações amplas, como **groupBy** e **join**, que exigem o embaralhamento de grandes quantidades de dados pela rede. Quando essas operações forem necessárias, otimize-as para reduzir o impacto no desempenho.
- **Prefira DataFrames e Datasets**: Utilize **DataFrames** e **Datasets** em vez de RDDs, pois eles oferecem otimizações automáticas e são mais fáceis de usar. Aproveite o **otimizador Catalyst** e o **mecanismo Tungsten** para obter um melhor desempenho nas operações.
- **Perfis de Código**: Crie **perfis do seu código** regularmente para identificar e solucionar gargalos de desempenho. Utilize ferramentas como o **Spark UI** para obter insights sobre a execução e melhorar a eficiência.
- **Instruções MERGE**: Quando possível, utilize a **remoção de partições** durante operações de MERGE, otimizando a execução dessas operações.

### 5.4. Carimbos de Tempo

- **Carimbos de Data/Hora**: No Databricks, os **carimbos de data/hora** são armazenados como números de ponto flutuante, representando o número de segundos (e frações de segundo) desde a época Unix.
- **Notebooks e Fusos Horários**: O valor dos carimbos de data/hora exibidos nos notebooks é ajustado de acordo com o fuso horário da sessão atual, que geralmente é **UTC**. Se os dados no arquivo não contêm um indicador de fuso horário, a análise dos carimbos de data/hora pode depender do fuso horário da sessão.
- **Armazéns SQL**: Nos **armazéns SQL**, o fuso horário padrão também é **UTC**, a menos que seja configurado de outra forma. No entanto, não há deslocamento ou indicador de fuso horário.

---

## 6. Otimização de Custos

Por fim, uma boa arquitetura não pode esquecer da **otimização de custos**. Gerenciar os recursos de forma inteligente e eficaz garante que a empresa maximize o retorno sobre o investimento, entregando valor sem desperdícios.

Controlar os custos no Databricks é essencial para garantir que você esteja aproveitando ao máximo a plataforma sem ultrapassar o orçamento. Aqui estão algumas práticas para ajudar a gerenciar os custos de maneira eficaz:

### 💰 6.1. Monitoramento de Custos

- **Monitoramento Regular**: É fundamental monitorar constantemente o uso e os custos no Databricks. Utilize a **Análise de Custos** disponível no Databricks ou ferramentas de terceiros para ter uma visão clara do seu consumo. No **console da conta do Databricks**, há uma página dedicada para analisar o uso de **DBUs** (Databricks Units), embora isso não inclua os custos de VMs ou armazenamento.
- **Orçamento e Notificações**: O Databricks oferece uma funcionalidade de **definição de orçamento**, onde você pode configurar notificações para ser alertado caso o uso exceda o valor estipulado, ajudando a manter os gastos sob controle.

### 💰 6.2 Clusters Otimizados

- **Configurações de Cluster Custo-Eficientes**: Utilize configurações de clusters que proporcionem uma boa relação custo-benefício. Para cargas de trabalho **não críticas**, considere o uso de **instâncias spot**, que são mais baratas, mas podem ser interrompidas a qualquer momento. Para garantir a resiliência, implemente uma política de repetição quando estiver usando essas instâncias.
- **Políticas de Término Automático**: Configure políticas de **término automático** para clusters que ficam ociosos, evitando que clusters desnecessários continuem rodando e acumulando custos.
- **Clusters Graviton (AWS)**: Se você está rodando no AWS, considere utilizar **clusters Graviton**, que oferecem uma relação desempenho/custo superior em comparação com outros tipos de instância.

### 💰 6.3 Photon e Otimização de Consultas

- **Photon Runtime**: O **Photon Runtime** do Databricks oferece um aumento significativo de desempenho em comparação com o Spark tradicional, além de ser mais eficiente em termos de custo. Ele é ideal para quem busca uma otimização de performance sem elevar os gastos.
- **Otimização de Consultas**: Regularmente, revise e otimize suas consultas Spark. Utilize o **Spark Query Profile** e analise os **planos de execução** para identificar gargalos de desempenho. Melhorar a eficiência das consultas reduz o tempo de execução e, consequentemente, os custos.

### 💰 6.4 Instâncias Sem Servidor

- **Opções Sem Servidor**: Quando apropriado, considere o uso de **warehouses**, **workflows** e **notebooks SQL sem servidor**. Essas opções podem ser mais econômicas, pois você paga apenas pelo tempo de uso, sem a necessidade de manter clusters dedicados.

---

## 🔄 7. Confiabilidade

Falhas acontecem. Mas a questão é: como sua plataforma reage a elas? A **confiabilidade** de um sistema Databricks envolve a capacidade de se recuperar rapidamente de falhas e continuar operando, sem afetar os processos críticos do negócio.

### 📊 7.1. Monitoramento e Registro

Manter um ambiente Databricks funcionando de maneira eficiente requer uma estratégia sólida de monitoramento e registro. Aqui estão algumas práticas recomendadas para garantir a integridade, desempenho e segurança do seu ambiente:

- **Habilitar Logs de Auditoria:** Ative os **logs de auditoria** no Databricks para capturar informações detalhadas sobre atividades, como eventos de login, acesso a dados e ações administrativas. Esses logs ajudam a manter um histórico das operações e podem ser configurados com **filtros de auditoria** para evitar o vazamento de dados entre diferentes ambientes.
- **Azure Monitor:** Utilize o **Azure Monitor** para rastrear a saúde e o desempenho do seu ambiente Databricks, garantindo que as operações estejam funcionando conforme o esperado e identificando possíveis problemas antes que se agravem.
- **Integração com Ferramentas de Monitoramento:** Quando necessário, integre o Databricks com ferramentas de monitoramento, como **Datadog, Prometheus, Splunk** ou o próprio **Azure Monitor**, para melhorar a visibilidade do ambiente e o acompanhamento de métricas críticas.
- **Monitoramento de Cluster:** Faça o **monitoramento regular** dos clusters, verificando a integridade, o desempenho e os logs. Configure **alertas automáticos** para métricas importantes, como uso de CPU, memória ou duração de jobs, para evitar interrupções inesperadas. A integração com plataformas como **Slack** ou **PagerDuty** pode ser útil para receber notificações imediatas.
- **Gerenciamento de Recursos:** Monitore a utilização de recursos dos clusters com ferramentas como **Ganglia** ou a **Databricks Cluster UI**, garantindo que os recursos estejam sendo usados de maneira eficiente.
- **Monitoramento do Auto Loader:** O **Auto Loader** permite inspecionar o estado de um fluxo de dados por meio de uma **API SQL** e da **Spark Streaming Query Listener**, fornecendo insights detalhados sobre os arquivos processados e o estado das consultas em tempo real.
- **Job Monitoring:** Utilize a interface do **Databricks Jobs** para monitorar o status e o desempenho dos jobs. Também é possível implementar **monitoramento personalizado** para métricas específicas, facilitando a identificação de gargalos.
- **Monitoramento do Delta Live Tables:** Cada pipeline no **Delta Live Tables** gera um **log de eventos** que inclui logs de auditoria, verificações de qualidade de dados, progresso do pipeline e informações sobre a linhagem de dados. Isso facilita o acompanhamento contínuo dos pipelines.
- **Monitoramento de Streaming:** Com a interface de **Structured Streaming**, você pode monitorar taxas de entrada, processamento e latência de suas consultas de streaming. O método **StreamingQuery.progress** fornece relatórios detalhados em formato JSON para uma análise mais aprofundada.
- **Monitoramento de ML e IA:** Para **monitoramento de modelos de Machine Learning e IA**, utilize tabelas de inferência que registram continuamente entradas e saídas de modelos em uma **tabela Delta**. Isso permite monitorar, depurar e otimizar modelos com o auxílio de consultas SQL, notebooks e ferramentas de monitoramento do Lakehouse.
- **Monitoramento de Segurança e Custos:** O monitoramento de segurança deve ser implementado para garantir conformidade e privacidade. Além disso, monitore e controle os custos regularmente para evitar surpresas no orçamento.

### 📦 7.2. Outros Aspectos Importantes

- **Armazenamento Padrão do Workspace:** Evite usar o **armazenamento padrão** do workspace para dados de produção. Em vez disso, crie locais de armazenamento dedicados, configurados e ajustados de acordo com suas necessidades específicas, garantindo maior segurança e flexibilidade.
- **Resiliência a Falhas de Zona de Disponibilidade (AZ):** O Databricks já é **resiliente a falhas de AZ** por padrão. Certifique-se de que os clusters estejam configurados para **Auto-Scaling** e tenha uma política de repetição para jobs. A recuperação da funcionalidade do plano de controle deve ocorrer em aproximadamente 15 minutos após uma falha da AZ.
- **Falha Regional:** Embora uma implantação multirregional **ativo-ativo** no Databricks seja geralmente pouco viável financeiramente, é recomendável usar **Infraestrutura como Código (IaC)** para criar uma implantação secundária em uma região de backup. Utilize armazenamento em nuvem replicado para garantir a continuidade das operações.

### 🛠️ 7.3. Infraestrutura no Azure

- **GRS (Geo-Redundant Storage):** Na maioria dos casos, o GRS (Geo-Redundant Storage) oferece uma opção de armazenamento econômica e ainda garante durabilidade de 16 9s. No entanto, se o tempo de recuperação regional for crítico, considere o uso do GZRS (Zone-Redundant Storage).

---

Concluímos nossa jornada galáctica pelo Databricks, explorando os principais pilares para configurar essa poderosa plataforma de forma estratégica e eficiente.

Assim como um Jedi domina a Força, dominar o Databricks exige boas práticas que garantam o equilíbrio entre governança de dados, otimização de custos e desempenho. Essas diretrizes são como o código Jedi, oferecendo orientação, mas sempre flexíveis o suficiente para se adaptarem às necessidades e realidades de cada organização.

Que o poder dos dados esteja com você enquanto você constrói uma plataforma de sucesso!

Obrigada pela leitura e acompanhe outros artigos da newsletter.

## Referências

Databricks SAT: <https://github.com/databricks-industry-solutions/security-análise-t>

Data Lakehouse: <https://learn.microsoft.com/en-us/azure/databricks/lakehouse-arch>

Melhores práticas: <https://learn.microsoft.com/en-us/azure/databricks/data-governan>

Proteção: <https://www.databricks.com/blog/data-exfiltration-protection-with->

Conectividade do cluster: <https://learn.microsoft.com/en-us/azure/databricks/security/netw>

API de orçamentos do Databricks: <https://www.databricks.com/blog/best-practices-cost-management-databricks#:~:text=Warehouse%20creation%20permissions.-,Monitoring%20usage,-Along%20with%20controlling>

Databricks Photon: <https://www.databricks.com/product/photon#:~:text=no%20rewrite%20required.-,Por> [que%20Photon%3F,-Desempenho%20da%20consulta](https://www.databricks.com/product/photon#:~:text=no%20rewrite%20required.-,Why%20Photon%3F,-Query%20performance%20on)
