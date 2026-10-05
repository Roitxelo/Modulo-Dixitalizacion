notas = []

while True:

    nombre = input("Nombre del alumno (fin para terminar): ")

    if nombre == "fin":
        break

    nota = float(input("Nota: "))
    notas.append(nota)

if len(notas) > 0:
    print("Nota media:", sum(notas) / len(notas))
    print("Nota más alta:", max(notas))
    print("Nota más baja:", min(notas))