from MyLinkedList import LinkedList

lista = LinkedList()

while True:
    print("\n--- LISTA SIMPLEMENTE LIGADA (MyLinkedList) ---")
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Eliminar el inicio")
    print("4. Eliminar el final")
    print("5. Insertar antes de X")
    print("6. Insertar después de X")
    print("7. Mostrar lista")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        lista.insert_start(input("Ingrese el dato: "))
        print("Nodo insertado al inicio.")
    elif opcion == "2":
        lista.insert_end(input("Ingrese el dato: "))
        print("Nodo insertado al final.")
    elif opcion == "3":
        eliminado = lista.delete_start()
        print("La lista está vacía." if eliminado is None else f"Se eliminó: {eliminado}")
    elif opcion == "4":
        eliminado = lista.delete_end()
        print("La lista está vacía." if eliminado is None else f"Se eliminó: {eliminado}")
    elif opcion == "5":
        x = input("Ingrese el dato X: ")
        nuevo = input("Ingrese el nuevo dato: ")
        print("Nodo insertado antes de X." if lista.insert_before(x, nuevo)
              else "No se encontró el dato X (o la lista está vacía).")
    elif opcion == "6":
        x = input("Ingrese el dato X: ")
        nuevo = input("Ingrese el nuevo dato: ")
        print("Nodo insertado después de X." if lista.insert_after(x, nuevo)
              else "No se encontró el dato X.")
    elif opcion == "7":
        lista.show()
    elif opcion == "8":
        print("Programa terminado.")
        break
    else:
        print("Opción no válida.")