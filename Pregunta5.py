class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = None

    def display(self):
        try:
            if self.edad is None:
                edad_info = "Edad no asignada"
            else:
                edad_info = f"Edad: {self.edad}"
            
            if self.notas is None:
                notas_info = "Notas no asignadas"
            else:
                notas_info = f"Notas: {self.notas}"
                
            print(f"Nombre: {self.nombre}")
            print(f"Número de Registro: {self.numero_registro}")
            print(edad_info)
            print(notas_info)
        except Exception as e:
            print(f"Error al mostrar la información: {e}")

    def set_age(self, edad):
        try:
            # Validar que la edad sea un número entero positivo
            if not isinstance(edad, int) or edad <= 0:
                raise ValueError("La edad debe ser un número entero positivo.")
            self.edad = edad
        except ValueError as e:
            print(f"Error al asignar la edad: {e}")
        except TypeError:
            print("Error: La edad debe ser un número entero.")

    def set_nota(self, notas):
        try:
            # Validar que las notas sean una lista de números
            if not isinstance(notas, list) or not all(isinstance(nota, (int, float)) for nota in notas):
                raise ValueError("Las notas deben ser una lista de números.")
            self.notas = notas
        except ValueError as e:
            print(f"Error al asignar las notas: {e}")
        except TypeError:
            print("Error: Las notas deben ser una lista de números.")
# Ejemplo de uso
nombre = input("Ingrese el nombre del alumno: ")
num_registro = int(input("Ingrese el número de registro: "))
edad = int(input("Ingrese la edad: "))

try:
    alumno = Alumno(nombre,num_registro)
    alumno.set_age(edad)
    alumno.set_nota([8.5,14,13.5])
    alumno.display()
except Exception as e:
    print(f"Error al crear el alumno: {e}")
