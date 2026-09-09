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
