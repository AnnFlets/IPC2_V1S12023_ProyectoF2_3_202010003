# Librería utilizada para la lectura del archivo XML
import xml.dom.minidom as MD
# Librería utilizada para la escritura del archivo XML
import xml.etree.cElementTree as ET
from tarjetas.nodo import Nodo
from tarjetas.tarjeta import Tarjeta

class ListaTarjetas:
    # Método constructor
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
        self.id = 0

    # Métodos para hacer iterable la lista
    def loop(self):
        if self.cabeza != None:
            actual = self.cabeza
            while actual != None:
                yield actual.get_tarjeta()
                actual = actual.get_siguiente()

    def __iter__(self):
        return iter(self.loop())

    # Método para saber si la lista está vacía
    def esta_vacia(self):
        if self.tamanio == 0:
            return True
        else:
            return False

    # Método para agregar una tarjeta a la lista
    def agregar_tarjeta(self, tarjeta):
        self.id = self.id + 1
        tarjeta.set_id(self.id)
        nuevo = Nodo(tarjeta)
        if self.cabeza == None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.get_siguiente() != None:
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo)
            nuevo.set_anterior(actual)
        self.tamanio = self.tamanio + 1

    # Método para leer el XML de tarjetas y guardar los datos en la lista
    def cargar_tarjetas(self):
        try:
            ruta = "tarjetas\\tarjetas.xml"
            xml = MD.parse(ruta)
            lista_tarjetas = xml.getElementsByTagName("tarjeta")
            for tarjeta in lista_tarjetas:
                tipo = tarjeta.getElementsByTagName("tipo")[0].firstChild.data
                numero = int(tarjeta.getElementsByTagName("numero")[0].firstChild.data)
                titular = tarjeta.getElementsByTagName("titular")[0].firstChild.data
                fecha_exp = tarjeta.getElementsByTagName("fecha_expiracion")[0].firstChild.data
                if not self.verificar_duplicado(numero):
                    tarjeta_leida = Tarjeta(tipo, numero, titular, fecha_exp)
                    self.agregar_tarjeta(tarjeta_leida)
            print("*** Tarjetas cargadas con éxito")
        except:
            print("[ERROR-CT]: Archivo no encontrado")

    # Método para modificar los datos de una tarjeta de la lista
    def modificar_tarjeta(self, id, tarjeta):
        tarjeta_modificada = False
        if self.cabeza != None:
            actual = self.cabeza
            while actual != None:
                if actual.get_id() == id:
                    if not self.verificar_duplicado_modificacion(id, tarjeta.get_numero()):
                        actual.set_tarjeta(tarjeta)
                        actual.set_id(id)
                        tarjeta_modificada = True
                    else:
                        print("[ERROR-MT]: Ya existe una tarjeta con el número ingresados")
                    break
                actual = actual.get_siguiente()
            if not tarjeta_modificada:
                print("[ERROR-MT]: La tarjeta con ID ingresado no existe")
        else:
            print("[ERROR-MT]: La lista está vacía")

    # Método para eliminar una tarjeta de la lista
    def eliminar_tarjeta(self, id):
        tarjeta_eliminada = False
        if self.cabeza != None:
            anterior = None
            actual = self.cabeza
            while actual != None:
                if actual.get_id() == id:
                    if anterior == None or self.tamanio == 1:
                        self.cabeza = actual.get_siguiente()
                        self.cabeza.set_anterior(None)
                        self.tamanio = self.tamanio - 1
                        tarjeta_eliminada = True
                        break
                    elif actual.get_siguiente() == None:
                        anterior.set_siguiente(None)
                        self.tamanio = self.tamanio - 1
                        tarjeta_eliminada = True
                        break
                    else:
                        anterior.set_siguiente(actual.get_siguiente())
                        posterior = actual.get_siguiente()
                        posterior.set_anterior(anterior)
                        self.tamanio = self.tamanio - 1
                        tarjeta_eliminada = True
                        break
                anterior = actual
                actual = actual.get_siguiente()
            if not tarjeta_eliminada:
                print("[ERROR-ET]: La tarjeta con ID ingresado no existe")
        else:
            print("[ERROR-ET]: La lista está vacía")

    # Método para escribir un nuevo XML de tarjetas con los cambios realizados
    def guardar_tarjetas(self):
        try:
            tarjetas = ET.Element("tarjetas")
            actual = self.cabeza
            for tarjeta_existente in range(self.tamanio):
                tarjeta = ET.SubElement(tarjetas, "tarjeta")
                ET.SubElement(tarjeta, "tipo").text = actual.get_tipo()
                ET.SubElement(tarjeta, "numero").text = str(actual.get_numero())
                ET.SubElement(tarjeta, "titular").text = actual.get_titular()
                ET.SubElement(tarjeta, "fecha_expiracion").text = actual.get_fecha_exp()
                actual = actual.get_siguiente()
            ET.ElementTree(tarjetas).write("tarjetas\\tarjetas.xml")
            archivo = open("tarjetas\\tarjetas.xml", "r")
            xml = MD.parseString(archivo.read())
            xml_ordenado = xml.toprettyxml()
            archivo.close()
            archivo = open("tarjetas\\tarjetas.xml", "w")
            archivo.write(xml_ordenado)
            archivo.close()
            print("*** Se han guardado los cambios")
        except:
            print("[ERROR-GT]: No se pudo guardar los cambios")

    # Método para devolver una tarjeta de acuerdo al ID
    def devolver_tarjeta(self, id):
        actual = self.cabeza
        while actual != None:
            if actual.get_id() == id:
                return actual.get_tarjeta()
            actual = actual.get_siguiente()
        return None

    # Método para comprobar que no exista tarjeta con números iguales
    def verificar_duplicado(self, numero):
        actual = self.cabeza
        while actual != None:
            if actual.get_numero() == numero:
                return True
            actual = actual.get_siguiente()
        return False

    # Método para comprobar que no exista una tarjeta duplicado (exceptuando la tarjeta a modificar)
    def verificar_duplicado_modificacion(self, id, numero):
        actual = self.cabeza
        while actual != None:
            if actual.get_numero() == numero:
                if id != actual.get_id():
                    return True
            actual = actual.get_siguiente()
        return False

    # Método para comprobar que exista una tarjeta con ID determinado
    def verificar_id(self, id):
        actual = self.cabeza
        while actual != None:
            if actual.get_id() == id:
                return True
            actual = actual.get_siguiente()
        return False

    # Método para imprimir la información de las tarjetas
    def imprimir(self):
        actual = self.cabeza
        while actual != None:
            actual.imprimir()
            actual = actual.get_siguiente()

    # Métodos GET
    def get_cabeza(self):
        return self.cabeza

    def get_tamanio(self):
        return self.tamanio

    # Métodos SET
    def set_cabeza(self, cabeza):
        self.cabeza = cabeza

    def set_tamanio(self, tamanio):
        self.tamanio = tamanio