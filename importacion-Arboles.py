from collections import deque
class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

    def es_hoja(self):
        return self.izquierdo is None and self.derecho is None


class Arbol:

    def __init__(self):
        self.raiz = None

    def esta_vacio(self):
        return self.raiz is None

    def insertar(self, dato):
        self.raiz = self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        if nodo is None:
            return Nodo(dato)
        if dato < nodo.dato:
            nodo.izquierdo = self._insertar(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._insertar(nodo.derecho, dato)
        else:
            print(f"El dato {dato} ya existe; no se insertó.")
        return nodo

    def buscar(self, dato):
        actual = self.raiz
        while actual is not None:
            if dato == actual.dato:
                return True
            actual = actual.izquierdo if dato < actual.dato else actual.derecho
        return False


    def eliminar(self, dato):
        self.raiz = self._eliminar(self.raiz, dato)

    def _eliminar(self, nodo, dato):
        if nodo is None:
            print(f"El dato {dato} no existe en el árbol.")
            return None
        if dato < nodo.dato:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._eliminar(nodo.derecho, dato)
        else:
            # Caso 1 y 2: sin hijo o con un hijo
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            # Caso 3: dos hijos -> sucesor inorden (mínimo del subárbol derecho)
            sucesor = self._minimo(nodo.derecho)
            nodo.dato = sucesor.dato
            nodo.derecho = self._eliminar(nodo.derecho, sucesor.dato)
        return nodo

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, res):
        if nodo:
            self._inorden(nodo.izquierdo, res)
            res.append(nodo.dato)
            self._inorden(nodo.derecho, res)

    def preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, res):
        if nodo:
            res.append(nodo.dato)
            self._preorden(nodo.izquierdo, res)
            self._preorden(nodo.derecho, res)

    def postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self, nodo, res):
        if nodo:
            self._postorden(nodo.izquierdo, res)
            self._postorden(nodo.derecho, res)
            res.append(nodo.dato)

    def por_niveles(self):
        resultado = []
        if self.raiz is None:
            return resultado
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.dato)
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)
        return resultado

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))

    def contar_nodos(self):
        return self._contar(self.raiz)

    def _contar(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar(nodo.izquierdo) + self._contar(nodo.derecho)

    def contar_hojas(self):
        return self._hojas(self.raiz)

    def _hojas(self, nodo):
        if nodo is None:
            return 0
        if nodo.es_hoja():
            return 1
        return self._hojas(nodo.izquierdo) + self._hojas(nodo.derecho)

    def _minimo(self, nodo):
        while nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo

    def minimo(self):
        return self._minimo(self.raiz).dato if self.raiz else None

    def maximo(self):
        if self.raiz is None:
            return None
        nodo = self.raiz
        while nodo.derecho:
            nodo = nodo.derecho
        return nodo.dato

    def mostrar(self):
        if self.raiz is None:
            print("(árbol vacío)")
        else:
            self._mostrar(self.raiz, 0)

    def _mostrar(self, nodo, nivel):
        if nodo:
            self._mostrar(nodo.derecho, nivel + 1)
            print("    " * nivel + str(nodo.dato))
            self._mostrar(nodo.izquierdo, nivel + 1)


def menu():
    arbol = Arbol()
    opciones = """
===== MENÚ ÁRBOL BINARIO DE BÚSQUEDA =====
1. Insertar        6. Postorden       11. Mínimo
2. Buscar          7. Por niveles     12. Máximo
3. Eliminar        8. Altura          13. Mostrar árbol
4. Inorden         9. Contar nodos    0. Salir
5. Preorden       10. Contar hojas
"""
    while True:
        print(opciones)
        op = input("Elige una opción: ").strip()
        if op == "0":
            print("¡Hasta luego!")
            break
        elif op in ("1", "2", "3"):
            try:
                dato = int(input("Dato (entero): "))
            except ValueError:
                print("Debes ingresar un número entero.")
                continue
            if op == "1":
                arbol.insertar(dato)
            elif op == "2":
                print("Encontrado" if arbol.buscar(dato) else "No encontrado")
            else:
                arbol.eliminar(dato)
        elif op == "4":
            print("Inorden:", arbol.inorden())
        elif op == "5":
            print("Preorden:", arbol.preorden())
        elif op == "6":
            print("Postorden:", arbol.postorden())
        elif op == "7":
            print("Por niveles:", arbol.por_niveles())
        elif op == "8":
            print("Altura:", arbol.altura())
        elif op == "9":
            print("Nodos:", arbol.contar_nodos())
        elif op == "10":
            print("Hojas:", arbol.contar_hojas())
        elif op == "11":
            print("Mínimo:", arbol.minimo())
        elif op == "12":
            print("Máximo:", arbol.maximo())
        elif op == "13":
            arbol.mostrar()
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
