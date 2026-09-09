# Estructura-D
Repositorio de la clase


# Estructura-datos-
portafolio de estructura de datos


#facorial 
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
a=5
print(factorial(a)) 


#Vectores 
def mostrar_vector(datos):
    for valor in datos:
        print(valor)

def media(datos):
    n = len(datos)
    suma = 0
    for valor in datos: 
        suma += valor
    return suma / n

if __name__== "__main__":
  pares = [2, 4, 6, 8, 10]
  impares = [1, 3, 5, 7, 9]

mostrar_vector(pares)
print(f"media ={media(pares)}")

mostrar_vector(impares)
print(f"media = {media(impares)}")


#Vectores 2
import random
import statistics

numeros = [random.randint(150, 250) for _ in range(50)]

print("Lista de números aleatorios:")
print(numeros)
print("-" * 40)

print(f"Media: {statistics.mean(numeros)}")
print(f"Mediana: {statistics.median(numeros)}")
print(f"Moda: {statistics.mode(numeros)}")
print(f"Varianza muestral: {statistics.variance(numeros):.2f}")
print(f"Desviación estándar: {statistics.stdev(numeros):.2f}")


#Tarea 1
calificaciones = [0] * 5

for i in range(5):
    calificaciones[i] = int(input("Captura la calificación: "))


#Tarea 2 
frutas = []

frutas.append("Mango")
frutas.append("Manzana")
frutas.append("Banana")
frutas.append("Uvas")

print(frutas)

frutas.remove("Mango")
frutas.remove("Banana")

frutas.append("Sandia")

print(frutas)
