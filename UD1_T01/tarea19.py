class Empleado:

    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f"Empleada con nombre: {self.nombre} y sueldo {self.sueldo}. "

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return super().__str__()+f"Gerente del departamento {self.departamento}"

class Programador(Empleado):
    def __init__(self, nombre, sueldo, lenguaje):
        super().__init__(nombre, sueldo)
        self.lenguaje = lenguaje

    def __str__(self):
        return super().__str__()+f"Programador en lenguaje {self.lenguaje}"

if __name__ == "__main__":
    pepe = Empleado("Pepe", 1000)

    antonio = Gerente("Antonio", 2000, "Ventas")

    paquiño = Programador("Paco", 1500, "Python")

    empleados = [pepe, antonio, paquiño]

    for e in empleados:
        print(e)