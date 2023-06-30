from facturas.nodo import Nodo

class ListaFacturas:
    # Método constructor
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
        self.id_factura = 0
        self.id_boleto = 0

    # Métodos para hacer iterable la lista
    def loop(self):
        if self.cabeza != None:
            actual = self.cabeza
            while actual != None:
                yield actual.get_factura()
                actual = actual.get_siguiente()

    def __iter__(self):
        return iter(self.loop())

    # Método para saber si la lista está vacía
    def esta_vacia(self):
        if self.tamanio == 0:
            return True
        else:
            return False

    # Método para devolver una lista con los boletos existentes
    def devolver_boletos(self):
        boletos_existentes = []
        actual = self.cabeza
        while actual != None:
            factura = actual.get_factura()
            for boleto in factura.get_boletos():
                boletos_existentes.append(boleto)
            actual = actual.get_siguiente()
        return boletos_existentes

    # Método para agregar una factura a la lista
    def agregar_factura(self, factura):
        self.id_factura = self.id_factura + 1
        factura.set_id(self.id_factura)
        nuevo = Nodo(factura)
        if self.cabeza == None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.get_siguiente() != None:
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo)
        self.tamanio = self.tamanio + 1

    # Método para agregar boletos a una factura
    def agregar_boleto(self, factura, boleto):
        self.id_boleto = self.id_boleto + 1
        boleto.set_id(self.id_boleto)
        boleto.establecer_numero(self.id_boleto)
        factura.agregar_boleto(boleto)

    # Método para comprobar que exista una factura con ID determinado
    def verificar_id(self, id_factura):
        actual = self.cabeza
        while actual != None:
            if actual.get_id() == id_factura:
                for boleto in actual.get_boletos():
                    boleto.imprimir()
                return True
            actual = actual.get_siguiente()
        return False

    # Método para cambiar el estado de un boleto con ID determinado
    def verificar_cambio_estado_boleto(self, id_boleto, estado):
        actual = self.cabeza
        while actual != None:
            boletos = actual.get_boletos()
            for boleto in boletos:
                if boleto.get_id() == id_boleto:
                    boleto.set_estado(estado)
                    return True
            actual = actual.get_siguiente()
        return False

    # Método para imprimir la información de las facturas
    def imprimir(self):
        actual = self.cabeza
        while actual != None:
            actual.imprimir()
            actual = actual.get_siguiente()

    # Método para imprimir boletos de acuerdo al estado
    def imprimir_boletos_estado(self, estado):
        boletos_encontrados = 0
        actual = self.cabeza
        while actual != None:
            boletos = actual.get_boletos()
            for boleto in boletos:
                if boleto.get_estado() == estado:
                    boleto.imprimir()
                    boletos_encontrados = boletos_encontrados + 1
            actual = actual.get_siguiente()
        if boletos_encontrados == 0:
            return False
        else:
            return True

    # Método para imprimir facturas dependiendo el correo y teléfono
    def imprimir_facturas_usuario(self, correo, telefono):
        facturas_encontradas = 0
        actual = self.cabeza
        while actual != None:
            if correo == actual.get_correo() and telefono == actual.get_telefono():
                actual.imprimir()
                facturas_encontradas = facturas_encontradas + 1
            actual = actual.get_siguiente()
        if facturas_encontradas == 0:
            return False
        else:
            return True

    # Métodos GET
    def get_cabeza(self):
        return self.cabeza

    def get_tamanio(self):
        return self.tamanio

    def get_id_factura(self):
        return self.id_factura

    def get_id_boleto(self):
        return self.id_boleto

    # Métodos SET
    def set_cabeza(self, cabeza):
        self.cabeza = cabeza

    def set_tamanio(self, tamanio):
        self.tamanio = tamanio

    def set_id_factura(self, id_factura):
        self.id_factura = id_factura

    def set_id_boleto(self, id_boleto):
        self.id_boleto = id_boleto