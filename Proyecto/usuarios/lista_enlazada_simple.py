# Librería utilizada para la lectura del archivo XML
import xml.dom.minidom as MD
# Librería utilizada para la escritura del archivo XML
import xml.etree.cElementTree as ET
from usuarios.nodo import Nodo
from usuarios.usuario import Usuario

class ListaUsuarios:
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
                yield actual.get_usuario()
                actual = actual.get_siguiente()

    def __iter__(self):
        return iter(self.loop())

    # Método para saber si la lista está vacía
    def esta_vacia(self):
        if self.tamanio == 0:
            return True
        else:
            return False

    # Método para agregar un usuario a la lista
    def agregar_usuario(self, usuario):
        self.id = self.id + 1
        usuario.set_id(self.id)
        nuevo = Nodo(usuario)
        if self.cabeza == None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.get_siguiente() != None:
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo)
        self.tamanio = self.tamanio + 1

    # Método para leer el XML de usuarios y guardar los datos en la lista
    def cargar_usuarios(self):
        try:
            ruta = "usuarios\\usuarios.xml"
            xml = MD.parse(ruta)
            lista_usuarios = xml.getElementsByTagName("usuario")
            for usuario in lista_usuarios:
                nombre = usuario.getElementsByTagName("nombre")[0].firstChild.data
                apellido = usuario.getElementsByTagName("apellido")[0].firstChild.data
                telefono = int(usuario.getElementsByTagName("telefono")[0].firstChild.data)
                correo = usuario.getElementsByTagName("correo")[0].firstChild.data
                contrasena = usuario.getElementsByTagName("contrasena")[0].firstChild.data
                rol = usuario.getElementsByTagName("rol")[0].firstChild.data
                if not self.verificar_duplicado(telefono, correo):
                    usuario_leido = Usuario(nombre, apellido, telefono, correo, contrasena, rol)
                    self.agregar_usuario(usuario_leido)
            print("*** Usuarios cargados con éxito")
        except:
            print("[ERROR-CU]: Archivo no encontrado")

    # Método para modificar los datos de un usuario de la lista
    def modificar_usuario(self, id, usuario):
        if self.cabeza != None:
            actual = self.cabeza
            while actual != None:
                if actual.get_id() == id:
                    if not self.verificar_duplicado_modificacion(id, usuario.get_telefono(), usuario.get_correo()):
                        actual.set_usuario(usuario)
                        actual.set_id(id)
                    else:
                        print("[ERROR-MU]: Ya existe un usuario con el teléfono o correo ingresados")
                    break
                actual = actual.get_siguiente()
        else:
            print("[ERROR-MU]: La lista está vacía")

    # Método para eliminar un usuario de la lista
    def eliminar_usuario(self, id):
        usuario_eliminado = False
        if self.cabeza != None:
            anterior = None
            actual = self.cabeza
            while actual != None:
                if actual.get_id() == id:
                    if anterior == None or self.tamanio == 1:
                        self.cabeza = actual.get_siguiente()
                        self.tamanio = self.tamanio - 1
                        usuario_eliminado = True
                        break
                    else:
                        anterior.set_siguiente(actual.get_siguiente())
                        self.tamanio = self.tamanio - 1
                        usuario_eliminado = True
                        break
                anterior = actual
                actual = actual.get_siguiente()
            if not usuario_eliminado:
                print("[ERROR-EU]: El usuario con ID ingresado no existe")
        else:
            print("[ERROR-EU]: La lista está vacía")

    # Método para escribir un nuevo XML de usuarios con los cambios realizados
    def guardar_usuarios(self):
        try:
            actual = self.cabeza
            usuarios = ET.Element("usuarios")
            for i in range(self.tamanio):
                usuario = ET.SubElement(usuarios, "usuario")
                ET.SubElement(usuario, "rol").text = actual.get_rol()
                ET.SubElement(usuario, "nombre").text = actual.get_nombre()
                ET.SubElement(usuario, "apellido").text = actual.get_apellido()
                ET.SubElement(usuario, "telefono").text = str(actual.get_telefono())
                ET.SubElement(usuario, "correo").text = actual.get_correo()
                ET.SubElement(usuario, "contrasena").text = actual.get_contrasena()
                actual = actual.get_siguiente()
            ET.ElementTree(usuarios).write("usuarios\\usuarios.xml")
            archivo = open("usuarios\\usuarios.xml", "r")
            xml = MD.parseString(archivo.read())
            xml_ordenado = xml.toprettyxml()
            archivo.close()
            archivo = open("usuarios\\usuarios.xml", "w")
            archivo.write(xml_ordenado)
            archivo.close()
            print("*** Se han guardado los cambios")
        except:
            print("[ERROR-GU]: No se pudo guardar los cambios")

    # Método para comprobar que no exista un usuario con teléfono o correo iguales
    def verificar_duplicado(self, telefono, correo):
        actual = self.cabeza
        while actual != None:
            if (actual.get_telefono() == telefono) and (actual.get_correo() == correo):
                return True
            actual = actual.get_siguiente()
        return False

    # Método para comprobar que no exista un usuario duplicado (exceptuando el usuario a modificar)
    def verificar_duplicado_modificacion(self, id, telefono, correo):
        actual = self.cabeza
        while actual != None:
            if (actual.get_telefono() == telefono) and (actual.get_correo() == correo):
                if id != actual.get_id():
                    return True
            actual = actual.get_siguiente()
        return False

    # Método para comprobar que exista un usuario con ID determinado
    def verificar_id(self, id):
        actual = self.cabeza
        while actual != None:
            if actual.get_id() == id:
                return True
            actual = actual.get_siguiente()
        return False

    # Método para encontrar y devolver un usuario
    def iniciar_sesion_usuario(self, correo, contrasena):
        actual = self.cabeza
        while actual != None:
            usuario = actual.get_usuario()
            if (usuario.get_correo() == correo) and (usuario.get_contrasena() == contrasena):
                return usuario
            actual = actual.get_siguiente()
        return None

    def devolver_usuario(self, id):
        actual = self.cabeza
        while actual != None:
            usuario = actual.get_usuario()
            if usuario.get_id() == id:
                return usuario
            actual = actual.get_siguiente()
        return None

    # Método para imprimir la información de los usuarios
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