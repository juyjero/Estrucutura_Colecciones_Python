agenda = {}
while True:
    nombre = input("Nombre: ")
    if nombre.lower() == "fin":
        break
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono
print(agenda)