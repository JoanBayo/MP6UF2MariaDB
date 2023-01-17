import sys

import mariadb
from flask import Flask, request
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route("/")
def llistat_equips():
    environment = Environment(loader=FileSystemLoader("Template/"))
    template = environment.get_template("plantillaLlistatEquips.html")
    try:
        conn = mariadb.connect(
            user="pythonMaster",
            password="Admin1234",
            host="localhost",
            port=3306,
            database="proves"
        )
    except mariadb.Error as e:
        print(f"Error conectando a la base de datos: {e}")
        sys.exit(1)

    arrayEquips = []
    sentenciaSQL = f"""SELECT idequipo,nombre FROM equipos order by idequipo;
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    resultados = cur.fetchall()
    conn.close()

    for jugador in resultados:
        arrayEquips.append({"idEqupo": jugador[0], "nombreEquipo": jugador[1]})

    info = {"equips": arrayEquips}
    contingut = template.render(info)
    return f'{contingut}'

@app.route("/home")
def home():
    return "<h1>HOME</h1>"

# @app.route('/equips/<int:equip>')
# def mostrar_equips(equip):
#     enviroment = Environment(loader=FileSystemLoader("Template/"))
#     template = enviroment.get_template("plantillaLlistatEquips.html")
#     info = {"equip": f"{equip}"}
#     contingut = template.render(info)
#     return f'{contingut}'

@app.route('/', methods=['GET', 'POST'])
def capturar_boto():
    if request.method == 'POST':
        enviroment = Environment(loader=FileSystemLoader("Template/"))
        template = enviroment.get_template("plantillaEquip.html")

        try:
            conn = mariadb.connect(
                user="pythonMaster",
                password="Admin1234",
                host="localhost",
                port=3306,
                database="proves"
            )
        except mariadb.Error as e:
            print(f"Error conectando a la base de datos: {e}")
            sys.exit(1)

        arrayJugadors = []
        pepe = {f"{request.form.get('mostrarEquip')}"}
        print(pepe)
        sentenciaSQL = f"""SELECT jugadores.idJugador,jugadores.numero,jugadores.nombre,jugadores.nacimiento,jugadores.altura,jugadores.valorMercado,jugadores.posicion,equipos.nombre,equipos.ciudad, equipos.estadio, equipos.fundacion FROM jugadores INNER JOIN equipos ON 
        jugadores.equipos_id = equipos.idequipo where idequipo = '{request.form.get('mostrarEquip')}';"""

        if sentenciaSQL:
            cur = conn.cursor()
            cur.execute(sentenciaSQL)
            resultados = cur.fetchall()
            conn.close()

            for jugador in resultados:
                arrayJugadors.append(
                    {"jugadoresId": jugador[0], "jugadoresNumero": jugador[1], "jugadoresNombre": jugador[2],
                     "jugadoresNacimiento": jugador[3], "jugadoresAltura": jugador[4],
                     "jugadoresValordeMercado": jugador[5],
                     "jugadoresPoscicion": jugador[6], "equiposNombre": jugador[7], "equiposCiudad": jugador[8],
                     "equiposEstadio": jugador[9], "equiposFundacion": jugador[10]})


            info = {"plantilles": arrayJugadors}
            contingut = template.render(info)
            return f'{contingut}'
        else:
            return "hola"