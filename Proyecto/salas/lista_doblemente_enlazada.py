# Librería utilizada para la lectura del archivo XML
import xml.dom.minidom as MD
# Librería utilizada para la escritura del archivo XML
import xml.etree.cElementTree as ET
from salas.nodo import Nodo
from salas.sala import Sala

class ListaSalas:
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
                yield actual.get_sala()
                actual = actual.get_siguiente()

    def __iter__(self):
        return iter(self.loop())

    # Método para saber si la lista está vacía
    def esta_vacia(self):
        if self.tamanio == 0:
            return True
        else:
            return False

    # Método para agregar una sala a la lista
    def agregar_sala(self, sala):
        self.id = self.id + 1
        sala.set_id(self.id)
        nuevo = Nodo(sala)
        if self.cabeza == None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.get_siguiente() != None:
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo)
            nuevo.set_anterior(actual)
        self.tamanio = self.tamanio + 1

    # Método para leer el XML de salas y guardar los datos en la lista
    def cargar_salas(self):
        try:
            ruta = "salas\\salas.xml"
            xml = MD.parse(ruta)
            lista_cines = xml.getElementsByTagName("cine")
            for cine in lista_cines:
                nombre_cine = cine.getElementsByTagName("nombre")[0].firstChild.data
                lista_salas_cine = cine.getElementsByTagName("salas")
                for salas in lista_salas_cine:
                    lista_salas = salas.getElementsByTagName("sala")
                    for sala in lista_salas:
                        numero = sala.getElementsByTagName("numero")[0].firstChild.data
                        asientos = int(sala.getElementsByTagName("asientos")[0].firstChild.data)
                        if not self.verificar_duplicado(numero):
                            sala_leida = Sala(nombre_cine, numero, asientos)
                            self.agregar_sala(sala_leida)
            print("*** Salas cargadas con éxito")
        except:
            print("[ERROR-CS]: Archivo no encontrado")

    # Método para modificar los datos de una sala de la lista
    def modificar_sala(self, id, sala):
        sala_modificada = False
        if self.cabeza != None:
            actual = self.cabeza
            while actual != None:
                if actual.get_id() == id:
                    if not self.verificar_duplicado_modificacion(id, sala.get_numero()):
                        actual.set_sala(sala)
                        actual.set_id(id)
                        sala_modificada = True
                    else:
                        print("[ERROR-MS]: Ya existe una sala con el número ingresados")
                    break
                actual = actual.get_siguiente()
            if not sala_modificada:
                print("[ERROR-MS]: La sala con ID ingresado no existe")
        else:
            print("[ERROR-MS]: La lista está vacía")

    # Método para eliminar una sala de la lista
    def eliminar_sala(self, id):
        sala_eliminada = False
        if self.cabeza != None:
            anterior = None
            actual = self.cabeza
            while actual != None:
                if actual.get_id() == id:
                    if anterior == None or self.tamanio == 1:
                        self.cabeza = actual.get_siguiente()
                        self.cabeza.set_anterior(None)
                        self.tamanio = self.tamanio - 1
                        sala_eliminada = True
                        break
                    elif actual.get_siguiente() == None:
                        anterior.set_siguiente(None)
                        self.tamanio = self.tamanio - 1
                        sala_eliminada = True
                        break
                    else:
                        anterior.set_siguiente(actual.get_siguiente())
                        posterior = actual.get_siguiente()
                        posterior.set_anterior(anterior)
                        self.tamanio = self.tamanio - 1
                        sala_eliminada = True
                        break
                anterior = actual
                actual = actual.get_siguiente()
            if not sala_eliminada:
                print("[ERROR-ES]: La sala con ID ingresado no existe")
        else:
            print("[ERROR-ES]: La lista está vacía")

    # Método para escribir un nuevo XML de salas con los cambios realizados
    def guardar_salas(self):
        try:
            cines = ET.Element("cines")
            for cine_existente in self.devolver_cines():
                cine = ET.SubElement(cines, "cine")
                ET.SubElement(cine, "nombre").text = cine_existente
                salas = ET.SubElement(cine, "salas")
                actual = self.cabeza
                for sala_existente in range(self.tamanio):
                    if actual.get_cine() == cine_existente:
                        sala = ET.SubElement(salas, "sala")
                        ET.SubElement(sala, "numero").text = actual.get_numero()
                        ET.SubElement(sala, "asientos").text = str(actual.get_cantidad_asientos())
                    actual = actual.get_siguiente()
            ET.ElementTree(cines).write("salas\\salas.xml")
            archivo = open("salas\\salas.xml", "r")
            xml = MD.parseString(archivo.read())
            xml_ordenado = xml.toprettyxml()
            archivo.close()
            archivo = open("salas\\salas.xml", "w")
            archivo.write(xml_ordenado)
            archivo.close()
            print("*** Se han guardado los cambios")
        except:
            print("[ERROR-GS]: No se pudo guardar los cambios")

    # Método para devolver una lista con los cines existentes
    def devolver_cines(self):
        cines = []
        actual = self.cabeza
        while actual != None:
            cine = actual.get_cine()
            if not (cine in cines):
                cines.append(cine)
            actual = actual.get_siguiente()
        return cines

    # Método para devolver una sala de acuerdo al ID
    def devolver_sala(self, id):
        actual = self.cabeza
        while actual != None:
            if actual.get_id() == id:
                return actual.get_sala()
            actual = actual.get_siguiente()
        return None

    # Método para devolver una sala de acuerdo al número
    def devolver_sala_por_numero(self, numero):
        actual = self.cabeza
        while actual != None:
            if actual.get_numero() == numero:
                return actual.get_sala()
            actual = actual.get_siguiente()
        return None

    # Método para comprobar que no exista sala con números iguales
    def verificar_duplicado(self, numero):
        actual = self.cabeza
        while actual != None:
            if actual.get_numero() == numero:
                return True
            actual = actual.get_siguiente()
        return False

    # Método para comprobar que no exista una sala duplicado (exceptuando la sala a modificar)
    def verificar_duplicado_modificacion(self, id, numero):
        actual = self.cabeza
        while actual != None:
            if actual.get_numero() == numero:
                if id != actual.get_id():
                    return True
            actual = actual.get_siguiente()
        return False

    # Método para comprobar que exista una sala con ID determinado
    def verificar_id(self, id):
        actual = self.cabeza
        while actual != None:
            if actual.get_id() == id:
                return True
            actual = actual.get_siguiente()
        return False

    # Método para imprimir la información de las salas
    def imprimir(self):
        actual = self.cabeza
        while actual != None:
            actual.imprimir()
            actual = actual.get_siguiente()

    # Método para imprimir la información y estado de las salas
    def imprimir_info_estado(self):
        actual = self.cabeza
        while actual != None:
            actual.imprimir_info_estado()
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