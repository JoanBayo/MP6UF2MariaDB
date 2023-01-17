
import mariadb
import sys
from jinja2 import Environment, FileSystemLoader

def crearWebPlantilla():
    environment = Environment(loader=FileSystemLoader("templatesPlantilla/"))
    template = environment.get_template("plantillaWebPlantilla.html")

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


    idequip = input("Posa la ID del equip que vols crear la seva paguina web: ")

    arrayJugadors = []
    sentenciaSQL = f"""SELECT jugadores.idJugador,jugadores.numero,jugadores.nombre,jugadores.nacimiento,jugadores.altura,jugadores.valorMercado,jugadores.posicion,equipos.nombre,equipos.ciudad, equipos.estadio, equipos.fundacion FROM jugadores INNER JOIN equipos ON jugadores.equipos_id = equipos.idequipo where idequipo = '{idequip}';
    """

    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    resultados = cur.fetchall()
    conn.close()

    for jugador in resultados:
        arrayJugadors.append({"jugadoresId": jugador[0], "jugadoresNumero": jugador[1], "jugadoresNombre": jugador[2], "jugadoresNacimiento": jugador[3], "jugadoresAltura": jugador[4], "jugadoresValordeMercado": jugador[5],
                              "jugadoresPoscicion": jugador[6], "equiposNombre": jugador[7], "equiposCiudad": jugador[8], "equiposEstadio": jugador[9], "equiposFundacion": jugador[10]})

    info = {"plantilles": arrayJugadors}
    contingut = template.render(info)
    file = open("templatesPlantilla/llistatJugadors.html", "w")
    file.write(contingut)