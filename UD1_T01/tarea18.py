class Cuenta:

    def __init__(self, saldo):
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            raise Exception("Saldo insuficiente...")

    def mostrar_saldo(self):
        print("Saldo actual:", self.saldo)

