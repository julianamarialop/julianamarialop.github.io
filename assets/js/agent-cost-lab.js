/* Calculadora de custo de agentes.
 *
 * Nenhuma conta mora aqui. O navegador carrega o Pyodide e roda o MESMO
 * agent_cost.py do repositorio agent-cost-math, entao o numero da pagina e o
 * numero do notebook sao o mesmo numero. Este arquivo so desenha e coleta
 * entradas. Se uma conta aparecer em JavaScript, ela vira uma segunda fonte e as
 * duas vao divergir sem ninguem ver.
 */
(function () {
  "use strict";

  var raiz = document.getElementById("acl");
  if (!raiz) return;

  var LANG = raiz.dataset.lang === "pt" ? "pt" : "en";
  var BASE = raiz.dataset.base;                 // ".../agent-cost-math/"
  var PYODIDE = raiz.dataset.pyodide;           // ".../pyodide/vX/full/"
  var REPO = raiz.dataset.repo;

  var T = {
    pt: {
      carregando: "Carregando o Python no navegador. Na primeira visita isso baixa cerca de 10 MB; depois fica em cache.",
      lendo: "Lendo o motor e os preços...",
      semMotor: "A calculadora ainda não está disponível nesta página. O código roda igual na sua máquina:",
      falhou: "Não consegui carregar a calculadora: ",
      precosTitulo: "Os preços usados",
      precosVivo: "Lidos das fontes públicas dos fornecedores em <strong>{quando}</strong> ({idade}). O build do site consulta de novo todo dia.",
      precosMao: "<strong>Tabela transcrita à mão</strong> e conferida em {quando}. A consulta às fontes não rodou neste build, e a página diz isso em vez de esconder.",
      modelo: "Modelo", entrada: "entrada /1M", saida: "saída /1M", leitura: "cache lido /1M", escrita: "cache gravado /1M", piso: "mínimo para cache",
      fontes: "Fontes",
      arqTitulo: "1. A conta da arquitetura",
      arqSub: "Uma triagem de sinistros com cinco componentes. Mude o volume, o modelo, o teto de iterações ou o cache e veja quem paga a conta. Apague o teto do especialista para ver a calculadora recusar.",
      componente: "Componente", papel: "Papel", chamadas: "Chamadas/mês", iteracoes: "Teto de iterações", cache: "Cache",
      entradaTarefa: "Entrada/tarefa", custo: "USD/mês", parte: "Parte da conta",
      total: "por mês, só o vetor de LLM",
      restaurar: "Voltar ao exemplo",
      recusa: "A calculadora recusa, e esse é o comportamento certo:",
      avisos: "Alertas", premissas: "Premissas declaradas",
      enganoso: "{n} entrada por tarefa contra {m} da conta ingênua ({it} iterações).",
      inflTitulo: "2. A inflação de contexto",
      inflSub: "O agente não guarda memória entre uma volta e outra, então o orquestrador reenvia o histórico inteiro a cada ciclo. A entrada cresce de forma quadrática, não linear.",
      base: "Prompt base (tokens)", delta: "Cresce por volta (tokens)", voltas: "Voltas",
      lidoNaVolta: "lido nesta volta", ingenuo: "estimativa ingênua por volta",
      volta: "volta", tokens: "tokens",
      inflFrase: "<strong>{n} voltas cobram {t} tokens</strong>, onde a conta ingênua diz {i}: <strong>{p}</strong>. Dobrar o teto não dobra a conta.",
      cascTitulo: "3. O ponto de equilíbrio da cascata",
      cascSub: "Tudo passa primeiro pelo modelo barato e só o que falha na validação sobe para o caro. Compensa exatamente quando a taxa de acerto do barato supera a razão de preço entre os dois.",
      barato: "Modelo barato", caro: "Modelo caro", tin: "Entrada por tarefa", tout: "Saída por tarefa", tarefas: "Tarefas/mês", acerto: "Acerto do modelo barato",
      cascata: "custo da cascata", direto: "direto no modelo caro", equilibrio: "equilíbrio",
      cascVale: "Com {r} de acerto, a cascata custa <strong>{c}</strong> contra <strong>{d}</strong> direto: <strong>{s} de economia</strong>. O equilíbrio é {b}, a razão de preço entre os dois modelos.",
      cascNaoVale: "Com {r} de acerto, a cascata custa <strong>{c}</strong> contra <strong>{d}</strong> direto: <strong>{s} mais cara</strong>. Abaixo de {b} de acerto ela perde dinheiro.",
      cascCondicao: "Condição inegociável: a resposta do modelo barato tem de ser validável por código (schema, linter, admissão explícita de falha). Validar com outro modelo devolve o custo que você estava evitando.",
      acerto_eixo: "acerto do modelo barato", custo_eixo: "USD/mês",
      rodapeMotor: "Mensagens do motor em inglês, como no código.",
      erroCampo: "valor inválido"
    },
    en: {
      carregando: "Loading Python in your browser. The first visit downloads about 10 MB; after that it is cached.",
      lendo: "Reading the engine and the prices...",
      semMotor: "The calculator is not available on this page yet. The code runs the same on your machine:",
      falhou: "Could not load the calculator: ",
      precosTitulo: "The prices in use",
      precosVivo: "Read from the vendors' public sources at <strong>{quando}</strong> ({idade}). The site build fetches them again every day.",
      precosMao: "<strong>Hand transcribed table</strong>, checked on {quando}. The source fetch did not run in this build, and the page says so instead of hiding it.",
      modelo: "Model", entrada: "input /1M", saida: "output /1M", leitura: "cache read /1M", escrita: "cache write /1M", piso: "cache floor",
      fontes: "Sources",
      arqTitulo: "1. The architecture's bill",
      arqSub: "A claims triage with five components. Change the volume, the model, the iteration ceiling or the cache and watch who pays the bill. Clear the specialist's ceiling to watch the calculator refuse.",
      componente: "Component", papel: "Role", chamadas: "Calls/month", iteracoes: "Iteration ceiling", cache: "Cache",
      entradaTarefa: "Input/task", custo: "USD/month", parte: "Share of the bill",
      total: "per month, LLM vector only",
      restaurar: "Back to the example",
      recusa: "The calculator refuses, and that is the correct behavior:",
      avisos: "Alerts", premissas: "Declared premises",
      enganoso: "{n} input per task against a naive {m} ({it} iterations).",
      inflTitulo: "2. Context inflation",
      inflSub: "An agent keeps no memory between turns, so the orchestrator resends the whole history every cycle. Input grows quadratically, not linearly.",
      base: "Base prompt (tokens)", delta: "Growth per turn (tokens)", voltas: "Turns",
      lidoNaVolta: "read on this turn", ingenuo: "naive estimate per turn",
      volta: "turn", tokens: "tokens",
      inflFrase: "<strong>{n} turns bill {t} tokens</strong> where the naive count says {i}: <strong>{p}</strong>. Doubling the ceiling does not double the bill.",
      cascTitulo: "3. The cascade break even",
      cascSub: "Everything hits the cheap model first and only what fails validation escalates. It pays exactly when the cheap model's success rate beats the price ratio between the two.",
      barato: "Cheap model", caro: "Expensive model", tin: "Input per task", tout: "Output per task", tarefas: "Tasks/month", acerto: "Cheap model success",
      cascata: "cascade cost", direto: "straight to the expensive model", equilibrio: "break even",
      cascVale: "At {r} success the cascade costs <strong>{c}</strong> against <strong>{d}</strong> direct: <strong>{s} saved</strong>. Break even is {b}, the price ratio of the two models.",
      cascNaoVale: "At {r} success the cascade costs <strong>{c}</strong> against <strong>{d}</strong> direct: <strong>{s} more expensive</strong>. Below {b} success it loses money.",
      cascCondicao: "Non negotiable condition: the cheap model's answer has to be validatable by code (schema, linter, explicit admission of failure). Validating with another model hands back the cost you were avoiding.",
      acerto_eixo: "cheap model success", custo_eixo: "USD/month",
      rodapeMotor: "",
      erroCampo: "invalid value"
    }
  }[LANG];

  var LOCALE = LANG === "pt" ? "pt-BR" : "en-US";
  var fmtN = new Intl.NumberFormat(LOCALE, { maximumFractionDigits: 0 });
  var fmtUSD = new Intl.NumberFormat(LOCALE, { style: "currency", currency: "USD", minimumFractionDigits: 2, maximumFractionDigits: 2 });
  var fmtPct = new Intl.NumberFormat(LOCALE, { style: "percent", maximumFractionDigits: 1 });
  var fmtPreco = new Intl.NumberFormat(LOCALE, { maximumFractionDigits: 3 });

  function t(chave, vars) {
    var s = T[chave] || chave;
    Object.keys(vars || {}).forEach(function (k) { s = s.split("{" + k + "}").join(vars[k]); });
    return s;
  }
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

  function estado(msg, tipo) {
    raiz.innerHTML = "";
    var box = el("div", { class: "lab-estado", "data-tipo": tipo || "info", role: "status" });
    if (!tipo) box.appendChild(el("span", { class: "lab-girando", "aria-hidden": "true" }));
    box.appendChild(el("span", { html: msg }));
    raiz.appendChild(box);
  }

  // ---------------------------------------------------------------- Python
  var py = null;
  function rodar(tipo, dados) {
    var saida = py.globals.get("rodar")(tipo, JSON.stringify(dados));
    return JSON.parse(saida);
  }
  var PONTE = [
    "import json, sys",
    "sys.path.insert(0, '/home/pyodide')",
    "import agent_cost as ac",
    "def rodar(tipo, payload):",
    "    p = json.loads(payload)",
    "    try:",
    "        if tipo == 'arch':",
    "            r = ac.price_architecture(p['arch'], p['prices'])",
    "        elif tipo == 'infl':",
    "            r = ac.context_inflation(p['base'], p['delta'], int(p['n']))",
    "        elif tipo == 'casc':",
    "            m = p['prices']['models']",
    "            def tarefa(nome):",
    "                return p['tin'] / 1000 * m[nome]['input_per_1k'] + p['tout'] / 1000 * m[nome]['output_per_1k']",
    "            c1, c2 = tarefa(p['cheap']), tarefa(p['exp'])",
    "            r = ac.cascade(c1, c2, p['rate'], int(p['tasks']))",
    "            r['c1'], r['c2'] = c1, c2",
    "            r['curve'] = [[x / 100, ac.cascade(c1, c2, x / 100, int(p['tasks']))['cascade_cost']] for x in range(0, 101)]",
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
    var motor = buscar("agent_cost.py", false);
    var arq = buscar("architecture.example.json", true);
    var vivos = buscar("prices.live.json", true).then(function (j) { precosVivos = true; return j; })
      .catch(function () { precosVivos = false; return buscar("prices.example.json", true); });

    Promise.all([motor, arq, vivos]).catch(function () {
      var cmd = "git clone " + REPO + "\ncd agent-cost-math\npython agent_cost.py --architecture architecture.example.json --live";
      raiz.innerHTML = "";
      raiz.appendChild(el("div", { class: "lab-estado", "data-tipo": "erro" }, [el("span", { text: T.semMotor })]));
      raiz.appendChild(el("pre", {}, [el("code", { text: cmd })]));
      throw new Error("sem motor");
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
      if (e && e.message === "sem motor") return;
      estado(T.falhou + esc(e && e.message || e), "erro");
    });
  }

  // ---------------------------------------------------------------- telas
  function montar() {
    raiz.innerHTML = "";
    raiz.appendChild(blocoArquitetura());
    raiz.appendChild(blocoInflacao());
    raiz.appendChild(blocoCascata());
    raiz.appendChild(blocoPrecos());
  }

  function nomesModelos() { return Object.keys(precos.models); }
  function selectModelo(valor, aoMudar) {
    var s = el("select", { onchange: aoMudar });
    nomesModelos().forEach(function (n) {
      var o = el("option", { value: n, text: n + " (" + precos.models[n].tier + ")" });
      if (n === valor) o.selected = true;
      s.appendChild(o);
    });
    return s;
  }
  function numero(valor, aoMudar, attrs) {
    var a = Object.assign({ type: "number", value: valor == null ? "" : valor, min: "0", step: "1", oninput: aoMudar, inputmode: "numeric" }, attrs || {});
    return el("input", a);
  }

  // 1. Arquitetura -------------------------------------------------------
  function blocoArquitetura() {
    var arq = JSON.parse(JSON.stringify(arqExemplo));
    var bloco = el("section", { class: "lab-bloco", "aria-labelledby": "acl-arq" }, [
      el("h2", { id: "acl-arq", text: T.arqTitulo }),
      el("p", { class: "lab-sub", text: T.arqSub })
    ]);
    var entradas = el("div", { class: "lab-rolagem" });
    var resultado = el("div", { "aria-live": "polite" });
    bloco.appendChild(entradas);
    bloco.appendChild(resultado);
    bloco.appendChild(el("p", {}, [el("button", { class: "lab-botao", type: "button", text: T.restaurar, onclick: function () {
      arq = JSON.parse(JSON.stringify(arqExemplo)); desenharEntradas(); calcular();
    } })]));

    function desenharEntradas() {
      var tb = el("tbody");
      arq.components.forEach(function (c) {
        var loop = Object.prototype.hasOwnProperty.call(c, "prompt_base_tokens");
        tb.appendChild(el("tr", {}, [
          el("td", { text: c.name }),
          el("td", {}, [el("span", { class: "lab-papel", text: c.role })]),
          el("td", { class: "dir" }, [numero(c.monthly_volume, function (e) {
            if (e.target.value === "") delete c.monthly_volume; else c.monthly_volume = Number(e.target.value);
            calcular();
          }, { "aria-label": T.chamadas + ", " + c.name })]),
          el("td", {}, [selectModelo(c.model, function (e) { c.model = e.target.value; calcular(); })]),
          el("td", { class: "dir" }, [loop ? numero(c.max_iterations, function (e) {
            if (e.target.value === "") delete c.max_iterations; else c.max_iterations = Number(e.target.value);
            calcular();
          }, { min: "1", "aria-label": T.iteracoes + ", " + c.name }) : el("span", { text: "-" })]),
          el("td", {}, [el("input", { type: "checkbox", "aria-label": T.cache + ", " + c.name, onchange: function (e) { c.caching = e.target.checked; calcular(); } })])
        ]));
        tb.lastChild.querySelector("input[type=checkbox]").checked = c.caching !== false;
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
      var r = rodar("arch", { arch: arq, prices: precos });
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
        el("span", { class: "lab-total-rotulo", text: T.total })
      ]));
      resultado.appendChild(el("div", { class: "lab-rolagem" }, [el("table", { class: "lab-tabela" }, [
        el("thead", {}, [el("tr", {}, [T.componente, T.modelo, T.chamadas, T.entradaTarefa, T.custo, T.parte].map(function (h, i) {
          return el("th", { class: (i >= 2 && i <= 4) ? "dir" : "", text: h });
        }))]),
        linhas
      ])]));

      var avisos = [];
      res.components.forEach(function (c) {
        if (c.input_per_task_naive && c.input_per_task !== c.input_per_task_naive) {
          avisos.push("<strong>" + esc(c.name) + "</strong>: " + esc(t("enganoso", {
            n: fmtN.format(c.input_per_task), m: fmtN.format(c.input_per_task_naive), it: c.inflation.iterations })));
        }
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
    return bloco;
  }

  // dica flutuante compartilhada pelos graficos
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
  // o SVG desenha na largura real da caixa: com viewBox fixo, a letra cresceria junto com a tela
  function largura(caixa) { return Math.max(300, Math.round(caixa.clientWidth || 720)); }
  var redesenhos = [];
  var adiado;
  window.addEventListener("resize", function () {
    clearTimeout(adiado);
    adiado = setTimeout(function () { redesenhos.forEach(function (f) { f(); }); }, 150);
  });
  function compacto(v) { return new Intl.NumberFormat(LOCALE, { notation: "compact", maximumFractionDigits: 1 }).format(v); }

  // 2. Inflacao ----------------------------------------------------------
  function blocoInflacao() {
    var v = { base: 2000, delta: 500, n: 10 };
    var bloco = el("section", { class: "lab-bloco", "aria-labelledby": "acl-infl" }, [
      el("h2", { id: "acl-infl", text: T.inflTitulo }),
      el("p", { class: "lab-sub", text: T.inflSub })
    ]);
    var nRot = el("span", { class: "lab-num", text: String(v.n) });
    bloco.appendChild(el("div", { class: "lab-campos" }, [
      el("label", { class: "lab-campo" }, [T.base, numero(v.base, function (e) { v.base = Number(e.target.value) || 0; desenhar(); })]),
      el("label", { class: "lab-campo" }, [T.delta, numero(v.delta, function (e) { v.delta = Number(e.target.value) || 0; desenhar(); })]),
      el("label", { class: "lab-campo" }, [el("span", {}, [T.voltas + ": ", nRot]),
        el("input", { type: "range", min: "1", max: "30", value: String(v.n), oninput: function (e) { v.n = Number(e.target.value); nRot.textContent = e.target.value; desenhar(); } })])
    ]));
    var caixa = el("div", { class: "lab-grafico" });
    var frase = el("p", { class: "lab-frase", "aria-live": "polite" });
    bloco.appendChild(caixa);
    bloco.appendChild(el("ul", { class: "lab-legenda" }, [
      el("li", {}, [el("i", { class: "barra" }), T.lidoNaVolta]),
      el("li", {}, [el("i", { class: "tracejada" }), T.ingenuo])
    ]));
    bloco.appendChild(frase);

    function desenhar() {
      var r = rodar("infl", v);
      caixa.innerHTML = "";
      if (!r.ok) { frase.textContent = r.error; return; }
      var res = r.r, per = res.input_per_iteration;
      var W = largura(caixa), H = 260, m = { t: 12, r: 12, b: 34, l: 56 };
      var topo = topoBonito(Math.max.apply(null, per.concat([v.base])));
      var y = escala(0, topo, H - m.b, m.t);
      var passo = (W - m.l - m.r) / per.length, larg = Math.max(2, passo - 2);
      var svg = sv("svg", { viewBox: "0 0 " + W + " " + H, role: "img", "aria-label": frase.textContent });
      [0, .5, 1].forEach(function (f) {
        var yy = y(topo * f);
        svg.appendChild(sv("line", { class: f === 0 ? "eixo" : "grade", x1: m.l, x2: W - m.r, y1: yy, y2: yy }));
        svg.appendChild(sv("text", { x: m.l - 8, y: yy + 4, "text-anchor": "end" }, compacto(topo * f)));
      });
      var tip = dica(caixa);
      per.forEach(function (tok, i) {
        var x = m.l + i * passo + 1, yy = y(tok), h = (H - m.b) - yy;
        var barra = sv("path", { class: "serie-1", d: "M" + x + "," + (H - m.b) + "V" + (yy + Math.min(4, h)) + "q0,-4 4,-4H" + (x + larg - 4) + "q4,0 4,4V" + (H - m.b) + "Z" });
        svg.appendChild(barra);
        var alvo = sv("rect", { class: "alvo", x: m.l + i * passo, y: m.t, width: passo, height: H - m.b - m.t });
        alvo.addEventListener("mousemove", function (ev) {
          barra.classList.add("ativo");
          var bb = caixa.getBoundingClientRect();
          tip.mostrar(T.volta + " " + (i + 1) + ": <strong>" + fmtN.format(tok) + "</strong> " + T.tokens, ev.clientX - bb.left, ev.clientY - bb.top);
        });
        alvo.addEventListener("mouseleave", function () { barra.classList.remove("ativo"); tip.esconder(); });
        svg.appendChild(alvo);
        if (per.length <= 12 || i === 0 || i === per.length - 1 || (i + 1) % 5 === 0) {
          svg.appendChild(sv("text", { x: x + larg / 2, y: H - m.b + 18, "text-anchor": "middle" }, String(i + 1)));
        }
      });
      var yb = y(v.base);
      svg.appendChild(sv("line", { class: "linha-2", x1: m.l, x2: W - m.r, y1: yb, y2: yb }));
      caixa.insertBefore(svg, caixa.firstChild);
      frase.innerHTML = t("inflFrase", {
        n: res.iterations, t: fmtN.format(res.input_total), i: fmtN.format(res.input_total_naive),
        p: (res.overspend_pct >= 0 ? "+" : "") + fmtPct.format(res.overspend_pct / 100)
      });
      svg.setAttribute("aria-label", frase.textContent);
    }
    redesenhos.push(desenhar);
    requestAnimationFrame(desenhar);
    return bloco;
  }

  // 3. Cascata -----------------------------------------------------------
  function blocoCascata() {
    var nomes = nomesModelos();
    var v = {
      cheap: nomes.indexOf("Claude Haiku 4.5") >= 0 ? "Claude Haiku 4.5" : nomes[0],
      exp: nomes.indexOf("Claude Opus 5") >= 0 ? "Claude Opus 5" : nomes[nomes.length - 1],
      tin: 3000, tout: 500, tasks: 100000, rate: 0.6
    };
    var bloco = el("section", { class: "lab-bloco", "aria-labelledby": "acl-casc" }, [
      el("h2", { id: "acl-casc", text: T.cascTitulo }),
      el("p", { class: "lab-sub", text: T.cascSub })
    ]);
    var rRot = el("span", { class: "lab-num", text: fmtPct.format(v.rate) });
    bloco.appendChild(el("div", { class: "lab-campos" }, [
      el("label", { class: "lab-campo" }, [T.barato, selectModelo(v.cheap, function (e) { v.cheap = e.target.value; desenhar(); })]),
      el("label", { class: "lab-campo" }, [T.caro, selectModelo(v.exp, function (e) { v.exp = e.target.value; desenhar(); })]),
      el("label", { class: "lab-campo" }, [T.tin, numero(v.tin, function (e) { v.tin = Number(e.target.value) || 0; desenhar(); })]),
      el("label", { class: "lab-campo" }, [T.tout, numero(v.tout, function (e) { v.tout = Number(e.target.value) || 0; desenhar(); })]),
      el("label", { class: "lab-campo" }, [T.tarefas, numero(v.tasks, function (e) { v.tasks = Number(e.target.value) || 0; desenhar(); })]),
      el("label", { class: "lab-campo" }, [el("span", {}, [T.acerto + ": ", rRot]),
        el("input", { type: "range", min: "0", max: "100", value: String(v.rate * 100), oninput: function (e) { v.rate = Number(e.target.value) / 100; rRot.textContent = fmtPct.format(v.rate); desenhar(); } })])
    ]));
    var caixa = el("div", { class: "lab-grafico" });
    var frase = el("p", { class: "lab-frase", "aria-live": "polite" });
    bloco.appendChild(caixa);
    bloco.appendChild(el("ul", { class: "lab-legenda" }, [
      el("li", {}, [el("i", {}), T.cascata]),
      el("li", {}, [el("i", { class: "tracejada" }), T.direto])
    ]));
    bloco.appendChild(frase);
    bloco.appendChild(el("p", { class: "lab-rodape", text: T.cascCondicao }));

    function desenhar() {
      var r = rodar("casc", { prices: precos, cheap: v.cheap, exp: v.exp, tin: v.tin, tout: v.tout, tasks: v.tasks, rate: v.rate });
      caixa.innerHTML = "";
      if (!r.ok) { frase.textContent = r.error; return; }
      var res = r.r;
      var W = largura(caixa), H = 280, m = { t: 14, r: 16, b: 40, l: 64 };
      var topo = topoBonito(Math.max(res.curve[0][1], res.direct_cost));
      var x = escala(0, 1, m.l, W - m.r), y = escala(0, topo, H - m.b, m.t);
      var svg = sv("svg", { viewBox: "0 0 " + W + " " + H, role: "img" });
      [0, .5, 1].forEach(function (f) {
        var yy = y(topo * f);
        svg.appendChild(sv("line", { class: f === 0 ? "eixo" : "grade", x1: m.l, x2: W - m.r, y1: yy, y2: yy }));
        svg.appendChild(sv("text", { x: m.l - 8, y: yy + 4, "text-anchor": "end" }, "$" + compacto(topo * f)));
      });
      [0, .25, .5, .75, 1].forEach(function (f) {
        svg.appendChild(sv("text", { x: x(f), y: H - m.b + 18, "text-anchor": "middle" }, fmtPct.format(f)));
      });
      svg.appendChild(sv("text", { x: (m.l + W - m.r) / 2, y: H - 4, "text-anchor": "middle" }, T.acerto_eixo));
      var d = res.curve.map(function (p, i) { return (i ? "L" : "M") + x(p[0]).toFixed(1) + "," + y(p[1]).toFixed(1); }).join("");
      svg.appendChild(sv("path", { class: "linha-1", d: d }));
      svg.appendChild(sv("line", { class: "linha-2", x1: m.l, x2: W - m.r, y1: y(res.direct_cost), y2: y(res.direct_cost) }));
      var be = res.min_success_rate;
      if (be <= 1) {
        svg.appendChild(sv("line", { class: "marco", x1: x(be), x2: x(be), y1: m.t, y2: H - m.b }));
        svg.appendChild(sv("text", { class: "forte", x: x(be) + 6, y: m.t + 12 }, T.equilibrio + " " + fmtPct.format(be)));
      }
      svg.appendChild(sv("circle", { class: "ponto", cx: x(v.rate), cy: y(res.cascade_cost), r: 5 }));
      var tip = dica(caixa);
      var alvo = sv("rect", { class: "alvo", x: m.l, y: m.t, width: W - m.l - m.r, height: H - m.b - m.t });
      alvo.addEventListener("mousemove", function (ev) {
        var bb = svg.getBoundingClientRect(), escalaX = W / bb.width;
        var px = (ev.clientX - bb.left) * escalaX;
        var rate = Math.min(1, Math.max(0, (px - m.l) / (W - m.l - m.r)));
        var p = res.curve[Math.round(rate * 100)];
        var cb = caixa.getBoundingClientRect();
        tip.mostrar(fmtPct.format(p[0]) + ": " + T.cascata + " <strong>" + fmtUSD.format(p[1]) + "</strong><br>" + T.direto + " " + fmtUSD.format(res.direct_cost),
          ev.clientX - cb.left, ev.clientY - cb.top);
      });
      alvo.addEventListener("mouseleave", tip.esconder);
      svg.appendChild(alvo);
      caixa.insertBefore(svg, caixa.firstChild);
      var vars = {
        r: fmtPct.format(v.rate), c: fmtUSD.format(res.cascade_cost), d: fmtUSD.format(res.direct_cost),
        s: fmtPct.format(Math.abs(res.saving_pct) / 100), b: fmtPct.format(be)
      };
      frase.innerHTML = t(res.worth_it ? "cascVale" : "cascNaoVale", vars);
      svg.setAttribute("aria-label", frase.textContent);
    }
    redesenhos.push(desenhar);
    requestAnimationFrame(desenhar);
    return bloco;
  }

  // 4. Precos ------------------------------------------------------------
  function blocoPrecos() {
    var bloco = el("section", { class: "lab-bloco", "aria-labelledby": "acl-precos" }, [el("h2", { id: "acl-precos", text: T.precosTitulo })]);
    var quando = precos.pricing_as_of || "?";
    var origem;
    if (precosVivos) {
      var data = new Date(quando);
      var horas = (Date.now() - data.getTime()) / 36e5;
      var idade = isFinite(horas) ? new Intl.RelativeTimeFormat(LOCALE, { numeric: "auto" }).format(-Math.round(horas), "hour") : "?";
      origem = t("precosVivo", { quando: esc(isFinite(horas) ? data.toLocaleString(LOCALE, { dateStyle: "medium", timeStyle: "short", timeZone: "UTC" }) + " UTC" : quando), idade: esc(idade) });
    } else {
      origem = t("precosMao", { quando: esc(quando) });
    }
    bloco.appendChild(el("p", { class: "lab-precos-origem", html: origem }));
    var tb = el("tbody");
    nomesModelos().forEach(function (n) {
      var mm = precos.models[n];
      function pm(v) { return v == null ? "-" : fmtPreco.format(v * 1000); }
      tb.appendChild(el("tr", {}, [
        el("td", { text: n }), el("td", { text: mm.tier }),
        el("td", { class: "dir lab-num", text: pm(mm.input_per_1k) }),
        el("td", { class: "dir lab-num", text: pm(mm.output_per_1k) }),
        el("td", { class: "dir lab-num", text: pm(mm.cache_read_per_1k) }),
        el("td", { class: "dir lab-num", text: pm(mm.cache_write_per_1k) }),
        el("td", { class: "dir lab-num", text: mm.min_cache_tokens ? fmtN.format(mm.min_cache_tokens) : "-" })
      ]));
    });
    bloco.appendChild(el("div", { class: "lab-rolagem" }, [el("table", { class: "lab-tabela" }, [
      el("thead", {}, [el("tr", {}, [T.modelo, "tier", "USD " + T.entrada, "USD " + T.saida, "USD " + T.leitura, "USD " + T.escrita, T.piso].map(function (h, i) {
        return el("th", { class: i >= 2 ? "dir" : "", text: h });
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
