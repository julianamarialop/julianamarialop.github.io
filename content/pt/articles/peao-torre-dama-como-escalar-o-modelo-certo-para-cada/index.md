---
title: "Peão, Torre, Dama: Como Escalar o Modelo Certo Para Cada Agente"
date: 2026-08-21T14:00:00Z
summary: "Todo enxadrista aprende cedo uma tabela que carrega pela vida inteira: peão vale 1, cavalo e bispo valem 3, torre vale 5, dama vale 9. Não é regra do jogo, é sabedoria acumulada de séculos sobre o poder relativo de cada…"
tags: ["Custos", "Agentes de IA", "IA Generativa", "Claude", "Microsoft Fabric", "Azure"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/pe%C3%A3o-torre-dama-como-escalar-o-modelo-certo-para-cada-lopes-llmsf"
cover:
  image: cover.jpg
  alt: "Peão, Torre, Dama: Como Escalar o Modelo Certo Para Cada Agente"
  relative: true
---

### O Valor das Peças

Todo enxadrista aprende cedo uma tabela que carrega pela vida inteira: peão vale 1, cavalo e bispo valem 3, torre vale 5, dama vale 9. Não é regra do jogo, é sabedoria acumulada de séculos sobre o poder relativo de cada peça. E dela derivam as lições que separam quem joga de quem entende. Não se usa a dama para trabalho de peão, porque cada lance dela em tarefa pequena é um lance em que ela não está decidindo o jogo. Philidor escreveu no século XVIII que os peões são a alma do xadrez: partidas se ganham e se perdem na estrutura deles, as peças humildes que fazem o trabalho de volume. E o rei, curiosamente a peça menos poderosa do tabuleiro, é a única insubstituível: ele anda uma casa por vez, mas tudo gira em torno dele, e quando ele cai, acabou.

O mercado de modelos de linguagem em 2026 é esse tabuleiro. Os preços públicos vão de cerca de 10 centavos a 75 dólares por milhão de tokens, uma diferença que faz o peão e a dama do xadrez parecerem próximos: no tabuleiro a dama vale 9 peões, no catálogo ela pode valer 60. E mesmo assim, a cena mais comum em projetos de IA corporativa segue sendo um tabuleiro montado só de damas: o modelo mais caro do catálogo executando classificação de texto, extração de campo e validação de regra, tarefas de peão, com cachê de dama.

Neste artigo eu apresento as peças uma a uma, com specs e números reais, e depois monto uma partida completa: um projeto multiagente sobre [Microsoft Fabric](https://www.linkedin.com/company/microsoft-fabric-world/) e Foundry em que cada função roda no modelo do seu valor.

### As Damas: Modelos de Fronteira

A dama é o modelo de raciocínio profundo, e em agosto de 2026 três dominam o topo dos índices independentes.

O Claude Opus 4.8, da Anthropic, lidera os rankings agregados de inteligência e é o rei do código: os comparativos reportam 88,6% no SWE-bench Verified, o benchmark que mede resolução de bugs reais em repositórios reais, com capacidade de coordenar subagentes paralelos em tarefas de larga escala. Contexto de 200 mil tokens, preço na faixa alta do mercado. É a dama para engenharia complexa, análise ambígua de várias etapas e orquestração. No Foundry, os modelos Claude estão em disponibilidade geral desde julho de 2026, em duas variantes de hospedagem.

A família GPT-5.6, da OpenAI, lançada em julho de 2026, trouxe a artilharia de contexto: 1.050.000 tokens de janela, com variantes que equilibram custo e capacidade. A geração anterior, GPT-5.5, segue forte em fluxos agênticos e multimodais, e os comparativos a colocam lado a lado com o Opus em código. É a dama para missões que precisam enxergar bases de código ou documentos inteiros de uma vez.

O Gemini 3.1 Pro, do Google, é a dama com melhor custo-benefício da fronteira: os comparativos reportam 80,6% no SWE-bench, praticamente empatado com os líderes, a uma fração do custo, com 1 milhão de tokens de contexto. A honestidade de tabuleiro: ele não vive no catálogo do Foundry, então para arquiteturas ancoradas no ecossistema Microsoft ele é uma dama do clube vizinho.

Quando usar uma dama: planejamento, decomposição de problemas ambíguos, código complexo multiarquivo, julgamento final. Quando não usar: qualquer tarefa que se descreve em uma frase e se verifica com uma regra.

### As Torres: Os Cavalos de Batalha

A torre vale 5: forte, direta, e é quem carrega o meio-jogo. São os modelos equilibrados, e a regra prática é que eles resolvem a maioria absoluta das tarefas corporativas por uma fração do custo da dama.

O Claude Sonnet 4.6 é o exemplo canônico: os comparativos reportam 79,6% no SWE-bench, alguns pontos atrás do Opus, com custo e latência bem menores. Para código do dia a dia, análise de dados, geração de documentos e agentes de produção, a torre entrega perto da dama pagando muito menos. O GPT-5.4 ocupa a mesma casa no lado OpenAI, com destaque reportado em raciocínio estruturado e uso de computador (75% no OSWorld, acima da linha de base de especialistas humanos) e a mesma janela expandida de 1.05 milhão de tokens. E o Llama 4 Maverick, da Meta, é a torre de peso aberto que aparece inclusive no pool do Model Router do Foundry.

Quando usar: como padrão. A torre deveria ser o modelo default da sua arquitetura, com a dama entrando por exceção justificada e o peão por otimização de volume.

### Os Bispos: Especialistas de Uma Cor Só

O bispo é poderoso com uma limitação estrutural: enxerga só as casas da sua cor. São os modelos especializados, imbatíveis na sua diagonal e inúteis fora dela.

O Grok 4.1 fast reasoning, da xAI, presente no router do Foundry, é o bispo da velocidade: raciocínio rápido para casos agênticos onde latência importa mais que profundidade máxima. Os modelos de embedding são bispos puros: não conversam, só transformam texto em vetores, e nenhuma busca semântica ou RAG existe sem eles. Modelos de visão e de geração de imagem seguem a mesma lógica. E o DeepSeek V3.2 e o novo V4, abertos sob licença MIT, são os bispos do custo: os comparativos os colocam poucos pontos atrás das damas proprietárias em código, custando dezenas de vezes menos, o que redefine a matemática de trabalho em lote massivo. Com a diagonal honesta declarada: para contexto regulado, o caminho de dados e a maturidade operacional precisam entrar na análise de risco antes do preço.

### Os Cavalos: O Movimento Que Ninguém Mais Faz

O cavalo vale os mesmos 3 pontos do bispo, mas tem o único movimento do jogo que salta sobre as outras peças. São os modelos de peso aberto e os SLMs, que chegam onde os fechados não chegam: dentro do seu datacenter, na borda, no dispositivo, no fine-tuning profundo com seus dados.

A família Phi, da Microsoft, é o cavalo da casa no Foundry: modelos pequenos que rodam com custo mínimo e até localmente, ideais para tarefas bem delimitadas em altíssimo volume. O Llama 4 em seus tamanhos menores cumpre o mesmo papel com o maior ecossistema de comunidade. O salto do cavalo é a resposta para os requisitos que travam projetos: dado que não pode sair do perímetro, latência de milissegundos, custo por chamada tendendo a zero.

### Os Peões: A Alma da Operação

E chegamos à peça de Philidor. Os peões são os modelos leves das famílias de fronteira: Claude Haiku 4.5, GPT-5.4-nano e mini, os Flash e Flash-Lite do mundo, com preços na casa dos centavos por milhão de tokens. Individualmente modestos, em estrutura eles decidem partidas: classificação, extração de campos, roteamento de mensagens, validação de regras, tudo que roda milhares de vezes por dia e se verifica com critério objetivo.

A estrutura de peões da sua arquitetura é a camada de validação e triagem. Time que monta essa estrutura bem gasta centavos onde os concorrentes gastam dólares, e chega ao final do jogo com as damas intactas para o que importa.

### O Rei e o Enxadrista

Duas figuras faltam, e a distinção entre elas organiza a arquitetura inteira.

O rei é o orquestrador: o agente que recebe a missão, decompõe em tarefas, aciona cada peça e julga os resultados. Como no tabuleiro, ele não é quem mais se move; ele faz poucos lances, mas cada um decide a partida, e se ele cai, a missão inteira cai. Por isso o rei justifica um modelo de fronteira ou um equilibrado superior: errar uma classificação custa centavos, errar a decomposição custa a batalha.

E o enxadrista é você. Aqui vale desfazer uma confusão comum no Foundry: o Model Router, que roteia cada prompt entre 28 modelos otimizando custo e qualidade, é uma ferramenta valiosa, mas é um seletor de peça por lance, não um jogador. Orquestração de missão, com estado, sequência e julgamento, é papel de agente desenhado por você, tipicamente com o rei rodando num modelo forte e carregando os protocolos da operação, as skills, hoje hospedáveis no próprio Foundry.

### A Partida: O Projeto Multiagente

Agora a partida completa, no meu mundo: a torre de controle de qualidade de dados com relatório executivo diário, sobre Fabric e Foundry.

A abertura é evento, não prompt: o Activator do Fabric detecta a chegada da carga diária no OneLake e dispara a missão, sem nenhum token gasto perguntando se o dado chegou.

O rei acorda: o orquestrador, num Claude Opus ou GPT-5.6, lê o protocolo da operação e decompõe a missão em quatro tarefas com dependências.

Os peões avançam: agentes de validação em Haiku e Phi varrem centenas de regras de qualidade, contagens, duplicidades e domínios. Volume puro, custo em centavos, resultado verificável por regra.

A torre entra no meio-jogo: um agente de análise em Sonnet ou GPT-5.4 investiga as variações do dia conversando com o Data Agent do Fabric, que responde ancorado nos modelos semânticos onde vivem as definições oficiais de KPI. A definição de receita líquida mora no modelo semântico, não copiada em cinco prompts.

O bispo escreve: um agente redator transforma os achados no relatório executivo, no formato do protocolo.

E o lance final vem da tradição enxadrística moderna: nenhum grande mestre confia a análise de uma partida a um único engine. Usa-se o Stockfish e a Leela, motores de estilos diferentes, porque a discordância entre eles é onde mora o aprendizado. O quinto agente é esse segundo engine: um crítico de outra família de modelo que a do redator. Se o redator é Claude, o crítico é GPT, e vice-versa. A revisão cruzada entre famílias reduz o vício de estilo e a complacência de linhagem, prima daquela sycophancy sobre a qual já escrevi. Só com o aval do crítico o rei publica e encerra.

Uma missão, seis modelos, quatro valores de peça, duas famílias. O custo despenca em relação ao tabuleiro só de damas, e a qualidade sobe, porque discordância virou arquitetura.

### O Que Muda Para Times de Dados

Três regras de clube de xadrez para levar. Primeira: dimensione pelo volume, não pelo prestígio. Liste as funções que rodam milhares de vezes por dia e empurre para peões e cavalos; a economia paga a dama do orquestrador com sobra. Segunda: institua o segundo engine. Revisão cruzada entre famílias como regra de arquitetura, o que o catálogo unificado do Foundry, com mais de 1.900 modelos sob a mesma governança e política central de implantação, torna trivial. Terceira: benchmarks mudam mensalmente e a liderança troca de mãos a cada trimestre, então construa para trocar de peça barato: modelo é configuração, não fundação. Quem acopla a arquitetura a um modelo específico está jogando a partida de hoje com a teoria de abertura do ano passado.

E a honestidade de sempre: multiagente é final de jogo, não abertura. Se um agente só resolve, cinco agentes são complexidade sem retorno. Monte o tabuleiro completo quando as funções forem genuinamente diferentes a ponto de pedirem peças diferentes.

### Conclusão: Quem Vence a Partida

No xadrez, os dois jogadores começam com exatamente as mesmas peças. O tabuleiro é público, os valores são conhecidos, e mesmo assim alguém vence. A diferença nunca esteve nas peças; esteve em quem entende o valor relativo delas e aloca cada uma na casa certa, no lance certo.

Com modelos de LLM, o catálogo também é público e igual para todos. Seus concorrentes têm acesso às mesmas damas, torres e peões que você. A vantagem competitiva não está em ter o modelo mais forte, está na escalação: a dama guardada para o que decide, os peões estruturados no volume, o segundo engine conferindo a análise, e o rei protegido no centro da arquitetura.

A pergunta que fica no tabuleiro: quantas damas do seu projeto estão, neste momento, fazendo trabalho de peão?

### Referências

- Microsoft Learn. Model router for Microsoft Foundry concepts. <https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-router>
- Microsoft Azure. Foundry Models. <https://azure.microsoft.com/en-us/products/ai-foundry/models>
- LM Council. AI Model Benchmarks. <https://lmcouncil.ai/benchmarks>
- Iternal. LLM Comparison 2026: 30+ Models Benchmarked. <https://iternal.ai/llm-selection-guide>
- TechieHub. Best AI Models Compared 2026. <https://techiehub.blog/best-ai-models-compared/>
