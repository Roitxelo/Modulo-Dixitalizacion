num1 = float(input("Primer número: "))
operacion = input("Operación (+, -, *, /): ")
num2 = float(input("Segundo número: "))

if operacion == "+":
    print(num1 + num2)

elif operacion == "-":
    print(num1 - num2)

elif operacion == "*":
    print(num1 * num2)

elif operacion == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("No se puede dividir entre cero")

else:
    print("Operación incorrecta")