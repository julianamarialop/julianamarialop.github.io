# -*- coding: utf-8 -*-
"""Copia o motor da calculadora de custo de agentes para static/agent-cost-math/,
para a pagina /agent-cost/ funcionar no `hugo server` local.

No site publicado quem faz isso e o workflow (.github/workflows/hugo.yml), a
partir do repositorio publico. Aqui a origem e o clone vizinho:

    python tools/agent_cost_engine.py                 # copia e busca os precos
    python tools/agent_cost_engine.py --sem-precos    # so copia (a pagina usa a tabela manual)
    python tools/agent_cost_engine.py --origem ../outro/agent-cost-math

A pasta de destino esta no .gitignore: o motor nunca e versionado no blog, para
a pagina e o `git clone` rodarem sempre o mesmo arquivo.
"""
from __future__ import annotations

import argparse
import pathlib
import shutil
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
DESTINO = RAIZ / "static" / "agent-cost-math"
ARQUIVOS = ("agent_cost.py", "live_prices.py", "architecture.example.json", "prices.example.json")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--origem", default=str(RAIZ.parent / "agent-cost-math"))
    ap.add_argument("--sem-precos", action="store_true")
    a = ap.parse_args()

    origem = pathlib.Path(a.origem)
    faltam = [n for n in ARQUIVOS if not (origem / n).is_file()]
    if faltam:
        print("nao achei %s em %s" % (", ".join(faltam), origem), file=sys.stderr)
        return 1
    DESTINO.mkdir(parents=True, exist_ok=True)
    for n in ARQUIVOS:
        shutil.copy2(origem / n, DESTINO / n)
    print("motor copiado para %s" % DESTINO)

    vivo = DESTINO / "prices.live.json"
    if a.sem_precos:
        vivo.unlink(missing_ok=True)
        print("sem precos ao vivo: a pagina vai dizer que usa a tabela manual")
        return 0
    r = subprocess.run([sys.executable, "live_prices.py", "--out", vivo.name], cwd=DESTINO)
    if r.returncode != 0:
        vivo.unlink(missing_ok=True)
        print("a busca de precos falhou: a pagina vai dizer que usa a tabela manual", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
