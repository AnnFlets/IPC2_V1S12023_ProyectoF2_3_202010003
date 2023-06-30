class Nodo:
    # Método constructor
    def __init__(self, pelicula):
        self.pelicula = pelicula
        self.siguiente = None
        self.anterior = None

    # Método para imprimir la información de las películas
    def imprimir(self):
        self.pelicula.imprimir()

    # Métodos GET
    def get_pelicula(self):
        return self.pelicula

    def get_siguiente(self):
        return self.siguiente

    def get_anterior(self):
        return self.anterior

    def get_id(self):
        return self.pelicula.get_id()

    def get_categoria(self):
        return self.pelicula.get_categoria()

    def get_titulo(self):
        return self.pelicula.get_titulo()

    def get_director(self):
        return self.pelicula.get_director()

    def get_anio(self):
        return self.pelicula.get_anio()

    def get_fecha(self):
        return self.pelicula.get_fecha()

    def get_hora(self):
        return self.pelicula.get_hora()

    def get_imagen(self):
        return self.pelicula.get_imagen()

    def get_precio(self):
        return self.pelicula.get_precio()

    # Métodos SET
    def set_pelicula(self, pelicula):
        self.pelicula = pelicula

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def set_anterior(self, anterior):
        self.anterior = anterior

    def set_id(self, id):
        self.pelicula.set_id(id)

    def set_categoria(self, categoria):
        self.pelicula.set_categoria(categoria)

    def set_titulo(self, titulo):
        self.pelicula.set_titulo(titulo)

    def set_director(self, director):
        self.pelicula.set_director(director)

    def set_anio(self, anio):
        self.pelicula.set_anio(anio)

    def set_fecha(self, fecha):
        self.pelicula.set_fecha(fecha)

    def set_hora(self, hora):
        self.pelicula.set_hora(hora)

    def set_imagen(self, imagen):
        self.pelicula.set_imagen(imagen)

    def set_precio(self, precio):
        self.pelicula.set_precio(precio)