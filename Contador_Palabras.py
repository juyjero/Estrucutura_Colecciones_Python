frase = input("Ingrese una frase: ")
contador = {}
for palabra in frase.split():
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print(contador)