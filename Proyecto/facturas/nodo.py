class Nodo:
    # Método constructor con parámetro
    def __init__(self, factura):
        self.factura = factura
        self.siguiente = None

    # Método para imprimir la información de las facturas
    def imprimir(self):
        self.factura.imprimir()

    # Método para agregar un boleto a la factura
    def agregar_boleto(self, boleto):
        self.factura.agregar_boleto(boleto)

    # Métodos GET
    def get_factura(self):
        return self.factura

    def get_siguiente(self):
        return self.siguiente

    def get_id(self):
        return self.factura.get_id()

    def get_correo(self):
        return self.factura.get_correo()

    def get_telefono(self):
        return self.factura.get_telefono()

    def get_nombre(self):
        return self.factura.get_nombre()

    def get_nit(self):
        return self.factura.get_nit()

    def get_direccion(self):
        return self.factura.get_direccion()

    def get_pago(self):
        return self.factura.get_pago()

    def get_total(self):
        return self.factura.get_total()

    def get_boletos(self):
        return self.factura.get_boletos()

    # Métodos SET
    def set_factura(self, factura):
        self.factura = factura

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def set_id(self, id):
        self.factura.set_id(id)

    def set_correo(self, correo):
        self.factura.set_correo(correo)

    def set_telefono(self, telefono):
        self.factura.set_telefono(telefono)

    def set_nombre(self, nombre):
        self.factura.set_nombre(nombre)

    def set_nit(self, nit):
        self.factura.set_nit(nit)

    def set_direccion(self, direccion):
        self.factura.set_direccion(direccion)

    def set_pago(self, pago):
        self.factura.set_pago(pago)

    def set_total(self, total):
        self.factura.set_total(total)

    def set_boletos(self, boletos):
        self.factura.set_boletos(boletos)