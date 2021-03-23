class Autor:
    nombre=''
    apellidos=''
    def __init__(self, nombre, apellidos):
        self.nombre=nombre
        self.apellidos=apellidos
    def MostrarAutor (self):
        print ('Autor: ', self.nombre, 'Apellidos: ', self.apellidos)
class Libro:
    titulo:''
    isbn=''
    autor=''
    def __init__(self, titulo, isbn, autor):
        self.titulo=titulo
        self.isbn=isbn
        self.autor=autor
    def AniadirAutor (self,autor):
        self.autor=autor
    def MostrarLibro(self):
        print ('Titulo: ', self.titulo, '\n ISBN: ', self.isbn, '\n Autor: ', self.autor.MostrarAutor())
    def DevolverTitulo(self):
        return self.titulo
class Biblioteca:
    libros=[]
    def __init__(self):
        self.libros=[]
    def DevolverNumeroLibros (self):
        return len(self.libros)
    def AniadirLibros(self, libro):
        self.libros=self.libros+[libro]
    def MostrarLibros (self):
        for a in self.libros:
            print('**************************************')
            a.MostrarLibro()
    def EliminarLibro(titulo):
        encontrado=False
        posicion=-1
        for a in self.libros:
            posicion +=1
            if a.DevolverTitulo ==titulo:              
                encontrado=True
                break
            
        if encontrado == True:
            del self.libros[posicion]
def MostrarMenu():
    print ("""Menu
    1) Añadir libro a la biblioteca
    2) Mostrar biblioteca
    3) Borrar libro
    4) ¿Numero de libros?
    5) Salir""")
def AñadirLibroABiblioteca(biblioteca):
    titulo = input("Introduzca el titulo del libro: ")
    isbn = input("Introduzca el ISBN del libro: ")
    autornombre = input("Introduzca el nombre del autor: ")
    autorapellidos = input("Introduzca el apellido del autor: ")
    autor = Autor( autornombre,autorapellidos)
    libro = Libro(titulo, isbn, autor)
    biblioteca.AniadirLibros(libro)
    return biblioteca
def MostrarBiblioteca(biblioteca):
    biblioteca.MostrarLibros()
def BorrarLibro(biblioteca):
    titulo = input("Introduzca el titulo del libro a borrar: ")
    biblioteca.BorrarLibro(titulo)
def NumeroLibros(biblioteca):
    print("El numero de libros en la biblioteca es: ",biblioteca.DevolverNumeroLibros())

fin = False
biblioteca = Biblioteca()
while not fin:
    MostrarMenu()
    opcion = int(input(' Seleccione opcion: '))
    if(opcion == 1):
        biblioteca = AñadirLibroABiblioteca(biblioteca)
    elif(opcion == 2):
        MostrarBiblioteca(biblioteca)
    elif(opcion == 3):
        BorrarLibro(biblioteca)
    elif(opcion == 4):
        NumeroLibros(biblioteca)
    elif(opcion == 5):
        fin = True
        print("¡Adios!")
        
