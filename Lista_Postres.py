class Nodo:
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente
        self.siguiente = None          # None = NIL


class ListaIngredientes:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def buscar(self, ingrediente):
        actual = self.cabeza
        while actual is not None:
            if actual.ingrediente.lower() == ingrediente.lower():
                return True
            actual = actual.siguiente
        return False

    def insertar_final(self, ingrediente):
        """Inserta al final. Devuelve False si ya existía."""
        if self.buscar(ingrediente):
            return False
        nuevo = Nodo(ingrediente)
        if self.cabeza is None:                 
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        return True

    def eliminar(self, ingrediente):
        """Elimina un ingrediente. Devuelve True si lo encontró."""
        anterior, actual = None, self.cabeza
        while actual is not None:
            if actual.ingrediente.lower() == ingrediente.lower():
                if anterior is None:            
                    self.cabeza = actual.siguiente
                else:                           
                    anterior.siguiente = actual.siguiente
                return True
            anterior, actual = actual, actual.siguiente
        return False

    def a_python(self):
        res, actual = [], self.cabeza
        while actual is not None:
            res.append(actual.ingrediente)
            actual = actual.siguiente
        return res


class Postre:
    """Elemento del arreglo: nombre + lista de ingredientes."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = ListaIngredientes()


POSTRES = []   # arreglo ordenado alfabéticamente por nombre


# ---------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------
def pedir_texto(mensaje):
    """Pide texto no vacío (valida cadenas vacías)."""
    while True:
        t = input(mensaje).strip()
        if t:
            return t
        print("  ERROR: no puede estar vacío.")


def buscar_postre(nombre):
    """Búsqueda binaria en el arreglo ordenado.
    Devuelve (encontrado, posición). Si no existe, posición = donde insertar."""
    bajo, alto = 0, len(POSTRES) - 1
    clave = nombre.lower()
    while bajo <= alto:
        medio = (bajo + alto) // 2
        actual = POSTRES[medio].nombre.lower()
        if actual == clave:
            return True, medio
        if actual < clave:
            bajo = medio + 1
        else:
            alto = medio - 1
    return False, bajo


def pedir_ingredientes(lista):
    """Captura ingredientes hasta que el usuario deje vacío."""
    print("  Escribe los ingredientes (Enter vacío para terminar):")
    agregados = 0
    while True:
        ing = input("   - ").strip()
        if not ing:
            break
        if lista.insertar_final(ing):
            agregados += 1
        else:
            print(f"     AVISO: '{ing}' ya está en la lista, se omite.")
    return agregados


# ---------------------------------------------------------------
# Ejercicio 1
# ---------------------------------------------------------------
def imprimir_ingredientes():                       # inciso a
    if not POSTRES:
        print("ERROR: el arreglo POSTRES está vacío.")
        return
    nombre = pedir_texto("Nombre del postre: ")
    existe, pos = buscar_postre(nombre)
    if not existe:
        print(f"ERROR: el postre '{nombre}' no existe.")
        return
    lista = POSTRES[pos].ingredientes
    if lista.esta_vacia():
        print(f"El postre '{POSTRES[pos].nombre}' no tiene ingredientes (NIL).")
        return
    print(f"Ingredientes de {POSTRES[pos].nombre}:")
    for ing in lista.a_python():
        print("  -", ing)


def insertar_ingredientes():                       # inciso b
    if not POSTRES:
        print("ERROR: el arreglo POSTRES está vacío.")
        return
    nombre = pedir_texto("Nombre del postre: ")
    existe, pos = buscar_postre(nombre)
    if not existe:
        print(f"ERROR: el postre '{nombre}' no existe.")
        return
    n = pedir_ingredientes(POSTRES[pos].ingredientes)
    print(f"Se agregaron {n} ingrediente(s).")


def eliminar_ingrediente():                        # inciso c
    if not POSTRES:
        print("ERROR: el arreglo POSTRES está vacío.")
        return
    nombre = pedir_texto("Nombre del postre: ")
    existe, pos = buscar_postre(nombre)
    if not existe:
        print(f"ERROR: el postre '{nombre}' no existe.")
        return
    lista = POSTRES[pos].ingredientes
    if lista.esta_vacia():
        print("ERROR: el postre no tiene ingredientes que eliminar.")
        return
    ing = pedir_texto("Ingrediente a eliminar: ")
    if not lista.eliminar(ing):
        print(f"ERROR: '{ing}' no está en la lista.")
        return
    print(f"Ingrediente '{ing}' eliminado.")
    if lista.esta_vacia():
        print("AVISO: el postre se quedó sin ingredientes (NIL).")


def alta_postre():                                 # inciso d
    nombre = pedir_texto("Nombre del nuevo postre: ")
    existe, pos = buscar_postre(nombre)
    if existe:
        print(f"ERROR: el postre '{nombre}' ya existe.")
        return
    nuevo = Postre(nombre)
    n = pedir_ingredientes(nuevo.ingredientes)
    if n == 0:
        print("AVISO: se dará de alta sin ingredientes.")
    POSTRES.insert(pos, nuevo)      # mantiene el orden alfabético
    print(f"Postre '{nombre}' dado de alta en la posición {pos}.")


def baja_postre():                                 # inciso e
    if not POSTRES:
        print("ERROR: el arreglo POSTRES está vacío, no hay nada que dar de baja.")
        return
    nombre = pedir_texto("Nombre del postre a dar de baja: ")
    existe, pos = buscar_postre(nombre)
    if not existe:
        print(f"ERROR: el postre '{nombre}' no existe.")
        return
    eliminado = POSTRES.pop(pos)    # se pierde su lista de ingredientes completa
    print(f"Postre '{eliminado.nombre}' dado de baja junto con sus ingredientes.")


def mostrar_todo():
    if not POSTRES:
        print("POSTRES está vacío.")
        return
    for i, p in enumerate(POSTRES):
        ings = " -> ".join(p.ingredientes.a_python()) or ""
        print(f"[{i}] {p.nombre}: {ings} -> NIL")


# ---------------------------------------------------------------
# Ejercicio 2: eliminar elementos repetidos de POSTRES
# ---------------------------------------------------------------
def cargar_datos_con_repetidos():
    """Carga datos de prueba CON postres repetidos (se inserta directo,
    sin validar, para poder probar el ejercicio 2)."""
    POSTRES.clear()
    datos = [
        ("Flan",    ["huevo", "leche", "azucar"]),
        ("Flan",    ["huevo", "leche", "vainilla"]),   
        ("Gelatina", ["grenetina", "agua"]),
        ("Pastel",  ["harina", "huevo", "azucar"]),
        ("Pastel",  ["harina", "huevo", "azucar"]),    
        ("Pastel",  ["harina", "chocolate"]),          
    ]
    for nombre, ings in datos:
        p = Postre(nombre)
        for i in ings:
            p.ingredientes.insertar_final(i)
        POSTRES.append(p)
    
    POSTRES.sort(key=lambda p: p.nombre.lower())
    print("Datos de prueba cargados (con repetidos):")
    mostrar_todo()


def eliminar_repetidos():
    if not POSTRES:
        print("ERROR: el arreglo POSTRES está vacío, no hay repetidos.")
        return
    if len(POSTRES) == 1:
        print("Solo hay un elemento, no hay repetidos.")
        return

    unico = [POSTRES[0]]
    eliminados = 0
    for p in POSTRES[1:]:
        base = unico[-1]
        if p.nombre.lower() == base.nombre.lower():
            eliminados += 1
            perdidos = [i for i in p.ingredientes.a_python()
                        if not base.ingredientes.buscar(i)]
            print(f"- Repetido '{p.nombre}' eliminado.")
            if perdidos:
                print(f"  ERROR: su lista tenía ingredientes que NO están en "
                      f"la lista conservada: {perdidos}. ¡Se pierden!")
                resp = input("  ¿Fusionarlos a la lista conservada? (s/n): ")
                if resp.strip().lower() == "s":
                    for i in perdidos:
                        base.ingredientes.insertar_final(i)
                    print("  Ingredientes fusionados.")
                else:
                    print("  Ingredientes descartados.")
            else:
                print("  Su lista era igual o subconjunto de la conservada: "
                      "no se perdió información.")
        else:
            unico.append(p)

    POSTRES[:] = unico
    if eliminados == 0:
        print("No se encontraron elementos repetidos.")
    else:
        print(f"\nSe eliminaron {eliminados} elemento(s) repetido(s). Resultado:")
        mostrar_todo()


# ---------------------------------------------------------------
# Menú
# ---------------------------------------------------------------
def menu():
    opciones = {
        "1": ("a) Imprimir ingredientes de un postre", imprimir_ingredientes),
        "2": ("b) Insertar ingredientes a un postre", insertar_ingredientes),
        "3": ("c) Eliminar un ingrediente de un postre", eliminar_ingrediente),
        "4": ("d) Alta de un postre", alta_postre),
        "5": ("e) Baja de un postre", baja_postre),
        "6": ("Mostrar toda la estructura", mostrar_todo),
        "7": ("Ejercicio 2: cargar datos de prueba con repetidos",
              cargar_datos_con_repetidos),
        "8": ("Ejercicio 2: eliminar elementos repetidos", eliminar_repetidos),
        "0": ("Salir", None),
    }
    while True:
        print("\n===== POSTRES =====")
        for k, (texto, _) in opciones.items():
            print(f" {k}. {texto}")
        op = input("Opción: ").strip()
        if op == "0":
            print("Hasta luego.")
            break
        if op in opciones:
            opciones[op][1]()
        else:
            print("ERROR: opción inválida.")


if __name__ == "__main__":
    menu()
