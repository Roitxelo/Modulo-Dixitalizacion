import random

numero = random.randint(1, 100)

while True:

    intento = int(input("Adivina el número: "))

    if intento < numero:
        print("El número es mayor")

    elif intento > numero:
        print("El número es menor")

    else:
        print("Has acertado")
        break