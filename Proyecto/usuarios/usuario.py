class Usuario:
    # Método constructor con parámetros
    def __init__(self, nombre, apellido, telefono, correo, contrasena, rol):
        self.id = 0
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol
        self.peliculas_fav = []

    # Método para imprimir la información del usuario
    def imprimir(self):
        if self.rol == "cliente":
            rol_usuario = "CLIENTE"
        else:
            rol_usuario = "ADMINISTRADOR"
        print(self.id, "-", rol_usuario, ":", self.nombre, self.apellido, "|", self.telefono, "|", self.correo)

    # Método para imprimir la información de las películas favoritas
    def imprimir_peliculas_fav(self):
        for pelicula in self.peliculas_fav:
            print(pelicula.get_id(), "- TÍTULO:", pelicula.get_titulo(), "| DIRECTOR:", pelicula.get_director(), "| AÑO:", pelicula.get_anio())

    # Método para agregar película a favoritas
    def agregar_pelicula_favorita(self, pelicula):
        if self.duplicado_pelicula_favorita(pelicula) == 0:
            self.peliculas_fav.append(pelicula)
            print("*** Película agregada a favoritos con éxito")
        else:
            print("[ERROR-APF]: La película ya se encuentra en favoritos")

    # Método para eliminar una película de favoritas
    def eliminar_pelicula_favorita(self, id_pelicula):
        for pelicula_fav in self.peliculas_fav:
            if pelicula_fav.get_id() == id_pelicula:
                self.peliculas_fav.remove(pelicula_fav)
                print("*** Película eliminada de favoritos con éxito")
                break
        else:
            print("[ERROR-EPF]: No existe una película en favoritos con el ID ingresado")

    # Método para verificar duplicado en las películas favoritas
    def duplicado_pelicula_favorita(self, pelicula):
        pelicula_encontrada = 0
        for pelicula_lista in self.peliculas_fav:
            if (pelicula.get_titulo() == pelicula_lista.get_titulo()
                    and pelicula.get_director() == pelicula_lista.get_director()
                    and pelicula.get_anio() == pelicula_lista.get_anio()):
                pelicula_encontrada = pelicula_encontrada + 1
        return pelicula_encontrada

    # Método para devolver una lista con las categorias existentes
    def devolver_categorias(self):
        categorias = []
        for pelicula in self.peliculas_fav:
            categoria = pelicula.get_categoria()
            if not (categoria in categorias):
                categorias.append(categoria)
        return categorias

    # Métodos GET
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_telefono(self):
        return self.telefono

    def get_correo(self):
        return self.correo

    def get_contrasena(self):
        return self.contrasena

    def get_rol(self):
        return self.rol

    def get_peliculas_fav(self):
        return self.peliculas_fav

    # Métodos SET
    def set_id(self, id):
        self.id = id

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_correo(self, correo):
        self.correo = correo

    def set_contrasena(self, contrasena):
        self.contrasena = contrasena

    def set_rol(self, rol):
        self.rol = rol

    def set_peliculas_fav(self, peliculas_fav):
        self.peliculas_fav = peliculas_fav