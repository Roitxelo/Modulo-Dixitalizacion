a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

for numero in range(a, b + 1):

    if numero > 1:
        primo = True

        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break

        if primo:
            print(numero)