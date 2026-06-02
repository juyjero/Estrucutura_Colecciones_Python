dic = {'a': 1, 'b': 2, 'c': 3}
invertido = {}
for clave, valor in dic.items():
    invertido[valor] = clave
print(invertido)