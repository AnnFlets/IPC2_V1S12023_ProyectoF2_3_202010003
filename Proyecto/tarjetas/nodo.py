class Nodo:
    # Método constructor con parámetros
    def __init__(self, tarjeta):
        self.tarjeta = tarjeta
        self.anterior = None
        self.siguiente = None

    # Imprimir tarjeta
    def imprimir(self):
        self.tarjeta.imprimir()

    # Métodos GET
    def get_tarjeta(self):
        return self.tarjeta

    def get_anterior(self):
        return self.anterior

    def get_siguiente(self):
        return self.siguiente

    def get_id(self):
        return self.tarjeta.get_id()

    def get_tipo(self):
        return self.tarjeta.get_tipo()

    def get_numero(self):
        return self.tarjeta.get_numero()

    def get_titular(self):
        return self.tarjeta.get_titular()

    def get_fecha_exp(self):
        return self.tarjeta.get_fecha_exp()

    # Métodos SET
    def set_tarjeta(self, tarjeta):
        self.tarjeta = tarjeta

    def set_anterior(self, anterior):
        self.anterior = anterior

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def set_id(self, id):
        self.tarjeta.set_id(id)

    def set_tipo(self, tipo):
        self.tarjeta.set_tipo(tipo)

    def set_numero(self, numero):
        self.tarjeta.set_numero(numero)

    def set_titular(self, titular):
        self.tarjeta.set_titular(titular)

    def set_fecha_exp(self, fecha_exp):
        self.tarjeta.set_fecha_exp(fecha_exp)