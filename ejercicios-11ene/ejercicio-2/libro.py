class Libro:
    def __init__(self,autor=None,titulo=None,genero=None,paginas=None):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero
        self.paginas = paginas

    def get_autor(self):
        return self.autor
    
    def get_titulo(self):
        return self.titulo
    
    def get_genero(self):
        return self.genero

    def get_paginas(self):
        return self.paginas
    
    def set_autor(self,autor):
        self.autor=autor

    def set_titulo(self,titulo):
        self.titulo=titulo
    
    def set_genero(self,genero):
        self.genero=genero

    def set_paginas(self,paginas):
        self.paginas=paginas

    def clone(self):
        return Libro(self.autor,self.titulo,self.genero,self.paginas)

    def copy(self):
        return self

    def equals(self, objeto):
        return True if self is objeto else False

libro1 = Libro("pepito","el retorno","suspenso","1485")
print(libro1)
libro_clone = libro1.clone()
print(libro_clone)

libro_copia = libro1.copy()
print(libro_copia)

print(libro1.equals(libro_clone))
print(libro1.equals(libro_copia))

libro1.set_autor("p")
print(libro_copia.get_autor())