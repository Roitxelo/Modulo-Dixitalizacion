frase = input("Introduce una frase: ")

palabras = frase.split()

print("Orden alfabético:")
print(sorted(palabras))

print("Orden por longitud:")
print(sorted(palabras, key=len))