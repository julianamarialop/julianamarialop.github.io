/* Calculadora de custo de agentes.
 *
 * Este arquivo nao realiza calculos. O navegador carrega o Pyodide e executa o
 * MESMO agent_cost.py do repositorio agent-cost-math, de modo que o resultado
 * da pagina e o da linha de comando sao identicos. Aqui ficam apenas a coleta
 * de entradas e a exibicao. Um calculo escrito em JavaScript seria uma segunda
 * fonte, e as duas divergiriam sem que a divergencia fosse percebida.
 *
 * A pagina e didatica: quatro etapas, um conceito por etapa, sobre o mesmo
 * exemplo (o assistente de atendimento de uma loja online). A arquitetura
 * completa fica ao final, recolhida, para aprofundamento.
 */
(function () {
  "use strict";

  var raiz = document.getElementById("acl");
  if (!raiz) return;

  var LANG = raiz.dataset.lang === "pt" ? "pt" : "en";
  var BASE = raiz.dataset.base;
  var PYODIDE = raiz.dataset.pyodide;
  var REPO = raiz.dataset.repo;

  var T = {
    pt: {
      carregando: "Carregando o ambiente Python no navegador. No primeiro acesso, são transferidos cerca de 10 MB, que permanecem em cache para os acessos seguintes.",
      lendo: "Carregando o código da calculadora e a tabela de preços.",
      semMotor: "A calculadora não está disponível nesta página no momento. O mesmo código pode ser executado localmente:",
      falhou: "Não foi possível carregar a calculadora: ",
      etapa: "Etapa",

      e1Titulo: "Uma pergunta, uma resposta",
      e1Texto: [
        "Os modelos de linguagem cobram por <strong>token</strong>, a unidade em que o texto é dividido para processamento. Em média, uma palavra corresponde a um ou dois tokens. O preço dos tokens de <strong>entrada</strong> (o texto que o modelo lê) é diferente do preço dos tokens de <strong>saída</strong> (o texto que o modelo escreve).",
        "No exemplo, a primeira etapa do assistente classifica cada mensagem recebida: status do pedido, troca ou pagamento. Cada classificação é uma única chamada ao modelo, que lê cerca de {tin} tokens (as instruções e a mensagem do cliente) e escreve {tout}."
      ],
      e1Controle: "Mensagens por mês",
      e1Porchamada: "custo por mensagem",
      e1Mensal: "custo mensal",
      e1Frase: "Nesta etapa, o custo é proporcional ao volume: o dobro de mensagens resulta no dobro do custo. Modelo: {modelo}.",

      e2Titulo: "O agente executa várias iterações",
      e2Texto: [
        "As mensagens sobre o status do pedido seguem para o agente de resolução. Para responder, ele consulta o sistema de pedidos, o rastreamento da transportadora e a política de entrega. Cada consulta corresponde a uma <strong>iteração</strong>: o modelo decide a próxima ação, recebe o resultado e decide novamente.",
        "O modelo não retém memória entre iterações. A cada iteração, o orquestrador reenvia as instruções e todo o histórico acumulado, de modo que cada iteração processa mais tokens que a anterior. O gráfico mostra os tokens de entrada de cada iteração; a linha tracejada indica o valor que a estimativa simples considera para todas elas."
      ],
      e2Controle: "Número de iterações",
      e2Tokens: "tokens de entrada por solicitação",
      e2Simples: "na estimativa simples",
      e2Mensal: "custo mensal do agente",
      e2Frase: "O agente recebe {vol} solicitações por mês e custa <strong>{custo}</strong>, {vezes} vezes o custo da classificação, que recebe {volc} mensagens. <strong>O volume não determina o custo; a orquestração determina.</strong>",
      e2Nota: "Modelo: {modelo}. O cálculo considera o reaproveitamento em cache da parte fixa das instruções, conforme os preços publicados pelo fornecedor.",
      iteracao: "iteração", tokens: "tokens",
      serieIteracao: "tokens de entrada na iteração", serieSimples: "estimativa simples",

      e3Titulo: "Cada solicitação no modelo adequado",
      e3Texto: [
        "Uma forma de reduzir o custo é encaminhar cada solicitação primeiro a um modelo de menor custo e enviar ao modelo de maior custo somente as que o primeiro não resolver. É o mesmo princípio do atendimento organizado em níveis.",
        "O arranjo reduz o custo apenas quando o primeiro modelo resolve uma parcela suficiente das solicitações, porque as não resolvidas passam pelos dois modelos. O ponto de equilíbrio é a razão entre o custo por solicitação dos dois modelos."
      ],
      e3Controle: "Parcela resolvida pelo modelo de menor custo",
      e3Primeiro: "primeiro nível", e3Segundo: "segundo nível",
      cascata: "custo com primeiro nível", direto: "custo somente com o modelo de maior custo", equilibrio: "equilíbrio",
      e3Eixo: "parcela resolvida pelo modelo de menor custo",
      e3Vale: "Com {r} das solicitações resolvidas no primeiro nível, o custo mensal é de <strong>{c}</strong>, contra <strong>{d}</strong> somente com o modelo de maior custo: <strong>redução de {s}</strong>.",
      e3NaoVale: "Com {r} das solicitações resolvidas no primeiro nível, o custo mensal é de <strong>{c}</strong>, contra <strong>{d}</strong> somente com o modelo de maior custo: <strong>aumento de {s}</strong>. Abaixo de {b}, o primeiro nível eleva o custo.",
      e3Condicao: "Condição obrigatória: a resposta do primeiro nível deve ser validada por código (formato esperado, regras de negócio ou declaração explícita de que não foi possível responder). A validação por outro modelo reintroduz o custo que o arranjo pretende evitar.",

      e4Titulo: "Conclusão: o custo do assistente",
      e4Texto: [
        "A tabela reúne os resultados das etapas anteriores e é atualizada quando eles mudam."
      ],
      e4ColItem: "", e4ColVol: "Solicitações por mês", e4ColMensal: "Custo mensal", e4ColUnit: "Custo por solicitação",
      e4Class: "Classificação (etapa 1)",
      e4Agente: "Agente de resolução (etapa 2)",
      e4Total: "Custo total do assistente",
      e4Simples: "Estimativa simples, uma chamada por solicitação",
      e4Cascata: "Com primeiro nível, {r} resolvidas (etapa 3)",
      e4Conclusao: "A estimativa simples indicaria <strong>{simples}</strong> por mês. O custo calculado a partir da arquitetura é de <strong>{total}</strong>, {vezes} vezes maior, e a diferença decorre das iterações do agente, e não do volume. Com o primeiro nível resolvendo {r} das solicitações, o custo mensal passa a <strong>{cascata}</strong>, e o custo por solicitação resolvida passa de {c2} para {c3}. <strong>Esse é o valor a comparar com o custo do mesmo atendimento realizado por uma pessoa.</strong>",
      aprofNota: "Inclui os três componentes adicionais, que as etapas 1 a 4 não consideram.",

      aprofTitulo: "Para aprofundamento: a arquitetura completa do exemplo",
      aprofTexto: "Além da classificação e do agente de resolução, o assistente completo inclui um leitor de documentos de entrega, um compressor de histórico e uma revisão por amostragem da qualidade das respostas. Os parâmetros de cada componente podem ser alterados. Ao remover o limite de iterações do agente, a calculadora recusa o cálculo, porque um componente estimado com valor zero desapareceria da proposta sem que a omissão fosse percebida.",
      componente: "Componente", papel: "Papel", chamadas: "Chamadas/mês", modelo: "Modelo", iteracoes: "Limite de iterações", cache: "Cache",
      entradaTarefa: "Entrada/solicitação", custo: "USD/mês", parte: "Participação no custo",
      total: "por mês, somente o consumo de modelos de linguagem",
      restaurar: "Restaurar o exemplo",
      recusa: "A calculadora recusa o cálculo, que é o comportamento esperado:",
      avisos: "Alertas", premissas: "Premissas declaradas",
      rodapeMotor: "As mensagens da calculadora são exibidas em inglês, idioma do código.",

      precosTitulo: "Preços utilizados",
      precosVivo: "Obtidos das fontes públicas dos fornecedores em <strong>{quando}</strong> ({idade}). O site consulta essas fontes novamente a cada dia.",
      precosMao: "<strong>Tabela de preços transcrita manualmente</strong>, verificada em {quando}. A consulta às fontes não foi concluída nesta publicação, e a página informa esse fato.",
      entrada: "entrada /1M", saida: "saída /1M", leitura: "leitura em cache /1M", escrita: "gravação em cache /1M", piso: "mínimo para cache",
      fontes: "Fontes"
    },
    en: {
      carregando: "Loading the Python environment in the browser. The first visit transfers about 10 MB, which remain cached for later visits.",
      lendo: "Loading the calculator code and the price table.",
      semMotor: "The calculator is not available on this page at the moment. The same code can be executed locally:",
      falhou: "The calculator could not be loaded: ",
      etapa: "Step",

      e1Titulo: "One question, one answer",
      e1Texto: [
        "Language models charge per <strong>token</strong>, the unit into which text is divided for processing. On average, a word corresponds to one or two tokens. <strong>Input</strong> tokens (the text the model reads) and <strong>output</strong> tokens (the text the model writes) have different prices.",
        "In the example, the assistant's first step classifies each incoming message: order status, exchange or payment. Each classification is a single model call that reads about {tin} tokens (the instructions and the customer's message) and writes {tout}."
      ],
      e1Controle: "Messages per month",
      e1Porchamada: "cost per message",
      e1Mensal: "monthly cost",
      e1Frase: "At this step, cost is proportional to volume: twice the messages result in twice the cost. Model: {modelo}.",

      e2Titulo: "The agent executes several iterations",
      e2Texto: [
        "Order status messages are forwarded to the resolution agent. To answer, it queries the order system, the carrier tracking service and the delivery policy. Each query corresponds to one <strong>iteration</strong>: the model decides the next action, receives the result and decides again.",
        "The model retains no memory between iterations. On every iteration, the orchestrator resends the instructions and the full accumulated history, so each iteration processes more tokens than the previous one. The chart shows the input tokens of each iteration; the dashed line shows the value the simple estimate assumes for all of them."
      ],
      e2Controle: "Number of iterations",
      e2Tokens: "input tokens per request",
      e2Simples: "in the simple estimate",
      e2Mensal: "monthly cost of the agent",
      e2Frase: "The agent receives {vol} requests per month and costs <strong>{custo}</strong>, {vezes} times the cost of the classification, which receives {volc} messages. <strong>Volume does not determine cost; orchestration does.</strong>",
      e2Nota: "Model: {modelo}. The calculation includes cache reuse of the fixed part of the instructions, according to the prices published by the vendor.",
      iteracao: "iteration", tokens: "tokens",
      serieIteracao: "input tokens in the iteration", serieSimples: "simple estimate",

      e3Titulo: "Each request on the appropriate model",
      e3Texto: [
        "One way to reduce cost is to route every request first to a lower cost model and forward to the higher cost model only those the first one cannot resolve. It is the same principle as tiered customer support.",
        "The arrangement reduces cost only when the first model resolves a sufficient share of the requests, because unresolved requests pass through both models. The break even point is the ratio between the two models' cost per request."
      ],
      e3Controle: "Share resolved by the lower cost model",
      e3Primeiro: "first tier", e3Segundo: "second tier",
      cascata: "cost with a first tier", direto: "cost with the higher cost model only", equilibrio: "break even",
      e3Eixo: "share resolved by the lower cost model",
      e3Vale: "With {r} of requests resolved by the first tier, the monthly cost is <strong>{c}</strong>, against <strong>{d}</strong> with the higher cost model only: <strong>a {s} reduction</strong>.",
      e3NaoVale: "With {r} of requests resolved by the first tier, the monthly cost is <strong>{c}</strong>, against <strong>{d}</strong> with the higher cost model only: <strong>a {s} increase</strong>. Below {b}, the first tier raises the cost.",
      e3Condicao: "Mandatory condition: the first tier's answer must be validated by code (expected format, business rules or an explicit statement that no answer was possible). Validation by another model reintroduces the cost the arrangement is meant to avoid.",

      e4Titulo: "Conclusion: the cost of the assistant",
      e4Texto: [
        "The table brings together the results of the previous steps and is updated when they change."
      ],
      e4ColItem: "", e4ColVol: "Requests per month", e4ColMensal: "Monthly cost", e4ColUnit: "Cost per request",
      e4Class: "Classification (step 1)",
      e4Agente: "Resolution agent (step 2)",
      e4Total: "Total cost of the assistant",
      e4Simples: "Simple estimate, one call per request",
      e4Cascata: "With a first tier, {r} resolved (step 3)",
      e4Conclusao: "The simple estimate would indicate <strong>{simples}</strong> per month. The cost calculated from the architecture is <strong>{total}</strong>, {vezes} times higher, and the difference comes from the agent's iterations, not from volume. With the first tier resolving {r} of requests, the monthly cost becomes <strong>{cascata}</strong>, and the cost per resolved request changes from {c2} to {c3}. <strong>That is the value to compare with the cost of the same service performed by a person.</strong>",
      aprofNota: "Includes the three additional components, which steps 1 to 4 do not consider.",

      aprofTitulo: "Further detail: the complete architecture of the example",
      aprofTexto: "Besides the classification and the resolution agent, the complete assistant includes a shipping document reader, a history compressor and a sampled review of answer quality. Each component's parameters can be changed. When the agent's iteration limit is removed, the calculator declines to calculate, because a component estimated at zero would disappear from a proposal without the omission being noticed.",
      componente: "Component", papel: "Role", chamadas: "Calls/month", modelo: "Model", iteracoes: "Iteration limit", cache: "Cache",
      entradaTarefa: "Input/request", custo: "USD/month", parte: "Share of cost",
      total: "per month, language model consumption only",
      restaurar: "Restore the example",
      recusa: "The calculator declines to calculate, which is the expected behavior:",
      avisos: "Alerts", premissas: "Declared premises",
      rodapeMotor: "",

      precosTitulo: "Prices in use",
      precosVivo: "Retrieved from the vendors' public sources at <strong>{quando}</strong> ({idade}). The site queries these sources again every day.",
      precosMao: "<strong>Manually transcribed price table</strong>, verified on {quando}. The source query did not complete for this publication, and the page states so.",
      entrada: "input /1M", saida: "output /1M", leitura: "cache read /1M", escrita: "cache write /1M", piso: "cache minimum",
      fontes: "Sources"
    }
  }[LANG];

  var LOCALE = LANG === "pt" ? "pt-BR" : "en-US";
  var fmtN = new Intl.NumberFormat(LOCALE, { maximumFractionDigits: 0 });
  var fmtUSD = new Intl.NumberFormat(LOCALE, { style: "currency", currency: "USD", minimumFractionDigits: 2, maximumFractionDigits: 2 });
  var fmtUSDfino = new Intl.NumberFormat(LOCALE, { style: "currency", currency: "USD", minimumFractionDigits: 3, maximumFractionDigits: 4 });
  var fmtPct = new Intl.NumberFormat(LOCALE, { style: "percent", maximumFractionDigits: 1 });
  var fmtPreco = new Intl.NumberFormat(LOCALE, { maximumFractionDigits: 3 });

  function el(tag, attrs, filhos) {
    var e = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      if (k === "html") e.innerHTML = attrs[k];
      else if (k === "text") e.textContent = attrs[k];
      else if (k.slice(0, 2) === "on") e.addEventListener(k.slice(2), attrs[k]);
      else e.setAttribute(k, attrs[k]);
    });
    (filhos || []).forEach(function (f) { if (f) e.appendChild(typeof f === "string" ? document.createTextNode(f) : f); });
    return e;
  }
  var SVGNS = "http://www.w3.org/2000/svg";
  function sv(tag, attrs, texto) {
    var e = document.createElementNS(SVGNS, tag);
    Object.keys(attrs || {}).forEach(function (k) { e.setAttribute(k, attrs[k]); });
    if (texto != null) e.textContent = texto;
    return e;
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function clonar(o) { return JSON.parse(JSON.stringify(o)); }
  function usd(v) { return Math.abs(v) < 0.1 ? fmtUSDfino.format(v) : fmtUSD.format(v); }

  function estado(msg, tipo) {
    raiz.innerHTML = "";
    var box = el("div", { class: "lab-estado", "data-tipo": tipo || "info", role: "status" });
    if (!tipo) box.appendChild(el("span", { class: "lab-girando", "aria-hidden": "true" }));
    box.appendChild(el("span", { html: msg }));
    raiz.appendChild(box);
  }

  // ---------------------------------------------------------------- Python
  var py = null;
  function executar(tipo, dados) {
    return JSON.parse(py.globals.get("executar")(tipo, JSON.stringify(dados)));
  }
  var PONTE = [
    "import json, sys",
    "sys.path.insert(0, '/home/pyodide')",
    "import agent_cost as ac",
    "OPTS = {'hit_rate': 0.40, 'calls_per_write': 50}",
    "def executar(tipo, payload):",
    "    p = json.loads(payload)",
    "    try:",
    "        if tipo == 'arch':",
    "            r = ac.price_architecture(p['arch'], p['prices'])",
    "        elif tipo == 'comp':",
    "            r = ac.price_component(p['comp'], p['prices'], OPTS)",
    "        elif tipo == 'infl':",
    "            r = ac.context_inflation(p['base'], p['delta'], int(p['n']))",
    "        elif tipo == 'casc':",
    "            c1, c2, tasks = p['c1'], p['c2'], int(p['tasks'])",
    "            r = ac.cascade(c1, c2, p['rate'], tasks)",
    "            r['curve'] = [[x / 100, ac.cascade(c1, c2, x / 100, tasks)['cascade_cost']] for x in range(0, 101)]",
    "        else:",
    "            raise ValueError('unknown run %r' % tipo)",
    "        return json.dumps({'ok': True, 'r': r})",
    "    except ValueError as e:",
    "        return json.dumps({'ok': False, 'error': str(e)})"
  ].join("\n");

  function carregarScript(src) {
    return new Promise(function (ok, falha) {
      var s = document.createElement("script");
      s.src = src; s.onload = ok; s.onerror = function () { falha(new Error(src)); };
      document.head.appendChild(s);
    });
  }
  function buscar(nome, comoJson) {
    return fetch(BASE + nome, { cache: "no-cache" }).then(function (r) {
      if (!r.ok) throw new Error(nome + " " + r.status);
      return comoJson ? r.json() : r.text();
    });
  }

  var precos, arqExemplo, precosVivos;

  function iniciar() {
    estado(T.carregando);
    var codigo = buscar("agent_cost.py", false);
    var arq = buscar("architecture.example.json", true);
    var vivos = buscar("prices.live.json", true).then(function (j) { precosVivos = true; return j; })
      .catch(function () { precosVivos = false; return buscar("prices.example.json", true); });

    Promise.all([codigo, arq, vivos]).catch(function () {
      var cmd = "git clone " + REPO + "\ncd agent-cost-math\npython agent_cost.py --architecture architecture.example.json --live";
      raiz.innerHTML = "";
      raiz.appendChild(el("div", { class: "lab-estado", "data-tipo": "erro" }, [el("span", { text: T.semMotor })]));
      raiz.appendChild(el("pre", {}, [el("code", { text: cmd })]));
      throw new Error("indisponivel");
    }).then(function (arr) {
      precos = arr[2];
      arqExemplo = arr[1];
      return carregarScript(PYODIDE + "pyodide.js").then(function () {
        return window.loadPyodide({ indexURL: PYODIDE });
      }).then(function (p) {
        estado(T.lendo);
        py = p;
        py.FS.writeFile("/home/pyodide/agent_cost.py", arr[0]);
        py.runPython(PONTE);
        montar();
      });
    }).catch(function (e) {
      if (e && e.message === "indisponivel") return;
      estado(T.falhou + esc(e && e.message || e), "erro");
    });
  }

  // ---------------------------------------------------------------- estado compartilhado
  // As quatro etapas leem o mesmo estado; mudar uma recalcula as seguintes.
  var S = { mensagens: 40000, iteracoes: 8, parcela: 0.6 };
  var ouvintes = [];
  function mudou() { ouvintes.forEach(function (f) { f(); }); }

  function componente(nome) {
    var c = arqExemplo.components.filter(function (x) { return x.role === nome; })[0];
    return clonar(c);
  }
  function classificacao() {
    var c = componente("router");
    c.monthly_volume = S.mensagens;
    return executar("comp", { comp: c, prices: precos }).r;
  }
  function agente(modelo) {
    var c = componente("specialist");
    c.max_iterations = S.iteracoes;
    if (modelo) c.model = modelo;
    return executar("comp", { comp: c, prices: precos }).r;
  }
  function modeloMenorCusto() {
    var nomes = Object.keys(precos.models).filter(function (n) { return precos.models[n].tier === "cheap"; });
    var cls = componente("router").model;
    return nomes.indexOf(cls) >= 0 ? cls : nomes[0];
  }
  function precoModelo(nome) {
    var m = precos.models[nome];
    return nome + " (" + (LANG === "pt" ? "US$ " : "USD ") + fmtPreco.format(m.input_per_1k * 1000) + " / " + fmtPreco.format(m.output_per_1k * 1000) + " " + (LANG === "pt" ? "por milhão de tokens de entrada e de saída" : "per million input and output tokens") + ")";
  }

  // ---------------------------------------------------------------- telas
  function montar() {
    raiz.innerHTML = "";
    raiz.appendChild(etapa1());
    raiz.appendChild(etapa2());
    raiz.appendChild(etapa3());
    raiz.appendChild(etapa4());
    raiz.appendChild(aprofundamento());
    raiz.appendChild(blocoPrecos());
  }

  function cabecalho(n, titulo, paragrafos, vars) {
    var bloco = el("section", { class: "lab-bloco lab-etapa", "aria-labelledby": "acl-e" + n });
    bloco.appendChild(el("p", { class: "lab-etapa-num", text: T.etapa + " " + n }));
    bloco.appendChild(el("h2", { id: "acl-e" + n, text: titulo }));
    paragrafos.forEach(function (p) { bloco.appendChild(el("p", { class: "lab-sub", html: interpolar(p, vars || {}) })); });
    return bloco;
  }
  function interpolar(s, vars) {
    Object.keys(vars).forEach(function (k) { s = s.split("{" + k + "}").join(vars[k]); });
    return s;
  }
  function deslizador(rotulo, min, max, passo, valor, formatar, aoMudar) {
    var saida = el("span", { class: "lab-num lab-deslizador-valor", text: formatar(valor) });
    var input = el("input", { type: "range", min: String(min), max: String(max), step: String(passo), value: String(valor), "aria-label": rotulo,
      oninput: function (e) { var v = Number(e.target.value); saida.textContent = formatar(v); aoMudar(v); } });
    return el("label", { class: "lab-campo lab-campo-largo" }, [el("span", {}, [rotulo + ": ", saida]), input]);
  }
  function indicador(valor, rotulo, detalhe) {
    return el("div", { class: "lab-indicador" }, [
      el("span", { class: "lab-indicador-valor lab-num", text: valor }),
      el("span", { class: "lab-indicador-rotulo", text: rotulo }),
      detalhe ? el("span", { class: "lab-indicador-detalhe", text: detalhe }) : null
    ]);
  }

  // Etapa 1 ---------------------------------------------------------------
  function etapa1() {
    var c = componente("router");
    var bloco = cabecalho(1, T.e1Titulo, T.e1Texto, { tin: fmtN.format(c.input_tokens), tout: fmtN.format(c.output_tokens) });
    bloco.appendChild(el("div", { class: "lab-campos" }, [
      deslizador(T.e1Controle, 5000, 100000, 5000, S.mensagens, function (v) { return fmtN.format(v); },
        function (v) { S.mensagens = v; mudou(); })
    ]));
    var indicadores = el("div", { class: "lab-indicadores", "aria-live": "polite" });
    var frase = el("p", { class: "lab-frase" });
    bloco.appendChild(indicadores);
    bloco.appendChild(frase);
    function desenhar() {
      var r = classificacao();
      indicadores.innerHTML = "";
      indicadores.appendChild(indicador(usd(r.cost_usd / r.monthly_calls), T.e1Porchamada));
      indicadores.appendChild(indicador(fmtUSD.format(r.cost_usd), T.e1Mensal));
      frase.innerHTML = interpolar(T.e1Frase, { modelo: esc(precoModelo(r.model)) });
    }
    ouvintes.push(desenhar);
    desenhar();
    return bloco;
  }

  // graficos -------------------------------------------------------------
  function dica(caixa) {
    var d = el("div", { class: "lab-dica", role: "tooltip" });
    caixa.appendChild(d);
    return {
      mostrar: function (html, x, y) { d.innerHTML = html; d.style.left = x + "px"; d.style.top = y + "px"; d.classList.add("visivel"); },
      esconder: function () { d.classList.remove("visivel"); }
    };
  }
  function escala(d0, d1, r0, r1) { return function (v) { return r0 + (v - d0) / ((d1 - d0) || 1) * (r1 - r0); }; }
  function topoBonito(v) {
    if (v <= 0) return 1;
    var p = Math.pow(10, Math.floor(Math.log10(v))), m = v / p;
    return (m <= 1 ? 1 : m <= 2 ? 2 : m <= 2.5 ? 2.5 : m <= 5 ? 5 : 10) * p;
  }
  function compacto(v) { return new Intl.NumberFormat(LOCALE, { notation: "compact", maximumFractionDigits: 1 }).format(v); }
  function largura(caixa) { return Math.max(300, Math.round(caixa.clientWidth || 720)); }
  var redesenhos = [];
  var adiado;
  window.addEventListener("resize", function () {
    clearTimeout(adiado);
    adiado = setTimeout(function () { redesenhos.forEach(function (f) { f(); }); }, 150);
  });

  // Etapa 2 ---------------------------------------------------------------
  function etapa2() {
    var bloco = cabecalho(2, T.e2Titulo, T.e2Texto);
    bloco.appendChild(el("div", { class: "lab-campos" }, [
      deslizador(T.e2Controle, 1, 20, 1, S.iteracoes, function (v) { return String(v); },
        function (v) { S.iteracoes = v; mudou(); })
    ]));
    var caixa = el("div", { class: "lab-grafico" });
    var indicadores = el("div", { class: "lab-indicadores", "aria-live": "polite" });
    var frase = el("p", { class: "lab-frase" });
    var nota = el("p", { class: "lab-rodape" });
    bloco.appendChild(caixa);
    bloco.appendChild(el("ul", { class: "lab-legenda" }, [
      el("li", {}, [el("i", { class: "barra" }), T.serieIteracao]),
      el("li", {}, [el("i", { class: "tracejada" }), T.serieSimples])
    ]));
    bloco.appendChild(indicadores);
    bloco.appendChild(frase);
    bloco.appendChild(nota);

    function desenhar() {
      var c = componente("specialist");
      var infl = executar("infl", { base: c.prompt_base_tokens, delta: c.delta_tokens_per_iteration, n: S.iteracoes }).r;
      var ag = agente();
      var cls = classificacao();
      grafico(infl, c.prompt_base_tokens);
      indicadores.innerHTML = "";
      indicadores.appendChild(indicador(fmtN.format(infl.input_total), T.e2Tokens, fmtN.format(infl.input_total_naive) + " " + T.e2Simples));
      indicadores.appendChild(indicador(fmtUSD.format(ag.cost_usd), T.e2Mensal));
      var vezes = cls.cost_usd > 0 ? Math.round(ag.cost_usd / cls.cost_usd) : 0;
      frase.innerHTML = interpolar(T.e2Frase, { vol: fmtN.format(ag.monthly_calls), custo: fmtUSD.format(ag.cost_usd), vezes: fmtN.format(vezes), volc: fmtN.format(cls.monthly_calls) });
      nota.textContent = interpolar(T.e2Nota, { modelo: precoModelo(ag.model) });
    }
    function grafico(res, base) {
      caixa.innerHTML = "";
      var per = res.input_per_iteration;
      var W = largura(caixa), H = 240, m = { t: 12, r: 12, b: 34, l: 56 };
      var topo = topoBonito(Math.max.apply(null, per.concat([base])));
      var y = escala(0, topo, H - m.b, m.t);
      var passo = (W - m.l - m.r) / per.length, larg = Math.max(2, passo - 2);
      var svg = sv("svg", { viewBox: "0 0 " + W + " " + H, role: "img" });
      [0, .5, 1].forEach(function (f) {
        var yy = y(topo * f);
        svg.appendChild(sv("line", { class: f === 0 ? "eixo" : "grade", x1: m.l, x2: W - m.r, y1: yy, y2: yy }));
        svg.appendChild(sv("text", { x: m.l - 8, y: yy + 4, "text-anchor": "end" }, compacto(topo * f)));
      });
      var tip = dica(caixa);
      per.forEach(function (tok, i) {
        var x = m.l + i * passo + 1, yy = y(tok), h = (H - m.b) - yy, r = Math.min(4, h, larg / 2);
        var barra = sv("path", { class: "serie-1", d: "M" + x + "," + (H - m.b) + "V" + (yy + r) + "q0,-" + r + " " + r + ",-" + r + "H" + (x + larg - r) + "q" + r + ",0 " + r + "," + r + "V" + (H - m.b) + "Z" });
        svg.appendChild(barra);
        var alvo = sv("rect", { class: "alvo", x: m.l + i * passo, y: m.t, width: passo, height: H - m.b - m.t });
        alvo.addEventListener("mousemove", function (ev) {
          barra.classList.add("ativo");
          var bb = caixa.getBoundingClientRect();
          tip.mostrar(T.iteracao + " " + (i + 1) + ": <strong>" + fmtN.format(tok) + "</strong> " + T.tokens, ev.clientX - bb.left, ev.clientY - bb.top);
        });
        alvo.addEventListener("mouseleave", function () { barra.classList.remove("ativo"); tip.esconder(); });
        svg.appendChild(alvo);
        if (per.length <= 12 || i === 0 || i === per.length - 1 || (i + 1) % 5 === 0) {
          svg.appendChild(sv("text", { x: x + larg / 2, y: H - m.b + 18, "text-anchor": "middle" }, String(i + 1)));
        }
      });
      var yb = y(base);
      svg.appendChild(sv("line", { class: "linha-2", x1: m.l, x2: W - m.r, y1: yb, y2: yb }));
      svg.setAttribute("aria-label", fmtN.format(res.input_total) + " " + T.tokens);
      caixa.insertBefore(svg, caixa.firstChild);
    }
    ouvintes.push(desenhar);
    redesenhos.push(desenhar);
    requestAnimationFrame(desenhar);
    return bloco;
  }

  // Etapa 3 ---------------------------------------------------------------
  function custosPorSolicitacao() {
    var caro = agente();
    var barato = agente(modeloMenorCusto());
    return { c1: barato.cost_usd / barato.monthly_calls, c2: caro.cost_usd / caro.monthly_calls,
             tarefas: caro.monthly_calls, modeloBarato: barato.model, modeloCaro: caro.model };
  }
  function etapa3() {
    var bloco = cabecalho(3, T.e3Titulo, T.e3Texto);
    bloco.appendChild(el("div", { class: "lab-campos" }, [
      deslizador(T.e3Controle, 0, 100, 1, Math.round(S.parcela * 100), function (v) { return fmtPct.format(v / 100); },
        function (v) { S.parcela = v / 100; mudou(); })
    ]));
    var modelos = el("p", { class: "lab-rodape" });
    var caixa = el("div", { class: "lab-grafico" });
    var frase = el("p", { class: "lab-frase", "aria-live": "polite" });
    bloco.appendChild(modelos);
    bloco.appendChild(caixa);
    bloco.appendChild(el("ul", { class: "lab-legenda" }, [
      el("li", {}, [el("i", {}), T.cascata]),
      el("li", {}, [el("i", { class: "tracejada" }), T.direto])
    ]));
    bloco.appendChild(frase);
    bloco.appendChild(el("p", { class: "lab-rodape", text: T.e3Condicao }));

    function desenhar() {
      var k = custosPorSolicitacao();
      modelos.textContent = T.e3Primeiro + ": " + k.modeloBarato + " · " + T.e3Segundo + ": " + k.modeloCaro;
      var r = executar("casc", { c1: k.c1, c2: k.c2, rate: S.parcela, tasks: k.tarefas });
      caixa.innerHTML = "";
      if (!r.ok) { frase.textContent = r.error; return; }
      var res = r.r;
      var W = largura(caixa), H = 260, m = { t: 14, r: 16, b: 40, l: 64 };
      var topo = topoBonito(Math.max(res.curve[0][1], res.direct_cost));
      var x = escala(0, 1, m.l, W - m.r), y = escala(0, topo, H - m.b, m.t);
      var svg = sv("svg", { viewBox: "0 0 " + W + " " + H, role: "img" });
      [0, .5, 1].forEach(function (f) {
        var yy = y(topo * f);
        svg.appendChild(sv("line", { class: f === 0 ? "eixo" : "grade", x1: m.l, x2: W - m.r, y1: yy, y2: yy }));
        svg.appendChild(sv("text", { x: m.l - 8, y: yy + 4, "text-anchor": "end" }, "US$ " + compacto(topo * f)));
      });
      [0, .25, .5, .75, 1].forEach(function (f) {
        svg.appendChild(sv("text", { x: x(f), y: H - m.b + 18, "text-anchor": "middle" }, fmtPct.format(f)));
      });
      svg.appendChild(sv("text", { x: (m.l + W - m.r) / 2, y: H - 4, "text-anchor": "middle" }, T.e3Eixo));
      var d = res.curve.map(function (p, i) { return (i ? "L" : "M") + x(p[0]).toFixed(1) + "," + y(p[1]).toFixed(1); }).join("");
      svg.appendChild(sv("path", { class: "linha-1", d: d }));
      svg.appendChild(sv("line", { class: "linha-2", x1: m.l, x2: W - m.r, y1: y(res.direct_cost), y2: y(res.direct_cost) }));
      var be = res.min_success_rate;
      if (be <= 1) {
        svg.appendChild(sv("line", { class: "marco", x1: x(be), x2: x(be), y1: m.t, y2: H - m.b }));
        svg.appendChild(sv("text", { class: "forte", x: x(be) + 6, y: m.t + 12 }, T.equilibrio + " " + fmtPct.format(be)));
      }
      svg.appendChild(sv("circle", { class: "ponto", cx: x(S.parcela), cy: y(res.cascade_cost), r: 5 }));
      var tip = dica(caixa);
      var alvo = sv("rect", { class: "alvo", x: m.l, y: m.t, width: W - m.l - m.r, height: H - m.b - m.t });
      alvo.addEventListener("mousemove", function (ev) {
        var bb = svg.getBoundingClientRect(), fx = W / bb.width;
        var px = (ev.clientX - bb.left) * fx;
        var p = res.curve[Math.round(Math.min(1, Math.max(0, (px - m.l) / (W - m.l - m.r))) * 100)];
        var cb = caixa.getBoundingClientRect();
        tip.mostrar(fmtPct.format(p[0]) + ": " + T.cascata + " <strong>" + fmtUSD.format(p[1]) + "</strong><br>" + T.direto + " " + fmtUSD.format(res.direct_cost),
          ev.clientX - cb.left, ev.clientY - cb.top);
      });
      alvo.addEventListener("mouseleave", tip.esconder);
      svg.appendChild(alvo);
      svg.setAttribute("aria-label", T.equilibrio + " " + fmtPct.format(be));
      caixa.insertBefore(svg, caixa.firstChild);
      frase.innerHTML = interpolar(res.worth_it ? T.e3Vale : T.e3NaoVale, {
        r: fmtPct.format(S.parcela), c: fmtUSD.format(res.cascade_cost), d: fmtUSD.format(res.direct_cost),
        s: fmtPct.format(Math.abs(res.saving_pct) / 100), b: fmtPct.format(be)
      });
    }
    ouvintes.push(desenhar);
    redesenhos.push(desenhar);
    requestAnimationFrame(desenhar);
    return bloco;
  }

  // Etapa 4 ---------------------------------------------------------------
  // A estimativa simples e literalmente a da abertura da pagina: o preco de UMA
  // chamada ao modelo multiplicado pelas solicitacoes, sem iteracoes e sem cache.
  function agenteChamadaUnica() {
    var c = componente("specialist");
    c.max_iterations = 1;
    c.caching = false;
    return executar("comp", { comp: c, prices: precos }).r;
  }
  function etapa4() {
    var bloco = cabecalho(4, T.e4Titulo, T.e4Texto);
    var tabela = el("div", { class: "lab-rolagem", "aria-live": "polite" });
    var conclusao = el("p", { class: "lab-frase lab-conclusao" });
    bloco.appendChild(tabela);
    bloco.appendChild(conclusao);
    function linha(rotulo, vol, mensal, unit, classe) {
      return el("tr", { class: classe || "" }, [
        el("td", { html: rotulo }),
        el("td", { class: "dir lab-num", text: vol == null ? "" : fmtN.format(vol) }),
        el("td", { class: "dir lab-num", text: mensal == null ? "" : fmtUSD.format(mensal) }),
        el("td", { class: "dir lab-num", text: unit == null ? "" : usd(unit) })
      ]);
    }
    function desenhar() {
      var cls = classificacao();
      var k = custosPorSolicitacao();
      var ag = agente();
      var unica = agenteChamadaUnica();
      var casc = executar("casc", { c1: k.c1, c2: k.c2, rate: S.parcela, tasks: k.tarefas }).r;
      var total = cls.cost_usd + ag.cost_usd;
      var simples = cls.cost_usd + unica.cost_usd;
      var comCascata = cls.cost_usd + casc.cascade_cost;
      var r = fmtPct.format(S.parcela);
      tabela.innerHTML = "";
      tabela.appendChild(el("table", { class: "lab-tabela lab-resumo" }, [
        el("thead", {}, [el("tr", {}, [T.e4ColItem, T.e4ColVol, T.e4ColMensal, T.e4ColUnit].map(function (h, i) {
          return el("th", { class: i ? "dir" : "", text: h });
        }))]),
        el("tbody", {}, [
          linha(T.e4Class, cls.monthly_calls, cls.cost_usd, cls.cost_usd / cls.monthly_calls),
          linha(T.e4Agente, ag.monthly_calls, ag.cost_usd, ag.cost_usd / ag.monthly_calls),
          linha(T.e4Total, null, total, null, "lab-linha-total"),
          linha(T.e4Simples, null, simples, null, "lab-linha-secundaria"),
          linha(interpolar(T.e4Cascata, { r: esc(r) }), null, comCascata, casc.cascade_cost / k.tarefas, "lab-linha-total")
        ])
      ]));
      var vezes = simples > 0 ? total / simples : 0;
      conclusao.innerHTML = interpolar(T.e4Conclusao, {
        simples: fmtUSD.format(simples), total: fmtUSD.format(total),
        vezes: new Intl.NumberFormat(LOCALE, { maximumFractionDigits: 1 }).format(vezes),
        r: r, cascata: fmtUSD.format(comCascata),
        c2: usd(k.c2), c3: usd(casc.cascade_cost / k.tarefas)
      });
    }
    ouvintes.push(desenhar);
    desenhar();
    return bloco;
  }

  // Aprofundamento: arquitetura completa ------------------------------------
  function aprofundamento() {
    var arq = clonar(arqExemplo);
    var det = el("details", { class: "lab-bloco lab-aprofundamento" });
    det.appendChild(el("summary", { text: T.aprofTitulo }));
    det.appendChild(el("p", { class: "lab-sub", text: T.aprofTexto }));
    var entradas = el("div", { class: "lab-rolagem" });
    var resultado = el("div", { "aria-live": "polite" });
    det.appendChild(entradas);
    det.appendChild(resultado);
    det.appendChild(el("p", {}, [el("button", { class: "lab-botao", type: "button", text: T.restaurar, onclick: function () {
      arq = clonar(arqExemplo); desenharEntradas(); calcular();
    } })]));

    function selectModelo(valor, aoMudar) {
      var s = el("select", { onchange: aoMudar });
      Object.keys(precos.models).forEach(function (n) {
        var o = el("option", { value: n, text: n });
        if (n === valor) o.selected = true;
        s.appendChild(o);
      });
      return s;
    }
    function numero(valor, aoMudar, attrs) {
      return el("input", Object.assign({ type: "number", value: valor == null ? "" : valor, min: "0", step: "1", oninput: aoMudar, inputmode: "numeric" }, attrs || {}));
    }
    function desenharEntradas() {
      var tb = el("tbody");
      arq.components.forEach(function (c) {
        var iterativo = Object.prototype.hasOwnProperty.call(c, "prompt_base_tokens");
        var caixaCache = el("input", { type: "checkbox", "aria-label": T.cache + ", " + c.name, onchange: function (e) { c.caching = e.target.checked; calcular(); } });
        caixaCache.checked = c.caching !== false;
        tb.appendChild(el("tr", {}, [
          el("td", { text: c.name }),
          el("td", {}, [el("span", { class: "lab-papel", text: c.role })]),
          el("td", { class: "dir" }, [numero(c.monthly_volume, function (e) {
            if (e.target.value === "") delete c.monthly_volume; else c.monthly_volume = Number(e.target.value);
            calcular();
          }, { "aria-label": T.chamadas + ", " + c.name })]),
          el("td", {}, [selectModelo(c.model, function (e) { c.model = e.target.value; calcular(); })]),
          el("td", { class: "dir" }, [iterativo ? numero(c.max_iterations, function (e) {
            if (e.target.value === "") delete c.max_iterations; else c.max_iterations = Number(e.target.value);
            calcular();
          }, { min: "1", "aria-label": T.iteracoes + ", " + c.name }) : el("span", { text: "-" })]),
          el("td", {}, [caixaCache])
        ]));
      });
      entradas.innerHTML = "";
      entradas.appendChild(el("table", { class: "lab-tabela" }, [
        el("thead", {}, [el("tr", {}, [T.componente, T.papel, T.chamadas, T.modelo, T.iteracoes, T.cache].map(function (h, i) {
          return el("th", { class: (i === 2 || i === 4) ? "dir" : "", text: h });
        }))]),
        tb
      ]));
    }
    function calcular() {
      var r = executar("arch", { arch: arq, prices: precos });
      resultado.innerHTML = "";
      if (!r.ok) {
        resultado.appendChild(el("div", { class: "lab-recusa", role: "alert" }, [el("strong", { text: T.recusa }), el("span", { text: r.error })]));
        return;
      }
      var res = r.r;
      var linhas = el("tbody");
      res.components.forEach(function (c) {
        linhas.appendChild(el("tr", {}, [
          el("td", { text: c.name }),
          el("td", { text: c.model }),
          el("td", { class: "dir lab-num", text: fmtN.format(c.monthly_calls) }),
          el("td", { class: "dir lab-num", text: fmtN.format(c.input_per_task) }),
          el("td", { class: "dir lab-num", text: fmtUSD.format(c.cost_usd) }),
          el("td", {}, [el("div", { class: "lab-parte", title: c.name + ": " + fmtPct.format(c.cost_share_pct / 100) }, [
            el("div", { class: "lab-parte-trilho" }, [el("div", { class: "lab-parte-barra", style: "width:" + Math.max(c.cost_share_pct, 0.5) + "%" })]),
            el("span", { text: fmtPct.format(c.cost_share_pct / 100) })
          ])])
        ]));
      });
      resultado.appendChild(el("div", { class: "lab-total" }, [
        el("span", { class: "lab-total-valor", text: fmtUSD.format(res.monthly_cost_usd) }),
        el("span", { class: "lab-total-rotulo", text: T.total + ". " + T.aprofNota })
      ]));
      resultado.appendChild(el("div", { class: "lab-rolagem" }, [el("table", { class: "lab-tabela" }, [
        el("thead", {}, [el("tr", {}, [T.componente, T.modelo, T.chamadas, T.entradaTarefa, T.custo, T.parte].map(function (h, i) {
          return el("th", { class: (i >= 2 && i <= 4) ? "dir" : "", text: h });
        }))]),
        linhas
      ])]));
      var avisos = [];
      res.components.forEach(function (c) {
        c.alerts.forEach(function (a) { avisos.push("<strong>" + esc(c.name) + "</strong>: " + esc(a)); });
      });
      res.architecture_alerts.forEach(function (a) { avisos.push(esc(a)); });
      if (avisos.length) {
        resultado.appendChild(el("h3", { class: "lab-total-rotulo", text: T.avisos }));
        var ul = el("ul", { class: "lab-avisos" });
        avisos.forEach(function (a) { ul.appendChild(el("li", { html: a })); });
        resultado.appendChild(ul);
      }
      resultado.appendChild(el("p", { class: "lab-rodape", text: T.premissas + ": " + res.premises.join(" · ") + (T.rodapeMotor ? " " + T.rodapeMotor : "") }));
    }
    desenharEntradas();
    calcular();
    return det;
  }

  // Precos -----------------------------------------------------------------
  function blocoPrecos() {
    var bloco = el("section", { class: "lab-bloco", "aria-labelledby": "acl-precos" }, [el("h2", { id: "acl-precos", text: T.precosTitulo })]);
    var quando = precos.pricing_as_of || "?";
    var origem;
    if (precosVivos) {
      var data = new Date(quando);
      var horas = (Date.now() - data.getTime()) / 36e5;
      var idade = isFinite(horas) ? new Intl.RelativeTimeFormat(LOCALE, { numeric: "auto" }).format(-Math.round(horas), "hour") : "?";
      origem = interpolar(T.precosVivo, { quando: esc(isFinite(horas) ? data.toLocaleString(LOCALE, { dateStyle: "medium", timeStyle: "short", timeZone: "UTC" }) + " UTC" : quando), idade: esc(idade) });
    } else {
      origem = interpolar(T.precosMao, { quando: esc(quando) });
    }
    bloco.appendChild(el("p", { class: "lab-precos-origem", html: origem }));
    var tb = el("tbody");
    Object.keys(precos.models).forEach(function (n) {
      var mm = precos.models[n];
      function pm(v) { return v == null ? "-" : fmtPreco.format(v * 1000); }
      tb.appendChild(el("tr", {}, [
        el("td", { text: n }),
        el("td", { class: "dir lab-num", text: pm(mm.input_per_1k) }),
        el("td", { class: "dir lab-num", text: pm(mm.output_per_1k) }),
        el("td", { class: "dir lab-num", text: pm(mm.cache_read_per_1k) }),
        el("td", { class: "dir lab-num", text: pm(mm.cache_write_per_1k) }),
        el("td", { class: "dir lab-num", text: mm.min_cache_tokens ? fmtN.format(mm.min_cache_tokens) : "-" })
      ]));
    });
    bloco.appendChild(el("div", { class: "lab-rolagem" }, [el("table", { class: "lab-tabela" }, [
      el("thead", {}, [el("tr", {}, [T.modelo, "USD " + T.entrada, "USD " + T.saida, "USD " + T.leitura, "USD " + T.escrita, T.piso].map(function (h, i) {
        return el("th", { class: i >= 1 ? "dir" : "", text: h });
      }))]),
      tb
    ])]));
    var fontes = [];
    Object.keys(precos.sources || {}).forEach(function (k) {
      [].concat(precos.sources[k]).forEach(function (u) { fontes.push('<a href="' + esc(u) + '" target="_blank" rel="noopener">' + esc(u.replace(/^https:\/\//, "")) + "</a>"); });
    });
    if (fontes.length) bloco.appendChild(el("p", { class: "lab-rodape", html: T.fontes + ": " + fontes.join(" · ") }));
    return bloco;
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", iniciar);
  else iniciar();
})();
