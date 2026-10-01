---
title: "O Que o Aranhaverso Me Ensinou Sobre Levar Skills do Claude Para o Microsoft Foundry"
date: 2026-07-17T17:33:00Z
summary: "A premissa mais bonita de Homem-Aranha: Através do Aranhaverso não é visual, é filosófica. Em todo universo existe um Homem-Aranha. Miles Morales em um, Gwen Stacy em outro, Peter B. Parker de moletom em um terceiro, um…"
tags: ["Agentes de IA", "Claude", "MCP"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/o-que-aranhaverso-me-ensinou-sobre-levar-skills-do-claude-lopes-pwdkf"
cover:
  image: cover.jpg
  alt: "O Que o Aranhaverso Me Ensinou Sobre Levar Skills do Claude Para o Microsoft Foundry"
  relative: true
---

### Em Todo Universo Existe Um Homem-Aranha

A premissa mais bonita de Homem-Aranha: Através do Aranhaverso não é visual, é filosófica. Em todo universo existe um Homem-Aranha. Miles Morales em um, Gwen Stacy em outro, Peter B. Parker de moletom em um terceiro, um Peter noir em preto e branco, até um porco chamado Peter Porker. Os trajes mudam, os poderes variam nos detalhes, o desenho de cada mundo é completamente diferente. Mas existe algo que atravessa todos os universos intacto: o cânon. A picada, a perda, a responsabilidade. Os eventos que definem o que é ser o Homem-Aranha não pertencem a nenhum universo específico. Pertencem à história.

E o filme guarda um segundo detalhe, menos poético e mais técnico. Quando alguém visita um universo que não é o seu, o corpo começa a falhar. Miles em outro mundo sofre glitches: pixels quebrando, membros desalinhando, a realidade rejeitando o que não foi escrito para ela. O que é do personagem viaja bem. O que é do universo de origem, não.

Migrar skills do Claude para o Microsoft Foundry é exatamente essa física. O que é cânon atravessa o portal intacto. O que é traje precisa ser recosturado. E o que é glitch você aprende a identificar antes de pular.

### O Cânon: O Padrão Aberto

Uma skill é um arquivo SKILL.md: um cabeçalho YAML com nome e descrição, seguido de instruções em markdown puro. A Anthropic lançou as Agent Skills em outubro de 2025 e, em dezembro do mesmo ano, publicou o formato como padrão aberto em agentskills.io. A partir daí, a história deixou de ser sobre um recurso do Claude e virou uma história sobre interoperabilidade: o Codex CLI da OpenAI, o Gemini CLI do Google e o GitHub Copilot adotaram o mesmo formato. A própria Microsoft mantém hoje repositórios inteiros de skills nesse padrão, como o MicrosoftDocs/Agent-Skills, com skills que funcionam em qualquer assistente compatível.

Isso significa que o protocolo que você escreveu para o Claude, com suas definições de KPI, suas regras de validação, seu workflow de análise, já nasceu multiversal. O markdown é o cânon. Ele não pertence à plataforma onde foi escrito.

### Um Novo Universo: Skills Nativas no Foundry

Em 2026 o portal abriu do lado da Microsoft. O Microsoft Foundry passou a oferecer, em preview, suporte nativo a skills através de uma Skills REST API versionada. O fluxo: você autora o SKILL.md, armazena centralmente no Foundry com controle de versão, e anexa a skill a toolboxes ou a hosted agents.

O problema que isso resolve é o mesmo que motivou as skills no Claude, e a documentação da Microsoft descreve com precisão cirúrgica. Times que constroem agentes acumulam diretrizes comportamentais que precisam ser consistentes em toda conversa: o agente de suporte segue uma política fixa de escalonamento, o agente de code review aplica o mesmo checklist, o agente de vendas respeita as mesmas restrições de mensagem. Quando essas diretrizes vivem embutidas no system prompt ou no código de cada agente, nasce a duplicação. A política muda, e você atualiza e redeploya cada agente que a usa. A skill desacopla a diretriz do código: escrita uma vez, versionada centralmente, herdada por todos.

Se essa descrição soa familiar, é porque é o mesmo argumento da governança como código que venho defendendo aqui na newsletter. A novidade é que agora ele vale dos dois lados do portal.

### A Migração: O Que Atravessa Intacto

Na prática, uma skill construída no Claude tem três camadas, e cada uma atravessa o portal de um jeito.

A primeira camada é o protocolo em markdown, e ela migra praticamente por cópia. Definições de negócio, regras de validação, réguas de complexidade, workflows passo a passo, tudo isso é cânon. No máximo você ajusta a descrição de gatilho para o vocabulário do novo ambiente. Se a sua skill foi escrita como conhecimento estruturado, e não como script de automação, essa camada é a maior parte do arquivo.

A segunda camada são as referências ao runtime de origem, e elas precisam de recostura. Paths como /mnt/skills, menções a artifacts, nomes de ferramentas específicas do Claude, instruções de orquestração em que uma skill invoca outra pelo nome. Nada disso existe no universo Foundry. Lá, a lógica de orquestração vira responsabilidade do hosted agent, tipicamente construído em Microsoft Agent Framework, LangGraph ou framework custom em Python ou C#. O protocolo continua dizendo o que fazer; quem coordena a execução muda de figura.

A terceira camada são os motores de código que muitas skills maduras carregam: scripts Python determinísticos de cálculo, geração de arquivos, validação. Esses não atravessam por cópia, atravessam por engenharia. Os caminhos naturais são dois: rodar dentro do próprio hosted agent containerizado, ou expor o motor como servidor MCP e deixar qualquer plataforma consumi-lo como ferramenta. O MCP, aliás, é a ponte universal dessa história: enquanto a skill carrega o conhecimento, o MCP carrega a capacidade de agir, e ambos são padrões abertos que o Claude e o Foundry falam.

### O Glitch: O Que Quebra Fora do Universo de Origem

Miles descobre da pior forma que o corpo dele não foi escrito para o universo errado. Com skills, o glitch aparece nas linhas que assumem o ambiente de origem sem declarar. Compare:

```
Salve o resultado em /mnt/user-data/outputs e gere
um artifact React com o dashboard.        
```
```
Gere o dashboard no formato interativo disponível
no ambiente e disponibilize o arquivo ao usuário.        
```

A primeira versão funciona perfeitamente no Claude e glitcha em qualquer outro lugar. A segunda atravessa universos. A lição prática: escreva o protocolo em termos de intenção e regra de negócio, isole o que é específico de plataforma em seções claramente marcadas, e delegue ações externas a ferramentas MCP em vez de assumir ferramentas nativas. Skill portável não é a que evita o runtime, é a que sabe exatamente onde o runtime começa.

### O Que Muda Para Times de Dados

Para quem lidera arquitetura, a consequência estratégica é maior que a técnica: o repositório de protocolos vira um ativo independente de plataforma. Um único repo Git com os SKILL.md do time, versionado com pull request e dono, passa a servir o Claude hoje, o Foundry amanhã e o que vier depois. O investimento em documentar as regras do seu domínio deixa de ser aposta em um fornecedor e vira patrimônio da organização. É a resposta concreta para a pergunta de lock-in que todo comitê de arquitetura faz.

E os caveats importam, porque honestidade técnica é o que separa artigo de propaganda. O suporte a skills no Foundry é preview: sem SLA, não recomendado para produção. E há uma restrição que pesa em ambientes regulados: a Skills API não suporta private networking, então não é possível criar, gerenciar ou baixar skills em um recurso Foundry com acesso público desabilitado. Para cliente bancário com rede fechada, isso hoje é um bloqueador de adoção que precisa entrar no desenho da solução, não uma nota de rodapé.

### Disponibilidade e Acesso

No Claude, as skills estão disponíveis nos planos pagos e, nos planos Team e Enterprise, com controle administrativo central sobre o que fica provisionado para a organização. No Microsoft Foundry, o suporte a skills está em preview e requer um projeto Foundry ativo e a role Foundry User no projeto, com autoria e gestão via Skills REST API. O padrão aberto, com especificação e exemplos, está publicado em agentskills.io.

### Conclusão: O Cânon Atravessa

No Aranhaverso, o que faz alguém ser o Homem-Aranha nunca foi o traje, o universo ou o estilo de desenho. É o cânon: a história essencial que se repete intacta em cada mundo. Os trajes são recosturados a cada universo. Os glitches ensinam o que não deveria ter atravessado.

Com skills, a física é a mesma. O conhecimento do seu domínio escrito em markdown é o cânon, e ele agora atravessa do Claude para o Foundry, para o Codex, para o Gemini CLI, para o Copilot. O runtime é o traje, recosturado em cada plataforma. Os paths e as ferramentas nativas são o glitch, e você aprende a isolá-los antes de pular.

Escreva seus protocolos como cânon. Porque no multiverso de agentes que está se formando, a pergunta deixou de ser em qual plataforma você aposta. Passou a ser: o que da sua arquitetura sobrevive à viagem entre todas elas?

### Referências

- Microsoft Learn. Use skills with Microsoft Foundry agents (preview). <https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills>
- Agent Skills. Especificação do padrão aberto. <https://agentskills.io>
- Anthropic. Equipping agents for the real world with Agent Skills. <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills>
- MicrosoftDocs. Agent-Skills: Curated Agent Skills for Microsoft & Azure. <https://github.com/MicrosoftDocs/Agent-Skills>
