---
title: "O Que Como Treinar o Seu Dragão Me Ensinou Sobre Prompt, Context, Harness e Loop Engineering"
date: 2026-08-19T13:45:00Z
summary: "Em Berk, vikings resolvem o problema dos dragões do único jeito que conhecem: na força. Soluço não tem força. Quando ele finalmente fica cara a cara com um Fúria da Noite, o dragão mais rápido e mais temido de todos, o…"
tags: ["Agentes de IA", "Prompt Engineering", "Microsoft Fabric"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/o-que-como-treinar-seu-drag%C3%A3o-me-ensinou-sobre-prompt-lopes-bcpmf"
cover:
  image: cover.jpg
  alt: "O Que Como Treinar o Seu Dragão Me Ensinou Sobre Prompt, Context, Harness e Loop Engineering"
  relative: true
---

### O Garoto Que Gritava Com o Dragão

Em Berk, vikings resolvem o problema dos dragões do único jeito que conhecem: na força. Soluço não tem força. Quando ele finalmente fica cara a cara com um Fúria da Noite, o dragão mais rápido e mais temido de todos, o garoto descobre que gritar comandos não funciona. O Banguela é absurdamente poderoso e não entende ordens.

O que Soluço faz a partir daí é o que separa o filme de qualquer outra história de domar feras. Ele para de gritar e começa a observar. Aprende o que o dragão percebe: os peixes que ele aceita, a grama que o hipnotiza, o jeito de se aproximar sem ameaçar. Depois, percebe que o Banguela não voa porque perdeu metade da cauda, e constrói a solução: uma cauda protética, uma sela, um sistema de pedais. Um equipamento inteiro em volta do dragão, calibrado a cada voo de teste. E no último ato dessa evolução, Soluço constrói uma cauda automática, que abre e ajusta sozinha. O Banguela ganha o céu sem precisar do cavaleiro em cima.

Gritar melhor. Entender o que o outro percebe. Construir o equipamento em volta. Sair de cima. Essas quatro etapas ganharam nomes na engenharia de IA nos últimos meses, e formam a progressão que explica onde o mercado de agentes está agora: prompt engineering, context engineering, harness engineering e loop engineering.

Para ninguém se perder, vou usar um único exemplo do início ao fim: o relatório de vendas da sua empresa. O mesmo relatório, subindo de camada em camada.

### Camada 1. Gritar Comandos: Prompt Engineering

Prompt engineering é caprichar no pedido. No nosso exemplo: em vez de "faz um relatório de vendas", você escreve "gere o relatório de vendas do primeiro semestre com receita líquida por mês e ticket médio por região, em tabela, com um parágrafo executivo no topo". O pedido melhorou, a resposta melhora junto.

Foi a habilidade dominante dos primeiros anos, e continua útil. Mas tem um teto baixo, pelo mesmo motivo que gritar mais alto não fazia o Banguela voar: o problema nunca foi o volume da ordem. Era tudo que o dragão não sabia sobre você.

### Camada 2. Entender o Que o Dragão Enxerga: Context Engineering

O modelo responde com base no que enxerga naquele momento. Se ele não conhece o schema das suas tabelas, a definição oficial de receita líquida da sua empresa e o formato dos relatórios anteriores, o prompt perfeito produz um relatório genérico. Context engineering é a disciplina de decidir o que entra no campo de visão do modelo: quais arquivos, quais documentações, quais memórias de interações passadas, e igualmente importante, o que fica de fora para não poluir.

No exemplo: você anexa o dicionário de dados, a regra de cálculo dos KPIs e um relatório antigo como referência de formato. O mesmo prompt de antes, agora com visão, produz outra qualidade de resposta. Soluço descobrindo que o Banguela odeia enguia e ama peixe é isso: você não mudou o dragão, mudou o que ele percebe.

No ecossistema Microsoft, essa camada tem nome e endereço: o Fabric. O OneLake como fonte única do dado, os modelos semânticos carregando as definições oficiais de cada métrica, e os Data Agents respondendo perguntas ancorados nesses modelos. Quando a regra de receita líquida vive no modelo semântico, você para de anexá-la a cada conversa: o contexto deixa de ser um anexo e vira infraestrutura.

### Camada 3. A Sela e a Cauda: Harness Engineering

Aqui a palavra ajuda, porque harness é literalmente arreio, o equipamento que se coloca no animal. E a cena do Soluço construindo a cauda protética com pedais é a definição visual perfeita do conceito.

Harness engineering é desenhar tudo que existe em volta do modelo: as ferramentas que ele pode chamar, o ambiente isolado onde executa código, as validações que rodam antes e depois de cada ação, as permissões do que ele pode e não pode tocar. A fórmula que cristalizou o conceito veio de Mitchell Hashimoto, criador do Terraform, em fevereiro de 2026, depois de uma publicação da OpenAI sobre sua infraestrutura interna de agentes: agente = modelo + harness. O modelo é o cérebro; o harness é o corpo, os sentidos e os limites. Martin Fowler e Birgitta Böckeler, da Thoughtworks, organizaram o vocabulário que virou padrão: o harness tem guias, que direcionam o agente antes de agir, e sensores, que detectam e corrigem problemas depois.

No exemplo do relatório: o agente agora tem uma ferramenta de SQL para calcular os números em vez de estimar, um protocolo escrito com as validações obrigatórias de qualidade, permissão de leitura nos dados e nenhuma permissão de escrita, e um sensor que confere se as contagens de linhas reconciliam antes de liberar o resultado. Se você acompanha esta newsletter, reconheceu: skills são harness engineering. Quem escreve protocolos em markdown está construindo selas há meses, talvez sem usar o nome.

E do lado corporativo, o Microsoft Foundry é exatamente isso vendido como serviço gerenciado: agentes hospedados com ferramentas, guardrails, observabilidade e, desde este ano, suporte nativo a skills em preview, com API versionada para armazenar os protocolos centralmente e anexá-los aos agentes. A fórmula agente = modelo + harness virou arquitetura de produto: você escolhe o modelo, o Foundry fornece a sela.

O detalhe que importa: harness não é só segurança. Uma sela bem construída não serve para prender o dragão, serve para ele voar melhor. Um harness bem desenhado dá ao modelo o contexto certo, a ferramenta certa e a restrição certa na hora certa, e é isso que transforma demo impressionante em sistema confiável.

### Camada 4. A Cauda Automática: Loop Engineering

Até aqui, você continua em cima do dragão, ditando cada voo. A quarta camada é sair de cima.

Todo agente já roda num ciclo: raciocina, age, observa o resultado, decide o próximo passo. Loop engineering, o termo que dominou as conversas a partir de junho de 2026, é desenhar esse ciclo de propósito: definir o objetivo, a verificação e a condição de parada, e deixar o sistema fazer os prompts pelo agente. A faísca foi uma fala de Boris Cherny, criador do Claude Code, dizendo que já não faz prompts diretamente; ele mantém loops rodando, e são os loops que decidem o que pedir ao modelo. Addy Osmani, do Google, nomeou e estruturou a prática dias depois.

No exemplo do relatório de vendas, a mudança é concreta: em vez de você pedir o relatório toda segunda-feira, existe um loop agendado que ingere o dado novo, roda as validações do protocolo, gera o relatório, confere o resultado contra as regras de qualidade e publica. Se a verificação falha, o loop tenta corrigir; se não consegue, aí sim te chama. Você saiu da execução e virou o projetista do voo.

Montando esse voo com peças Microsoft, o desenho fica concreto: o Activator do Fabric dispara o ciclo quando o dado novo chega no OneLake, o agente hospedado no Foundry executa o protocolo com as validações, e o resultado volta para o Fabric, onde relatório e trilha de verificação ficam auditáveis. O Fabric é o território onde o dragão voa, o Foundry é a sela, e o loop é o plano de voo que conecta os dois.

Duas lições dessa camada que os entusiastas costumam pular. Primeira: o gargalo do loop é o verificador, não o modelo. Um loop sem verificação confiável é um dragão voando cego, queimando orçamento convencido de que está progredindo. Segunda, e aqui vale registrar o alerta que a IBM formalizou ao definir a disciplina: existe uma linha entre delegar execução e abrir mão do pensamento crítico, que eles chamam de rendição cognitiva. Sair do loop de execução não é sair do loop de julgamento.

E para provar que a camada 4 não exige sofisticação, a comunidade tem um exemplo folclórico: a técnica Ralph, de Geoffrey Huntley, que roda um agente dentro de um simples while loop, com o mesmo prompt contra uma especificação escrita, recomeçando até o trabalho acabar. Batizada em homenagem ao Ralph Wiggum dos Simpsons porque parece simples demais para funcionar. E funciona, justamente porque a especificação e a verificação carregam o peso.

### O Que Muda Para Times de Dados

A progressão vira um diagnóstico de maturidade honesto. A maioria dos times que conheço está entre as camadas 1 e 2: prompts cada vez melhores, contexto cada vez mais organizado. O salto de valor imediato está na camada 3, e times de dados têm vantagem injusta nela: governança, validação e reconciliação de contagens já são nossa cultura, só mudou o lugar onde escrevemos as regras. Um protocolo de qualidade de dados é uma sela pronta.

E a camada 4 tem um pré-requisito que ninguém pula: só automatize o ciclo de trabalhos cuja verificação você sabe escrever. Relatórios recorrentes com regras de qualidade claras são o candidato perfeito para o primeiro loop. Análises exploratórias abertas, ainda não. O critério não é o que o agente consegue fazer sozinho, é o que você consegue verificar sozinho.

### Conclusão: O Voo

A genialidade do Soluço nunca foi domar o dragão. Foi entender que a força do Banguela sempre esteve lá, e que o que faltava era engenharia em volta dela: primeiro os olhos, depois a sela, depois a cauda que voa sozinha.

Com IA, a força do modelo também já está lá, e cresce a cada versão. A alavanca mudou de lugar: de escrever o pedido perfeito para desenhar a visão, o equipamento e o ciclo. Prompt, contexto, harness, loop. Quatro camadas, uma pergunta de diagnóstico: em qual delas o seu time está gastando energia, e em qual deveria?

O dragão está pronto faz tempo. A sela é sua responsabilidade.

### Referências

- Martin Fowler / Birgitta Böckeler. Harness engineering for coding agent users. <https://martinfowler.com/articles/harness-engineering.html>
- Addy Osmani. Agent Harness Engineering. <https://addyosmani.com/blog/agent-harness-engineering/>
- IBM. What Is Loop Engineering? <https://www.ibm.com/think/topics/loop-engineering>
- Hugging Face. Harness, Scaffold, and the AI Agent Terms Worth Getting Right. <https://huggingface.co/blog/agent-glossary>
