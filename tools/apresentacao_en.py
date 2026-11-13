# -*- coding: utf-8 -*-
"""Gera a versao em ingles da apresentacao a partir da portuguesa.

    python tools/apresentacao_en.py

Origem: static/apresentacao/custo-de-agentes/index.html (portugues, a fonte).
Destino: static/apresentacao/agent-cost/index.html (ingles, gerado).

A versao em ingles nao e editada a mao: qualquer ajuste entra na portuguesa e este
script e executado de novo. Cada trecho traduzido precisa existir na origem; se a
portuguesa mudar e um trecho deixar de existir, o script para e aponta qual, em vez
de publicar uma tela meio traduzida. No fim, recusa a saida se ainda houver texto
em portugues.

A apresentacao em ingles tem endereco e canal de transmissao proprios, para que uma
sessao nao interfira na outra; a chave da apresentadora e a mesma.
"""
from __future__ import annotations

import pathlib
import re
import shutil
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
ORIGEM = RAIZ / "static" / "apresentacao" / "custo-de-agentes"
DESTINO = RAIZ / "static" / "apresentacao" / "agent-cost"

# (portugues, ingles). Aplicados em ordem; cada um precisa ocorrer na origem.
TRAD = [
    # cabecalho, formatos e canal
    ('<html lang="pt-BR">', '<html lang="en">'),
    ("<title>Quanto custa um agente de IA?</title>", "<title>What does an AI agent cost?</title>"),
    ('id="ant">Anterior</button>', 'id="ant">Back</button>'),
    ('id="prox">Avançar</button>', 'id="prox">Next</button>'),
    ('(i + 1) + " de " + telas.length', '(i + 1) + " of " + telas.length'),
    ('"https://julianamarialop.github.io/apresentacao/custo-de-agentes/"', '"https://julianamarialop.github.io/apresentacao/agent-cost/"'),
    ('"jml/apresentacao/custo-de-agentes/c3afb6c601ebe883"', '"jml/apresentacao/agent-cost/7655dbef4bfb5d72"'),
    ('new Intl.NumberFormat("pt-BR"', 'new Intl.NumberFormat("en-US"'),
    # depende do par anterior: so existe depois da troca de "pt-BR" por "en-US"
    ('return "US$ " + new Intl.NumberFormat("en-US"', 'return "$" + new Intl.NumberFormat("en-US"'),
    ("usd(v).slice(4)", "usd(v).slice(1)"),
    ("<small>US$</small>", "<small>$</small>"),
    ('"<b>Transmitindo para o público</b>"', '"<b>Broadcasting to the audience</b>"'),
    ('"Sem conexão com o público: a navegação segue manual"', '"No connection to the audience: navigation stays manual"'),
    ('"<b>Acompanhando a apresentação</b>"', '"<b>Following the presentation</b>"'),
    ('id="seguir">Acompanhar a apresentação</button>', 'id="seguir">Follow the presentation</button>'),

    # tela 1
    ('l: "O custo de um agente é uma <strong>decisão de arquitetura</strong>, não uma contagem de tokens." }',
     'l: "An agent\'s cost is an <strong>architecture decision</strong>, not a token count." }'),
    ('aria-label="QR code desta apresentação"', 'aria-label="QR code for this presentation"'),

    # tela 2: a autora
    ('{ t: "Quem conduz <em>esta conversa</em>",', '{ t: "About <em>the speaker</em>",'),
    ("<li>Mentora Imagine Cup 2026</li>", "<li>Imagine Cup 2026 Mentor</li>"),
    ('<p class="livro-ref">Autora de <b>Construindo Agentes Inteligentes</b></p>', '<p class="livro-ref">Author of <b>Building Intelligent Agents</b></p>'),

    # tela 3: os dois agentes
    ('aria-label="Animação: muitas mensagens atravessam o agente de classificação uma única vez; poucas solicitações entram no agente de resolução, que consulta três sistemas em vários passos."',
     'aria-label="Animation: many messages pass through the classification agent once; fewer requests enter the resolution agent, which checks three systems over several steps."'),
    ('<p class="nome">Agente de classificação</p>', '<p class="nome">Classification agent</p>'),
    ('<p class="nome">Agente de resolução</p>', '<p class="nome">Resolution agent</p>'),
    ("</strong>solicitações por mês</p>", "</strong>requests per month</p>"),
    ('<p class="rot">Participação no custo mensal do assistente</p>', '<p class="rot">Share of the assistant&#39;s monthly cost</p>'),
    (">Classificação ' + n1.format", ">Classification ' + n1.format"),
    (">Resolução ' + n1.format", ">Resolution ' + n1.format"),
    (">Demais componentes</li>", ">Other components</li>"),

    # tela 4: historico
    ('l: "O modelo <strong>não guarda memória</strong> entre um passo e outro. A cada passo, o agente envia novamente as instruções e <strong>todo o histórico acumulado</strong>." }',
     'l: "The model <strong>keeps no memory</strong> between steps. On every step, the agent resends the instructions and <strong>the entire accumulated history</strong>." }'),
    ('{ t: "Em dez passos, ele lê <em>mais que o dobro</em> do previsto",', '{ t: "In ten steps, it reads <em>more than double</em> the estimate",'),
    ('l: "Dez passos somam <strong>" + num(D.inflacao.total) + " tokens</strong> lidos. A estimativa simples, que considera o mesmo volume em todos os passos, prevê <strong>" + num(D.inflacao.simples) + "</strong>." }',
     'l: "Ten steps add up to <strong>" + num(D.inflacao.total) + " tokens</strong> read. The simple estimate, which assumes the same volume on every step, predicts <strong>" + num(D.inflacao.simples) + "</strong>." }'),
    ("<b>estimativa simples</b>", "<b>simple estimate</b>"),
    (">Instruções e pergunta</li>", ">Instructions and question</li>"),
    (">Histórico acumulado</li>", ">Accumulated history</li>"),
    ('<p class="rot">Tokens lidos</p>', '<p class="rot">Tokens read</p>'),
    ('<p class="sub">em dez passos</p>', '<p class="sub">in ten steps</p>'),
    ('<p class="rot">Estimativa simples</p>', '<p class="rot">Simple estimate</p>'),
    ('<p class="sub">dez vezes o primeiro passo</p>', '<p class="sub">ten times the first step</p>'),

    # tela 5: modelo adequado

    # tela 6: cache
    (">O que o agente lê em cada passo</p>", ">What the agent reads on each step</p>"),
    ('<span class="hist">Histórico</span>', '<span class="hist">History</span>'),
    ('<p class="rot">Custo mensal do agente de resolução</p>', '<p class="rot">Monthly cost of the resolution agent</p>'),

    # tela 7: passos
    ('l: "O limite de passos é uma decisão de arquitetura. De 8 para 16 passos, o custo <strong>triplica</strong>, porque o histórico lido também cresce. Altere o limite para comparar." }',
     'l: "The step limit is an architecture decision. From 8 to 16 steps, the cost <strong>triples</strong>, because the history being reread grows too. Change the limit to compare." }'),
    ('{ t: "O histórico também pode ser <em>resumido</em>",', '{ t: "The history can also be <em>summarized</em>",'),
    ('l: "Resumir o histórico entre os passos reduz o que é lido novamente. O resumo tem custo próprio: no exemplo, <strong>" + usd(D.compressor) + " por mês</strong> em um modelo de menor custo." }',
     'l: "Summarizing the history between steps reduces what is reread. The summary has its own cost: in the example, <strong>" + usd(D.compressor) + " a month</strong> on a lower cost model." }'),
    ('>Limite de passos: <b id="nPassos">', '>Step limit: <b id="nPassos">'),
    ("<span>Histórico resumido entre os passos</span>", "<span>History summarized between steps</span>"),
    ('(n === 1 ? " passo" : " passos") + (resumo ? ", com histórico resumido" : "")', '(n === 1 ? " step" : " steps") + (resumo ? ", with summarized history" : "")'),

    # tela 8: primeiro nivel
    ('l: "Todo pedido passa primeiro pelo modelo mais barato. Só os que ele <strong>não resolve</strong> seguem para o modelo mais caro. Mova a régua." }',
     'l: "Every request goes first to the cheaper model. Only the ones it <strong>cannot resolve</strong> move on to the more expensive model. Move the slider." }'),
    ('{ t: "Abaixo de " + Math.round(D.cascata.equilibrio * 100) + " em cada 100, <em>a economia se inverte</em>",',
     '{ t: "Below " + Math.round(D.cascata.equilibrio * 100) + " in every 100, <em>the saving reverses</em>",'),
    ('l: "Os pedidos não resolvidos <strong>pagam duas vezes</strong>. Se o modelo mais barato resolve menos de " + Math.round(D.cascata.equilibrio * 100) + " em cada 100, o custo sobe. A resposta dele precisa ser <strong>validada por código</strong>." }',
     'l: "Unresolved requests <strong>pay twice</strong>. If the cheaper model resolves fewer than " + Math.round(D.cascata.equilibrio * 100) + " in every 100, the cost goes up. Its answer must be <strong>validated by code</strong>." }'),
    ('<p class="rot">Custo mensal com o primeiro nível</p>', '<p class="rot">Monthly cost with the first tier</p>'),
    ('<span>O modelo mais barato resolve <b id="nCasc"></b> de cada 100 pedidos</span>', '<span>The cheaper model resolves <b id="nCasc"></b> of every 100 requests</span>'),
    ('aria-label="Custo mensal conforme a quantidade de pedidos resolvidos pelo modelo mais barato"', 'aria-label="Monthly cost by the number of requests the cheaper model resolves"'),
    (">todos os pedidos no modelo mais caro</text>", ">all requests on the more expensive model</text>"),
    ('text-anchor="middle">economia</text>', 'text-anchor="middle">savings</text>'),
    ('text-anchor="end">mais caro</text>', 'text-anchor="end">more expensive</text>'),
    ("'\">equilíbrio: ' + Math.round(C.equilibrio * 100) + \" de cada 100</text>\"", "'\">break even: ' + Math.round(C.equilibrio * 100) + \" of every 100</text>\""),
    ('dif >= 0 ? "economia de " + pct(dif) + " em relação a " + usd(C.direto) + ", com todos os pedidos no modelo mais caro" : "aumento de " + pct(-dif) + " em relação a " + usd(C.direto) + ": mais caro do que sem o primeiro nível"',
     'dif >= 0 ? "a " + pct(dif) + " saving compared with " + usd(C.direto) + ", with all requests on the more expensive model" : "a " + pct(-dif) + " increase compared with " + usd(C.direto) + ": more expensive than without the first tier"'),

    # tela 9: escada
    ('["Ponto de partida", "sem nenhum ajuste"]', '["Starting point", "no adjustments"]'),
    ('["Segunda decisão", "cache das instruções"]', '["Second decision", "instruction cache"]'),
    ('["Terceira decisão", "5 passos e histórico resumido"]', '["Third decision", "5 steps and summarized history"]'),
    ('["Quarta decisão", "primeiro nível, 60 de cada 100"]', '["Fourth decision", "first tier, 60 of every 100"]'),
    ('{ t: "Ponto de partida: <em>" + usd(ESC[0]) + " por mês</em>",', '{ t: "Starting point: <em>" + usd(ESC[0]) + " a month</em>",'),
    ('l: "O agente de resolução <strong>sem nenhum ajuste</strong>: " + num(AG.volume) + " pedidos por mês, " + AG.passos + " passos e todas as instruções lidas a preço integral." }',
     'l: "The resolution agent <strong>with no adjustments</strong>: " + num(AG.volume) + " requests a month, " + AG.passos + " steps, and all instructions read at full price." }'),
    ('{ t: "Com o cache, <em>" + usd(ESC[1]) + "</em>",', '{ t: "With caching, <em>" + usd(ESC[1]) + "</em>",'),
    ('l: "As instruções fixas passam a ser <strong>lidas do cache</strong>, em todos os passos." }', 'l: "The fixed instructions are now <strong>read from the cache</strong> on every step." }'),
    ('{ t: "Com 5 passos e histórico resumido, <em>" + usd(ESC[2]) + "</em>",', '{ t: "With 5 steps and summarized history, <em>" + usd(ESC[2]) + "</em>",'),
    ('l: "O agente passa a ter <strong>limite de 5 passos</strong>, e o histórico é <strong>resumido</strong> entre um passo e outro." }',
     'l: "The agent now has a <strong>5 step limit</strong>, and the history is <strong>summarized</strong> between steps." }'),
    ('{ t: "Somadas, as decisões reduzem o custo <em>a um nono</em>",', '{ t: "Combined, the decisions cut the cost <em>to one ninth</em>",'),
    ('l: "Com o modelo mais barato resolvendo <strong>60 de cada 100 pedidos</strong>. O limite de passos e essa parcela dependem da tarefa e devem ser medidos em um piloto." }',
     'l: "With the cheaper model resolving <strong>60 of every 100 requests</strong>. The step limit and that share depend on the task and should be measured in a pilot." }'),
    ("'<div class=\"final\" id=\"final\"><p class=\"grande\">De <b>' + centavos(ESC[0]) + \" centavos</b> para <b>\" + centavos(ESC[3]) + \" centavos</b> por pedido resolvido.</p>\"",
     "'<div class=\"final\" id=\"final\"><p class=\"grande\">From <b>' + centavos(ESC[0]) + \" cents</b> to <b>\" + centavos(ESC[3]) + \" cents</b> per resolved request.</p>\""),
    ('"<p>E quanto custa esse mesmo atendimento feito por uma pessoa?</p></div>"', '"<p>And what does the same service cost when a person does it?</p></div>"'),

    # tela 10: o livro
    ('{ t: "O cálculo está aqui. <em>O método está no livro.</em>",', '{ t: "The math is here. <em>The method is in the book.</em>",'),
    ('l: "<strong>Construindo Agentes Inteligentes</strong>: Skills, Automação e Economia de Tokens. Esta apresentação mostra o cálculo; o livro apresenta o método." }',
     'l: "<strong>Building Intelligent Agents</strong>: Skills, Automation, and Token Economics. This presentation shows the math; the book presents the method." }'),
    ('<img src="capa-pt.jpg" alt="Capa do livro Construindo Agentes Inteligentes" width="560" height="831">',
     '<img src="capa-en.jpg" alt="Cover of the book Building Intelligent Agents" width="560" height="838">'),
    ("""'<p class="rot">Edição em português</p><div class="links3">' +
      '<a class="dest sem-toque" href="https://loja.uiclap.com/titulo/ua177496" target="_blank" rel="noopener">Impresso</a>' +
      '<a class="dest sem-toque" href="https://www.amazon.com.br/dp/B0H1BPJ1L6" target="_blank" rel="noopener">Kindle</a>' +
      '<a class="dest sem-toque" href="https://a.co/d/0c4r76Nb" target="_blank" rel="noopener">Amazon</a></div>' +
      '<p class="rot">English edition</p><div class="links3">' +
      '<a class="sem-toque" href="https://loja.uiclap.com/titulo/ua205923" target="_blank" rel="noopener">Print</a>' +
      '<a class="sem-toque" href="https://www.amazon.com.br/dp/B0HLFMLG8C" target="_blank" rel="noopener">Kindle</a>' +
      '<a class="sem-toque" href="https://a.co/d/0eeBrlXg" target="_blank" rel="noopener">Amazon</a></div></div></div>' +""",
     """'<p class="rot">English edition</p><div class="links3">' +
      '<a class="dest sem-toque" href="https://loja.uiclap.com/titulo/ua205923" target="_blank" rel="noopener">Print</a>' +
      '<a class="dest sem-toque" href="https://www.amazon.com.br/dp/B0HLFMLG8C" target="_blank" rel="noopener">Kindle</a>' +
      '<a class="dest sem-toque" href="https://a.co/d/0eeBrlXg" target="_blank" rel="noopener">Amazon</a></div>' +
      '<p class="rot">Portuguese edition</p><div class="links3">' +
      '<a class="sem-toque" href="https://loja.uiclap.com/titulo/ua177496" target="_blank" rel="noopener">Print</a>' +
      '<a class="sem-toque" href="https://www.amazon.com.br/dp/B0H1BPJ1L6" target="_blank" rel="noopener">Kindle</a>' +
      '<a class="sem-toque" href="https://a.co/d/0c4r76Nb" target="_blank" rel="noopener">Amazon</a></div></div></div>' +"""),
    ("'<a class=\"sem-toque\" href=\"/custo-de-agentes/\">Calculadora</a>'", "'<a class=\"sem-toque\" href=\"/en/agent-cost/\">Calculator</a>'"),
    ('rel="noopener">Código aberto</a>', 'rel="noopener">Open source code</a>'),
    ('rel="noopener">Juliana Maria Lopes no LinkedIn</a>', 'rel="noopener">Juliana Maria Lopes on LinkedIn</a>'),

    # estrutura em tres partes: historia, quatro decisoes, raciocinio
    ('var PARTES = ["Engenharia de agentes de IA", "A história", "Quatro decisões", "O raciocínio", "A conversa"];',
     'var PARTES = ["AI agent engineering", "The story", "Four decisions", "The reasoning", "The conversation"];'),
    ('{ t: "Por que o custo da IA <em>sai tão alto?</em>",',
     '{ t: "Why is the AI bill <em>so high?</em>",'),
    ('l: "Mais de 25 anos em <strong>IA, Dados e Analytics</strong>, com foco em <strong>Azure, Databricks e IA</strong>." }',
     'l: "More than 25 years in <strong>AI, Data and Analytics</strong>, focused on <strong>Azure, Databricks and AI</strong>." }'),
    ('{ t: "Um agente atende muito e <em>custa pouco</em>",',
     '{ t: "One agent works a lot and <em>costs little</em>",'),
    ('l: "O agente de classificação recebe <strong>" + num(CL.volume) + " mensagens por mês</strong> e lê cada uma <strong>uma única vez</strong>." }',
     'l: "The classification agent gets <strong>" + num(CL.volume) + " messages a month</strong> and reads each one <strong>only once</strong>." }'),
    ('{ t: "Outro atende pouco e <em>custa muito</em>",',
     '{ t: "Another works less and <em>costs a lot</em>",'),
    ('l: "O agente de resolução recebe <strong>" + num(AG.volume) + " pedidos</strong> e consulta pedidos, entrega e política em <strong>" + AG.passos + " passos</strong>." }',
     'l: "The resolution agent gets <strong>" + num(AG.volume) + " requests</strong> and checks orders, shipping and policy in <strong>" + AG.passos + " steps</strong>." }'),
    ('{ t: "Por que o que atende menos <em>custa mais?</em>",',
     '{ t: "Why does the one that works less <em>cost more?</em>",'),
    ('l: "O agente com <strong>menos pedidos</strong> responde por <strong>" + Math.round(D.participacao.agente) + "% do custo</strong>." }',
     'l: "The agent with <strong>fewer requests</strong> is <strong>" + Math.round(D.participacao.agente) + "% of the cost</strong>." }'),
    ('{ t: "A cada passo, o agente relê <em>tudo novamente</em>",',
     '{ t: "On every step, the agent reads <em>everything again</em>",'),
    ('l: "O modelo <strong>não guarda memória</strong> entre os passos. Por isso, o agente reenvia as instruções e <strong>todo o histórico</strong> a cada passo." }',
     'l: "The model <strong>has no memory</strong> between steps. So on every step, the agent sends the instructions and <strong>the full history</strong> again." }'),
    ('>Instruções</li>',
     '>Instructions</li>'),
    ('>Histórico</li>',
     '>History</li>'),
    ('>Resumo</li>',
     '>Summary</li>'),
    ('<p class="rot ad-r">Custo por mês</p>',
     '<p class="rot ad-r">Cost per month</p>'),
    ('{ t: "Decisão 1: tarefa simples, <em>modelo pequeno</em>",',
     '{ t: "Decision 1: simple task, <em>small model</em>",'),
    ('l: "Classificar uma mensagem é simples. No modelo grande, o custo seria <strong>mais de três vezes maior</strong>, sem ganho na resposta." }',
     'l: "Sorting a message is simple. On the big model, it would cost <strong>more than three times as much</strong>, with no better answer." }'),
    ('{ t: "Tarefa difícil, <em>modelo grande</em>",',
     '{ t: "Hard task, <em>big model</em>",'),
    ('l: "Resolver o pedido exige decisões em vários passos, e <strong>um erro compromete os passos seguintes</strong>. Nesse caso, o modelo grande é o adequado." }',
     'l: "Solving the request takes decisions over many steps, and <strong>one mistake breaks the next steps</strong>. Here, the big model is the right one." }'),
    ('>Tarefa simples<small>classificar a mensagem</small></span>',
     '>Simple task<small>sort the message</small></span>'),
    ('>Tarefa difícil<small>resolver o pedido</small></span>',
     '>Hard task<small>solve the request</small></span>'),
    ("'Modelo pequeno</span></div>'",
     "'Small model</span></div>'"),
    ("'Modelo grande</span></div>'",
     "'Big model</span></div>'"),
    ('"no modelo grande", CL.custo, "no modelo pequeno"',
     '"on the big model", CL.custo, "on the small model"'),
    ('{ t: "Decisão 2: o que se repete <em>vem do cache</em>",',
     '{ t: "Decision 2: what repeats <em>comes from the cache</em>",'),
    ('l: "As instruções do agente são <strong>as mesmas em todos os passos</strong>. Sem cache, elas são pagas a preço integral em cada passo." }',
     'l: "The agent\'s instructions are <strong>the same on every step</strong>. Without a cache, you pay full price for them on every step." }'),
    ('{ t: "Com o cache, o custo cai <em>para menos da metade</em>",',
     '{ t: "With the cache, the cost drops <em>to less than half</em>",'),
    ('l: "A parte que se repete passa a ser lida por <strong>um décimo do preço</strong>." }',
     'l: "The repeated part is read at <strong>one tenth of the price</strong>." }'),
    ('id="fixa">Instruções</span>',
     'id="fixa">Instructions</span>'),
    ('? "Instruções lidas do cache" : "Instruções"',
     '? "Instructions from the cache" : "Instructions"'),
    ('"sem cache", AG.custo, "com cache"',
     '"without cache", AG.custo, "with cache"'),
    ('{ t: "Decisão 3: <em>menos passos</em>",',
     '{ t: "Decision 3: <em>fewer steps</em>",'),
    ('l: "Cada passo novo relê um histórico maior. <strong>Limitar os passos</strong> limita o custo." }',
     'l: "Each new step reads a longer history. <strong>Fewer steps</strong> means a lower cost." }'),
    ('{ t: "E um histórico <em>resumido</em>",',
     '{ t: "And a <em>shorter history</em>",'),
    ('l: "Entre um passo e outro, o histórico é <strong>resumido</strong>. Com 5 passos, cada passo lê muito menos." }',
     'l: "Between steps, the history is <strong>summarized</strong>. With 5 steps, each step reads much less." }'),
    ('"8 passos", D.escada[2], "5 passos e resumo"',
     '"8 steps", D.escada[2], "5 steps and summary"'),
    ('{ t: "Decisão 4: o modelo <em>mais barato primeiro</em>",',
     '{ t: "Decision 4: the <em>cheaper model first</em>",'),
    ('l: "O modelo pequeno tenta primeiro. Só o que ele <strong>não resolve</strong> segue para o modelo grande." }',
     'l: "The small model tries first. Only what it <strong>cannot solve</strong> goes to the big model." }'),
    ('<span>Modelo pequeno<small>resolve 60 de cada 100 pedidos</small></span>',
     '<span>Small model<small>solves 60 of every 100 requests</small></span>'),
    ('>↓ seguem 40 de cada 100</p>',
     '>↓ 40 of every 100 move up</p>'),
    ('<span>Modelo grande<small>resolve o restante</small></span>',
     '<span>Big model<small>solves the rest</small></span>'),
    ('"tudo no modelo grande", D.cascata.curva[60], "o pequeno primeiro"',
     '"all on the big model", D.cascata.curva[60], "small model first"'),
    ('{ t: "Por que funciona: o histórico <em>cresce a cada passo</em>",',
     '{ t: "Why it works: the history <em>grows on every step</em>",'),
    ('{ t: "O limite de passos <em>em detalhe</em>",',
     '{ t: "The step limit <em>in detail</em>",'),
    ('{ t: "O limite do modelo <em>mais barato primeiro</em>",',
     '{ t: "The limit of the <em>cheaper model first</em>",'),
    ('{ t: "E os seus <em>agentes?</em>",',
     '{ t: "And your <em>agents?</em>",'),
    ('l: "Quantos passos eles executam? O cache está ativo? Quanto custa cada pedido resolvido?" }',
     'l: "How many steps do they take? Is the cache on? What does each resolved request cost?" }'),
]

