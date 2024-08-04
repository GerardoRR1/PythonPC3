def main():
    try:
        calificaciones_string = input("Introduce una lista de calificaciones separadas por comas: ")

        calificaciones_lista = calificaciones_string.split(',')

        calificaciones_int = []
        for calificacion in calificaciones_lista:
            calificaciones_int.append(int(calificacion.strip()))

        # Imprimir la lista de calificaciones como enteros
        print("Lista de calificaciones convertidas a enteros:", calificaciones_int)

    except ValueError as ValE:
        # Informar al usuario si hay un error de conversión
        print("Error: Uno o más valores no pudieron ser convertidos a enteros. Verifique el formato de entrada.")
        print("Detalles del error:", ValE)

if __name__ == "__main__":
    main()
