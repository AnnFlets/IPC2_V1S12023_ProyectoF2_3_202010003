# Librería utilizada para la lectura del archivo XML
import xml.dom.minidom as MD
# Librería utilizada para la escritura del archivo XML
import xml.etree.cElementTree as ET
from peliculas.nodo import Nodo
from peliculas.pelicula import Pelicula

class ListaPeliculas:
    # Método constructor
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
        self.id = 0

    # Métodos para hacer iterable la lista
    def loop(self):
        if self.cabeza != None:
            actual = self.cabeza
            while True:
                yield actual.get_pelicula()
                actual = actual.get_siguiente()
                if actual == self.cabeza:
                    break

    def __iter__(self):
        return iter(self.loop())

    # Método para saber si la lista está vacía
    def esta_vacia(self):
        if self.tamanio == 0:
            return True
        else:
            return False

    # Método para agregar una película a la lista
    def agregar_pelicula(self, pelicula):
        self.id = self.id + 1
        pelicula.set_id(self.id)
        nuevo = Nodo(pelicula)
        if self.cabeza == None:
            nuevo.set_siguiente(nuevo)
            nuevo.set_anterior(nuevo)
            self.cabeza = nuevo
        else:
            ultimo = self.cabeza.get_anterior()
            nuevo.set_siguiente(self.cabeza)
            nuevo.set_anterior(ultimo)
            self.cabeza.set_anterior(nuevo)
            ultimo.set_siguiente(nuevo)
        self.tamanio = self.tamanio + 1

    # Método para leer el XML de películas y guardar los datos en la lista
    def cargar_peliculas(self):
        try:
            ruta = "peliculas\\peliculas.xml"
            xml = MD.parse(ruta)
            lista_categorias = xml.getElementsByTagName("categoria")
            for categoria in lista_categorias:
                nombre_categoria = categoria.getElementsByTagName("nombre")[0].firstChild.data
                lista_peliculas_categoria = categoria.getElementsByTagName("peliculas")
                for peliculas in lista_peliculas_categoria:
                    lista_peliculas = peliculas.getElementsByTagName("pelicula")
                    for pelicula in lista_peliculas:
                        titulo = pelicula.getElementsByTagName("titulo")[0].firstChild.data
                        director = pelicula.getElementsByTagName("director")[0].firstChild.data
                        anio = int(pelicula.getElementsByTagName("anio")[0].firstChild.data)
                        fecha = pelicula.getElementsByTagName("fecha")[0].firstChild.data
                        hora = pelicula.getElementsByTagName("hora")[0].firstChild.data
                        imagen = pelicula.getElementsByTagName("imagen")[0].firstChild.data
                        precio = int(pelicula.getElementsByTagName("precio")[0].firstChild.data)
                        if not self.verificar_duplicado(nombre_categoria, titulo, director, anio, fecha, hora):
                            pelicula_leida = Pelicula(nombre_categoria, titulo, director, anio, fecha, hora, imagen, precio)
                            self.agregar_pelicula(pelicula_leida)
            print("*** Películas cargadas con éxito")
        except:
            print("[ERROR-CP]: Archivo no encontrado")

    # Método para modificar los datos de una película
    def modificar_pelicula(self, id, pelicula):
        pelicula_modificada = False
        if self.cabeza != None:
            actual = self.cabeza
            while True:
                if actual.get_id() == id:
                    if not self.verificar_duplicado_modificacion(id, pelicula.get_categoria(), pelicula.get_titulo(), pelicula.get_director(),
                                                    int(pelicula.get_anio()), pelicula.get_fecha(), pelicula.get_hora()):
                        actual.set_pelicula(pelicula)
                        actual.set_id(id)
                        pelicula_modificada = True
                    else:
                        print("[ERROR-MP]: Ya existe una película con la información ingresada")
                    break
                actual = actual.get_siguiente()
                if actual == self.cabeza:
                    break
            if not pelicula_modificada:
                print("[ERROR-MP]: La película con el ID ingresado no existe")
        else:
            print("[ERROR-MP]: La lista está vacía")

    # Método para eliminar una película de la lista
    def eliminar_pelicula(self, id):
        pelicula_eliminada = False
        if self.cabeza != None:
            anterior = self.cabeza.get_anterior()
            actual = self.cabeza
            while actual != None:
                if actual.get_id() == id:
                    if self.tamanio == 1:
                        self.cabeza = None
                        self.tamanio = self.tamanio - 1
                        pelicula_eliminada = True
                        break
                    else:
                        if actual == self.cabeza:
                            self.cabeza = actual.get_siguiente()
                        anterior.set_siguiente(actual.get_siguiente())
                        posterior = actual.get_siguiente()
                        posterior.set_anterior(anterior)
                        self.tamanio = self.tamanio - 1
                        pelicula_eliminada = True
                        break
                anterior = actual
                actual = actual.get_siguiente()
                if actual == self.cabeza:
                    break
            if not pelicula_eliminada:
                print("[ERROR-EP]: La película con ID ingresado no existe")
        else:
            print("[ERROR-EP]: La lista está vacía")

    # Método para escribir un nuevo XML de películas con los cambios realizados
    def guardar_peliculas(self):
        try:
            categorias = ET.Element("categorias")
            for categoria_existente in self.devolver_categorias():
                categoria = ET.SubElement(categorias, "categoria")
                ET.SubElement(categoria, "nombre").text = categoria_existente
                peliculas = ET.SubElement(categoria, "peliculas")
                actual = self.cabeza
                for pelicula_existente in range(self.tamanio):
                    if actual.get_categoria() == categoria_existente:
                        pelicula = ET.SubElement(peliculas, "pelicula")
                        ET.SubElement(pelicula, "titulo").text = actual.get_titulo()
                        ET.SubElement(pelicula, "director").text = actual.get_director()
                        ET.SubElement(pelicula, "anio").text = str(actual.get_anio())
                        ET.SubElement(pelicula, "fecha").text = actual.get_fecha()
                        ET.SubElement(pelicula, "hora").text = actual.get_hora()
                        ET.SubElement(pelicula, "imagen").text = actual.get_imagen()
                        ET.SubElement(pelicula, "precio").text = str(actual.get_precio())
                    actual = actual.get_siguiente()
            ET.ElementTree(categorias).write("peliculas\\peliculas.xml")
            archivo = open("peliculas\\peliculas.xml", "r")
            xml = MD.parseString(archivo.read())
            xml_ordenado = xml.toprettyxml()
            archivo.close()
            archivo = open("peliculas\\peliculas.xml", "w")
            archivo.write(xml_ordenado)
            archivo.close()
            print("*** Se han guardado los cambios")
        except:
            print("[ERROR-GP]: No se pudo guardar los cambios")

    # Método para devolver una lista con las categorias existentes
    def devolver_categorias(self):
        categorias = []
        actual = self.cabeza
        while actual != None:
            categoria = actual.get_categoria()
            if not (categoria in categorias):
                categorias.append(categoria)
            actual = actual.get_siguiente()
            if actual == self.cabeza:
                break
        return categorias

    # Método para devolver una película de acuerdo al ID
    def devolver_pelicula(self, id):
        actual = self.cabeza
        while actual != None:
            if (actual.get_id() == id):
                return actual.get_pelicula()
            actual = actual.get_siguiente()
            if actual == self.cabeza:
                break
        return None

    # Método para comprobar que no existan películas con datos iguales
    def verificar_duplicado(self, categoria, titulo, director, anio, fecha, hora):
        actual = self.cabeza
        while actual != None:
            if (actual.get_categoria() == categoria and actual.get_titulo() == titulo and actual.get_director() == director and int(actual.get_anio()) == anio and actual.get_fecha() == fecha and actual.get_hora() == hora):
                return True
            actual = actual.get_siguiente()
            if actual == self.cabeza:
                break
        return False

    # Método para comprobar que no exista una película duplicada (exceptuando la película a modificar)
    def verificar_duplicado_modificacion(self, id, categoria, titulo, director, anio, fecha, hora):
        actual = self.cabeza
        while actual != None:
            if (actual.get_categoria() == categoria and actual.get_titulo() == titulo and actual.get_director() == director and int(actual.get_anio()) == anio and actual.get_fecha() == fecha and actual.get_hora() == hora):
                if id != actual.get_id():
                    return True
            actual = actual.get_siguiente()
            if actual == self.cabeza:
                break
        return False

    # Método para comprobar que exista una película con ID determinado
    def verificar_id(self, id):
        actual = self.cabeza
        while actual != None:
            if actual.get_id() == id:
                return True
            actual = actual.get_siguiente()
            if actual == self.cabeza:
                return False
        return False

    # Método para imprimir la información de las películas
    def imprimir(self):
        if self.cabeza != None:
            actual = self.cabeza
            while True:
                actual.imprimir()
                actual = actual.get_siguiente()
                if actual == self.cabeza:
                    break

    # Método para imprimir el ID y titulo de las películas
    def imprimir_id_titulo(self):
        if self.cabeza != None:
            actual = self.cabeza
            while True:
                print(actual.get_id(), "-", actual.get_titulo())
                actual = actual.get_siguiente()
                if actual == self.cabeza:
                    break

    # Método para imprimir la información de las películas de acuerdo a la categoría:
    def imprimir_segun_categoria(self, categoria):
        pelicula_encontrada = 0
        if self.cabeza != None:
            actual = self.cabeza
            while True:
                if categoria == actual.get_categoria():
                    actual.imprimir()
                    pelicula_encontrada = pelicula_encontrada + 1
                actual = actual.get_siguiente()
                if actual == self.cabeza:
                    if pelicula_encontrada == 0:
                        print("[ERROR-VP]: No hay películas disponibles para la categoría ingresada")
                    break

    # Método para imprimir la información de las películas de acuerdo al ID:
    def imprimir_segun_id(self, id):
        pelicula_encontrada = 0
        if self.cabeza != None:
            actual = self.cabeza
            while True:
                if id == actual.get_id():
                    actual.imprimir()
                    pelicula_encontrada = pelicula_encontrada + 1
                actual = actual.get_siguiente()
                if actual == self.cabeza:
                    if pelicula_encontrada == 0:
                        print("[ERROR-VP]: No hay películas con el ID ingresado")
                    break

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