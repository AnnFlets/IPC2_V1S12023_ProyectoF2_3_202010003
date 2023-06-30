class Nodo:
    # Método constructor con parámetro
    def __init__(self, usuario):
        self.usuario = usuario
        self.siguiente = None

    # Método para imprimir usuario
    def imprimir(self):
        self.usuario.imprimir()

    # Método para imprimir películas favoritas
    def imprimir_peliculas_fav(self):
        self.usuario.imprimir_peliculas_fav()

    # Método para agregar una película a favoritos
    def agregar_pelicula_favorita(self, pelicula):
        self.usuario.agregar_pelicula_favorita(pelicula)

    # Métodos GET
    def get_usuario(self):
        return self.usuario

    def get_siguiente(self):
        return self.siguiente

    def get_id(self):
        return self.usuario.get_id()

    def get_nombre(self):
        return self.usuario.get_nombre()

    def get_apellido(self):
        return self.usuario.get_apellido()

    def get_telefono(self):
        return self.usuario.get_telefono()

    def get_correo(self):
        return self.usuario.get_correo()

    def get_contrasena(self):
        return self.usuario.get_contrasena()

    def get_rol(self):
        return self.usuario.get_rol()

    def get_peliculas_fav(self):
        return self.usuario.get_peliculas_fav()

    # Métodos SET
    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def set_id(self, id):
        self.usuario.set_id(id)

    def set_nombre(self, nombre):
        self.usuario.set_nombre(nombre)

    def set_apellido(self, apellido):
        self.usuario.set_apellido(apellido)

    def set_telefono(self, telefono):
        self.usuario.set_telefono(telefono)

    def set_correo(self, correo):
        self.usuario.set_correo(correo)

    def set_contrasena(self, contrasena):
        self.usuario.set_contrasena(contrasena)

    def set_rol(self, rol):
        self.usuario.set_rol(rol)

    def set_peliculas_fav(self, peliculas_fav):
        self.usuario.set_peliculas_fav(peliculas_fav)