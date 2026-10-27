class Nodo:
    def __init__(self, info):
        self.info = info  # Campo INFO del nodo
        self.liga = None  # Campo LIGA del nodo (inicialmente NIL / None)


class NodoDoble:
    def __init__(self, infor):
        self.infor = infor      # Campo INFOR
        self.ligaizq = None     # Campo LIGAIZQ
        self.ligader = None     # Campo LIGADER


# --- Validación de la respuesta Sí/No ---
def pedir_respuesta():
    while True:
        try:
            return int(input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0: "))
        except ValueError:
            print("Ingrese 1 o 0.")


# ---------- LISTA SIMPLEMENTE LIGADA ----------

# --- Inserta_inicio ---
def inserta_inicio(p, dato):
    """Inserta un nodo al inicio de una lista simplemente ligada."""
    q = Nodo(dato)
    q.liga = p
    p = q
    return p


# --- Crea_inicio ---
def crea_inicio():
    print("--- Creación de la Lista (Crea_inicio) ---")
    info_inicial = input("Ingrese el valor del primer nodo (P^.INFO): ")
    p = Nodo(info_inicial)
    p.liga = None

    res = pedir_respuesta()
    while res == 1:
        dato = input("Ingrese el valor del nuevo nodo (DATO): ")
        p = inserta_inicio(p, dato)
        res = pedir_respuesta()

    return p


# --- Busqueda_recursivo ---
def busqueda_recursivo(p, x):
    """Busca recursivamente un elemento con información X en la lista."""
    if p is not None:
        if p.info == x:
            print("El elemento se encuentra en la lista")
            return True
        else:
            return busqueda_recursivo(p.liga, x)
    else:
        print("El elemento no se encuentra en la lista")
        return False


# --- Ejemplo 5.8: Eliminar el último nodo (Figura 5.11) ---
def elimina_final(p):
    """Elimina el último nodo de una lista simplemente ligada."""
    if p is None:
        print("La lista está vacía.")
        return p

    q = p
    t = None

    # Q recorre la lista hasta el último nodo; T queda en el anterior
    while q.liga is not None:
        t = q
        q = q.liga

    if p == q:                  # La lista tenía un solo nodo
        p = None
    else:
        t.liga = None           # T pasa a ser el último nodo

    print(f"Elemento '{q.info}' eliminado del final.")
    del q                       # Quitar(Q)
    return p


# --- Recorrer la lista simple ---
def recorrer_lista(p, mensaje="\nContenido actual de la lista (del inicio al final):"):
    q = p
    print(mensaje)
    if q is None:
        print("NIL (Lista vacía)")
        return
    while q is not None:
        print(f"[{q.info}] -> ", end="")
        q = q.liga
    print("NIL")


# ---------- LISTA DOBLEMENTE LIGADA ----------

# --- Ejemplo 5.12: Insertar al final (Figura 5.18) ---
def inserta_final(p, f, dato):
    """Inserta un nodo al final de una lista doble usando F (apuntador al último)."""
    q = NodoDoble(dato)         # Crear(Q)
    q.ligader = None
    if p is None:               # Lista vacía
        q.ligaizq = None
        p = q
        f = q
    else:
        q.ligaizq = f
        f.ligader = q
        f = q                   # F apunta al nuevo último nodo
    return p, f


# --- Recorrer lista doble ---
def recorrer_doble(p):
    q = p
    print("\nLista doblemente ligada:")
    if q is None:
        print("NIL (Lista vacía)")
        return
    print("NIL <-> ", end="")
    while q is not None:
        print(f"[{q.infor}] <-> ", end="")
        q = q.ligader
    print("NIL")


# ---------- BLOQUE PRINCIPAL ----------
if __name__ == "__main__":
    # 1. Creamos la lista
    p = crea_inicio()
    recorrer_lista(p)

    # 2. Probar Búsqueda
    print("\n--- Búsqueda en la Lista ---")
    x = input("Ingrese el elemento a buscar: ")
    busqueda_recursivo(p, x)

    # 3. Probar Inserción de un nuevo elemento al inicio
    print("\n--- Inserción de un nuevo elemento ---")
    dato = input("Ingrese el valor a insertar al inicio: ")
    p = inserta_inicio(p, dato)
    recorrer_lista(p)

    # 4. Ejemplo 5.8: Eliminar el último nodo
    print("\n--- Ejemplo 5.8: Eliminación del último nodo ---")
    p = elimina_final(p)
    recorrer_lista(p)

    # 5. Demostración de dos nodos distintos apuntando a un mismo nodo
    print("\n--- Demostración: Dos nodos diferentes apuntando a un mismo nodo ---")

    nodo_comun = Nodo("Común")
    nodo_comun.liga = None

    nodo_a = Nodo("Rama_A")
    nodo_b = Nodo("Rama_B")

    nodo_a.liga = nodo_comun
    nodo_b.liga = nodo_comun

    recorrer_lista(nodo_a, "\nRecorriendo desde Rama A:")
    recorrer_lista(nodo_b, "Recorriendo desde Rama B:")

    if nodo_a.liga is nodo_b.liga:
        print("\n¡Comprobado! Las ligas de 'Rama_A' y 'Rama_B' apuntan al mismo objeto en memoria.")

    # 6. Ejemplo 5.12: Insertar al final en lista doblemente ligada
    print("\n--- Ejemplo 5.12: Inserción al final (lista doble) ---")
    pd = None   # P: primer nodo
    fd = None   # F: último nodo

    dato = input("Ingrese el valor del primer nodo (DATO): ")
    pd, fd = inserta_final(pd, fd, dato)

    res = pedir_respuesta()
    while res == 1:
        dato = input("Ingrese el valor del nuevo nodo (DATO): ")
        pd, fd = inserta_final(pd, fd, dato)
        res = pedir_respuesta()

    recorrer_doble(pd)
