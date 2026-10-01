"""Converte os artigos do export do LinkedIn em page bundles do Hugo.

Fonte: Configuracoes > Privacidade de dados > Obter uma copia dos seus dados > Artigos.
O export chega como um HTML por artigo em Articles/Articles/. Cada artigo vira
content/<idioma>/articles/<slug>/index.md com as imagens dentro da propria pasta.

O export e a fonte do TEXTO. A pagina publica do artigo so preenche o que o export
perde, e ele perde quatro coisas:
  1. blocos de codigo: o LinkedIn exporta a maior parte dos <pre> VAZIOS;
  2. codigo inline: `SELECT`, `.claude/skills/` e afins somem do meio da frase,
     e o paragrafo sai como "Comecamos pelo , mas...";
  3. legendas de figura: boa parte sai vazia;
  4. a capa: o export traz a capa numa URL curta que responde 404.
Os <pre> vazios e as legendas sao preenchidos pelo elemento de mesma posicao da
pagina publica, e so quando as duas contagens batem. Um paragrafo so e trocado pela
versao publica quando o texto publico e o texto do export MAIS insercoes, nunca com
palavra removida ou trocada, entao o texto da autora so e completado, nunca reescrito.
O que nao passa nessas regras fica como veio, marcado no relatorio.

As imagens do corpo vem em URLs assinadas que expiram (parametro e=<epoch>), entao
o script baixa todas para dentro do bundle.

Uso:
  python tools/linkedin_to_hugo.py --export Complete_LinkedInDataExport.zip
  python tools/linkedin_to_hugo.py --export pasta_extraida --sem-pagina-publica
  python tools/linkedin_to_hugo.py --export x.zip --so "wandavision" --force
"""
from __future__ import annotations

import argparse
import difflib
import html
import json
import re
import sys
import tempfile
import time
import unicodedata
import urllib.parse
import urllib.request
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

try:
    from bs4 import BeautifulSoup, NavigableString, Tag
    from markdownify import markdownify
except ImportError:
    sys.exit("Faltam dependencias: pip install -r tools/requirements.txt")

RAIZ = Path(__file__).resolve().parent.parent
CACHE = RAIZ / ".cache" / "linkedin"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
PAUSA_ENTRE_PAGINAS = 2.0

LINGUAGENS = {
    "bash", "sh", "shell", "powershell", "ps1", "python", "py", "sql", "tsql", "plsql",
    "yaml", "yml", "json", "markdown", "md", "javascript", "js", "typescript", "ts",
    "csharp", "cs", "java", "scala", "r", "html", "xml", "css", "dax", "kql", "toml",
    "dockerfile", "hcl", "terraform", "go", "rust", "text", "plaintext",
}

# Tag do blog -> padroes procurados no titulo e no corpo. Os padroes casam contra o
# texto minusculo e SEM acento; o nome da tag e o que aparece no site, com acento.
TAGS = {
    "Azure": [r"\bazure\b"],
    "Microsoft Fabric": [r"\bfabric\b"],
    "Databricks": [r"databricks"],
    "Power BI": [r"power ?bi"],
    "Snowflake": [r"snowflake"],
    "Oracle": [r"\boracle\b"],
    "AWS": [r"\baws\b", r"bedrock"],
    "Google Cloud": [r"\bgcp\b", r"google cloud", r"vertex"],
    "Agentes de IA": [r"\bagentes?\b", r"\bagentic", r"\bagents?\b"],
    "IA Generativa": [r"generativa", r"\bgenai\b", r"\bllms?\b", r"\bgpt"],
    "Claude": [r"\bclaude\b", r"anthropic"],
    "Copilot": [r"copilot"],
    "MCP": [r"\bmcp\b", r"model context protocol"],
    "RAG": [r"\brag\b", r"retrieval"],
    "Prompt Engineering": [r"\bprompts?\b"],
    "Engenharia de Dados": [r"engenh\w* de dados", r"data engineer", r"pipelines?", r"\betl\b"],
    "Arquitetura de Dados": [r"lakehouse", r"data mesh", r"arquitetura de dados", r"medall?ion"],
    "Governança de Dados": [r"governanca", r"unity catalog", r"purview", r"\blgpd\b"],
    "SQL": [r"\bsql\b"],
    "Custos": [r"\bfinops\b", r"\bcustos?\b", r"\btokens?\b"],
    "Segurança": [r"seguranca", r"security", r"\bzero trust\b"],
    "Carreira": [r"carreira", r"certifica", r"\bmvp\b", r"mentoria"],
}
MAX_TAGS = 6
EN_STOP = {"the", "and", "of", "to", "is", "in", "that", "for", "with", "this", "you", "are"}
PT_STOP = {"de", "que", "para", "com", "uma", "os", "as", "do", "da", "em", "nao", "voce", "mais"}


