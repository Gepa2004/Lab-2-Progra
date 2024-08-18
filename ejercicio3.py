class Vehiculo:  # Clase Vehículo con su constructor y una para mostrar la información
    def __init__(self, modelo_vehiculo, tipo_vehiculo, fabricante, ano_fabricacion, recorrido, precio_venta, color_vehiculo, tipo_transmision, matricula, tipo_traccion):
        self.modelo_vehiculo = modelo_vehiculo
        self.tipo_vehiculo = tipo_vehiculo
        self.fabricante = fabricante
        self.ano_fabricacion = ano_fabricacion
        self.recorrido = recorrido
        self.precio_venta = precio_venta
        self.color_vehiculo = color_vehiculo
        self.tipo_transmision = tipo_transmision
        self.matricula = matricula
        self.tipo_traccion = tipo_traccion
        self.capacidad = "5 pasajeros"
        self.numero_ruedas = "4 ruedas"

    def mostrar_datos(self):  # Función para formatear la impresión de los datos
        print("-" * 30)
        print(f"Modelo: {self.modelo_vehiculo}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Tipo: {self.tipo_vehiculo}")
        print(f"Año: {self.ano_fabricacion}")
        print(f"Color: {self.color_vehiculo}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Número de Ruedas: {self.numero_ruedas}")
        print(f"Transmisión: {self.tipo_transmision}")
        print(f"Matrícula: {self.matricula}")
        print(f"Kilometraje: {self.recorrido}")
        print(f"Precio de Venta: ${self.precio_venta}")
        print("-" * 30)

def registrar_vehiculo():  # Inputs del usuario
    modelo_vehiculo = input("Ingrese el modelo del vehículo: ")
    tipo_vehiculo = input("Ingrese el tipo del vehículo: ")
    fabricante = input("Ingrese el fabricante del vehículo: ")
    ano_fabricacion = int(input("Ingrese el año de fabricación del vehículo: "))
    recorrido = int(input("Ingrese el kilometraje del vehículo: "))
    precio_compra = float(input(f"Ingrese el precio de compra del vehículo {modelo_vehiculo}: $"))
    color_vehiculo = input("Ingrese el color del vehículo: ")
    tipo_transmision = input("Ingrese el tipo de transmisión del vehículo: ")
    matricula = input("Ingrese la matrícula del vehículo: ")
    tipo_traccion = input("Ingrese el tipo de tracción del vehículo: ")
    precio_venta = calcular_precio_venta(precio_compra)
    return Vehiculo(modelo_vehiculo, tipo_vehiculo, fabricante, ano_fabricacion, recorrido, precio_venta, color_vehiculo, tipo_transmision, matricula, tipo_traccion)

def calcular_precio_venta(precio_compra, margen=1.4):  # Función para calcular el precio de venta
    precio_venta = precio_compra * margen
    return precio_venta

# Lista global
vehiculos = []

def mostrar_vehiculos(vehiculos):  # Función para mostrar los vehículos
    print("\nVehículos registrados:")
    for vehiculo in vehiculos:
        vehiculo.mostrar_datos()

def menu_principal():  # Función para el menú principal
    while True:
        opcion = int(input("Ingrese la opción que desea realizar: \n Opción 1: Registrar vehículo \n Opción 2: Mostrar Vehículos \n Opción 3: Salir \n"))
        if opcion == 1:
            nuevo_vehiculo = registrar_vehiculo()
            vehiculos.append(nuevo_vehiculo)
        elif opcion == 2:
            mostrar_vehiculos(vehiculos)
        elif opcion == 3:
            print("Gracias por utilizar el sistema")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu_principal()  # Ejecutar la función del menú principal
