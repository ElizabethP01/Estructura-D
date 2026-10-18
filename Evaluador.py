class Pila:

    def __init__(self):
        self.items = []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()

    def peek(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items[-1]

    def esta_vacia(self):
        return len(self.items) == 0

    def tamanio(self):
        return len(self.items)


OPERADORES = {"+", "-", "*", "/", "^"}


def operar(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("División entre cero")
        return a / b
    if op == "^":
        return a ** b
    raise ValueError(f"Operador desconocido: {op}")


def evaluar_posfija(expresion):
    """Evalúa una expresión posfija. Ej: '3 4 + 2 *' -> 14"""
    pila = Pila()
    for token in expresion.split():
        if token in OPERADORES:
            b = pila.pop()  # el primero que sale es el operando derecho
            a = pila.pop()
            pila.push(operar(a, b, token))
        else:
            pila.push(float(token))

    resultado = pila.pop()
    if not pila.esta_vacia():
        raise ValueError("Expresión mal formada")
    return resultado


def evaluar_prefija(expresion):
    """Evalúa una expresión prefija. Ej: '* + 3 4 2' -> 14"""
    pila = Pila()
    # Se recorre de derecha a izquierda
    for token in reversed(expresion.split()):
        if token in OPERADORES:
            a = pila.pop()  # aquí el primero que sale es el operando izquierdo
            b = pila.pop()
            pila.push(operar(a, b, token))
        else:
            pila.push(float(token))

    resultado = pila.pop()
    if not pila.esta_vacia():
        raise ValueError("Expresión mal formada")
    return resultado


def main():
    print("=== Evaluador de expresiones con pila ===")
    print("Escribe los números y operadores separados por espacios.")
    print("Operadores válidos: + - * / ^")
    print("Ejemplos:  posfija -> 3 4 + 2 *   |   prefija -> * + 3 4 2\n")

    while True:
        print("1. Evaluar expresión posfija")
        print("2. Evaluar expresión prefija")
        print("3. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "3":
            print("¡Hasta luego!")
            break
        if opcion not in ("1", "2"):
            print("Opción no válida.\n")
            continue

        expresion = input("Expresión: ")
        try:
            if opcion == "1":
                resultado = evaluar_posfija(expresion)
            else:
                resultado = evaluar_prefija(expresion)
            print(f"Resultado: {resultado:g}\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")
        except (IndexError, ValueError):
            print("Error: la expresión no es válida.\n")


if __name__ == "__main__":
    main()
