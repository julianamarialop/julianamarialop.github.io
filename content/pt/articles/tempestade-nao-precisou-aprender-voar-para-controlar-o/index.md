---
title: "Tempestade Não Precisou Aprender a Voar Para Controlar o Clima: Como Usar o VS Code com Claude Sem Ser Desenvolvedor"
date: 2026-04-16T11:30:00Z
summary: "Existe uma crença no mundo de dados que poucos questionam: a IDE é território de desenvolvedor. O VS Code, com suas pastas, arquivos e terminal, seria um ambiente hostil para quem não escreve código todos os dias."
tags: ["Claude", "Engenharia de Dados", "Custos"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/tempestade-n%C3%A3o-precisou-aprender-voar-para-controlar-o-lopes-efwdf"
cover:
  image: cover.jpg
  alt: "Tempestade Não Precisou Aprender a Voar Para Controlar o Clima: Como Usar o VS Code com Claude Sem Ser Desenvolvedor"
  relative: true
---

### O Mito da Barreira Técnica

Existe uma crença no mundo de dados que poucos questionam: a IDE é território de desenvolvedor. O VS Code, com suas pastas, arquivos e terminal, seria um ambiente hostil para quem não escreve código todos os dias.

Tempestade nunca acreditou em barreiras assim.

Quando ela entra em combate, não precisa entender a física atmosférica para invocar um raio. Ela não calcula a pressão do ar nem a resistência elétrica antes de agir. Ela sabe quais poderes tem, sabe quando acioná-los, e confia na combinação certa para entregar o resultado. O conhecimento técnico profundo existe por baixo, mas não é o que ela precisa para operar.

Com duas extensões no VS Code, Claude Code e GitLab, qualquer profissional de dados pode trabalhar com projetos reais, entender código, propor mudanças, acompanhar pipelines e colaborar com times de engenharia, sem escrever uma linha de código sequer.

Este artigo é o manual que Tempestade daria para qualquer recruta antes de entrar no campo.

### Por Que o VS Code e Não o Claude.ai?

Essa é a primeira pergunta que surge. Afinal, o claude.ai já está no navegador, já responde perguntas sobre código e já ajuda a analisar arquivos. Por que instalar um programa diferente?

A resposta está na diferença entre pedir conselho por telefone e ter o especialista sentado ao seu lado olhando para a mesma tela.

No claude.ai, você copia um trecho de código, cola na conversa e Claude responde. Funciona, mas tem limites sérios: você precisa copiar manualmente o que quer analisar, Claude não vê o projeto inteiro, não sabe como os arquivos se relacionam e não consegue fazer mudanças reais nos arquivos.

No VS Code com Claude Code, Claude **vive dentro do projeto**. Ele lê todas as pastas e arquivos ao mesmo tempo, entende como os componentes se conectam, faz mudanças reais diretamente nos arquivos e salva. Você não copia nada. Você aponta e pede.

É a diferença entre descrever um problema de pipeline para alguém que nunca viu o projeto e sentar com um especialista que já leu cada arquivo antes da reunião começar.

Para quem trabalha com projetos de dados que envolvem dezenas de arquivos, pipelines interligados e repositórios compartilhados com times de engenharia, essa diferença é o que torna o VS Code o ambiente certo.

### Antes de Começar: O Que Você Precisa

Antes de instalar qualquer extensão, verifique se você tem o seguinte:

**VS Code instalado.** Acesse [code.visualstudio.com](http://code.visualstudio.com) e baixe a versão para o seu sistema operacional. A instalação é simples e gratuita.

**Conta Claude com plano Pro ou superior.** O Claude Code não está disponível no plano gratuito. Você precisa de um plano Pro ($20/mês), Max, Team ou Enterprise. Se ainda não tem, acesse [claude.ai/pricing](http://claude.ai/pricing) para assinar.

**Node.js instalado.** O Claude Code precisa do Node.js para funcionar. Acesse [nodejs.org](http://nodejs.org), baixe a versão LTS e instale. Não é necessário saber usá-lo, apenas tê-lo instalado na máquina.

**Conta no GitLab.** Se o seu time usa GitLab, você já tem. Se ainda não tem, acesse [gitlab.com](http://gitlab.com) e crie uma conta gratuita.

Com esses quatro itens prontos, você está equipado para começar.

### O Que Você Vai Conseguir Fazer

Com a extensão **Claude Code** da [Anthropic](https://www.linkedin.com/company/anthropicresearch/) você consegue abrir qualquer arquivo de um projeto, pedir para Claude explicar o que aquele código faz em linguagem simples, solicitar alterações descrevendo o que quer em português, pedir documentação, identificar problemas e entender a estrutura do projeto inteiro sem precisar ler cada arquivo manualmente.

Com a extensão **GitLab** você consegue ver issues do projeto diretamente no VS Code, acompanhar o status dos pipelines de CI/CD em tempo real, revisar merge requests, deixar comentários e aprovar mudanças, tudo sem abrir o navegador.

Juntas, essas duas extensões transformam o VS Code em um ambiente de trabalho completo para qualquer profissional que precisa colaborar com times de engenharia ou entender projetos técnicos.

**Passo 1: Instale as Extensões**

Abra o VS Code. Na barra lateral esquerda, clique no ícone que parece quatro quadrados (ou pressione Ctrl+Shift+X no Windows ou Cmd+Shift+X no Mac). Isso abre o marketplace de extensões.

**Instalando Claude Code:**

No campo de busca, digite Claude Code. Procure a extensão publicada por **Anthropic** com mais de 2 milhões de instalações. Clique em **Install**.

Após a instalação, um ícone de faísca (Spark) vai aparecer na barra lateral esquerda. Clique nele. Na primeira vez, uma tela de autenticação vai aparecer. Clique em **Sign in**, autorize no navegador e volte ao VS Code. Você está conectado.

**Instalando GitLab:**

No mesmo campo de busca, digite GitLab Workflow. Procure a extensão publicada por **GitLab** com o ícone da raposa. Clique em **Install**.

Após a instalação, você vai precisar conectar sua conta GitLab. Clique no ícone da raposa na barra lateral. A extensão vai pedir um **Personal Access Token** do GitLab. Para gerar um:

1. Acesse seu GitLab
2. Vá em **Settings → Access Tokens**
3. Crie um token com os escopos api e read\_user
4. Copie o token e cole na extensão

Pronto. As duas extensões estão instaladas e configuradas.

**Passo 2: Abra um Projeto**

Para trabalhar com um projeto existente, vá em **File → Open Folder** e navegue até a pasta do projeto no seu computador. Se o projeto está no GitLab e você ainda não tem ele localmente, use **File → New Window**, depois Ctrl+Shift+P para abrir a paleta de comandos e digite Git: Clone. Cole a URL do repositório GitLab e escolha onde salvar.

Quando o VS Code abrir a pasta do projeto, a extensão GitLab vai reconhecer automaticamente o repositório e começar a mostrar informações na barra lateral.

Tempestade não precisa construir o campo de batalha. Ela entra nele como está e orienta os elementos ao redor.

**Passo 3: Use Claude Para Entender o Projeto**

Clique no ícone de faísca na barra lateral para abrir o painel do Claude Code. Aqui começa a parte onde a barreira técnica desaparece.

**Entendendo a estrutura do projeto:**

No painel do Claude, digite:

```
> "Explique a estrutura deste projeto em português. Quais são as pastas principais, o que cada uma contém e como os componentes se relacionam?"        
```

Claude vai ler o projeto inteiro e entregar uma explicação em linguagem simples, sem jargão desnecessário.

**Entendendo um arquivo específico:**

Abra qualquer arquivo no editor. No painel do Claude, use @ para referenciar o arquivo pelo nome e pergunte:

```
> "@pipeline_vendas.py O que esse arquivo faz? Explica cada parte em linguagem simples."        
```

Claude lê o arquivo com o contexto completo do projeto e explica cada bloco de forma clara.

**Identificando problemas:**

```
> "Analise os arquivos de pipeline neste projeto e me diga se há algum padrão que poderia causar problemas de performance ou falhas."        
```

Claude vai ler os arquivos relevantes, cruzar com boas práticas e entregar um diagnóstico em linguagem acessível.

**Passo 4: Peça Mudanças Sem Escrever Código**

Essa é a parte onde o impacto fica mais evidente. Você não precisa saber Python, SQL ou qualquer linguagem para propor e aplicar mudanças em um projeto.

**Exemplos de pedidos que funcionam:**

```
> "Adicione um comentário explicativo no início de cada função do arquivo @utils.py descrevendo o que ela faz."        
```
```
> "Esse arquivo está sem tratamento de erros. Adicione mensagens de erro claras para os casos onde a conexão com o banco de dados falha."        
```
```
> "Crie um arquivo README.md na pasta raiz explicando o que este projeto faz, como está estruturado e quais são os principais pipelines."        
```

Quando Claude sugere uma mudança, ela aparece como um **diff visual** no editor: o que vai ser removido marcado em vermelho, o que vai ser adicionado em verde. Você revisa, aprova com um clique ou pede ajuste antes de aceitar.

Tempestade não constrói o raio manualmente. Ela diz onde quer que ele caia e observa o resultado antes de confirmar.

**Passo 5: Use GitLab Para Acompanhar e Colaborar**

Com a extensão GitLab ativa, a barra lateral mostra tudo que você precisa sobre o projeto sem sair do VS Code.

**Acompanhando issues:**

Clique no ícone da raposa na barra lateral. Expanda **Issues and Merge Requests**. Você vê todas as issues abertas do projeto com título, status e responsável. Clique em qualquer issue para ler a descrição completa diretamente no VS Code.

**Monitorando pipelines:**

Na barra inferior do VS Code, a extensão GitLab mostra em tempo real o status do pipeline do branch atual: executando, passou ou falhou. Clique no status para ver os detalhes de cada job.

**Revisando e aprovando merge requests:**

Na seção de Merge Requests da extensão, você vê todos os MRs abertos. Clique em qualquer um para ver o diff das mudanças, deixar comentários em linhas específicas e aprovar usando o comando GitLab: Approve Merge Request na paleta de comandos (`Ctrl+Shift+P`).

**Combinando Claude com GitLab:**

Aqui a combinação fica poderosa. Você abre um merge request na extensão GitLab, vê quais arquivos foram modificados, seleciona o conteúdo alterado e pede para Claude:

```
> "Esse é o código que foi modificado neste merge request. Explica o que mudou e quais podem ser os impactos dessas mudanças."        
```

Claude analisa o diff e entrega uma explicação que qualquer profissional entende, mesmo sem saber programar.

**Passo 6: Crie sua Primeira Skill Sem Escrever Código**

Skills são instruções reutilizáveis que ensinam Claude a executar tarefas específicas do seu projeto de forma padronizada. E a melhor parte: você não precisa escrever código para criar uma.

No painel do Claude Code, digite:

```
> "Crie uma skill chamada revisar-pipeline que sempre que eu acionar, analisa os arquivos de pipeline do projeto e me retorna um relatório com status, possíveis erros e sugestões de melhoria em português."        
```

Claude vai criar automaticamente a estrutura de pastas .claude/skills/revisar-pipeline/ com o arquivo SKILL.md configurado e pronto para uso.

**Como usar a skill criada:**

Você não precisa importar, instalar ou configurar nada. Para acionar a skill, basta digitar no painel do Claude:

```
> /revisar-pipeline        
```

Claude carrega as instruções da skill e executa a tarefa exatamente como você definiu. Toda vez. Com o mesmo padrão.

Se quiser ver todas as skills disponíveis no projeto, digite /init no painel. Claude lista tudo que está configurado e disponível para uso imediato.

Tempestade não precisa reaprender a invocar um raio a cada missão. Ela calibrou o poder uma vez e aciona quando precisa.

**O Que Você Passa a Conseguir Fazer**

Depois de configurar esse ambiente, a relação com times de engenharia muda completamente.

Você consegue entrar em qualquer repositório do time e entender o que está lá sem depender de ninguém para explicar. Consegue revisar merge requests com entendimento real do impacto das mudanças. Consegue identificar problemas em pipelines sem precisar chamar um engenheiro para decifrar os logs. Consegue propor melhorias de documentação, tratamento de erros e organização de código descrevendo em linguagem natural o que quer.

Tempestade não precisou aprender a voar para controlar o clima. Ela precisou entender quais poderes tinha e quando usá-los.

O próximo passo é simples: abra o repositório do seu time hoje, clique no ícone de faísca e faça a primeira pergunta. Claude já leu o projeto. Agora é só conversar.

### Referências

- *Anthropic. Use Claude Code in VS Code.* [*https://code.claude.com/docs/en/vs-code*](https://code.claude.com/docs/en/vs-code*)
- *GitLab. GitLab for VS Code Extension.* [*https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/*](https://docs.gitlab.com/editor_extensions/visual_studio_code/*)
- *Anthropic. Claude Code for VS Code — Visual Studio Marketplace.* [*https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code*](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code*)
- *Anthropic. Plans & Pricing.* [*https://claude.com/pricing*](https://claude.com/pricing*)
