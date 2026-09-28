def ahorrar(meta, ahorro, semanas=0, total=0):
    if total >= meta:
        return semanas

    return ahorrar(meta, ahorro, semanas + 1, total + ahorro)


meta = float(input("¿Cuánto quieres ahorrar? $"))
ahorro = float(input("¿Cuánto puedes ahorrar cada semana? $"))

semanas = ahorrar(meta, ahorro)

print("Necesitas", semanas, "semanas para alcanzar tu meta.")
