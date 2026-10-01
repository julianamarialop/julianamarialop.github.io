---
title: "Survival ou Criativo: Como Construir Seu Primeiro Agente de IA na Oracle Sem Nunca Ter Aberto o Console"
date: 2026-09-08T15:55:00Z
summary: "Quem já jogou Minecraft sabe que a primeira decisão do jogo não é sobre onde construir. É sobre em qual modo jogar."
tags: ["Agentes de IA", "Oracle", "Copilot", "MCP", "Custos", "Microsoft Fabric"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/survival-ou-criativo-como-construir-seu-primeiro-agente-lopes-2shtf"
cover:
  image: cover.png
  alt: "Survival ou Criativo: Como Construir Seu Primeiro Agente de IA na Oracle Sem Nunca Ter Aberto o Console"
  relative: true
---

Quem já jogou Minecraft sabe que a primeira decisão do jogo não é sobre onde construir. É sobre em qual modo jogar.

No criativo, o inventário já vem cheio. Você abre o menu, arrasta o bloco que quiser e a casa sobe em minutos. No survival, você começa de mãos vazias, soca uma árvore para conseguir madeira, fabrica uma bancada, depois uma picareta, depois desce na mina. A mesma casa demora horas.

O jogador de criativo constrói mais rápido. O jogador de survival sabe de onde veio cada bloco, quanto custou e o que acontece se ele quiser mudar de bioma.

Essa é exatamente a diferença entre as duas formas de construir agentes corporativos hoje. E se você nunca abriu um console da Oracle na vida, este artigo é para você, porque vamos jogar no survival do começo ao fim, socando a primeira árvore e chegando até a tela de debug, com o código que realmente funciona.

De um lado, o OCI Enterprise AI, que ficou GA em março de 2026. Do outro, o Copilot Studio, reconstruído no Build 2026. Vou passar a maior parte do tempo no primeiro, porque ele é o menos conhecido e o mais mal explicado dos dois.

### Por Que a Oracle Resolveu Vender Blocos

A [Oracle](https://www.linkedin.com/company/oracle/) passou anos com um problema de percepção. Todo mundo sabia que ela tinha banco de dados e ERP. Quase ninguém associava o nome dela a plataforma de IA.

O OCI Enterprise AI foi a resposta, e ele junta numa oferta só três camadas que antes viviam separadas.

A primeira é a inteligência, que são os modelos e a inferência. E aqui vale reparar em algo que quase ninguém espera da Oracle: o catálogo é de terceiros. Grok da xAI, Gemini do Google, gpt-oss aberto, modelos da Cohere e a opção de importar o seu próprio.

A segunda é a capacidade de agir, que são os agentes e as ferramentas. Busca em documento, interpretador de código em container isolado, chamada de função, chamada de servidor MCP e conversão de pergunta em SQL.

A terceira é o controle, que já vem junto em vez de ser costurado depois. Identidade por OCI IAM, endpoints com retenção zero de dados, rastreio de cada passo executado, opção de IA soberana e cluster dedicado para quem precisa de isolamento.

A decisão mais inteligente dessa plataforma foi sobre a API. Em vez de inventar um dialeto próprio, a Oracle adotou a Responses API da OpenAI como interface. Você usa o SDK oficial da OpenAI, troca a base URL, a autenticação e o nome do modelo, e o resto do seu código continua igual. LangChain, LlamaIndex e o Agents SDK da OpenAI funcionam sem refatoração.

Traduzindo para quem nunca viu Oracle: você não precisa aprender Oracle para usar Oracle. Esse é o ponto inteiro.

### Entrando no Mundo

Vamos construir de verdade. O cenário é um agente que responde dúvidas sobre a política interna de reembolso e consulta o sistema de despesas quando precisa de um número real.

### 1. A permissão para entrar no servidor

Nada acontece na OCI sem política de IAM. Um compartimento é a caixa lógica onde os recursos vivem, e a política diz quem pode fazer o quê dentro dela. Peça ao administrador:

```
allow group <seu-grupo>
to manage generative-ai-family
in compartment <seu-compartimento>        
```

Essa é uma política de sandbox, o equivalente a entrar no servidor com permissão de construir em qualquer lugar. Em produção você restringe, e no passo 3 mostro como amarrar a permissão a uma chave específica.

### 2. Gerando o mundo, e as escolhas que não voltam atrás

Projeto é o recurso que organiza agentes e ativos relacionados. Você cria pelo console, e nessa tela existem três decisões que muita gente clica sem ler.

Retenção define por quanto tempo respostas e conversas ficam guardadas, com máximo de 720 horas, ou seja, 30 dias.

Compactação de memória de curto prazo resume o histórico recente para economizar token e latência. Você escolhe o modelo de compactação na criação e não muda depois.

Memória de longo prazo extrai e persiste informação importante das conversas como embeddings, e exige escolher modelo de extração e de embedding na criação.

Nos dois últimos casos, habilitou e quis desfazer, o caminho é deletar o projeto. É como o seed do mundo. Escolheu, é aquele. Guarde o OCID do projeto, ele vai no código.

### 3. A picareta

Crie uma API key de Generative AI pelo console, pegue o OCID dela e amarre a permissão a essa chave específica:

```
allow group <grupo-dos-builders>
to manage generative-ai-response
in compartment <seu-compartimento>
where ALL {request.principal.type='generativeaiapikey',
request.principal.id='<ocid-da-chave>'}        
```

Chave de API serve para teste e desenvolvimento inicial. Para produção a recomendação da Oracle é autenticação por IAM, com principal de instância ou de recurso, que evita credencial de vida longa.

### 4. Socando a primeira árvore

Instale o SDK da OpenAI, não o SDK da OCI. Esse detalhe derruba muita gente no primeiro dia.

```
pip install openai        
```

E o primeiro agente:

```
from openai import OpenAI

client = OpenAI(
    base_url="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com/openai/v1",
    api_key="<sua-api-key>",
    project="ocid1.generativeaiproject.oc1.us-chicago-1.xxxxxxxx"
)

response = client.responses.create(
    model="xai.grok-4.3",
    input="Explique em uma frase o que é um banco de dados."
)

print(response.output_text)        
```

Três coisas para reparar, porque explicam a filosofia da plataforma inteira.

A base URL carrega a região. Troque us-chicago-1 pela sua e o tráfego muda de continente, o que importa quando existe exigência de residência de dado.

O modelo é uma string, e a Oracle hospeda modelos de terceiros. Grok da xAI, Gemini do Google, gpt-oss aberto. Trocar de modelo é trocar uma linha, e é assim que você negocia custo contra qualidade sem reescrever a aplicação.

Se quiser capacidade dedicada em vez de sob demanda, o identificador do modelo passa a ser o OCID do endpoint do cluster. Mesmo código, infraestrutura isolada.

### 5. A bancada de trabalho

Um agente que só sabe o que o modelo já sabia não serve para nada corporativo. Ele precisa responder com base na sua política de reembolso, não com base na internet.

Você sobe o arquivo, cria um vector store e declara a ferramenta de busca na própria chamada:

```
response = client.responses.create(
    model="openai.gpt-oss-120b",
    input="Qual o prazo para solicitar reembolso de viagem?",
    tools=[
        {
            "type": "file_search",
            "vector_store_ids": ["<id-do-vector-store>"]
        }
    ]
)        
```

Repare que você não construiu pipeline de RAG. A recuperação é gerenciada pela plataforma. É a bancada de trabalho do jogo, aquele momento em que blocos soltos viram ferramenta.

### 6. Redstone, ou o agente que age

Consultar documento é bom, mas agente de verdade executa. Function calling é o padrão para isso, e a mecânica importa: o modelo não roda a sua função. Ele devolve o nome dela e os argumentos, a sua aplicação executa, e você manda o resultado de volta.

```
tools = [
    {
        "type": "function",
        "name": "consultar_despesas",
        "description": "Retorna as despesas lançadas por um colaborador em um período.",
        "parameters": {
            "type": "object",
            "properties": {
                "colaborador": {"type": "string"},
                "mes": {"type": "string", "description": "Formato 2026-08"}
            },
            "required": ["colaborador", "mes"],
        },
    },
]        
```

Quem executa é você. Quem tem acesso ao sistema é você. O modelo só pede. Para arquitetura corporativa, essa fronteira é a diferença entre uma prova de conceito e algo que passa em revisão de segurança.

Conte as idas e voltas desse caminho: a aplicação manda o prompt, o modelo devolve a chamada, a aplicação executa, a aplicação devolve o resultado, e só então o modelo responde. São duas viagens completas entre a sua aplicação e a plataforma.

Se a ferramenta já existir num servidor MCP, você corta esse vaivém pela metade. Declare o servidor na própria chamada e a plataforma conversa com ele diretamente, sem devolver o controle para o seu código no meio do caminho. Três passos em vez de cinco, uma viagem em vez de duas:

```
response = client.responses.create(
    model="openai.gpt-oss-120b",
    tools=[
        {
            "type": "mcp",
            "server_label": "despesas",
            "server_url": "https://interno.exemplo.com/mcp",
            "require_approval": "never",
            "allowed_tools": ["consultar_despesas"]
        }
    ],
    input="Quanto o time de dados gastou em viagem em agosto?"
)        
```

### 7. O mapa do tesouro

Essa é a peça mais oracle de todas, e a que mais interessa a quem trabalha com dado. O NL2SQL do Enterprise AI converte pergunta em linguagem natural em SQL validado, usando uma camada de enriquecimento semântico que mapeia termo de negócio para tabela, coluna e join.

O detalhe de segurança que merece aplauso: o NL2SQL gera o SQL e não executa. Quem executa é o Database Tools MCP Server, usando a identidade do usuário final. E a configuração exige duas conexões separadas, uma de enriquecimento, com privilégio maior para ler metadado e amostra, e outra de query, com privilégio menor para rodar em nome do usuário.

Se você vem de engenharia de dados, reconhece o padrão na hora. É separação de papéis aplicada a agente.

### 8. Apertando F3

Todo jogador de Minecraft conhece a tela de debug. Na Responses API ela vem de graça: toda resposta traz um campo output que é a lista dos passos executados, com tipos como message, file\_search\_call e mcp\_call.

```
for item in response.output:
    print(item.type)        
```

Rastreabilidade nativa, sem instrumentar nada. E se quiser observabilidade completa, com latência e custo, dá para plugar Langfuse trocando apenas o import do cliente OpenAI.

### O Modo Criativo

Do outro lado, o Copilot Studio resolve o mesmo problema com o inventário cheio.

Você não escreve código. Cria o agente numa tela, liga a orquestração generativa e o modelo decide sozinho qual ferramenta chamar. Depois do Build 2026 o produto tem quatro superfícies mais uma: Skills, que são instruções reutilizáveis em markdown, Tools, Knowledge, Connected agents e Memory.

O poder dele não está nessas superfícies. Está no Microsoft IQ, a camada de contexto com três fontes: Work IQ, com e-mail, chat, arquivo, calendário e pessoas do Microsoft 365, Fabric IQ, com dado de negócio no Fabric, e Foundry IQ, com bases indexadas pelo Azure AI Search. Ligar uma fonte dá leitura e ação ao mesmo tempo, dentro da permissão do usuário logado.

Se a sua empresa vive no Microsoft 365, o inventário já está cheio e a casa sobe em minutos. Se não vive, você está no criativo de um mundo onde os blocos que interessam não vieram no menu, e cada conector é uma tentativa de importar bloco de outro mundo.

Colocando os dois lado a lado, a diferença aparece em cinco pontos. Você constrói escrevendo código contra uma API ou clicando em telas com orquestração automática. O agente roda na sua conta OCI, na região que você escolher, ou na plataforma da Microsoft. O contexto que vem de graça é o seu banco e os seus arquivos de um lado, e o Microsoft 365, o Fabric e o Foundry do outro. A conta chega por transação de caractere e compromisso de cluster, ou por crédito consumido por ação. E cada um ganha onde o dado já mora.

### O Custo de Cada Bloco

A Oracle cobra minério. A inferência sob demanda é medida em transações, e uma transação é um caractere, somando prompt e resposta. Cluster dedicado exige compromisso mínimo de 744 unit-hours, que é um mês corrido. Modelo importado não carrega essa exigência.

A Microsoft cobra construção. Copilot Credits vêm em pacotes de 25 mil por 200 dólares ao mês, ou por consumo no Azure à mesma taxa.

Isso muda quem aprova a conta dentro do cliente. Uma vai para infraestrutura, com capacidade e compromisso mensal. A outra vai para a área de negócio, com crédito por ação. Já vi proposta ser mal calibrada por não perceber isso e ir para o comitê errado.

### No Fim, a Mesma Construção

Quem joga survival e quem joga criativo terminam com a mesma casa na tela. O que muda é quem carregou o material e quanto cada um sabe sobre a própria construção.

E os dois modos estão convergindo mais rápido do que o discurso comercial admite. A Oracle e a Microsoft adotaram MCP como protocolo de ferramenta. As duas decidiram que agente precisa de identidade própria, uma com autenticação IAM nos endpoints hospedados, a outra com Entra Agent ID automático em todo agente novo desde julho de 2026. As duas entenderam que instrução reutilizável precisa ser artefato versionável, não texto colado num campo.

Vindas de pontos opostos, chegaram nas mesmas três conclusões. É como se as duas fábricas tivessem combinado o mesmo encaixe.

Então a pergunta não é qual modo é melhor. É de que lado da fronteira mora o dado que decide o seu negócio. Se a resposta for e-mail, reunião e arquivo, o inventário do criativo já resolve. Se for banco, aplicação própria ou dado que não pode atravessar fronteira geográfica, pegue a picareta.

O código está aí em cima, e ele roda hoje.

### Referências

- Quick Start Guide, Enterprise AI Agents: <https://docs.oracle.com/en-us/iaas/Content/generative-ai/get-started-agents.htm>
- OCI OpenAI-Compatible Endpoints: <https://docs.oracle.com/en-us/iaas/Content/generative-ai/openai-compatible-api.htm>
- Announcing GA of OCI Enterprise AI: <https://blogs.oracle.com/ai-and-datascience/announcing-oci-enterprise-ai-ga>
- What's New in Oracle AI, August 2026: <https://blogs.oracle.com/ai-and-datascience/whats-new-in-ai-august-2026>
- Paying for Dedicated AI Clusters: <https://docs.oracle.com/en-us/iaas/Content/generative-ai/pay-dedicated.htm>
- Build an agent, Microsoft Copilot Studio: <https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/build-overview>
- What's new in Copilot Studio: <https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new>
