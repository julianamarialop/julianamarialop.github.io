---
title: "O Arsenal Completo do Herói Fabric: Novos Poderes e Equipamentos de Julho 2025"
date: 2025-07-16T14:19:00Z
summary: "Julho de 2025 chegou com uma chuva de atualizações que transformaram o Microsoft Fabric em um super-herói ainda mais poderoso. Como todo bom herói que se preza, o Fabric não para de evoluir, adquirindo novos poderes e…"
tags: ["Microsoft Fabric", "Governança de Dados", "Segurança", "Azure", "SQL", "Databricks"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/o-arsenal-completo-do-her%C3%B3i-fabric-novos-poderes-e-de-lopes-gx1pf"
cover:
  image: cover.jpg
  alt: "O Arsenal Completo do Herói Fabric: Novos Poderes e Equipamentos de Julho 2025"
  relative: true
---

Julho de 2025 chegou com uma chuva de atualizações que transformaram o [Microsoft Fabric](https://www.linkedin.com/company/microsoft-fabric-world/) em um super-herói ainda mais poderoso. Como todo bom herói que se preza, o Fabric não para de evoluir, adquirindo novos poderes e equipamentos para enfrentar os desafios cada vez mais complexos do mundo dos dados.

Este mês foi particularmente especial, com seis grandes novidades que expandiram significativamente as capacidades da plataforma. Desde uma nova armadura cósmica até gadgets de tempo real, passando por escudos personalizados e pontes interdimensionais, o arsenal do nosso herói nunca esteve tão completo.

Vamos explorar cada um desses novos poderes e entender como eles podem transformar a forma como trabalhamos com dados, tornando nossas missões mais eficientes, seguras e poderosas.

### A Nova Armadura Cósmica: Cosmos DB no Fabric

Imagine o Tony Stark desenvolvendo uma nova versão da armadura do Homem de Ferro, mas desta vez com tecnologia cósmica avançada. É exatamente isso que representa o lançamento do Cosmos DB no Microsoft Fabric. Esta nova "armadura" não é apenas uma adição ao arsenal - é uma transformação fundamental que permite ao nosso herói operar em dimensões completamente novas.

O Cosmos DB no Fabric traz o poder do Azure Cosmos DB diretamente para a plataforma, combinando alta disponibilidade, escalabilidade dinâmica e performance otimizada para IA em uma experiência totalmente gerenciada. É como se o Fabric tivesse ganhado a capacidade de processar dados NoSQL nativamente, mantendo toda a flexibilidade e poder que já conhecemos.

A grande revolução desta armadura cósmica está no mirroring automático para o OneLake. Assim que você cria um banco Cosmos DB no seu workspace, o Fabric automaticamente começa a replicar todos os dados para o OneLake em formato Delta, em tempo quase real. É como ter um sistema de backup inteligente que não apenas protege seus dados, mas os torna instantaneamente disponíveis para análises avançadas.

Mas os poderes desta armadura vão além. Com suporte nativo para vector search e full-text search, o Cosmos DB no Fabric permite que você execute buscas por similaridade usando embeddings vetoriais, encontrando resultados baseados no significado e contexto dos dados, não apenas em palavras-chave. É como ter um radar que detecta não apenas objetos, mas também suas intenções e relacionamentos.

Para equipes que trabalham com aplicações modernas, esta nova armadura oferece casos de uso poderosos. Imagine um assistente de conhecimento inteligente que acessa manuais, documentos de suporte e logs de chat armazenados como JSON no Cosmos DB. Com indexação vetorial, o assistente entrega resultados semanticamente relevantes para consultas dos usuários, enquanto os dados replicados no OneLake permitem análises contínuas para refinar o conteúdo.

### O Escudo Personalizado: Customer Managed Keys no OneLake

Todo super-herói precisa de um escudo confiável, e o Capitão América sempre soube disso. Agora, o Microsoft Fabric ganhou seu próprio escudo personalizado com o lançamento das Customer Managed Keys (CMK) no OneLake. Mas diferentemente do vibranium do Capitão América, este escudo pode ser forjado exatamente conforme suas especificações de segurança.

As Customer Managed Keys representam uma das funcionalidades mais solicitadas pelos usuários corporativos do Fabric. Por padrão, a Microsoft já criptografa todos os dados em repouso no OneLake usando chaves gerenciadas pela própria Microsoft. Mas para organizações em setores regulamentados como finanças, saúde e governo, ter controle total sobre as chaves de criptografia não é apenas desejável - é essencial.

Com as CMK, você pode usar suas próprias chaves, armazenadas no Azure Key Vault, para criptografar dados no OneLake. É como ter um cofre pessoal onde apenas você possui a combinação. Imagine uma empresa de serviços financeiros que precisa demonstrar controle total sobre a criptografia de dados para auditores. Com as CMK, eles podem mostrar que apenas sua equipe de segurança tem acesso à chave de criptografia, e que revogar a chave bloqueará imediatamente o acesso aos dados sensíveis.

O poder deste escudo personalizado vai além da simples criptografia. Ele oferece controle granular no nível do workspace, permitindo que organizações criptografem seletivamente apenas os workspaces que requerem proteção de dados aprimorada. É uma abordagem flexível que não impõe uma solução única para todos os cenários.

A funcionalidade também suporta rotação e revogação de chaves. Se uma organização de saúde precisa rotacionar chaves de criptografia a cada 90 dias para manter conformidade, ela pode automatizar políticas de rotação no Azure Key Vault sem interromper os fluxos de trabalho de análise. E se for necessário revogar acesso, o OneLake automaticamente bloqueia operações de leitura e escrita em até uma hora, garantindo que os dados permaneçam seguros.

### A Ponte Interdimensional: Mirroring do Unity Catalog

O Doutor Estranho sempre impressionou com sua capacidade de abrir portais entre dimensões, conectando mundos que antes pareciam impossíveis de alcançar. O Microsoft Fabric acaba de ganhar um poder similar com o lançamento da funcionalidade de Mirroring do Azure Databricks Unity Catalog, agora em disponibilidade geral.

Esta ponte interdimensional permite que tabelas governadas no Unity Catalog sejam acessadas diretamente pelo Microsoft Fabric, criando uma experiência unificada e governada entre ambas as plataformas, sem duplicação de dados. É como se o Fabric tivesse ganhado a habilidade de "enxergar" através das dimensões, acessando dados que residem no universo Databricks como se fossem nativos.

A magia desta ponte está na sua transparência. Datasets gerenciados pelo Databricks tornam-se instantaneamente utilizáveis no Fabric, mantendo toda a governança e controle de acesso estabelecidos no Unity Catalog. É uma integração que respeita as políticas de segurança existentes enquanto expande dramaticamente as possibilidades de análise e colaboração.

Para equipes que trabalham com ambas as plataformas, esta ponte interdimensional elimina a necessidade de processos complexos de sincronização ou duplicação de dados. Cientistas de dados podem continuar trabalhando no Databricks com suas ferramentas preferidas, enquanto analistas de negócio acessam os mesmos dados através do Power BI e outras ferramentas do Fabric, tudo mantendo uma única fonte de verdade.

O impacto desta funcionalidade vai além da conveniência técnica. Ela representa uma mudança fundamental na forma como pensamos sobre ecossistemas de dados, permitindo que organizações aproveitem o melhor de ambos os mundos sem compromissos ou complexidade adicional.

### O Gadget de Tempo Real: SQL Operator no Eventstream

Batman sempre foi conhecido por seus gadgets engenhosos, ferramentas especializadas que ele desenvolve para situações específicas. O Microsoft Fabric acaba de adicionar um novo gadget ao seu cinto de utilidades: o SQL Operator no Eventstream, uma ferramenta poderosa para missões que exigem processamento de dados em tempo real.

O SQL Operator representa uma evolução significativa no Eventstream, oferecendo controle total sobre transformações de dados em tempo real usando a linguagem SQL familiar. Enquanto o Eventstream já oferecia uma experiência rica sem código com operadores integrados como Filter, Aggregate e Join, o SQL Operator permite que você empacote toda a lógica de transformação de dados em um só lugar.

Este gadget brilha especialmente em cenários complexos que exigem lógica condicional, expressões aninhadas, manipulação de strings e agregações avançadas. É como ter uma ferramenta multiuso que se adapta a qualquer situação, permitindo que você escreva transformações personalizadas com a precisão de um cirurgião e a flexibilidade de um artista.

A experiência de desenvolvimento é intuitiva e poderosa. Você pode testar suas consultas em dados em tempo real antes de publicar, garantindo que a lógica esteja correta. O suporte ao IntelliSense aumenta a produtividade e minimiza erros com destaque de sintaxe e autocompletar. É como ter um assistente pessoal que conhece todas as funções e sintaxes disponíveis.

Para equipes que já trabalham com Azure Stream Analytics, este gadget oferece uma transição suave, permitindo que você traga sua lógica de transformação existente diretamente para o Fabric Eventstream. É uma ponte que conecta conhecimento existente com novas possibilidades, acelerando a adoção e reduzindo a curva de aprendizado.

### O Sistema de Segurança Avançado: Limites de Acesso em Workspaces

Assim como a Fortaleza da Solidão do Superman possui sistemas de segurança avançados para proteger conhecimentos e tecnologias perigosas, o Microsoft Fabric está implementando um novo sistema de proteção: os Limites de Acesso em Workspaces, que serão introduzidos em agosto de 2025.

Este sistema de segurança avançado foi projetado para melhorar a qualidade do serviço, a confiabilidade e encorajar o controle adequado de acesso aos workspaces. É uma medida proativa que visa proteger tanto os usuários individuais quanto o ecossistema como um todo, garantindo que os recursos sejam utilizados de forma eficiente e responsável.

Os limites de acesso funcionam como um sistema de monitoramento inteligente que observa padrões de uso e implementa controles quando necessário. É como ter um guardião digital que entende quando o uso está dentro de parâmetros normais e quando pode estar causando impacto na performance geral da plataforma.

Esta funcionalidade representa um equilíbrio cuidadoso entre flexibilidade e controle. Enquanto mantém a facilidade de uso que caracteriza o Fabric, ela introduz salvaguardas que protegem a experiência de todos os usuários. É uma abordagem que prioriza a sustentabilidade a longo prazo da plataforma.

Para administradores e equipes de governança, este sistema oferece maior visibilidade e controle sobre como os recursos são utilizados, permitindo planejamento mais eficaz e gestão proativa de capacidade.

### O Comunicador Universal: Conectividade SAP Aprimorada

A Federação Estelar sempre dependeu de comunicadores universais para conectar diferentes espécies e culturas. O Microsoft Fabric acaba de aprimorar seu próprio comunicador universal com melhorias significativas na conectividade SAP, facilitando a integração com um dos ecossistemas empresariais mais importantes do mundo.

As novas opções de integração de dados de fontes SAP representam um avanço importante para organizações que dependem destes sistemas para operações críticas de negócio. Com mais de 170 conectores disponíveis no Data Factory, o Fabric continua expandindo sua capacidade de se comunicar com praticamente qualquer sistema empresarial.

Esta conectividade aprimorada é especialmente valiosa para empresas que precisam unificar dados SAP com outras fontes para análises abrangentes e casos de uso de IA. É como ter um tradutor universal que não apenas entende diferentes "idiomas" de dados, mas também os harmoniza em uma linguagem comum que pode ser utilizada por toda a organização.

As melhorias incluem opções mais robustas de extração, transformação e carregamento de dados SAP, permitindo que organizações aproveitem melhor seus investimentos existentes em sistemas SAP enquanto modernizam suas capacidades analíticas.

### Conclusão

Cada uma dessas funcionalidades não apenas adiciona capacidades técnicas, mas representa uma evolução na forma como pensamos sobre integração, segurança, governança e processamento de dados. Juntas, elas criam um ecossistema mais robusto, flexível e poderoso que pode se adaptar às necessidades em constante evolução das organizações modernas.

Até o próximo artigo !
