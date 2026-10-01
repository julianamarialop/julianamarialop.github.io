"""Confere a traducao EN de cada artigo contra o original PT.

Uma traducao pode sair fluente e ainda assim cortar um paragrafo, perder um bloco
de codigo ou trocar uma imagem, e nada disso aparece lendo so o ingles. Este
script compara a estrutura dos dois arquivos e falha quando ela diverge.

Confere, por artigo:
  - a traducao existe e tem front matter com title, slug, date, summary e tags;
  - date, linkedin e cover.image iguais ao original;
  - tags so do vocabulario EN (TAGS_EN), na mesma quantidade e ordem do original;
  - mesmo numero de titulos (por nivel), itens de lista, imagens e links;
  - blocos de codigo identicos byte a byte, na mesma ordem;
  - nenhum travessao (em dash) e nenhum resto de portugues no titulo;
  - tamanho do texto entre 70% e 140% do original (corte ou enxerto).

Uso:
  python tools/check_translation.py              # todos
  python tools/check_translation.py slug1 slug2  # so estes
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PT = RAIZ / "content" / "pt" / "articles"
EN = RAIZ / "content" / "en" / "articles"

TAGS_EN = {
    "Azure": "Azure",
    "Microsoft Fabric": "Microsoft Fabric",
    "Databricks": "Databricks",
    "Power BI": "Power BI",
    "Snowflake": "Snowflake",
    "Oracle": "Oracle",
    "AWS": "AWS",
    "Google Cloud": "Google Cloud",
    "Agentes de IA": "AI Agents",
    "IA Generativa": "Generative AI",
    "Claude": "Claude",
    "Copilot": "Copilot",
    "MCP": "MCP",
    "RAG": "RAG",
    "Prompt Engineering": "Prompt Engineering",
    "Engenharia de Dados": "Data Engineering",
    "Arquitetura de Dados": "Data Architecture",
    "Governança de Dados": "Data Governance",
    "SQL": "SQL",
    "Custos": "Costs",
    "Segurança": "Security",
    "Carreira": "Career",
}

CERCA = re.compile(r"^(`{3,})[^\n]*\n(.*?)^\1\s*$", re.M | re.S)


def separar(texto: str) -> tuple[dict, str]:
    m = re.match(r"---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return {}, texto
    fm: dict = {}
    bloco = None
    for linha in m.group(1).splitlines():
        if not linha.strip() or linha.lstrip().startswith("#"):
            continue
        if linha.startswith("  ") and bloco:
            k, _, v = linha.strip().partition(":")
            fm.setdefault(bloco, {})[k.strip()] = v.strip()
            continue
        k, _, v = linha.partition(":")
        k, v = k.strip(), v.strip()
        if v == "":
            bloco = k
            fm[k] = {}
            continue
        bloco = None
        try:
            fm[k] = json.loads(v)
        except Exception:
            fm[k] = v.strip('"')
    return fm, texto[m.end():]


def estrutura(corpo: str) -> dict:
    codigos = [c.group(2) for c in CERCA.finditer(corpo)]
    sem_codigo = CERCA.sub("", corpo)
    return {
        "codigos": codigos,
        "h2": len(re.findall(r"^## ", sem_codigo, re.M)),
        "h3": len(re.findall(r"^### ", sem_codigo, re.M)),
        "h4": len(re.findall(r"^#### ", sem_codigo, re.M)),
        "itens": len(re.findall(r"^\s*(?:[-*]|\d+\.) ", sem_codigo, re.M)),
        "imagens": re.findall(r"!\[[^\]]*\]\(([^)\s]+)", sem_codigo),
        "links": len(re.findall(r"(?<!!)\[[^\]]*\]\([^)]+\)", sem_codigo)),
        "palavras": len(re.findall(r"\w+", sem_codigo)),
    }


def conferir(slug: str) -> list[str]:
    erros = []
    pt_txt = (PT / slug / "index.md").read_text(encoding="utf-8")
    alvo = EN / slug / "index.md"
    if not alvo.exists():
        return ["traducao ausente"]
    en_txt = alvo.read_text(encoding="utf-8")
    fpt, cpt = separar(pt_txt)
    fen, cen = separar(en_txt)

    for campo in ("title", "slug", "date", "summary"):
        if not fen.get(campo):
            erros.append(f"front matter sem {campo}")
    if "tags" not in fen:
        erros.append("front matter sem tags")
    for campo in ("date", "linkedin"):
        if fpt.get(campo) != fen.get(campo):
            erros.append(f"{campo} diferente do original")
    if (fpt.get("cover") or {}).get("image") != (fen.get("cover") or {}).get("image"):
        erros.append("cover.image diferente do original")
    esperadas = [TAGS_EN.get(t, f"?{t}") for t in fpt.get("tags") or []]
    if (fen.get("tags") or []) != esperadas:
        erros.append(f"tags {fen.get('tags')} deveriam ser {esperadas}")
    if fen.get("slug") and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(fen["slug"])):
        erros.append(f"slug invalido: {fen['slug']}")
    if fen.get("title") and fen.get("title") == fpt.get("title") and re.search(r"[ãõçáéíóúâêô]", str(fen["title"]), re.I):
        erros.append("titulo nao traduzido")

    if "—" in en_txt:
        erros.append(f"{en_txt.count(chr(0x2014))} travessao(oes) no texto")

    a, b = estrutura(cpt), estrutura(cen)
    if a["codigos"] != b["codigos"]:
        erros.append(f"blocos de codigo diferentes ({len(a['codigos'])} no PT, {len(b['codigos'])} no EN, ou conteudo alterado)")
    for k in ("h2", "h3", "h4", "itens", "links"):
        if a[k] != b[k]:
            erros.append(f"{k}: {a[k]} no PT, {b[k]} no EN")
    if a["imagens"] != b["imagens"]:
        erros.append(f"imagens diferentes: {a['imagens']} x {b['imagens']}")
    if a["palavras"]:
        razao = b["palavras"] / a["palavras"]
        if not 0.7 <= razao <= 1.4:
            erros.append(f"tamanho {razao:.0%} do original")
    return erros


def main() -> int:
    slugs = sys.argv[1:] or sorted(p.name for p in PT.iterdir() if p.is_dir())
    falhas = 0
    for s in slugs:
        erros = conferir(s)
        if erros:
            falhas += 1
            print(f"FALHA {s}")
            for e in erros:
                print(f"   - {e}")
    print(f"{len(slugs) - falhas}/{len(slugs)} traducoes conferidas sem divergencia")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