@dataclass
class Resultado:
    arquivo: str
    titulo: str = ""
    destino: str = ""
    idioma: str = "pt"
    imagens: int = 0
    imagens_falhas: list[str] = field(default_factory=list)
    codigo_recuperado: int = 0
    codigo_pendente: int = 0
    paragrafos_completados: int = 0
    paragrafos_divergentes: int = 0
    legendas_recuperadas: int = 0
    capa: str = "ausente"
    status: str = "ok"


def sem_acento(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()


def slug_de(url: str, com_id: bool = False) -> str:
    """Slug a partir da URL do LinkedIn, sem o sufixo '-lopes-xxxxx'.

    Artigos de uma serie dividem o mesmo prefixo de URL e so se distinguem pelo
    sufixo, entao `com_id=True` mantem o id. O cache usa sempre o id; a pasta do
    bundle so o usa quando dois artigos colidiriam.
    """
    bruto = urllib.parse.unquote(url.rstrip("/").rsplit("/", 1)[-1])
    m = re.search(r"-lopes(?:-([a-z0-9]{4,6}))?$", bruto)
    ident = (m.group(1) or "") if m else ""
    bruto = bruto[: m.start()] if m else bruto
    s = re.sub(r"[^a-z0-9]+", "-", sem_acento(bruto).lower()).strip("-")[:90].rstrip("-") or "artigo"
    return f"{s}-{ident}" if com_id and ident else s


def link_de(arquivo: Path) -> str:
    m = re.search(r'<h1><a href="([^"]+)"', arquivo.read_text(encoding="utf-8"))
    return m.group(1) if m else ""


def baixar(url: str, timeout: int = 30) -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "pt-BR,pt;q=0.9"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read(), r.headers.get("Content-Type", "")


def extensao(content_type: str, url: str) -> str:
    ct = content_type.split(";")[0].strip().lower()
    mapa = {"image/jpeg": ".jpg", "image/png": ".png", "image/gif": ".gif",
            "image/webp": ".webp", "image/svg+xml": ".svg"}
    if ct in mapa:
        return mapa[ct]
    m = re.search(r"\.(jpe?g|png|gif|webp)(\?|$)", url, re.I)
    return "." + m.group(1).lower().replace("jpeg", "jpg") if m else ".jpg"


def pagina_publica(url: str) -> str | None:
    """HTML da pagina publica, com cache em disco para nao bater no LinkedIn de novo."""
    CACHE.mkdir(parents=True, exist_ok=True)
    alvo = CACHE / f"{slug_de(url, com_id=True)}.html"
    if alvo.exists():
        return alvo.read_text(encoding="utf-8")
    try:
        dados, _ = baixar(url)
    except Exception:
        return None
    texto = dados.decode("utf-8", "ignore")
    if "<pre" not in texto and "og:image" not in texto:
        return None  # authwall ou pagina de erro
    alvo.write_text(texto, encoding="utf-8")
    time.sleep(PAUSA_ENTRE_PAGINAS)
    return texto


BLOCOS = ["p", "li", "h1", "h2", "h3", "h4", "blockquote"]


LARGURA_ZERO = re.compile("[​‌‍⁠﻿]")


def corrido(t: str) -> str:
    return re.sub(r"\s+", " ", LARGURA_ZERO.sub("", t)).strip()


def folhas(raiz: Tag) -> list[Tag]:
    """Blocos de texto sem bloco aninhado, na ordem do documento."""
    return [b for b in raiz.find_all(BLOCOS) if not b.find(BLOCOS + ["ul", "ol", "pre"])
            and corrido(b.get_text(""))]


def so_insercoes(curto: str, longo: str) -> bool:
    """True quando `longo` e `curto` com trechos inseridos, sem nada removido ou trocado."""
    if len(longo) <= len(curto):
        return False
    for op, i1, i2, _, _ in difflib.SequenceMatcher(None, curto, longo, autojunk=False).get_opcodes():
        if op in ("delete", "replace") and curto[i1:i2].strip():
            return False
    return True


def inline_da_pagina(origem: Tag, soup: BeautifulSoup) -> list:
    """Converte o inline da pagina publica (spans com classe) em strong/em/a/br."""
    saida = []
    for no in origem.children:
        if isinstance(no, NavigableString):
            if type(no) is NavigableString:  # ignora comentarios
                saida.append(NavigableString(str(no)))
            continue
        if no.name == "br":
            saida.append(soup.new_tag("br"))
            continue
        filhos = inline_da_pagina(no, soup)
        classes = " ".join(no.get("class", []))
        if no.name == "a" and no.get("href"):
            envelope = [soup.new_tag("a", href=no["href"])]
        else:
            envelope = []
            if no.name in ("strong", "b") or "font-[700]" in classes:
                envelope.append(soup.new_tag("strong"))
            if no.name in ("em", "i") or "italic" in classes:
                envelope.append(soup.new_tag("em"))
        if not envelope or not no.get_text().strip():
            saida.extend(filhos)
            continue
        externo = envelope[0]
        atual = externo
        for t in envelope[1:]:
            atual.append(t)
            atual = t
        for f in filhos:
            atual.append(f)
        saida.append(externo)
    return saida


def completar_paragrafos(corpo: Tag, raiz_pub: Tag, soup: BeautifulSoup, res: Resultado) -> None:
    exp, pub = folhas(corpo), folhas(raiz_pub)
    te = [corrido(b.get_text("")) for b in exp]
    tp = [corrido(b.get_text("")) for b in pub]
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, te, tp, autojunk=False).get_opcodes():
        if op != "replace":
            continue
        # Dentro do trecho desalinhado (o widget "Recomendados pelo LinkedIn" fica dentro
        # do container e empurra a contagem), pareia em ordem: cada bloco do export
        # procura adiante o primeiro bloco publico que seja ele mesmo mais insercoes.
        j = j1
        for i in range(i1, i2):
            achou = None
            for k in range(j, j2):
                if so_insercoes(te[i], tp[k]):
                    achou = k
                    break
            if achou is None:
                res.paragrafos_divergentes += 1
                continue
            novos = inline_da_pagina(pub[achou], soup)
            exp[i].clear()
            for n in novos:
                exp[i].append(n)
            res.paragrafos_completados += 1
            j = achou + 1


