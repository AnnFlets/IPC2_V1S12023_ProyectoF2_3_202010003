class Nodo:
    # Método constructor con parámetro
    def __init__(self, sala):
        self.sala = sala
        self.anterior = None
        self.siguiente = None

    # Imprimir sala
    def imprimir(self):
        self.sala.imprimir()

    # Imprimir información y estado de la sala
    def imprimir_info_estado(self):
        self.sala.imprimir_info_estado()

    # Métodos GET
    def get_sala(self):
        return self.sala

    def get_anterior(self):
        return self.anterior

    def get_siguiente(self):
        return self.siguiente

    def get_id(self):
        return self.sala.get_id()

    def get_cine(self):
        return self.sala.get_cine()

    def get_numero(self):
        return self.sala.get_numero()

    def get_asientos(self):
        return self.sala.get_asientos()

    def get_cantidad_asientos(self):
        return self.sala.get_cantidad_asientos()

    def get_asientos_disponibles(self):
        return self.sala.get_asientos_disponibles()

    # Métodos SET
    def set_sala(self, sala):
        self.sala = sala

    def set_anterior(self, anterior):
        self.anterior = anterior

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def set_id(self, id):
        self.sala.set_id(id)

    def set_cine(self, cine):
        self.sala.set_cine(cine)

    def set_numero(self, numero):
        self.sala.set_numero(numero)

    def set_asientos(self, asientos):
        self.sala.set_asientos(asientos)

    def set_cantidad_asientos(self, cantidad_asientos):
        self.sala.set_cantidad_asientos(cantidad_asientos)

    def set_asientos_disponibles(self, asientos_disponibles):
        self.sala.set_asientos_disponibles(asientos_disponibles)