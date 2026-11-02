#!/usr/bin/env python3

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CONFIG = RAIZ / "data" / "config.json"


def revisar_pregunta(q, i):
    """Devuelve la lista de problemas de una pregunta (vacía si está bien)."""
    p = []
    n = f"pregunta #{i}"
    if not isinstance(q, dict):
        return [f"{n}: no es un objeto {{...}}"]
    if not isinstance(q.get("question"), str) or not q["question"].strip():
        p.append(f"{n}: falta 'question' (enunciado)")
    ops = q.get("options")
    if not isinstance(ops, list) or not 2 <= len(ops) <= 6:
        p.append(f"{n}: 'options' debe ser una lista de 2 a 6 opciones")
    else:
        if any(not isinstance(o, str) or not o.strip() for o in ops):
            p.append(f"{n}: hay opciones vacías o que no son texto")
        if len({o.strip().lower() for o in ops if isinstance(o, str)}) < len(ops):
            p.append(f"{n}: hay opciones repetidas")
        a = q.get("answer")
        if isinstance(a, bool) or not isinstance(a, int) or not 0 <= a < len(ops):
            p.append(f"{n}: 'answer' debe ser un número entre 0 y {len(ops) - 1} (0 = A, 1 = B, ...)")
    return p


def main():
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    registrados = {Path(b["archivo"]).name: b for b in cfg["bibliografias"]}
    todos = "--todos" in sys.argv
    errores = 0
    total = 0
    por_grupo = {}
    print(f"{'ARCHIVO':<64}{'PREGUNTAS':>10}  ESTADO")
    print("-" * 90)

    for nombre, b in registrados.items():
        ruta = RAIZ / b["archivo"]
        if not ruta.exists():
            print(f"{nombre[:62]:<64}{'—':>10}  ✖ no existe (corre tools/sync_bancos.py)")
            errores += 1
            continue
        try:
            datos = json.loads(ruta.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"{nombre[:62]:<64}{'—':>10}  ✖ JSON inválido: {e}")
            errores += 1
            continue
        preguntas = datos if isinstance(datos, list) else datos.get("preguntas")
        if not isinstance(preguntas, list):
            print(f"{nombre[:62]:<64}{'—':>10}  ✖ falta la lista \"preguntas\"")
            errores += 1
            continue

        problemas, vistos = [], set()
        for i, q in enumerate(preguntas, 1):
            problemas += revisar_pregunta(q, i)
            clave = (q.get("question", "") if isinstance(q, dict) else "").strip().lower()
            if clave and clave in vistos:
                problemas.append(f"pregunta #{i}: duplicada")
            vistos.add(clave)

        total += len(preguntas)
        por_grupo[b["grupo"]] = por_grupo.get(b["grupo"], 0) + len(preguntas)
        estado = "✔" if not problemas else f"✖ {len(problemas)} problema(s)"
        if todos or problemas:
            print(f"{nombre[:62]:<64}{len(preguntas):>10}  {estado}")
        for m in problemas[:8]:
            print(f"    · {m}")
        if len(problemas) > 8:
            print(f"    · … y {len(problemas) - 8} más")
        errores += len(problemas)

    for f in sorted((RAIZ / "data" / "bib").rglob("*.json")):
        if f.name not in registrados:
            print(f"⚠ {f.name}: no está registrado en data/config.json (la app lo ignora)")

    print("-" * 90)
    nombres = {g["id"]: g["nombre"] for g in cfg["grupos"]}
    for gid, n in por_grupo.items():
        arch = [b for b in cfg["bibliografias"] if b["grupo"] == gid]
        con = sum(1 for b in arch if (RAIZ / b["archivo"]).exists() and (json.loads((RAIZ / b["archivo"]).read_text(encoding="utf-8")).get("preguntas") if isinstance(json.loads((RAIZ / b["archivo"]).read_text(encoding="utf-8")), dict) else json.loads((RAIZ / b["archivo"]).read_text(encoding="utf-8"))))
        print(f"  {nombres.get(gid, gid):<24}{n:>6} preguntas · {con} de {len(arch)} archivos con preguntas")
    print(f"Total: {total} preguntas en {len(registrados)} bibliografías · " + ("sin errores ✔" if not errores else f"{errores} error(es) ✖"))
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