def completar_legendas(corpo: Tag, raiz_pub: Tag, res: Resultado) -> None:
    figs, figs_pub = corpo.find_all("figure"), raiz_pub.find_all("figure")
    if len(figs) != len(figs_pub):
        return
    for fig, fpub in zip(figs, figs_pub):
        leg, leg_pub = fig.find("figcaption"), fpub.find("figcaption")
        if leg is None or leg_pub is None:
            continue
        texto = corrido(leg_pub.get_text(" "))
        if texto and not corrido(leg.get_text(" ")):
            leg.string = texto
            res.legendas_recuperadas += 1


def texto_de_pre(pre: Tag) -> str:
    return html.unescape(pre.get_text()).replace("\r\n", "\n").strip("\n")


def cerca(codigo: str) -> str:
    linhas = codigo.split("\n")
    lang = ""
    if linhas and linhas[0].strip().lower() in LINGUAGENS:
        lang = linhas[0].strip().lower()
        linhas = linhas[1:]
    corpo = "\n".join(linhas).strip("\n")
    marca = "```"
    while marca in corpo:
        marca += "`"
    return f"{marca}{lang}\n{corpo}\n{marca}"


def detectar_idioma(texto: str) -> str:
    palavras = re.findall(r"[a-z]+", sem_acento(texto.lower()))
    en = sum(p in EN_STOP for p in palavras)
    pt = sum(p in PT_STOP for p in palavras)
    return "en" if en > pt * 1.5 else "pt"


def escolher_tags(titulo: str, corpo: str) -> list[str]:
    t = sem_acento(titulo.lower())
    c = sem_acento(corpo.lower())
    pontos = {}
    for tag, padroes in TAGS.items():
        n = sum(len(re.findall(p, c)) for p in padroes) + 5 * sum(bool(re.search(p, t)) for p in padroes)
        if n >= 3:
            pontos[tag] = n
    return [k for k, _ in sorted(pontos.items(), key=lambda kv: -kv[1])][:MAX_TAGS]


def resumo(corpo: Tag) -> str:
    for p in corpo.find_all("p"):
        t = re.sub(r"\s+", " ", p.get_text(" ")).strip()
        if len(t) >= 60:
            if len(t) <= 220:
                return t
            return t[:220].rsplit(" ", 1)[0].rstrip(",.;:") + "…"
    return ""


