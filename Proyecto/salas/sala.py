class Sala:
    # Método constructor con parámetros
    def __init__(self, cine, numero, asientos):
        self.id = 0
        self.cine = cine
        self.numero = numero
        self.cantidad_asientos = asientos
        self.asientos = self.determinar_asientos(asientos)
        self.asientos_disponibles = asientos

    # Método para definir el número de asientos
    def determinar_asientos(self, asientos):
        numero_asientos = []
        for i in range(int(asientos)):
            numero_asientos.append((i + 1))
        return numero_asientos

    # Método para establecer la cantidad de asientos disponibles
    def determinar_asientos_disponibles(self, asientos_disponibles):
        self.asientos_disponibles = len(self.asientos)

    # Método para imprimir la información de la sala
    def imprimir(self):
        print(self.id, "- SALA :", self.numero, "| CINE :", self.cine, "| ASIENTOS:", self.cantidad_asientos)

    # Método para imprimir la información y estado de la sala actualmente
    def imprimir_info_estado(self):
        print(self.id, "- SALA :", self.numero, "| CINE :", self.cine, "| ASIENTOS DISPONIBLES:", len(self.asientos))

    # Métodos GET
    def get_id(self):
        return self.id

    def get_cine(self):
        return self.cine

    def get_numero(self):
        return self.numero

    def get_asientos(self):
        return self.asientos

    def get_cantidad_asientos(self):
        return self.cantidad_asientos

    def get_asientos_disponibles(self):
        return self.asientos_disponibles

    # Métodos SET
    def set_id(self, id):
        self.id = id

    def set_cine(self, cine):
        self.cine = cine

    def set_numero(self, numero):
        self.numero = numero

    def set_asientos(self, asientos):
        self.asientos = asientos

    def set_cantidad_asientos(self, cantidad_asientos):
        self.cantidad_asientos = cantidad_asientos

    def set_asientos_disponibles(self, asientos_disponibles):
        self.asientos_disponibles = asientos_disponibles