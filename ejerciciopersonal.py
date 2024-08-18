#el ejercicio que hare es de una gestion de libros personales de mi blioteca este ejercicio me ayudara a mantener una organizacion mucho mejor.
#el ejercicio tendria que permitirme ingresar,buscar y eliminar libos de mi biblioteca personal
#esto seria la cosas que podrian hacer con el ejercicio:
#Registrar un libro: Cada vez que quieras añadir un nuevo libro a tu colección, utiliza la opción "Registrar un libro" en el menú
#Buscar un libro: Puedes buscar libros específicos por su título o autor
#Eliminar un libro: Si decides sacar un libro de tu colección puedes eliminarlo por su título
#Mostrar todos los libros: Esta opción te permitirá ver todos los libros que has registrado hasta el momento

class Libro:
    def __init__(self, titulo, autor, ano_publicacion, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
        self.genero = genero
        self.paginas = paginas

    def mostrar_info(self):
        print("-" * 30)
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.ano_publicacion}")
        print(f"Género: {self.genero}")
        print(f"Número de Páginas: {self.paginas}")
        print("-" * 30)

def registrar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    ano_publicacion = int(input("Ingrese el año de publicación del libro: "))
    genero = input("Ingrese el género del libro: ")
    paginas = int(input("Ingrese el número de páginas del libro: "))
    return Libro(titulo, autor, ano_publicacion, genero, paginas)

def buscar_libro(titulo=None, autor=None):
    for libro in biblioteca:
        if (titulo and libro.titulo.lower() == titulo.lower()) or (autor and libro.autor.lower() == autor.lower()):
            return libro
    return None

def eliminar_libro(titulo):
    libro = buscar_libro(titulo=titulo)
    if libro:
        biblioteca.remove(libro)
        print(f"El libro '{titulo}' ha sido eliminado de la colección.")
    else:
        print(f"No se encontró ningún libro con el título '{titulo}'.")

def mostrar_todos_los_libros():
    if not biblioteca:
        print("No hay libros en la colección.")
    else:
        for libro in biblioteca:
            libro.mostrar_info()

def menu_principal():
    while True:
        print("Opciones de gestión de la biblioteca:")
        print("1. Registrar un libro")
        print("2. Buscar un libro")
        print("3. Eliminar un libro")
        print("4. Mostrar todos los libros")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            nuevo_libro = registrar_libro()
            biblioteca.append(nuevo_libro)
            print("Libro registrado con éxito.")
        elif opcion == 2:
            criterio = input("¿Desea buscar por título o autor? (Ingrese 'título' o 'autor'): ").strip().lower()
            if criterio == 'título':
                titulo = input("Ingrese el título del libro: ")
                libro = buscar_libro(titulo=titulo)
            elif criterio == 'autor':
                autor = input("Ingrese el autor del libro: ")
                libro = buscar_libro(autor=autor)
            else:
                print("Opción no válida.")
                continue

            if libro:
                libro.mostrar_info()
            else:
                print("Libro no encontrado.")
        elif opcion == 3:
            titulo = input("Ingrese el título del libro que desea eliminar: ")
            eliminar_libro(titulo)
        elif opcion == 4:
            mostrar_todos_los_libros()
        elif opcion == 5:
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Lista global para almacenar los libros
biblioteca = []

# Ejecutar el menú principal
menu_principal()
