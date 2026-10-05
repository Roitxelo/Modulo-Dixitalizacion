cadena = input("Introduce una cadena: ")

frecuencias = {}

for caracter in cadena:
    if caracter in frecuencias:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1

print(frecuencias)