# Sinais de portugues que nao podem sobrar no texto visivel do resultado.
RESIDUO = re.compile(r"[ãõçÃÕÇ]|\b(?:de cada|por mês|solicitaç|pedidos?|decisão|histórico|modelo de|custo|Avançar|Anterior|dólares|centavos)\b")


def main() -> int:
    # Um apostrofo do ingles ("agent's") so e seguro dentro de string JavaScript entre
    # aspas duplas (titulos, legendas e textos do codigo). Nos trechos de HTML, que estao
    # entre aspas simples, ele quebra o script e todas as telas saem vazias: use &#39;.
    for pt, en in TRAD:
        if en.count("'") > pt.count("'") and not re.match(r'(\{ t: |l: |\? |dif )', pt):
            print("apostrofo fora de string entre aspas duplas; use &#39;: " + en[:90])
            return 1
    t = (ORIGEM / "index.html").read_text(encoding="utf-8")
    faltam = []
    for pt, en in TRAD:
        if pt not in t:
            faltam.append(pt[:90])
            continue
        t = t.replace(pt, en)
    if faltam:
        print("trechos que nao existem mais na versao portuguesa (atualize TRAD):")
        for f in faltam:
            print("  " + f)
        return 1
    # So o texto visivel interessa: comentarios e nomes de variaveis seguem em portugues.
    visivel = re.sub(r"/\*.*?\*/|<!--.*?-->|^\s*//.*$", "", t, flags=re.S | re.M)
    visivel = "\n".join(re.findall(r'"[^"\n]*"|\'[^\'\n]*\'|>[^<\n]+<', visivel))
    sobra = sorted({m.group(0) for m in RESIDUO.finditer(visivel)})
    if sobra:
        print("texto em portugues ainda presente na saida: " + ", ".join(sobra))
        for linha in visivel.splitlines():
            if RESIDUO.search(linha):
                print("  " + linha[:140])
        return 1
    DESTINO.mkdir(parents=True, exist_ok=True)
    (DESTINO / "index.html").write_text(t, encoding="utf-8", newline="\n")
    for nome in ("autora.jpg", "capa-en.jpg"):
        shutil.copy2(ORIGEM / nome, DESTINO / nome)
    limpar = (ORIGEM / "limpar.html").read_text(encoding="utf-8")
    limpar = limpar.replace("jml/apresentacao/custo-de-agentes/c3afb6c601ebe883", "jml/apresentacao/agent-cost/7655dbef4bfb5d72")
    limpar = limpar.replace('lang="pt-BR"', 'lang="en"').replace("Encerrar transmissão", "End broadcast")
    limpar = limpar.replace("Encerrando a transmissão da apresentação...", "Ending the presentation broadcast...")
    limpar = limpar.replace('"Transmissão encerrada em " + feitos + " de 3 servidores."', '"Broadcast ended on " + feitos + " of 3 servers."')
    (DESTINO / "limpar.html").write_text(limpar, encoding="utf-8", newline="\n")
    print("versao em ingles gerada em %s" % DESTINO)
    return 0


if __name__ == "__main__":
    sys.exit(main())
