diccionario = {
    "uno": 1,
    "dos": 2,
    "tres": 3
}

inverso = {}

for clave, valor in diccionario.items():
    inverso[valor] = clave

print(inverso)