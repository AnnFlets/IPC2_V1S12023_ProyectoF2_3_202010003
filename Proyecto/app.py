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
# Llave secreta para almacenar los datos de la sesión iniciada
app.secret_key = "secret_key"
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
# BOLETOS
boletos = []


def verificar_usuario_activo():
    if 'correo' in session:
        return True
    else:
        return False

# Ruta de la página de inicio
@app.route('/')
def inicio():
    # Verificar si hay una sesión activa
    if 'correo' in session:
        if session['rol'] == 'administrador':
            return redirect(url_for('menu_admin'))
        elif session['rol'] == 'cliente':
            return redirect(url_for('menu_cliente'))
    return render_template('index.html', lista_carrusel = lista_carrusel)

# Ruta para el login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Verificar si hay una sesión activa
    if 'correo' in session:
        if session['rol'] == 'administrador':
            return redirect(url_for('menu_admin'))
        elif session['rol'] == 'cliente':
            return redirect(url_for('menu_cliente'))
    # Verificar si hay un regreso de datos del formulario
    elif request.method == 'POST':
        # Recuperar los datos ingresados en el formulario
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario_logeado = lista_usuarios.iniciar_sesion_usuario(correo, contrasena)
        if usuario_logeado != None:
            # Guardar los datos del usuario logeado
            session['id'] = usuario_logeado.get_id()
            session['nombre'] = usuario_logeado.get_nombre()
            session['apellido'] = usuario_logeado.get_apellido()
            session['correo'] = usuario_logeado.get_correo()
            session['telefono'] = usuario_logeado.get_telefono()
            session['contrasena'] = usuario_logeado.get_contrasena()
            session['rol'] = usuario_logeado.get_rol()
            if usuario_logeado.get_rol() == 'administrador':
                return redirect(url_for('menu_admin'))
            elif usuario_logeado.get_rol() == 'cliente':
                return redirect(url_for('menu_cliente'))
            else:
                return redirect(url_for('inicio'))
    return render_template("/usuarios/login.html")

# Ruta para el registro de usuario
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    # Verificar si hay una sesión activa
    if 'correo' in session:
        if session['rol'] == 'administrador':
            return redirect(url_for('menu_admin'))
        elif session['rol'] == 'cliente':
            return redirect(url_for('menu_cliente'))
    # Verificar si hay un regreso de datos del formulario
    elif request.method == 'POST':
        # Recuperar los datos ingresados en el formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = int(request.form['telefono'])
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        if not lista_usuarios.verificar_duplicado(telefono, correo):
            usuario_creado = Usuario(nombre, apellido, telefono, correo, contrasena, 'cliente')
            lista_usuarios.agregar_usuario(usuario_creado)
            return redirect(url_for('inicio'))
        else:
            return redirect(url_for('registro'))
    return render_template("/usuarios/registro.html")

# Ruta para cerrar sesión y eliminar los datos del usuario guardados
@app.route('/logout')
def logout():
    if verificar_usuario_activo():
        # Borrar la sesión guardada
        session.clear()
    return redirect(url_for('inicio'))

@app.route('/catalogo', methods=['GET', 'POST'])
def ver_peliculas():
    categoria_elegida = 'General'
    if request.method == 'POST':
        categoria_elegida = request.form['categoria']
    return render_template('/peliculas/ver_peliculas.html', lista_peliculas = lista_peliculas, lista_categorias = lista_peliculas.devolver_categorias(), categoria_elegida = categoria_elegida, usuario = verificar_usuario_activo())

# ***------------------ MENÚ CLIENTE ------------------***
@app.route('/cliente')
def menu_cliente():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    return render_template("menu_cliente.html", nombre = session['nombre'], apellido = session['apellido'])

# *------ PELÍCULAS FAVORITAS ------*
@app.route('/catalogo/agregar_favorita/<int:id>')
def agregar_pelicula_favorita(id):
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    usuario = lista_usuarios.devolver_usuario(session['id'])
    pelicula = lista_peliculas.devolver_pelicula(id)
    usuario.agregar_pelicula_favorita(pelicula)
    return redirect(url_for('ver_peliculas'))

@app.route('/cliente/peliculas/favoritas', methods=['GET', 'POST'])
def ver_favoritas():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    usuario = lista_usuarios.devolver_usuario(session['id'])
    categoria_elegida = 'General'
    if request.method == 'POST':
        categoria_elegida = request.form['categoria']
    return render_template('/peliculas/ver_favoritas.html', lista_peliculas = usuario.get_peliculas_fav(), lista_categorias = usuario.devolver_categorias(), categoria_elegida = categoria_elegida)

