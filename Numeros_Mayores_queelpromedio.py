numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
promedio = sum(numeros) / len(numeros)
mayores = [n for n in numeros if n > promedio]
print("Promedio:", promedio)
print("Mayores que el promedio:", mayores)