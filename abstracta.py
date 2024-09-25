from abc import ABC, abstractmethod


# 1. Clase abstracta Publicacion
class Publicacion(ABC):

    @abstractmethod
    def informacion(self):
        pass

    @abstractmethod
    def resumen(self):
        pass


# 2. Clase derivada Libro
class Libro(Publicacion):
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Implementación de informacion
    def informacion(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"

    # Implementación de resumen
    def resumen(self):
        return f"El libro '{self.titulo}' fue escrito por {self.autor} y tiene {self.paginas} páginas."


# 2. Clase derivada Revista
class Revista(Publicacion):
    def __init__(self, titulo, edicion, mes):
        self.titulo = titulo
        self.edicion = edicion
        self.mes = mes

    # Implementación de informacion
    def informacion(self):
        return f"Revista: {self.titulo}, Edición: {self.edicion}, Mes: {self.mes}"

    # Implementación de resumen
    def resumen(self):
        return f"La revista '{self.titulo}', edición {self.edicion}, se publicó en el mes de {self.mes}."


# 4. Creación de instancias y llamada a métodos
libro = Libro("la guerra de las galacias", "carlos uribe", 897)
revista = Revista("los pitufos", "202", "Septiembre")

# Mostrar información y resumen de cada instancia
print(libro.informacion())
print(libro.resumen())

print(revista.informacion())
print(revista.resumen())