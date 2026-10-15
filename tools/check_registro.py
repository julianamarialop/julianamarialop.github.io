# -*- coding: utf-8 -*-
"""Verificacao de registro: barra linguagem coloquial em texto publico.

    python tools/check_registro.py                  # arquivos da calculadora
    python tools/check_registro.py caminho [...]    # quaisquer outros arquivos

Existe porque reler nao bastou: o texto da calculadora de custo de agentes saiu
publicado com "quantas voltas o loop da" e "a gente precifica na mesa". Regra
que depende de lembrar falha em silencio; esta sai com erro e lista cada
ocorrencia com o substituto.

Roda no workflow antes do build do Hugo. Termos tecnicos correntes ("janela de
contexto", "pipeline", "loop" em codigo) nao sao coloquialismo e ficam de fora.
"""
from __future__ import annotations

import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
PADRAO = [
    RAIZ / "content" / "pt" / "agent-cost" / "index.md",
    RAIZ / "content" / "en" / "agent-cost" / "index.md",
    RAIZ / "assets" / "js" / "agent-cost-lab.js",
]

# (expressao, substituto sugerido)
REGRAS_PT = [
    (r"\bd[áa]\s+voltas?\b|\bvoltas?\b", "iteração / iterações"),
    (r"\ba gente\b", "nós, ou construção impessoal"),
    (r"\bdespej\w*", "apresenta de uma só vez"),
    (r"\bo motor\b|\bmotor python\b", "o código / a calculadora"),
    (r"\brod(a|ar|ando|ou|e|ada)\b", "executa / executar / execução"),
    (r"\bvir(a|ar|ou)\b", "é convertido em / passa a ser"),
    (r"\bcabe\b|\bn[ãa]o cabe\b", "é comportado por / excede"),
    (r"\ba conta\b|\bda conta\b|\bna conta\b", "o custo / a estimativa"),
    (r"\bsome\b|\bsumir\b", "desaparece"),
    (r"\bningu[ée]m percebe\b", "sem que a omissão seja percebida"),
    (r"\bmex(e|er|a)\b", "altera / alterar"),
    (r"\bbonit\w*", "favorável"),
    (r"\barmadilha\b", "risco / distorção"),
    (r"\brende\b|\bdeixe correr\b", "(remover)"),
    (r"\bbasta\b", "requer apenas"),
    (r"\bpega\b|\bpegar\b", "identifica / identificar"),
    (r"\bt[áa]\b|\bpra\b|\bpro\b", "está / para / para o"),
]
REGRAS_EN = [
    (r"\bfree win\b", "a saving without conditions"),
    (r"\broom to breathe\b", "financial headroom"),
    (r"\bnobody notices\b", "without the omission being noticed"),
    (r"\bhammer\w*", "repeated requests"),
    (r"\bwhole point\b", "the purpose"),
    (r"\bundeniable\b", "demonstrated"),
    (r"\bthe trap\b", "the distortion"),
    (r"\blet it run\b|\bgoes wrong quietly\b", "(rephrase)"),
    (r"\bwe price it\b", "we estimate its cost"),
]
COMUNS = [(r"[—–]", "vírgula, dois-pontos ou ponto (nunca travessão)")]


def regras_para(caminho: pathlib.Path, linha: str):
    return REGRAS_PT + REGRAS_EN + COMUNS


def verificar(caminhos) -> list:
    achados = []
    for caminho in caminhos:
        texto = pathlib.Path(caminho).read_text(encoding="utf-8")
        for n, linha in enumerate(texto.splitlines(), 1):
            for expr, sugestao in regras_para(caminho, linha):
                for m in re.finditer(expr, linha, re.IGNORECASE):
                    achados.append((str(caminho), n, m.group(0), sugestao))
    return achados


def main(argv) -> int:
    caminhos = [pathlib.Path(a) for a in argv] or PADRAO
    achados = verificar(caminhos)
    if not achados:
        print("registro: nenhuma ocorrencia em %d arquivo(s)" % len(caminhos))
        return 0
    print("registro: %d ocorrencia(s) de linguagem coloquial" % len(achados))
    for caminho, n, trecho, sugestao in achados:
        print("  %s:%d  %r  ->  %s" % (caminho, n, trecho, sugestao))
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
