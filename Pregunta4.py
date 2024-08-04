class RECTANGULO:
    def __init__(self, largo, ancho):
        try:
            if largo <= 0 or ancho <= 0:
                raise ValueError("El largo y el ancho deben ser positivos.")
            self.largo = largo
            self.ancho = ancho
        except TypeError:
            print("Error: Los valores para largo y ancho deben ser números.")
        except ValueError as val_e:
            print(f"Error: {val_e}")

    def calcular_area(self):
        try:
            return self.largo * self.ancho
        except Exception as e:
            print(f"Error al calcular el área: {e}")

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        try:
            if lado <= 0:
                raise ValueError("El lado debe ser positivo.")
            super().__init__(lado, lado)
        except TypeError:
            print("Error: El valor del lado debe ser un número.")
        except ValueError as val_e:
            print(f"Error: {val_e}")

largo = float(input("Ingrese el largo: "))
ancho = float(input("Ingrese el ancho: "))

# Crear un objeto de tipo RECTANGULO
try:
    rectangulo = RECTANGULO(largo, ancho)
    print(f"Área del rectángulo: {rectangulo.calcular_area()}")
except Exception as e:
    print(f"Error al crear el rectángulo: {e}")

# Crear un objeto de tipo CUADRADO
try:
    cuadrado = CUADRADO(largo)
    print(f"Área del cuadrado: {cuadrado.calcular_area()}")
except Exception as e:
    print(f"Error al crear el cuadrado: {e}")
