from flask import Flask, render_template, url_for, redirect, request, session

from usuarios.lista_enlazada_simple import ListaUsuarios
from usuarios.usuario import Usuario
from salas.lista_doblemente_enlazada import ListaSalas
from salas.sala import Sala
from peliculas.lista_doblemente_circular import ListaPeliculas
from peliculas.pelicula import Pelicula
from facturas.lista_enlazada_simple import ListaFacturas
from facturas.factura import Factura
from boletos.boleto import Boleto
from tarjetas.lista_doblemente_enlazada import ListaTarjetas
from tarjetas.nodo import Nodo
from tarjetas.tarjeta import Tarjeta

app = Flask(__name__)
# Listas para almacenar y gestionar los datos
# USUARIOS
lista_usuarios = ListaUsuarios()
lista_usuarios.cargar_usuarios()
# PELÍCULAS
lista_peliculas = ListaPeliculas()
lista_peliculas.cargar_peliculas()
# PELÍCULAS DEL CARRUSEL
lista_carrusel = ListaPeliculas()
# Cargar 10 películas
for i in range(10):
    lista_carrusel.agregar_pelicula(lista_peliculas.devolver_pelicula(i + 1))
# SALAS
lista_salas = ListaSalas()
lista_salas.cargar_salas()
# FACTURAS
lista_facturas = ListaFacturas()
# TARJETAS
lista_tarjetas = ListaTarjetas()
lista_tarjetas.cargar_tarjetas()

# Ruta de la página de inicio
@app.route('/')
def inicio():
    return render_template('index.html', lista_carrusel = lista_carrusel)