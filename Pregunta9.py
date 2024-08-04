from Pregunta3 import Circulo
from Pregunta4 import RECTANGULO, CUADRADO

def validar_numero_positivo(valor):
    try:
        numero = float(valor)
        if numero > 0:
            return numero
        else:
            print("El número debe ser positivo.")
            return None
    except ValueError:
        print("El valor ingresado no es un número válido.")
        return None


def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            radio = validar_numero_positivo(input("Ingrese el radio del círculo: "))
            if radio is not None:
                circulo = Circulo(radio)
                print(f"El área del círculo es: {circulo.calcular_area()}")
        elif opcion == "2":
            largo = validar_numero_positivo(input("Ingrese el largo del rectángulo: "))
            ancho = validar_numero_positivo(input("Ingrese el ancho del rectángulo: "))
            if largo is not None and ancho is not None:
                rectangulo = RECTANGULO(largo, ancho)
                print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
        elif opcion == "3":
            lado = validar_numero_positivo(input("Ingrese el lado del cuadrado: "))
            if lado is not None:
                cuadrado = CUADRADO(lado)
                print(f"El área del cuadrado es: {cuadrado.calcular_area()}")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
