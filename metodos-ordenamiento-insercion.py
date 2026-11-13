# EJERCICIO 2: MÉTODO DE INSERCIÓN
# Situación: acabas de cambiar de celular y tus contactos de
# WhatsApp están todos revueltos; quieres ponerlos en orden
# alfabético.
# Idea: se toma cada contacto y se "inserta" en su lugar correcto
# dentro de la parte que ya está ordenada (como ordenar las cartas
# de un juego en tu mano).
# Complejidad: O(n^2), muy bueno si la lista ya está casi ordenada.

def ordenamiento_insercion(contactos):
    for i in range(1, len(contactos)):
        actual = contactos[i]
        j = i - 1
        while j >= 0 and contactos[j] > actual:
            contactos[j + 1] = contactos[j]  # desplaza a la derecha
            j -= 1
        contactos[j + 1] = actual
    return contactos


def ejercicio_2():
    print("EJERCICIO 2: Inserción - Contactos de WhatsApp en orden alfabético")
    contactos = ["Valeria", "Diego", "Sofi", "Mamá", "Andrés", "Camila", "Luis"]
    print("Original :", contactos)
    print("Ordenada :", ordenamiento_insercion(contactos.copy()))
    print()

if __name__ == "__main__":
    ejercicio_2()