@app.route('/cliente/peliculas/favoritas/eliminar_favorita/<int:id>')
def eliminar_pelicula_favotira(id):
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    usuario = lista_usuarios.devolver_usuario(session['id'])
    usuario.eliminar_pelicula_favorita(id)
    return redirect(url_for('ver_favoritas'))

# *------ COMPRA DE BOLETOS ------*
@app.route('/cliente/comprar/boleto/pelicula/<int:id>', methods=['GET', 'POST'])
def comprar_boletos(id):
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    sala_elegida = 'nada'
    cant_boletos = 1
    session['CB_id_pelicula'] = id
    if request.method == 'POST':
        sala_elegida = lista_salas.devolver_sala_por_numero(request.form['sala'])
        session['CB_num_sala'] = sala_elegida.get_numero()
        cant_boletos = int(request.form['num_boletos'])
        session['CB_num_boletos'] = cant_boletos
        pelicula = lista_peliculas.devolver_pelicula(session['CB_id_pelicula'])
        session['CB_total'] = int(cant_boletos * pelicula.get_precio())
    return render_template('/comprar/comprar_boletos.html', pelicula = lista_peliculas.devolver_pelicula(id), lista_salas = lista_salas, sala_elegida = sala_elegida, cant_boletos = cant_boletos)

@app.route('/cliente/comprar/boleto/asientos', methods=['GET', 'POST'])
def elegir_asientos():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    sala_elegida = lista_salas.devolver_sala_por_numero(session['CB_num_sala'])
    if request.method == 'POST':
        for i in range(session['CB_num_boletos']):
            boletos.append(int(request.form['boleto' + str(i)]))
        return redirect(url_for('ingresar_datos_facturacion'))
    return render_template('/comprar/elegir_asientos.html', num_asientos = session['CB_num_boletos'], asientos_disponibles = sala_elegida.get_asientos())

@app.route('/cliente/comprar/boleto/facturacion', methods=['GET', 'POST'])
def ingresar_datos_facturacion():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    if request.method == 'POST':
        pago = request.form['pago']
        nombre = request.form['nombre']
        nit = request.form['nit']
        direccion = request.form['direccion']
        if pago == "0":
            pago = "Efectivo"
        else:
            tarjeta = lista_tarjetas.devolver_tarjeta(int(pago))
            pago = str(tarjeta.get_numero())
        if nombre == "":
            nombre = "-"
        if nit == "":
            nit = "CF"
        if direccion == "":
            direccion = "-"
        factura = Factura(session['correo'], session['telefono'], nombre, nit, direccion, pago)
        lista_facturas.agregar_factura(factura)
        pelicula = lista_peliculas.devolver_pelicula(session['CB_id_pelicula'])
        sala = lista_salas.devolver_sala_por_numero(session['CB_num_sala'])
        asientos_sala = sala.get_asientos()
        for boleto_elegido in boletos:
            boleto = Boleto(pelicula.get_titulo(), pelicula.get_fecha(), pelicula.get_hora(), sala.get_cine(), sala.get_numero(), boleto_elegido, pelicula.get_precio())
            lista_facturas.agregar_boleto(factura, boleto)
            asientos_sala.remove(boleto_elegido)
        sala.set_asientos_disponibles(len(asientos_sala))
        factura.set_total(session['CB_total'])
        return redirect(url_for('menu_cliente'))
    return render_template('/comprar/facturacion.html', lista_tarjetas = lista_tarjetas, total = session['CB_total'])

@app.route('/cliente/historial')
def ver_historial():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    return render_template('/boletos/historial.html', lista_facturas = lista_facturas, correo = session['correo'], telefono = session['telefono'])

# ***------------------ MENÚ ADMINISTRADOR ------------------***
@app.route('/admin')
def menu_admin():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    return render_template("menu_admin.html", nombre = session['nombre'], apellido = session['apellido'])

# *------ GESTIÓN DE USUARIOS ------*
@app.route('/admin/menu_usuarios')
def menu_usuarios():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    return render_template("/usuarios/menu_usuarios.html", lista_usuarios = lista_usuarios)

