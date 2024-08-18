class Producto:  # Clase con su constructor y el formato para mostrar la información
    def __init__(self, categoria, fabricante, costo_compra, costo_venta):
        self.categoria = categoria
        self.fabricante = fabricante
        self.costo_compra = costo_compra
        self.costo_venta = costo_venta

    def mostrar_datos(self):  # Función para formatear la impresión de la información
        print(f"Producto: {self.categoria}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Costo de Compra: ${self.costo_compra}")
        print(f"Costo de Venta: ${self.costo_venta}")
        print("-" * 30)

def calcular_costo_venta(costo_compra, margen=1.30):  # Calcular el costo de venta
    return costo_compra * margen

def registrar_producto():  # Inputs del usuario
    print("Seleccione el tipo de producto que desea registrar:")
    print("1. Cuaderno")
    print("2. Lápiz")
    seleccion = int(input("Ingrese el número correspondiente al tipo de producto: "))
    
    if seleccion == 1:
        categoria = input("Ingrese el tipo de cuaderno (e.g., '50 hojas', '100 hojas'): ")
        fabricante = "HOJITAS"
    elif seleccion == 2:
        categoria = input("Ingrese el tipo de lápiz (e.g., 'grafito', 'colores'): ")
        fabricante = "RAYAS"
    else:
        print("Selección no válida. Por favor, intente de nuevo.")
        return registrar_producto()

    costo_compra = float(input(f"Ingrese el costo de compra para {categoria} ({fabricante}): "))
    costo_venta = calcular_costo_venta(costo_compra)
    return Producto(categoria=categoria, fabricante=fabricante, costo_compra=costo_compra, costo_venta=costo_venta)

# Registro de productos
productos = []

# Bucle para permitir el ingreso de múltiples productos
while True:
    productos.append(registrar_producto())
    
    seguir = input("¿Desea registrar otro producto? (s/n): ").strip().lower()
    if seguir == 'n':
        break

# Visualización de la información de los productos registrados
print("\nProductos registrados:")
for producto in productos:
    producto.mostrar_datos()

#GEPA