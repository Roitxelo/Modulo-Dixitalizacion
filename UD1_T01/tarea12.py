agenda = {}

while True:

    print("\n1. Añadir contacto")
    print("2. Buscar contacto")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":

        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")

        if nombre in agenda:
            agenda[nombre].append(telefono)
        else:
            agenda[nombre] = [telefono]

    elif opcion == "2":

        nombre = input("Nombre a buscar: ")

        if nombre in agenda:
            print(agenda[nombre])
        else:
            print("Contacto no encontrado")

    elif opcion == "0":
        break