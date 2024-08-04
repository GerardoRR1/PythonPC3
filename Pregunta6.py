class Producto:
    def __init__(self, nombre, marca, año, precio):
        try:
            # Validar los tipos de datos y rangos
            if not isinstance(nombre, str) or not isinstance(marca, str):
                raise TypeError("Nombre y marca deben ser cadenas de texto.")
            if not isinstance(año, int) or año <= 0:
                raise ValueError("El año debe ser un número entero positivo.")
            if not isinstance(precio, (int, float)) or precio < 0:
                raise ValueError("El precio debe ser un número positivo.")
            
            self.nombre = nombre
            self.marca = marca
            self.año = año
            self.precio = precio
        except ValueError as e:
            print(f"Error en los datos del producto: {e}")
        except TypeError as e:
            print(f"Error en el tipo de dato del producto: {e}")

    def __str__(self):
        return f"{self.nombre} - Marca: {self.marca}, Año: {self.año}, Precio: ${self.precio:.2f}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        try:
            if not isinstance(producto, Producto):
                raise TypeError("El objeto a agregar debe ser una instancia de la clase Producto.")
            self.productos.append(producto)
        except TypeError as e:
            print(f"Error al agregar producto: {e}")

    def mostrar_productos(self):
        try:
            if not self.productos:
                raise ValueError("El catálogo está vacío.")
            for producto in self.productos:
                print(producto)
        except ValueError as e:
            print(f"Error al mostrar productos: {e}")

    def filtrar_por_año(self, año):
        try:
            if not isinstance(año, int) or año <= 0:
                raise ValueError("El año debe ser un número entero positivo.")
            productos_filtrados = [producto for producto in self.productos if producto.año == año]
            if not productos_filtrados:
                print(f"No hay productos del año {año}.")
            for producto in productos_filtrados:
                print(producto)
        except ValueError as e:
            print(f"Error al filtrar por año: {e}")

    def filtrar_por_precio(self, precio_min, precio_max):
        try:
            if not isinstance(precio_min, (int, float)) or not isinstance(precio_max, (int, float)) or precio_min < 0 or precio_max < precio_min:
                raise ValueError("Los precios deben ser números positivos y el precio máximo debe ser mayor o igual que el mínimo.")
            productos_filtrados = [producto for producto in self.productos if precio_min <= producto.precio <= precio_max]
            if not productos_filtrados:
                print(f"No hay productos en el rango de precios ${precio_min} - ${precio_max}.")
            for producto in productos_filtrados:
                print(producto)
        except ValueError as e:
            print(f"Error al filtrar por precio: {e}")


# Crear el catálogo
catalogo = Catalogo()

# Crear productos
producto1 = Producto("Disco", "Bosch", 2024, 15.99)
producto2 = Producto("Filtro", "NGK", 2022, 9.49)
producto3 = Producto("Pastillas de freno", "Brembo", 2023, 50.00)

# Agregar productos al catálogo
try:
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)
except Exception as e:
    print(f"Error al agregar productos al catálogo: {e}")

# Mostrar todos los productos
print("Todos los productos en el catálogo:")
catalogo.mostrar_productos()

# Filtrar por año
print("\nProductos del año 2023:")
catalogo.filtrar_por_año(2023)

# Filtrar por rango de precio
print("\nProductos en el rango de precios $10 - $20:")
catalogo.filtrar_por_precio(10, 20)
