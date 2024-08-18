class Aparato:  # Clase que contiene el constructor y la función para mostrar información
    def __init__(self, fabricante, modelo_aparato, ano_fabricacion, pais_origen, precio_venta, resolucion_pantalla):
        self.fabricante = fabricante
        self.modelo_aparato = modelo_aparato
        self.ano_fabricacion = ano_fabricacion
        self.pais_origen = pais_origen
        self.precio_venta = precio_venta
        self.resolucion_pantalla = resolucion_pantalla

    def mostrar_datos(self):  # Función para formatear la impresión de la información
        print("-" * 30)
        print(f"Fabricante: {self.fabricante}")
        print(f"Modelo: {self.modelo_aparato}")
        print(f"Año de Fabricación: {self.ano_fabricacion}")
        print(f"País de Origen: {self.pais_origen}")
        print(f"Precio de Venta: ${self.precio_venta}")
        print(f"Resolución: {self.resolucion_pantalla}")
        print("-" * 30)

def registrar_aparato():  # Inputs del usuario
    fabricante = input("Ingrese la marca del aparato: ")
    modelo_aparato = input("Ingrese el modelo del aparato: ")
    ano_fabricacion = input("Ingrese el año de fabricación del aparato: ")
    pais_origen = input("Ingrese el país de origen del aparato: ")
    precio_compra = float(input("Ingrese el precio de compra del aparato: $"))
    precio_venta = calcular_precio_venta(precio_compra)
    resolucion_pantalla = input("Ingrese la resolución de la pantalla del aparato: ")
    return Aparato(fabricante, modelo_aparato, ano_fabricacion, pais_origen, precio_venta, resolucion_pantalla)

def calcular_precio_venta(precio_compra, margen=1.7):  # Función para calcular el precio de venta del aparato
    precio_venta = precio_compra * margen
    return precio_venta

# Lista global
aparatos = []

def mostrar_aparatos(aparatos):  # Función para mostrar los aparatos
    print("\nAparatos registrados:")
    for aparato in aparatos:
        aparato.mostrar_datos()

def menu_principal():  # Función que contiene el menú principal
    print("-" * 30)
    while True:
        opcion = int(input("Ingrese la opción que desea realizar: \n Opción 1: Registrar aparato \n Opción 2: Mostrar aparatos \n Opción 3: Salir \n"))
        if opcion == 1:
            nuevo_aparato = registrar_aparato()
            aparatos.append(nuevo_aparato)
        elif opcion == 2:
            mostrar_aparatos(aparatos)
        elif opcion == 3:
            print("Gracias por utilizar el sistema")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        print("-" * 30)

menu_principal()
