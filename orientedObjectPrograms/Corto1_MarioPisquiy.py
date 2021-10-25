class Libro:
    def __init__(self,titulo,autor,precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __str__(self):
        return "El libro {} de autor {} tiene un precio de Q.{}".format(self.titulo, self.autor, self.precio)

class DetallesLibro(Libro):
    def caracteristicas(self,NoPags,Lenguaje):
        return "El libro {} de autor {} tiene un precio de Q.{}, su No. de paginas es {} y esta escrito en {}".format(self.titulo, self.autor, self.precio, NoPags, Lenguaje)

class Genero(Libro):
    def caracteristicas(self,genero,Valoracion):
        return "El libro {} de autor {} tiene un precio de Q.{}, su genero es {} y su valoración es {} estrellas".format(self.titulo, self.autor, self.precio, genero, Valoracion)
        
libro1 = Libro("Historia de un Pepe","José Milla",60)
libro2 = DetallesLibro("Los Nazarenos","José Milla",55)
libro3 = Genero("La sombra de los vientos","Carlos Ruiz Zafón",170)
print(libro1)
print(libro2.caracteristicas(150,"Español"))
print(libro3.caracteristicas("Narración",5))