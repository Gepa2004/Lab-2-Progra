class Canino:  # Clase Canino con su constructor y función de mostrar información
    def __init__(self, apodo, anios, numero_propietario, tipo_raza, peso_canino, tamaño_canino):
        self.apodo = apodo
        self.anios = anios
        self.numero_propietario = numero_propietario
        self.tipo_raza = tipo_raza
        self.tamaño_canino = tamaño_canino
        self.peso_canino = peso_canino
        self.condicion = "No atendido"

    def mostrar_datos(self):  # Función para formatear la impresión de la información
        print(f"Apodo: {self.apodo}")
        print(f"Años: {self.anios}")
        print(f"Número del propietario: {self.numero_propietario}")
        print(f"Raza: {self.tipo_raza}")
        print(f"Tamaño: {self.tamaño_canino}")
        print(f"Condición: {self.condicion}")
        print("-" * 30)

def registrar_canino():  # Función para obtener los inputs del usuario
    apodo = input("Ingrese el nombre del canino: ")
    anios = input("Ingrese la edad del canino: ")
    numero_propietario = input("Ingrese el número del propietario: ")
    tipo_raza = input("Ingrese la raza del canino: ")
    peso_canino = float(input("Ingrese el peso del canino (en kg): "))
    if peso_canino < 10:  # if para determinar el tamaño del canino según el peso
        tamaño_canino = "Pequeño"
    else:
        tamaño_canino = "Grande"
    canino = Canino(apodo, anios, numero_propietario, tipo_raza, peso_canino, tamaño_canino)
    canino.condicion = "Atendido"  # Cambia la condición a Atendido
    return canino  # Devuelve el objeto con la condición modificada

def mostrar_caninos():  # Función para mostrar los caninos que están en la lista global
    print("\nCaninos registrados:")
    for canino in lista_caninos:
        canino.mostrar_datos()

def menu_principal():  # Función para el menú principal
    while True:
        print("Seleccione la opción que desea realizar:")
        print("1. Registrar canino")
        print("2. Mostrar caninos")
        print("3. Salir")
        opcion = int(input("Ingrese el número correspondiente a la opción que desea realizar: "))

        if opcion == 1:
            nuevo_canino = registrar_canino()
            lista_caninos.append(nuevo_canino)
        elif opcion == 2:
            mostrar_caninos()
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Lista global para almacenar los caninos
lista_caninos = []

# Ejecutar el menú principal
menu_principal()
