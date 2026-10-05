class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.titulo} escrito por {self.autor}."



class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def añadirLibros(self, libro):
        self.libros.append(libro)

    def buscarLibro(self, titulo):
        for l in self.libros:
            if l.titulo == titulo:
                return l

        return None

    def listarLibros(self):
        print(f"Listado de libros de {self.nombre}")
        for l in self.libros:
            print(l)


if __name__ == "__main__":

    libro1 = Libro("Mariposas", "JG Maestro")
    libro2 = Libro("Bochan", "Euclides")

    biblioteca = Biblioteca("BiblioCovelo")

    biblioteca.añadirLibros(libro1)
    biblioteca.añadirLibros(libro2)
    biblioteca.listarLibros()
    print(f"\nBuscando libro... \n{biblioteca.buscarLibro("Mariposas")}")