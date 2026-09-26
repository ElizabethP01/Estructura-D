meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]
departamentos = [
    "Ropa",
    "Deportes",
    "Juguetería"
]

ventas = [
    [0, 0, 0],  # Enero
    [0, 0, 0],  # Febrero
    [0, 0, 0],  # Marzo
    [0, 0, 0],  # Abril
    [0, 0, 0],  # Mayo
    [0, 0, 0],  # Junio
    [0, 0, 0],  # Julio
    [0, 0, 0],  # Agosto
    [0, 0, 0],  # Septiembre
    [0, 0, 0],  # Octubre
    [0, 0, 0],  # Noviembre
    [0, 0, 0]   # Diciembre
]


def insertar_venta():

    print("\n--- INSERTAR VENTA ---")

    # Mostrar los meses
    print("\nMeses:")
    for i in range(len(meses)):
        print(i + 1, "-", meses[i])

    mes = int(input("Selecciona el número del mes: ")) - 1

    print("\nDepartamentos:")
    for i in range(len(departamentos)):
        print(i + 1, "-", departamentos[i])

    departamento = int(input("Selecciona el departamento: ")) - 1

    venta = float(input("Ingresa el monto de la venta: $"))

    ventas[mes][departamento] = venta

    print("Venta insertada correctamente.")



def buscar_venta():

    print("\n--- BUSCAR VENTA ---")

    print("\nMeses:")
    for i in range(len(meses)):
        print(i + 1, "-", meses[i])

    mes = int(input("Selecciona el número del mes: "))
    print("\nDepartamentos:")
    for i in range(len(departamentos)):
        print(i + 1, "-", departamentos[i])

    departamento = int(input("Selecciona el departamento: ")) - 1

    # Buscar la venta
    venta = ventas[mes][departamento]

    print("\nMes:", meses[mes])
    print("Departamento:", departamentos[departamento])
    print("Venta: $", venta)




def eliminar_venta():

    print("\n--- ELIMINAR VENTA ---")

    print("\nMeses:")
    for i in range(len(meses)):
        print(i + 1, "-", meses[i])

    mes = int(input("Selecciona el número del mes: ")) - 1

    print("\nDepartamentos:")
    for i in range(len(departamentos)):
        print(i + 1, "-", departamentos[i])

    departamento = int(input("Selecciona el departamento: ")) - 1

    ventas[mes][departamento] = 0

    print("Venta eliminada correctamente.")


def mostrar_ventas():

    print("\n--- TABLA DE VENTAS ---")

    print(f"{'Mes':<15}{'Ropa':<15}{'Deportes':<15}{'Juguetería':<15}")

    for i in range(12):
        print(
            f"{meses[i]:<15}"
            f"{ventas[i][0]:<15}"
            f"{ventas[i][1]:<15}"
            f"{ventas[i][2]:<15}"
        )



while True:

    print("\n==============================")
    print("       SISTEMA DE VENTAS")
    print("==============================")
    print("1. Insertar venta")
    print("2. Buscar venta")
    print("3. Eliminar venta")
    print("4. Mostrar todas las ventas")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        insertar_venta()

    elif opcion == "2":
        buscar_venta()

    elif opcion == "3":
        eliminar_venta()

    elif opcion == "4":
        mostrar_ventas()

    elif opcion == "5":
        print("Programa terminado.")
        break

    else:
        print("Opción no válida.")
