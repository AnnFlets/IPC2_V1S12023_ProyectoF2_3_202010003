class Tarjeta:
    # Método constructor con parámetros
    def __init__(self, tipo, numero, titular, fecha_exp):
        self.id = 0
        self.tipo = tipo
        self.numero = numero
        self.titular = titular
        self.fecha_exp = fecha_exp

    # Método para imprimir la información de la tarjeta
    def imprimir(self):
        print(self.id, "- NO. :", self.numero, "| TITULAR :", self.titular,
              "\n\tTIPO :", self.tipo, "| FECHA DE EXPIRACIÓN :", self.fecha_exp)

    # Métodos GET
    def get_id(self):
        return self.id

    def get_tipo(self):
        return self.tipo

    def get_numero(self):
        return self.numero

    def get_titular(self):
        return self.titular

    def get_fecha_exp(self):
        return self.fecha_exp

    # Métodos SET
    def set_id(self, id):
        self.id = id

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_numero(self, numero):
        self.numero = numero

    def set_titular(self, titular):
        self.titular = titular

    def set_fecha_exp(self, fecha_exp):
        self.fecha_exp = fecha_exp