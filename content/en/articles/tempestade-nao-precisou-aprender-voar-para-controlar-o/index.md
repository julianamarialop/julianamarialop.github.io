---
title: "Storm Didn't Have to Learn to Fly to Control the Weather: How to Use VS Code with Claude Without Being a Developer"
slug: "storm-didnt-learn-to-fly-vs-code-with-claude-without-being-a-developer"
date: 2026-04-16T11:30:00Z
summary: "There's a belief in the data world that few people question: the IDE is developer territory. VS Code, with its folders, files, and terminal, would be a hostile environment for anyone who doesn't write code every day."
tags: ["Claude", "Data Engineering", "Costs"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/tempestade-n%C3%A3o-precisou-aprender-voar-para-controlar-o-lopes-efwdf"
cover:
  image: cover.jpg
  alt: "Storm Didn't Have to Learn to Fly to Control the Weather: How to Use VS Code with Claude Without Being a Developer"
  relative: true
---

### The Myth of the Technical Barrier

There's a belief in the data world that few people question: the IDE is developer territory. VS Code, with its folders, files, and terminal, would be a hostile environment for anyone who doesn't write code every day.

Storm never believed in barriers like that.

When she goes into battle, she doesn't need to understand atmospheric physics to summon lightning. She doesn't calculate air pressure or electrical resistance before acting. She knows what powers she has, knows when to trigger them, and trusts the right combination to deliver the result. The deep technical knowledge exists underneath, but it isn't what she needs to operate.

With two VS Code extensions, Claude Code and GitLab, any data professional can work on real projects, understand code, propose changes, follow pipelines, and collaborate with engineering teams, without writing a single line of code.

This article is the manual Storm would hand to any recruit before heading into the field.

### Why VS Code and Not Claude.ai?

That's the first question that comes up. After all, claude.ai is already in the browser, already answers questions about code, and already helps analyze files. Why install a different program?

The answer lies in the difference between asking for advice over the phone and having the expert sitting next to you, looking at the same screen.

In claude.ai, you copy a snippet of code, paste it into the conversation, and Claude answers. It works, but it has serious limits: you have to manually copy whatever you want analyzed, Claude doesn't see the whole project, doesn't know how the files relate to each other, and can't make real changes to the files.

In VS Code with Claude Code, Claude **lives inside the project**. It reads all the folders and files at once, understands how the components connect, makes real changes directly in the files, and saves them. You don't copy anything. You point and ask.

It's the difference between describing a pipeline problem to someone who has never seen the project and sitting down with an expert who has already read every file before the meeting starts.

For anyone working on data projects that involve dozens of files, interconnected pipelines, and repositories shared with engineering teams, that difference is what makes VS Code the right environment.

### Before You Start: What You Need

Before installing any extension, check that you have the following:

**VS Code installed.** Go to [code.visualstudio.com](http://code.visualstudio.com) and download the version for your operating system. Installation is simple and free.

**A Claude account on the Pro plan or higher.** Claude Code isn't available on the free plan. You need a Pro ($20/month), Max, Team, or Enterprise plan. If you don't have one yet, go to [claude.ai/pricing](http://claude.ai/pricing) to subscribe.

**Node.js installed.** Claude Code needs Node.js to run. Go to [nodejs.org](http://nodejs.org), download the LTS version, and install it. You don't need to know how to use it, just have it installed on your machine.

**A GitLab account.** If your team uses GitLab, you already have one. If not, go to [gitlab.com](http://gitlab.com) and create a free account.

With these four items ready, you're equipped to start.

### What You'll Be Able to Do

With the **Claude Code** extension from [Anthropic](https://www.linkedin.com/company/anthropicresearch/) you can open any file in a project, ask Claude to explain what that code does in plain language, request changes by describing what you want in your own language, ask for documentation, identify problems, and understand the structure of the whole project without having to read every file manually.

With the **GitLab** extension you can see the project's issues directly in VS Code, follow the status of CI/CD pipelines in real time, review merge requests, leave comments, and approve changes, all without opening the browser.

Together, these two extensions turn VS Code into a complete workspace for any professional who needs to collaborate with engineering teams or understand technical projects.

**Step 1: Install the Extensions**

Open VS Code. In the left sidebar, click the icon that looks like four squares (or press Ctrl+Shift+X on Windows or Cmd+Shift+X on Mac). This opens the extensions marketplace.

**Installing Claude Code:**

In the search field, type Claude Code. Look for the extension published by **Anthropic** with more than 2 million installs. Click **Install**.

After installation, a spark icon (Spark) will appear in the left sidebar. Click it. The first time, an authentication screen will appear. Click **Sign in**, authorize in the browser, and come back to VS Code. You're connected.

**Installing GitLab:**

In the same search field, type GitLab Workflow. Look for the extension published by **GitLab** with the fox icon. Click **Install**.

After installation, you'll need to connect your GitLab account. Click the fox icon in the sidebar. The extension will ask for a GitLab **Personal Access Token**. To generate one:

1. Go to your GitLab
2. Go to **Settings → Access Tokens**
3. Create a token with the api and read\_user scopes
4. Copy the token and paste it into the extension

Done. Both extensions are installed and configured.

**Step 2: Open a Project**

To work on an existing project, go to **File → Open Folder** and navigate to the project folder on your computer. If the project is on GitLab and you don't have it locally yet, use **File → New Window**, then Ctrl+Shift+P to open the command palette and type Git: Clone. Paste the GitLab repository URL and choose where to save it.

When VS Code opens the project folder, the GitLab extension will automatically recognize the repository and start showing information in the sidebar.

Storm doesn't need to build the battlefield. She walks into it as it is and directs the elements around her.

**Step 3: Use Claude to Understand the Project**

Click the spark icon in the sidebar to open the Claude Code panel. This is where the technical barrier disappears.

**Understanding the project structure:**

In the Claude panel, type:

```
> "Explique a estrutura deste projeto em português. Quais são as pastas principais, o que cada uma contém e como os componentes se relacionam?"        
```

Claude will read the entire project and give you an explanation in plain language, without unnecessary jargon.

**Understanding a specific file:**

Open any file in the editor. In the Claude panel, use @ to reference the file by name and ask:

```
> "@pipeline_vendas.py O que esse arquivo faz? Explica cada parte em linguagem simples."        
```

Claude reads the file with the full context of the project and explains each block clearly.

**Identifying problems:**

```
> "Analise os arquivos de pipeline neste projeto e me diga se há algum padrão que poderia causar problemas de performance ou falhas."        
```

Claude will read the relevant files, compare them against best practices, and deliver a diagnosis in accessible language.

**Step 4: Ask for Changes Without Writing Code**

This is where the impact becomes most obvious. You don't need to know Python, SQL, or any other language to propose and apply changes to a project.

**Examples of requests that work:**

```
> "Adicione um comentário explicativo no início de cada função do arquivo @utils.py descrevendo o que ela faz."        
```
```
> "Esse arquivo está sem tratamento de erros. Adicione mensagens de erro claras para os casos onde a conexão com o banco de dados falha."        
```
```
> "Crie um arquivo README.md na pasta raiz explicando o que este projeto faz, como está estruturado e quais são os principais pipelines."        
```

When Claude suggests a change, it shows up as a **visual diff** in the editor: what's going to be removed is marked in red, what's going to be added in green. You review it, approve it with a click, or ask for an adjustment before accepting.

Storm doesn't build the lightning bolt by hand. She says where she wants it to strike and watches the result before confirming.

**Step 5: Use GitLab to Follow Along and Collaborate**

With the GitLab extension active, the sidebar shows everything you need about the project without leaving VS Code.

**Following issues:**

Click the fox icon in the sidebar. Expand **Issues and Merge Requests**. You'll see all of the project's open issues with title, status, and assignee. Click any issue to read the full description directly in VS Code.

**Monitoring pipelines:**

In VS Code's bottom bar, the GitLab extension shows the pipeline status for the current branch in real time: running, passed, or failed. Click the status to see the details of each job.

**Reviewing and approving merge requests:**

In the extension's Merge Requests section, you'll see all the open MRs. Click any of them to see the diff of the changes, leave comments on specific lines, and approve using the GitLab: Approve Merge Request command in the command palette (`Ctrl+Shift+P`).

**Combining Claude with GitLab:**

This is where the combination gets powerful. You open a merge request in the GitLab extension, see which files were modified, select the changed content, and ask Claude:

```
> "Esse é o código que foi modificado neste merge request. Explica o que mudou e quais podem ser os impactos dessas mudanças."        
```

Claude analyzes the diff and delivers an explanation any professional can understand, even without knowing how to program.

**Step 6: Create Your First Skill Without Writing Code**

Skills are reusable instructions that teach Claude to carry out tasks specific to your project in a standardized way. And the best part: you don't need to write code to create one.

In the Claude Code panel, type:

```
> "Crie uma skill chamada revisar-pipeline que sempre que eu acionar, analisa os arquivos de pipeline do projeto e me retorna um relatório com status, possíveis erros e sugestões de melhoria em português."        
```

Claude will automatically create the folder structure .claude/skills/revisar-pipeline/ with the SKILL.md file configured and ready to use.

**How to use the skill you created:**

You don't need to import, install, or configure anything. To trigger the skill, just type in the Claude panel:

```
> /revisar-pipeline        
```

Claude loads the skill's instructions and carries out the task exactly as you defined it. Every time. With the same standard.

If you want to see all the skills available in the project, type /init in the panel. Claude lists everything that's configured and available for immediate use.

Storm doesn't need to relearn how to summon lightning on every mission. She calibrated the power once and triggers it when she needs it.

**What You'll Be Able to Do From Now On**

Once this environment is set up, your relationship with engineering teams changes completely.

You can walk into any of the team's repositories and understand what's there without depending on anyone to explain it. You can review merge requests with a real understanding of the impact of the changes. You can spot problems in pipelines without having to call an engineer to decipher the logs. You can propose improvements to documentation, error handling, and code organization by describing what you want in natural language.

Storm didn't have to learn to fly to control the weather. She had to understand what powers she had and when to use them.

The next step is simple: open your team's repository today, click the spark icon, and ask the first question. Claude has already read the project. Now all you have to do is talk.

### References

- *Anthropic. Use Claude Code in VS Code.* [*https://code.claude.com/docs/en/vs-code*](https://code.claude.com/docs/en/vs-code*)
- *GitLab. GitLab for VS Code Extension.* [*https://docs.gitlab.com/editor\_extensions/visual\_studio\_code/*](https://docs.gitlab.com/editor_extensions/visual_studio_code/*)
- *Anthropic. Claude Code for VS Code: Visual Studio Marketplace.* [*https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code*](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code*)
- *Anthropic. Plans & Pricing.* [*https://claude.com/pricing*](https://claude.com/pricing*)
