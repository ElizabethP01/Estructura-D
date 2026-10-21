class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

    def tamanio(self):
        return len(self.items)


# Servicios disponibles de la aseguradora
SERVICIOS = {
    1: "Pagos",
    2: "Siniestros",
    3: "Contratacion de polizas",
}

# Una cola por servicio y un contador de numeros de atencion por servicio
colas = {num: Cola() for num in SERVICIOS}
contadores = {num: 0 for num in SERVICIOS}


def llegada_cliente(servicio):
    """Llega un cliente: se le asigna el siguiente numero y entra a la cola."""
    contadores[servicio] += 1
    numero = contadores[servicio]
    colas[servicio].encolar(numero)
    print(f"Servicio: {SERVICIOS[servicio]} | Tu numero de atencion es: {numero}")


def atender_cliente(servicio):
    """Se atiende al primer cliente de la cola del servicio."""
    if colas[servicio].esta_vacia():
        print(f"No hay clientes en espera en {SERVICIOS[servicio]}.")
    else:
        numero = colas[servicio].desencolar()
        print(f"Servicio: {SERVICIOS[servicio]} | Llamando al numero: {numero}")


def main():
    print("=== Sistema de atencion - Aseguradora ===")
    print("Servicios:")
    for num, nombre in SERVICIOS.items():
        print(f"  {num} = {nombre}")
    print("Comandos: C<servicio> = llega cliente | A<servicio> = atender | S = salir")
    print("Ejemplo: C1, A1, C2\n")

    while True:
        comando = input("> ").strip().upper()

        if comando == "S":
            print("Hasta luego.")
            break

        if len(comando) < 2 or comando[0] not in ("C", "A") or not comando[1:].isdigit():
            print("Comando invalido. Usa C1, A1, C2, etc.")
            continue

        servicio = int(comando[1:])
        if servicio not in SERVICIOS:
            print(f"El servicio {servicio} no existe.")
            continue

        if comando[0] == "C":
            llegada_cliente(servicio)
        else:
            atender_cliente(servicio)


if __name__ == "__main__":
    main()
