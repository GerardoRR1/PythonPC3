
import operaciones

def main():
    try:
        
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        
        print(f"Suma: {operaciones.suma(a, b)}")
        print(f"Resta: {operaciones.resta(a, b)}")
        print(f"Producto: {operaciones.producto(a, b)}")
        
        resultado_division = operaciones.division(a, b)
        if resultado_division is not None:
            print(f"División: {resultado_division}")
    except ValueError:
        print("Error: Entrada no válida. Debe ingresar números.")

if __name__ == "__main__":
    main()
