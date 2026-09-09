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
