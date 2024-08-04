# operaciones.py

def suma(a, b):
    try:
        return a + b
    except TypeError:
        print("Error:Los argumentos deben ser números.")

def resta(a, b):
    try:
        return a - b
    except TypeError:
        print("Error:Los argumentos deben ser números.")

def producto(a, b):
    try:
        return a * b
    except TypeError:
        print("Error:Los argumentos deben ser números.")

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("No es posible dividir entre cero.")
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except TypeError:
        print("Error:Los argumentos deben ser números.")
