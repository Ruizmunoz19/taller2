from abc import ABC, abstractmethod


# 1. Clase abstracta Publicacion con método mágico __str__
class Publicacion(ABC):

    @abstractmethod
    def informacion(self):
        pass

    @abstractmethod
    def resumen(self):
        pass

    # Método mágico __str__ para mostrar tipo de publicación
    def __str__(self):
        return "Publicación genérica"


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

    # 2. Sobrescribiendo __str__ para incluir título
    def __str__(self):
        return f"Libro: {self.titulo}"


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

    # 2. Sobrescribiendo __str__ para incluir título
    def __str__(self):
        return f"Revista: {self.titulo}"


# 3. Creación de instancias y llamada al método __str__
libro = Libro("la guerra de las galacias", "carlos uribe", 897)
revista = Revista("los pitufos", "202", "Septiembre")

# Imprimir instancias para comprobar la funcionalidad de __str__
print(libro)  # Debería mostrar: Libro: la guerra de las galacias
print(revista)  # Debería mostrar: Revista: los pitufos