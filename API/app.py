from flask import Flask, jsonify
from flask import request
import json

app = Flask(__name__)


@app.route('/getUsuarios', methods=['GET'])
def getUsuarios():
    try:
        if request.method == 'GET':
            retorno = {
                "usuario": [
                    {
                        "rol": "administrador",
                        "nombre": "Tang",
                        "apellido": "Mo",
                        "telefono": "77777777",
                        "correo": "motang@gmail.com",
                        "contrasena": "mo123"
                    },
                    {
                        "rol": "administrador",
                        "nombre": "Fu",
                        "apellido": "Wenduo",
                        "telefono": "55555555",
                        "correo": "victor@hotmail.com",
                        "contrasena": "fu123"
                    },
                    {
                        "rol": "cliente",
                        "nombre": "Bai",
                        "apellido": "Ruoyan",
                        "telefono": "33333333",
                        "correo": "bairu@yahoo.com",
                        "contrasena": "bai123"
                    }
                ]
            }
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}


@app.route('/getPeliculas', methods=['GET'])
def getPeliculas():
    try:
        if request.method == 'GET':
            retorno = {
                "categoria": [
                    {
                        "nombre": "Aventura",
                        "peliculas": {
                            "pelicula": [
                                {
                                    "titulo": "The Super Mario Bros. Movie",
                                    "director": "Aaron Horvath, Michael Jelenic",
                                    "anio": "2023",
                                    "fecha": "2023-02-05",
                                    "hora": "19:30",
                                    "imagen": "https://m.media-amazon.com/images/M/MV5BOTJhNzlmNzctNTU5Yy00N2YwLThhMjQtZDM0YjEzN2Y0ZjNhXkEyXkFqcGdeQXVyMTEwMTQ4MzU5._V1_FMjpg_UX1000_.jpg",
                                    "precio": "60"
                                },
                                {
                                    "titulo": "Gato con botas: el ultimo deseo",
                                    "director": "Joel Crawford",
                                    "anio": "2022",
                                    "fecha": "2023-06-07",
                                    "hora": "20:00",
                                    "imagen": "https://ep00.epimg.net/tematicos/imagenes/2022/12/12/elpaismas/1670839160_351503_1670839620_noticia_normal.jpg",
                                    "precio": "54"
                                }
                            ]
                        }
                    },
                    {
                        "nombre": "Animacion",
                        "peliculas": {
                            "pelicula": [
                                {
                                    "titulo": "Valiente",
                                    "director": "Brenda Chapman, Mark Andrews",
                                    "anio": "2012",
                                    "fecha": "2023-05-05",
                                    "hora": "14:30",
                                    "imagen": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/FD087BADB61D3A5B7F0C9AD898F0AD283D8E4D5503D9F423687E064A79F6CB41/scale?width=1200&aspectRatio=1.78&format=jpeg",
                                    "precio": "47"
                                }
                            ]
                        }
                    }
                ]
            }
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}


@app.route('/getSalas', methods=['GET'])
def getSalas():
    try:
        if request.method == 'GET':
            retorno = {
                "cine": [
                    {
                        "nombre": "Cine Suzhou",
                        "salas": {
                            "sala": [
                                {
                                    "numero": "#USACIPC2_202212333_101",
                                    "asientos": "60"
                                },

                                {
                                    "numero": "#USACIPC2_202212333_102",
                                    "asientos": "25"
                                },

                                {
                                    "numero": "#USACIPC2_202212333_103",
                                    "asientos": "40"
                                }
                            ]
                        }
                    }
                ]
            }
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}


@app.route('/getTarjetas', methods=['GET'])
def getTarjetas():
    try:
        if request.method == 'GET':
            retorno = {
                "tarjeta": [
                    {
                        "tipo": "Debito",
                        "numero": "4545859565857102",
                        "titular": "Ruan Nanzhu",
                        "fecha_expiracion": "07/2028"
                    },
                    {
                        "tipo": "Credito",
                        "numero": "1523526589523152",
                        "titular": "Lin Qiushi",
                        "fecha_expiracion": "01/2025"
                    },
                    {
                        "tipo": "Credito",
                        "numero": "6523258541253698",
                        "titular": "Cheng Qianli",
                        "fecha_expiracion": "11/2029"
                    }
                ]
            }
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