@app.route('/admin/menu_usuarios/usuario/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = int(request.form['telefono'])
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        rol = request.form['rol']
        if not lista_usuarios.verificar_duplicado(telefono, correo):
            usuario_creado = Usuario(nombre, apellido, telefono, correo, contrasena, "cliente")
            lista_usuarios.agregar_usuario(usuario_creado)
        return redirect(url_for('menu_usuarios'))
    return render_template("/usuarios/agregar_usuario.html")

@app.route('/admin/menu_usuarios/usuario/cargar')
def cargar_usuarios():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_usuarios.cargar_usuarios()
    return redirect(url_for('menu_usuarios'))

@app.route('/admin/menu_usuarios/usuario/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = int(request.form['telefono'])
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        rol = request.form['rol']
        if not lista_usuarios.verificar_duplicado_modificacion(id, telefono, correo):
            usuario_modificado = Usuario(nombre, apellido, telefono, correo, contrasena, rol)
            lista_usuarios.modificar_usuario(id, usuario_modificado)
        return redirect(url_for('menu_usuarios'))
    return render_template("/usuarios/editar_usuario.html", usuario = lista_usuarios.devolver_usuario(id))

@app.route('/admin/menu_usuarios/usuario/eliminar/<int:id>')
def eliminar_usuario(id):
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_usuarios.eliminar_usuario(id)
    return redirect(url_for('menu_usuarios'))

@app.route('/admin/menu_usuarios/usuario/guardar')
def guardar_usuarios():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_usuarios.guardar_usuarios()
    return redirect(url_for('menu_usuarios'))

# *------ GESTIÓN DE PELÍCULAS ------*
@app.route('/admin/menu_peliculas')
def menu_peliculas():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    return render_template("/peliculas/menu_peliculas.html", lista_peliculas = lista_peliculas)

@app.route('/admin/menu_peliculas/pelicula/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    if request.method == 'POST':
        titulo = request.form['titulo']
        director = request.form['director']
        anio = int(request.form['anio'])
        categoria = request.form['categoria']
        fecha = str(request.form['fecha'])
        hora = str(request.form['hora'])
        imagen = request.form['imagen']
        precio = int(request.form['precio'])
        if not lista_peliculas.verificar_duplicado(categoria, titulo, director, anio, fecha, hora):
            pelicula_creada = Pelicula(categoria, titulo, director, anio, fecha, hora, imagen, precio)
            lista_peliculas.agregar_pelicula(pelicula_creada)
        return redirect(url_for('menu_peliculas'))
    return render_template("/peliculas/agregar_pelicula.html")

@app.route('/admin/menu_peliculas/pelicula/cargar')
def cargar_peliculas():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_peliculas.cargar_peliculas()
    return redirect(url_for('menu_peliculas'))

@app.route('/admin/menu_peliculas/pelicula/editar/<int:id>', methods=['GET', 'POST'])
def editar_pelicula(id):
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    if request.method == 'POST':
        titulo = request.form['titulo']
        director = request.form['director']
        anio = int(request.form['anio'])
        categoria = request.form['categoria']
        fecha = str(request.form['fecha'])
        hora = str(request.form['hora'])
        imagen = request.form['imagen']
        precio = int(request.form['precio'])
        if not lista_peliculas.verificar_duplicado_modificacion(id, categoria, titulo, director, anio, fecha, hora):
            pelicula_modificada = Pelicula(categoria, titulo, director, anio, fecha, hora, imagen, precio)
            lista_peliculas.modificar_pelicula(id, pelicula_modificada)
        return redirect(url_for('menu_peliculas'))
    return render_template("/peliculas/editar_pelicula.html", pelicula = lista_peliculas.devolver_pelicula(id))

@app.route('/admin/menu_peliculas/pelicula/eliminar/<int:id>')
def eliminar_pelicula(id):
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_peliculas.eliminar_pelicula(id)
    return redirect(url_for('menu_peliculas'))

@app.route('/admin/menu_peliculas/pelicula/guardar')
def guardar_peliculas():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_peliculas.guardar_peliculas()
    return redirect(url_for('menu_peliculas'))

# *------ GESTIÓN DE SALAS ------*
@app.route('/admin/menu_salas')
def menu_salas():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    return render_template("/salas/menu_salas.html", lista_salas = lista_salas)

@app.route('/admin/menu_salas/sala/agregar', methods=['GET', 'POST'])
def agregar_sala():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    if request.method == 'POST':
        numero = request.form['numero']
        cine = request.form['cine']
        asientos = int(request.form['asientos'])
        if not lista_salas.verificar_duplicado(numero):
            sala_creada = Sala(cine, numero, asientos)
            lista_salas.agregar_sala(sala_creada)
        return redirect(url_for('menu_salas'))
    return render_template("/salas/agregar_sala.html")

@app.route('/admin/menu_salas/sala/cargar')
def cargar_salas():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_salas.cargar_salas()
    return redirect(url_for('menu_salas'))

@app.route('/admin/menu_salas/sala/editar/<int:id>', methods=['GET', 'POST'])
def editar_sala(id):
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    if request.method == 'POST':
        numero = request.form['numero']
        cine = request.form['cine']
        asientos = int(request.form['asientos'])
        if not lista_salas.verificar_duplicado_modificacion(id, numero):
            sala_modificada = Sala(cine, numero, asientos)
            lista_salas.modificar_sala(id, sala_modificada)
        return redirect(url_for('menu_salas'))
    return render_template("/salas/editar_sala.html", sala = lista_salas.devolver_sala(id))

@app.route('/admin/menu_salas/sala/eliminar/<int:id>')
def eliminar_sala(id):
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_salas.eliminar_sala(id)
    return redirect(url_for('menu_salas'))

@app.route('/admin/menu_salas/sala/guardar')
def guardar_salas():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_salas.guardar_salas()
    return redirect(url_for('menu_salas'))

    # *------ GESTIÓN DE BOLETOS ------*
@app.route('/admin/menu_boletos')
def menu_boletos():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_facturas.imprimir_boletos_estado("activo")
    return render_template("/boletos/menu_boletos.html", lista_facturas = lista_facturas)

@app.route('/admin/menu_boletos/boleto/<int:id>/estado/<estado>')
def cambiar_estado_boleto(id, estado):
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_facturas.verificar_cambio_estado_boleto(id, 'cancelado')
    return redirect(url_for('menu_boletos'))

# *------ GESTIÓN DE TARJETAS ------*
@app.route('/admin/menu_tarjetas')
def menu_tarjetas():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    return render_template("/tarjetas/menu_tarjetas.html", lista_tarjetas = lista_tarjetas)

@app.route('/admin/menu_tarjetas/tarjeta/agregar', methods=['GET', 'POST'])
def agregar_tarjeta():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    if request.method == 'POST':
        numero = int(request.form['numero'])
        titular = request.form['titular']
        fecha_exp = request.form['fecha_exp']
        tipo = request.form['tipo']
        if not lista_tarjetas.verificar_duplicado(numero):
            tarjeta_creada = Tarjeta(tipo, numero, titular, fecha_exp)
            lista_tarjetas.agregar_tarjeta(tarjeta_creada)
        return redirect(url_for('menu_tarjetas'))
    return render_template("/tarjetas/agregar_tarjeta.html")

@app.route('/admin/menu_tarjetas/tarjeta/cargar')
def cargar_tarjetas():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_tarjetas.cargar_tarjetas()
    return redirect(url_for('menu_tarjetas'))

@app.route('/admin/menu_tarjetas/tarjeta/editar/<int:id>', methods=['GET', 'POST'])
def editar_tarjeta(id):
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    if request.method == 'POST':
        numero = int(request.form['numero'])
        titular = request.form['titular']
        fecha_exp = request.form['fecha_exp']
        tipo = request.form['tipo']
        if not lista_tarjetas.verificar_duplicado_modificacion(id, numero):
            tarjeta_modificada = Tarjeta(tipo, numero, titular, fecha_exp)
            lista_tarjetas.modificar_tarjeta(id, tarjeta_modificada)
        return redirect(url_for('menu_tarjetas'))
    return render_template("/tarjetas/editar_tarjeta.html", tarjeta = lista_tarjetas.devolver_tarjeta(id))

@app.route('/admin/menu_tarjetas/tarjeta/eliminar/<int:id>')
def eliminar_tarjeta(id):
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_tarjetas.eliminar_tarjeta(id)
    return redirect(url_for('menu_tarjetas'))

@app.route('/admin/menu_tarjetas/tarjeta/guardar')
def guardar_tarjetas():
    if not verificar_usuario_activo():
        return redirect(url_for('inicio'))
    lista_tarjetas.guardar_tarjetas()
    return redirect(url_for('menu_tarjetas'))