def yaml_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def converter(arquivo: Path, conteudo: Path, usar_pagina: bool, force: bool, slug: str) -> Resultado:
    res = Resultado(arquivo=arquivo.name)
    soup = BeautifulSoup(arquivo.read_text(encoding="utf-8"), "html.parser")
    titulo = (soup.title.get_text() if soup.title else "").strip()
    link = soup.find("h1").find("a")["href"]
    data = re.search(r"Published on (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2})", soup.get_text())
    corpo = soup.body.find("div", recursive=False)
    res.titulo = titulo
    if not (titulo and data and corpo):
        res.status = "estrutura inesperada, artigo ignorado"
        return res

    res.idioma = detectar_idioma(corpo.get_text(" "))
    destino = conteudo / res.idioma / "articles" / slug
    res.destino = str(destino.relative_to(RAIZ))
    if destino.exists() and not force:
        res.status = "ja existe, mantido (use --force para regravar)"
        return res
    destino.mkdir(parents=True, exist_ok=True)

    publica = pagina_publica(link) if usar_pagina else None
    soup_pub = BeautifulSoup(publica, "html.parser") if publica else None
    raiz_pub = None
    if soup_pub:
        raiz_pub = soup_pub.find(attrs={"data-test-id": "article-content-blocks"}) or soup_pub

    if raiz_pub is not None:
        completar_paragrafos(corpo, raiz_pub, soup, res)
        completar_legendas(corpo, raiz_pub, res)

    # Codigo: a pagina publica preenche o <pre> vazio de mesma posicao.
    pres = corpo.find_all("pre")
    pres_pub = raiz_pub.find_all("pre") if raiz_pub is not None else []
    alinhado = len(pres_pub) == len(pres)
    blocos: dict[str, str] = {}
    for i, pre in enumerate(pres):
        codigo = texto_de_pre(pre)
        if not codigo.strip() and alinhado:
            codigo = texto_de_pre(pres_pub[i])
            if codigo.strip():
                res.codigo_recuperado += 1
        if not codigo.strip():
            res.codigo_pendente += 1
            bloco = f"<!-- TODO: bloco de codigo {i + 1} veio vazio no export; copiar de {link} -->"
        else:
            bloco = cerca(codigo)
        chave = f"BLOCOCODIGO{i:03d}X"
        blocos[chave] = bloco
        pre.replace_with(NavigableString(f"\n\n{chave}\n\n"))

    # Imagens do corpo: baixar tudo, as URLs assinadas expiram.
    for n, img in enumerate(corpo.find_all("img"), start=1):
        src = img.get("src", "")
        try:
            dados, ct = baixar(src)
            nome = f"img-{n:02d}{extensao(ct, src)}"
            (destino / nome).write_bytes(dados)
            img["src"] = nome
            res.imagens += 1
        except Exception:
            res.imagens_falhas.append(src)
    for fig in corpo.find_all("figure"):
        legenda = fig.find("figcaption")
        texto = legenda.get_text(" ").strip() if legenda else ""
        img = fig.find("img")
        if legenda:
            legenda.decompose()
        if img is not None:
            img["alt"] = texto
            img.attrs = {"src": img.get("src", ""), "alt": texto}
        if texto:
            fig.append(soup.new_tag("p"))
            fig.find_all("p")[-1].string = f"_{texto}_"
        fig.unwrap()

    # Capa: a URL do export responde 404; o og:image da pagina publica funciona.
    capa = None
    if soup_pub:
        meta = soup_pub.find("meta", property="og:image")
        if meta and meta.get("content"):
            try:
                dados, ct = baixar(html.unescape(meta["content"]))
                capa = f"cover{extensao(ct, meta['content'])}"
                (destino / capa).write_bytes(dados)
                res.capa = "pagina publica"
            except Exception:
                capa = None

    md = markdownify(str(corpo), heading_style="ATX", bullets="-", strong_em_symbol="*")
    for chave, bloco in blocos.items():
        md = md.replace(chave, bloco)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"

    fm = [
        "---",
        f"title: {yaml_str(titulo)}",
        f"date: {data.group(1)}T{data.group(2)}:00Z",
        f"summary: {yaml_str(resumo(corpo))}",
        f"tags: {json.dumps(escolher_tags(titulo, corpo.get_text(' ')), ensure_ascii=False)}",
        "series: [\"Ahead of the AI\"]",
        f"linkedin: {yaml_str(link)}",
    ]
    if capa:
        fm += ["cover:", f"  image: {capa}", f"  alt: {yaml_str(titulo)}", "  relative: true"]
    if res.codigo_pendente:
        fm.append("# revisar: ha blocos de codigo marcados com TODO no corpo")
    fm.append("---")
    (destino / "index.md").write_text("\n".join(fm) + "\n\n" + md, encoding="utf-8", newline="\n")
    return res


