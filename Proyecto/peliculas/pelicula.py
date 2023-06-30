class Pelicula:
    # Método constructor con parámetros
    def __init__(self, categoria, titulo, director, anio, fecha, hora, imagen, precio):
        self.id = 0
        self.categoria = categoria
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora
        self.imagen = imagen
        self.precio = precio

    # Método para imprimir la información de la película
    def imprimir(self):
        print(self.id, "- PELÍCULA :", self.titulo, "| DIRECTOR :", self.director, "| CATEGORÍA :", self.categoria,
              "\n\tAÑO :", self.anio, "| FECHA Y HORA :", self.fecha, self.hora, "| PRECIO :", self.precio,
              "\n\tIMAGEN :", self.imagen)

    # Métodos GET
    def get_id(self):
        return self.id

    def get_categoria(self):
        return self.categoria

    def get_titulo(self):
        return self.titulo

    def get_director(self):
        return self.director

    def get_anio(self):
        return self.anio

    def get_fecha(self):
        return self.fecha

    def get_hora(self):
        return self.hora

    def get_imagen(self):
        return self.imagen

    def get_precio(self):
        return self.precio

    # Métodos SET
    def set_id(self, id):
        self.id = id

    def set_categoria(self, categoria):
        self.categoria = categoria

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_director(self, director):
        self.director = director

    def set_anio(self, anio):
        self.anio = anio

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_hora(self, hora):
        self.hora = hora

    def set_imagen(self, imagen):
        self.imagen = imagen

    def set_precio(self, precio):
        self.precio = precio