from punto import Punto
from rectangulo import RECTANGULO

# Creación de los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0)
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Impresión de los puntos
print("Puntos:")
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")

#cuadrantes
print("\nCuadrantes:")
print(f"A está en el {A.cuadrante()}")
print(f"C está en el {C.cuadrante()}")
print(f"D está en el {D.cuadrante()}")
#vector
vector_AB = A.vector(B)
vector_BA = B.vector(A)
print("\nVectores:")
print(f"Vector AB: {vector_AB}")
print(f"Vector BA: {vector_BA}")

# Consulta la distancia 
distancia_AB = A.distancia(B)
distancia_BA = B.distancia(A)
print("\nDistancias:")
print(f"Distancia entre A y B: {distancia_AB}")
print(f"Distancia entre B y A: {distancia_BA}")

# (Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0)
distancia_A_origen = A.distancia(D)
distancia_B_origen = B.distancia(D)
distancia_C_origen = C.distancia(D)

mas_lejos = max(distancia_A_origen, distancia_B_origen, distancia_C_origen)
if mas_lejos == distancia_A_origen:
    print("El punto A está más lejos del origen.")
elif mas_lejos == distancia_B_origen:
    print("El punto B está más lejos del origen.")
else:
    print("El punto C está más lejos del origen.")

# Creación de un rectángulo utilizando los puntos A y B
rect = RECTANGULO(A, B)
print("\nRectángulo formado por A y B:")
print(f"Base: {rect.base()}")
print(f"Altura: {rect.altura()}")
print(f"Área: {rect.area()}")
