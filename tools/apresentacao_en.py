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
    ('<p class="sobre">Engenharia de agentes de IA</p>', '<p class="sobre">AI agent engineering</p>'),
    ('id="ant">Anterior</button>', 'id="ant">Back</button>'),
    ('id="prox">Avançar</button>', 'id="prox">Next</button>'),
    ('(i + 1) + " de " + telas.length', '(i + 1) + " of " + telas.length'),
    ('"https://julianamarialop.github.io/apresentacao/custo-de-agentes/"', '"https://julianamarialop.github.io/apresentacao/agent-cost/"'),
    ('"jml/apresentacao/custo-de-agentes/c3afb6c601ebe883"', '"jml/apresentacao/agent-cost/7655dbef4bfb5d72"'),
    ('new Intl.NumberFormat("pt-BR"', 'new Intl.NumberFormat("en-US"'),
    ('return "US$ " + new Intl.NumberFormat("en-US"', 'return "$" + new Intl.NumberFormat("en-US"'),
    ("usd(v).slice(4)", "usd(v).slice(1)"),
    ("<small>US$</small>", "<small>$</small>"),
    ("<b>US$ ' + D.modelos", "<b>$' + D.modelos"),
    ('"<b>Transmitindo para o público</b>"', '"<b>Broadcasting to the audience</b>"'),
    ('"Sem conexão com o público: a navegação segue manual"', '"No connection to the audience: navigation stays manual"'),
    ('"<b>Acompanhando a apresentação</b>"', '"<b>Following the presentation</b>"'),
    ('id="seguir">Acompanhar a apresentação</button>', 'id="seguir">Follow the presentation</button>'),

    # tela 1
    ('{ t: "Quanto custa um <em>agente de IA?</em>",', '{ t: "What does an <em>AI agent cost?</em>",'),
    ('l: "O custo de um agente é uma <strong>decisão de arquitetura</strong>, não uma contagem de tokens." }',
     'l: "An agent\'s cost is an <strong>architecture decision</strong>, not a token count." }'),
    ('aria-label="QR code desta apresentação"', 'aria-label="QR code for this presentation"'),

    # tela 2: a autora
    ('{ t: "Quem conduz <em>esta conversa</em>",', '{ t: "About <em>the speaker</em>",'),
    ('l: "Mais de 25 anos em <strong>Inteligência Artificial, Dados e Analytics</strong>, com atuação em arquitetura de soluções e modernização de plataformas, em especial <strong>Azure, Databricks e IA</strong>." }',
     'l: "More than 25 years in <strong>Artificial Intelligence, Data and Analytics</strong>, working on solution architecture and platform modernization, especially <strong>Azure, Databricks and AI</strong>." }'),
    ("<li>Mentora Imagine Cup 2026</li>", "<li>Imagine Cup 2026 Mentor</li>"),
    ('<p class="livro-ref">Autora de <b>Construindo Agentes Inteligentes</b></p>', '<p class="livro-ref">Author of <b>Building Intelligent Agents</b></p>'),

    # tela 3: os dois agentes
    ('{ t: "Um agente atende " + num(CL.volume) + " solicitações e custa <em>" + num(CL.custo) + " dólares</em>",',
     '{ t: "One agent serves " + num(CL.volume) + " requests and costs <em>" + usd(CL.custo) + "</em>",'),
    ('l: "O agente de classificação recebe <strong>" + num(CL.volume) + " mensagens por mês</strong>. Cada mensagem passa por ele <strong>uma única vez</strong>." }',
     'l: "The classification agent receives <strong>" + num(CL.volume) + " messages a month</strong>. Each message passes through it <strong>only once</strong>." }'),
    ('{ t: "Outro atende " + num(AG.volume) + " e custa <em>" + num(AG.custo) + " dólares</em>",',
     '{ t: "Another serves " + num(AG.volume) + " and costs <em>" + usd(AG.custo) + "</em>",'),
    ('l: "O agente de resolução recebe <strong>" + num(AG.volume) + " solicitações</strong>. Para responder, consulta pedidos, entrega e política em <strong>" + AG.passos + " passos</strong>, e a cada passo lê novamente todo o histórico." }',
     'l: "The resolution agent receives <strong>" + num(AG.volume) + " requests</strong>. To answer, it checks orders, shipping and policy in <strong>" + AG.passos + " steps</strong>, and on every step it rereads the entire history." }'),
    ('{ t: "O agente de menor volume responde por <em>" + Math.round(D.participacao.agente) + "% do custo</em>",',
     '{ t: "The lower volume agent accounts for <em>" + Math.round(D.participacao.agente) + "% of the cost</em>",'),
    ('l: "O agente com <strong>menos solicitações</strong> responde por <strong>" + Math.round(D.participacao.agente) + "% do custo</strong>. O que define o custo é a orquestração." }',
     'l: "The agent with <strong>fewer requests</strong> accounts for <strong>" + Math.round(D.participacao.agente) + "% of the cost</strong>. Orchestration is what sets the cost." }'),
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
    ('{ t: "O motivo: a cada passo, o agente relê <em>todo o histórico</em>",', '{ t: "The reason: on every step, the agent rereads <em>the entire history</em>",'),
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
    ('{ t: "Primeira decisão: cada papel no <em>modelo adequado</em>",', '{ t: "First decision: the right model <em>for each role</em>",'),
    ('l: "A classificação é uma tarefa simples. No modelo de maior capacidade, custaria <strong>mais de três vezes</strong> o valor, sem ganho na resposta." }',
     'l: "Classification is a simple task. On the most capable model it would cost <strong>more than three times</strong> as much, with no gain in the answer." }'),
    ('{ t: "O menor preço nem sempre é <em>o modelo adequado</em>",', '{ t: "The lowest price is not always <em>the right model</em>",'),
    ('l: "A resolução decide quais sistemas consultar e o que fazer com cada resultado. No modelo de menor custo o valor cai, mas <strong>um erro em um passo compromete os seguintes</strong>." }',
     'l: "Resolution decides which systems to check and what to do with each result. On the lowest cost model the cost drops, but <strong>an error in one step compromises the steps that follow</strong>." }'),
    (">Preço por milhão de tokens: entrada / saída</p>", ">Price per million tokens: input / output</p>"),
    ("</b>menor custo</div>", "</b>lowest cost</div>"),
    ("</b>intermediário</div>", "</b>mid tier</div>"),
    ("</b>maior capacidade</div>", "</b>most capable</div>"),
    ("<h2>Agente de classificação</h2>", "<h2>Classification agent</h2>"),
    ("<h2>Agente de resolução</h2>", "<h2>Resolution agent</h2>"),
    ("<span>Modelo de maior capacidade<small>acima do que a tarefa exige</small></span>", "<span>Most capable model<small>more than the task requires</small></span>"),
    ("<span>Modelo de menor custo<small>adequado</small></span>", "<span>Lowest cost model<small>right fit</small></span>"),
    ("<span>Modelo de menor custo<small>abaixo do que a tarefa exige</small></span>", "<span>Lowest cost model<small>less than the task requires</small></span>"),
    ("<span>Modelo de maior capacidade<small>adequado</small></span>", "<span>Most capable model<small>right fit</small></span>"),
    (">Valores mensais, com preços de referência de três modelos Claude.</p>", ">Monthly values, using reference prices for three Claude models.</p>"),

    # tela 6: cache
    ('{ t: "Segunda decisão: ler do cache <em>o que se repete</em>",', '{ t: "Second decision: read what repeats <em>from the cache</em>",'),
    ('l: "As instruções do agente são <strong>as mesmas em todos os passos</strong>. Com o cache, essa parte fixa é lida por <strong>um décimo do preço</strong>. Ative o cache para comparar." }',
     'l: "The agent\'s instructions are <strong>the same on every step</strong>. With caching, that fixed part is read at <strong>one tenth of the price</strong>. Turn on the cache to compare." }'),
    ('{ t: "O cache só é aplicado acima de <em>um tamanho mínimo</em>",', '{ t: "The cache only applies above <em>a minimum size</em>",'),
    ('l: "Cada modelo exige um tamanho mínimo de prompt para o cache. Abaixo dele, <strong>o cache não é aplicado e a API não informa</strong>: a estimativa indica economia que não ocorre." }',
     'l: "Each model requires a minimum prompt size for caching. Below it, <strong>the cache is not applied and the API does not say so</strong>: the estimate shows a saving that never happens." }'),
    (">O que o agente lê em cada passo</p>", ">What the agent reads on each step</p>"),
    ('id="fixa">Instruções fixas · \' + num(AG.prefixo) + \' tokens</span>', 'id="fixa">Fixed instructions · \' + num(AG.prefixo) + \' tokens</span>'),
    ('<span class="hist">Histórico</span>', '<span class="hist">History</span>'),
    ("<span>Cache das instruções</span>", "<span>Instruction cache</span>"),
    ('<p class="rot">Custo mensal do agente de resolução</p>', '<p class="rot">Monthly cost of the resolution agent</p>'),
    ('<p class="rot">Modelo de menor custo</p>', '<p class="rot">Lowest cost model</p>'),
    ('<p class="rot">Modelo de maior capacidade</p>', '<p class="rot">Most capable model</p>'),
    ('<p class="sub">tokens no mínimo</p>', '<p class="sub">tokens minimum</p>'),
    ('? "Instruções fixas · lidas do cache" : "Instruções fixas · " + num(AG.prefixo) + " tokens"', '? "Fixed instructions · read from the cache" : "Fixed instructions · " + num(AG.prefixo) + " tokens"'),
    ('? "com cache: menos da metade" : "sem cache: preço integral em todos os passos"', '? "with caching: less than half" : "without caching: full price on every step"'),

    # tela 7: passos
    ('{ t: "Terceira decisão: <em>o limite de passos</em>",', '{ t: "Third decision: <em>the step limit</em>",'),
    ('l: "O limite de passos é uma decisão de arquitetura. De 8 para 16 passos, o custo <strong>triplica</strong>, porque o histórico lido também cresce. Altere o limite para comparar." }',
     'l: "The step limit is an architecture decision. From 8 to 16 steps, the cost <strong>triples</strong>, because the history being reread grows too. Change the limit to compare." }'),
    ('{ t: "O histórico também pode ser <em>resumido</em>",', '{ t: "The history can also be <em>summarized</em>",'),
    ('l: "Resumir o histórico entre os passos reduz o que é lido novamente. O resumo tem custo próprio: no exemplo, <strong>" + usd(D.compressor) + " por mês</strong> em um modelo de menor custo." }',
     'l: "Summarizing the history between steps reduces what is reread. The summary has its own cost: in the example, <strong>" + usd(D.compressor) + " a month</strong> on a lower cost model." }'),
    ('>Limite de passos: <b id="nPassos">', '>Step limit: <b id="nPassos">'),
    ("<span>Histórico resumido entre os passos</span>", "<span>History summarized between steps</span>"),
    ('(n === 1 ? " passo" : " passos") + (resumo ? ", com histórico resumido" : "")', '(n === 1 ? " step" : " steps") + (resumo ? ", with summarized history" : "")'),

    # tela 8: primeiro nivel
    ('{ t: "Quarta decisão: o modelo <em>mais barato primeiro</em>",', '{ t: "Fourth decision: the <em>cheaper model first</em>",'),
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
