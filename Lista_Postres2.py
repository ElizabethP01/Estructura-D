"""
EJERCICIO 2
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
        ("Flan",    ["huevo", "leche", "vainilla"]),   # repetido, lista distinta
        ("Gelatina", ["grenetina", "agua"]),
        ("Pastel",  ["harina", "huevo", "azucar"]),
        ("Pastel",  ["harina", "huevo", "azucar"]),    # repetido, lista igual
        ("Pastel",  ["harina", "chocolate"]),          # repetido otra vez
    ]
    for nombre, ings in datos:
        p = Postre(nombre)
        for i in ings:
            p.ingredientes.insertar_final(i)
        POSTRES.append(p)
    # ordenar alfabéticamente (sort estable: conserva el orden de repetidos)
    POSTRES.sort(key=lambda p: p.nombre.lower())
    print("Datos de prueba cargados (con repetidos):")
    mostrar_todo()


def eliminar_repetidos():
    """Elimina postres repetidos (mismo nombre). Como el arreglo está
    ordenado, los repetidos quedan juntos. Se conserva la primera aparición.
    Reporta qué pasó con las listas de ingredientes de los repetidos."""
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
        "1": ("Cargar datos de prueba con repetidos", cargar_datos_con_repetidos),
        "2": ("Eliminar elementos repetidos", eliminar_repetidos),
        "3": ("Mostrar toda la estructura", mostrar_todo),
        "0": ("Salir", None),
    }
    while True:
        print("\n===== POSTRES (Ejercicio 2) =====")
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
