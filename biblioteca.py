class Autor:
    def __init__(self, nombre, apellidos):
        self.Nombre = nombre
        self.Apellidos = apellidos
    def MostrarAutor(self):
        print(f"Autor: {self.Nombre} {self.Apellidos}")

class Libro:
    def __init__(self, titulo, isbn):
        self.Titulo = titulo
        self.ISBN = isbn
    def AñadirAutor(self, objetoautor):
        self.Autor = objetoautor
    def MostrarLibro(self):
        print("------Libro------")
        print(f"Título: {self.Titulo}")
        print(f"ISBN: {self.ISBN}")
        self.Autor.MostrarAutor()
        print("-----------------")
    def ObtenerTitulo(self):
        return self.Titulo

class Biblioteca:
    def __init__(self):
        self.ListaLibros = []
    def NumeroLibros(self):
        return len(self.ListaLibros)
    def AñadirLibro(self, objetolibro):
        self.ListaLibros = self.ListaLibros + [objetolibro]
    def MostrarBiblioteca(self):
        for libro in self.ListaLibros:
           libro.MostrarLibro()
    def BorrarLibro(self, titulo):
        encontrado = False
        for item in self.ListaLibros:
            if item.ObtenerTitulo == titulo:
                encontrado == True
                break
        if encontrado:
            print("Libro borrado correctamente")
        else:
            print("Libro no encontrado")

def MostrarMenu():
    print ("""Menu
    1) Añadir libro a la biblioteca
    2) Mostrar biblioteca
    3) Borrar libro
    4) ¿Numero de libros?
    5) Salir""")

def AñadirLibroABiblioteca(biblioteca):
    titulo = input("Nombre del Libro: ")
    isbn = int(input("ISBN: "))
    nombresAutor = input("Nombre del autor: ")
    apellidosAutor = input("Apellidos del autor: ")
    libro = Libro(titulo, isbn)
    autor = Autor(nombresAutor, apellidosAutor)
    libro.AñadirAutor(autor)
    biblioteca.AñadirLibro(libro)
    return biblioteca

def MostrarBiblioteca(biblioteca):
    biblioteca.MostrarBiblioteca()

def BorrarLibro(biblioteca):
    titulo = input("Ingresa el titulo a borrar: ")
    biblioteca.BorrarLibro(titulo)

def NumeroLibros(biblioteca):
    print(f"El número de libros que hay en la biblioteca es: {biblioteca.NumeroLibros()}") 

fin = False
biblioteca = Biblioteca()

while fin == False:
    MostrarMenu()
    opc = int(input("Selecciona una opción: "))
    if opc == 1:
        AñadirLibroABiblioteca(biblioteca)
    if opc == 2:
        MostrarBiblioteca(biblioteca)
    if opc == 3:
        BorrarLibro(biblioteca)
    if opc == 4:
        NumeroLibros(biblioteca)
    if opc == 5:
        fin = True





        