def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a)
        siguiente = a + b
        a = b
        b = siguiente

# Cambia el 10 por la cantidad de números que quieras ver
fibonacci(10)