def localizar_artigos(export: Path) -> tuple[list[Path], tempfile.TemporaryDirectory | None]:
    tmp = None
    base = export
    if export.is_file() and zipfile.is_zipfile(export):
        tmp = tempfile.TemporaryDirectory()
        with zipfile.ZipFile(export) as z:
            for m in z.namelist():
                if m.startswith("Articles/") and m.endswith(".html"):
                    z.extract(m, tmp.name)
        base = Path(tmp.name)
    arquivos = sorted(base.rglob("Articles/**/*.html")) or sorted(base.rglob("*.html"))
    return arquivos, tmp


def relatorio(resultados: list[Resultado], caminho: Path) -> None:
    linhas = ["# Relatorio da ultima migracao", "",
              "Paragrafo divergente: o texto publico difere do export por algo alem de insercao,",
              "entao ficou o texto do export. Vale abrir o original e comparar.", "",
              "| Artigo | Idioma | Imagens | Codigo recuperado | Codigo pendente | Paragrafos completados "
              "| Paragrafos divergentes | Legendas | Capa | Status |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for r in resultados:
        falhas = f" ({len(r.imagens_falhas)} falharam)" if r.imagens_falhas else ""
        linhas.append(f"| {r.titulo.replace('|', '/')} | {r.idioma} | {r.imagens}{falhas} | "
                      f"{r.codigo_recuperado} | {r.codigo_pendente} | {r.paragrafos_completados} | "
                      f"{r.paragrafos_divergentes} | {r.legendas_recuperadas} | {r.capa} | {r.status} |")
    caminho.write_text("\n".join(linhas) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--export", required=True, type=Path, help="ZIP do export ou pasta extraida")
    ap.add_argument("--content", type=Path, default=RAIZ / "content")
    ap.add_argument("--sem-pagina-publica", action="store_true",
                    help="nao consultar a pagina publica (sem capa e sem recuperar codigo)")
    ap.add_argument("--force", action="store_true", help="regravar bundles que ja existem")
    ap.add_argument("--so", help="converter so os arquivos cujo nome contem este trecho")
    a = ap.parse_args()

    todos, tmp = localizar_artigos(a.export)
    arquivos = [f for f in todos if a.so.lower() in f.name.lower()] if a.so else todos
    if not arquivos:
        print("Nenhum artigo encontrado no export.", file=sys.stderr)
        return 1
    # Slugs calculados antes, sobre o export inteiro: quem colide mantem o id do LinkedIn.
    # Com --so o calculo continua sobre todos, para o slug nao mudar conforme o filtro.
    links = {f: link_de(f) for f in todos}
    contagem: dict[str, int] = {}
    for u in links.values():
        contagem[slug_de(u)] = contagem.get(slug_de(u), 0) + 1
    slugs = {f: slug_de(u, com_id=contagem[slug_de(u)] > 1) for f, u in links.items()}

    resultados = []
    for i, f in enumerate(arquivos, start=1):
        try:
            r = converter(f, a.content, not a.sem_pagina_publica, a.force, slugs[f])
        except Exception as e:  # um artigo quebrado nao derruba os outros
            r = Resultado(arquivo=f.name, status=f"erro: {e}")
        resultados.append(r)
        print(f"[{i}/{len(arquivos)}] {r.status:<10} {r.titulo[:70]}", flush=True)
    if tmp:
        tmp.cleanup()
    relatorio(resultados, RAIZ / "tools" / "ultima-migracao.md")
    ok = [r for r in resultados if r.status == "ok"]
    print(json.dumps({
        "artigos": len(resultados),
        "convertidos": len(ok),
        "outros_status": len(resultados) - len(ok),
        "por_idioma": {k: sum(r.idioma == k for r in ok) for k in ("pt", "en")},
        "imagens": sum(r.imagens for r in ok),
        "imagens_falhas": sum(len(r.imagens_falhas) for r in ok),
        "codigo_recuperado": sum(r.codigo_recuperado for r in ok),
        "codigo_pendente": sum(r.codigo_pendente for r in ok),
        "paragrafos_completados": sum(r.paragrafos_completados for r in ok),
        "paragrafos_divergentes": sum(r.paragrafos_divergentes for r in ok),
        "legendas_recuperadas": sum(r.legendas_recuperadas for r in ok),
        "sem_capa": sum(r.capa == "ausente" for r in ok),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
