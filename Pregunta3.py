import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

def main():
    try:
        radio_uno = float(input("Introduce el radio del primer círculo: "))
        radio_dos = float(input("Introduce el radio del segundo círculo: "))

        circulo1 = Circulo(radio_uno)
        circulo2 = Circulo(radio_dos)

        print(f"Área del círculo 1: {circulo1.calcular_area():.2f}")
        print(f"Área del círculo 2: {circulo2.calcular_area():.2f}")

    except ValueError as ValE:
        print("Error: El radio debe ser un número válido.")
        print("Detalles del error:", ValE)

if __name__ == "__main__":
    main()
