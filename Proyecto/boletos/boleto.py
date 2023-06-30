class Boleto:
    # Método constructor con parámetros
    def __init__(self, pelicula, fecha, hora, cine, sala, asiento, precio):
        self.id = 0
        self.numero = ""
        self.pelicula = pelicula
        self.fecha = fecha
        self.hora = hora
        self.cine = cine
        self.sala = sala
        self.asiento = asiento
        self.precio = precio
        self.estado = "activo"

    # Método para definir el número de boleto
    def establecer_numero(self, id):
        self.numero = "#USACIPC2_202010003_" + str(id)

    # Método para imprimir la información del boleto
    def imprimir(self):
        print(self.id, "- NO.:", self.numero, "| PELÍCULA:", self.pelicula, "| FECHA Y HORA:", self.fecha, self.hora,
              "\n\tSALA:", self.sala, "| ASIENTO:", self.asiento, "| ESTADO:", self.estado)

    # Métodos GET
    def get_id(self):
        return self.id

    def get_numero(self):
        return self.numero

    def get_pelicula(self):
        return self.pelicula

    def get_fecha(self):
        return self.fecha

    def get_hora(self):
        return self.hora

    def get_cine(self):
        return self.cine

    def get_sala(self):
        return self.sala

    def get_asiento(self):
        return self.asiento

    def get_precio(self):
        return self.precio

    def get_estado(self):
        return self.estado

    # Métodos SET
    def set_id(self, id):
        self.id = id

    def set_numero(self, numero):
        self.numero = numero

    def set_pelicula(self, pelicula):
        self.pelicula = pelicula

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_hora(self, hora):
        self.hora = hora

    def set_cine(self, cine):
        self.cine = cine

    def set_sala(self, sala):
        self.sala = sala

    def set_asiento(self, asiento):
        self.asiento = asiento

    def set_precio(self, precio):
        self.precio = precio

    def set_estado(self, estado):
        self.estado = estado