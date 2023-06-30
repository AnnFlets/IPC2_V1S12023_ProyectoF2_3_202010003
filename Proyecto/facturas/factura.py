class Factura:
    # Método constructor con parámetros
    def __init__(self, correo, telefono, nombre, nit, direccion, pago):
        self.id = 0
        self.correo = correo
        self.telefono = telefono
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.pago = pago
        self.total = 0
        self.boletos = []

    # Método para imprimir los datos de facturación
    def imprimir(self):
        print(self.id, "- NOMBRE:", self.nombre, "| NIT:", self.nit, "| DIRECCIÓN:", self.direccion,
              "\n\tCANTIDAD DE BOLETOS:", len(self.boletos),
              "\n\tTOTAL:", self.total)

    # Método para agregar un boleto a la lista
    def agregar_boleto(self, boleto):
        self.boletos.append(boleto)

    # Métodos GET
    def get_id(self):
        return self.id

    def get_correo(self):
        return self.correo

    def get_telefono(self):
        return self.telefono

    def get_nombre(self):
        return self.nombre

    def get_nit(self):
        return self.nit

    def get_direccion(self):
        return self.direccion

    def get_pago(self):
        return self.pago

    def get_total(self):
        return self.total

    def get_boletos(self):
        return self.boletos

    # Métodos SET
    def set_id(self, id):
        self.id = id

    def set_correo(self, correo):
        self.correo = correo

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_nit(self, nit):
        self.nit = nit

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_pago(self, pago):
        self.pago = pago

    def set_total(self, total):
        self.total = total

    def set_boletos(self, boletos):
        self.boletos = boletos