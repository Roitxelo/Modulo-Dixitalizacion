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
        for l in self.libros:
            print(libro)

            