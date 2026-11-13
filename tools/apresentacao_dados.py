# -*- coding: utf-8 -*-
"""Gera os numeros da apresentacao /apresentacao/custo-de-agentes/ a partir do
codigo publico agent-cost-math, para que nenhum valor da apresentacao seja
digitado manualmente.

    python tools/apresentacao_dados.py            # imprime o JSON
    python tools/apresentacao_dados.py --origem ../agent-cost-math

O JSON e colado no bloco `var DADOS = ...` do index.html da apresentacao.
"""
from __future__ import annotations

import argparse
import copy
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--origem", default=str(RAIZ.parent / "agent-cost-math"))
    a = ap.parse_args()
    origem = pathlib.Path(a.origem)
    sys.path.insert(0, str(origem))
    import agent_cost as ac

    precos = ac.load_prices(str(origem / "prices.example.json"))
    arq = json.loads((origem / "architecture.example.json").read_text(encoding="utf-8"))
    opts = {"hit_rate": 0.40, "calls_per_write": 50}
    cls = next(c for c in arq["components"] if c["role"] == "router")
    age = next(c for c in arq["components"] if c["role"] == "specialist")
    total = ac.price_architecture(arq, precos)

    def custo(comp, **mud):
        c = copy.deepcopy(comp)
        c.update(mud)
        return ac.price_component(c, precos, opts)

    barato, caro = cls["model"], age["model"]
    vol = age["monthly_volume"]
    infl = ac.context_inflation(2000, 500, 10)

    def serie(delta, modelo):
        return [custo(age, max_iterations=n, delta_tokens_per_iteration=delta, model=modelo)["cost_usd"]
                for n in range(1, 17)]

    c1 = custo(age, model=barato)["cost_usd"] / vol
    c2 = custo(age)["cost_usd"] / vol
    casc = [ac.cascade(c1, c2, p / 100, vol)["cascade_cost"] for p in range(0, 101)]

    # efeito somado: 5 passos, historico resumido, cache e primeiro nivel com 60%
    a5 = custo(age, max_iterations=5, delta_tokens_per_iteration=250)["cost_usd"]
    b5 = custo(age, max_iterations=5, delta_tokens_per_iteration=250, model=barato)["cost_usd"]
    somado = ac.cascade(b5 / vol, a5 / vol, 0.60, vol)
    # degraus da escada da tela de conclusao, na ordem em que as decisoes aparecem
    escada = [custo(age, caching=False)["cost_usd"], custo(age)["cost_usd"], a5, somado["cascade_cost"]]

    def por_milhao(nome):
        m = precos["models"][nome]
        return [round(m["input_per_1k"] * 1000, 3), round(m["output_per_1k"] * 1000, 3)]

    dados = {
        "precos_em": precos.get("pricing_as_of"),
        "classificacao": {"volume": cls["monthly_volume"], "custo": custo(cls)["cost_usd"],
                          "custo_modelo_maior": custo(cls, model=caro)["cost_usd"], "modelo": barato},
        "agente": {"volume": vol, "custo": custo(age)["cost_usd"], "passos": age["max_iterations"],
                   "tokens": custo(age)["input_per_task"], "tokens_simples": custo(age)["input_per_task_naive"],
                   "custo_modelo_menor": custo(age, model=barato)["cost_usd"], "modelo": caro,
                   "sem_cache": custo(age, caching=False)["cost_usd"],
                   "prefixo": age["static_prefix_tokens"]},
        "participacao": {
            "classificacao": next(c for c in total["components"] if c["role"] == "router")["cost_share_pct"],
            "agente": next(c for c in total["components"] if c["role"] == "specialist")["cost_share_pct"]},
        "total_arquitetura": total["monthly_cost_usd"],
        "compressor": next(c for c in total["components"] if c["role"] == "compressor")["cost_usd"],
        "inflacao": {"por_passo": infl["input_per_iteration"], "total": infl["input_total"],
                     "simples": infl["input_total_naive"], "pct": infl["overspend_pct"]},
        "passos": {"normal": serie(age["delta_tokens_per_iteration"], caro),
                   "resumido": serie(age["delta_tokens_per_iteration"] / 2, caro)},
        "cascata": {"curva": casc, "direto": round(c2 * vol, 2), "equilibrio": round(c1 / c2, 4),
                    "c1": c1, "c2": c2},
        "somado": {"custo": somado["cascade_cost"], "por_solicitacao": round(somado["cascade_cost"] / vol, 4)},
        "escada": escada,
        "modelos": {barato: por_milhao(barato), "Claude Sonnet 5": por_milhao("Claude Sonnet 5"), caro: por_milhao(caro)},
        "piso_cache": {n: precos["models"][n].get("min_cache_tokens") for n in (barato, caro)},
    }
    print(json.dumps(dados, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
