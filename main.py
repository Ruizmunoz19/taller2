class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Método mágico para mostrar el objeto como string (para usuarios)
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

    # Método mágico para representar formalmente el objeto (para desarrolladores)
    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', paginas={self.paginas})"

# Crear dos instancias de la clase Libro
libro1 = Libro("la guerra de las galacias", "carlos uribe", 234)
libro2 = Libro("del amor al odio", "juan carlos guerrero", 786)

# Imprimir usando __str__
print(str(libro1))  # Salida: 'la guerra de las galacias' por carlos uribe
print(str(libro2))  # Salida: 'del amor al odio' por juan carlos guerrero
# Mostrar representación formal usando __repr__
print(repr(libro1))  # Salida: Libro(titulo='la guerra de las galacias', autor='carlos uribe', paginas=234)
print(repr(libro2))  # Salida: Libro(titulo='del amor al odio', autor='juan carlos guerrero', paginas=286)
