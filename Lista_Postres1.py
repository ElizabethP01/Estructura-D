"""
EJERCICIO 1
"""

class Nodo:
    """Nodo de la lista ligada de ingredientes."""
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente
        self.siguiente = None          # None = NIL


class ListaIngredientes:
    """Lista ligada simple de ingredientes."""
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
        if self.cabeza is None:                 # lista vacía
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
                if anterior is None:            # era la cabeza
                    self.cabeza = actual.siguiente
                else:                           # medio o final
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
        "0": ("Salir", None),
    }
    while True:
        print("\n===== POSTRES (Ejercicio 1) =====")
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
