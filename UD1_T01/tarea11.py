import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))

x2 = float(input("x2: "))
y2 = float(input("y2: "))

punto1 = (x1, y1)
punto2 = (x2, y2)

distancia = math.sqrt(
    (punto2[0] - punto1[0]) ** 2 +
    (punto2[1] - punto1[1]) ** 2
)

print("Distancia:", distancia)