import mariadb
import sys

def mostrarEquip():

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

    idEquip = input("Posa la ID del equip que vols veure: ")

    sentenciaSQL = f"""SELECT * FROM equipos
    WHERE nombre = '{idEquip}';
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    resultado = cur.fetchall()
    conn.close()
    for i in resultado:
        print(i)

def introduirEquip():
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

    nombreEquipo = input("Posa el nom del nou equip: ")
    ciudadEquipo = input("Posa el nom de la ciutat de l'equip: ")
    estadioEquipo = input("Posa el nom del estadi de l'equip: ")
    fundacionEquipo = input("Posa el any que es va fundar l'equip: ")
    sentenciaSQL = f"""INSERT INTO equipos
    (nombre, ciudad, estadio, fundacion)
    VALUES
    ('{nombreEquipo}','{ciudadEquipo}','{estadioEquipo}',{fundacionEquipo});
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    conn.commit()
    conn.close()

def modificarEquip():
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

    idEquipo = input("Posa la ID del equip que vols modificar: ")
    nombreEquipo = input("Posa el nom del nou equip: ")
    ciudadEquipo = input("Posa el nom de la ciutat de l'equip: ")
    estadioEquipo = input("Posa el nom del estadi de l'equip: ")
    fundacionEquipo = input("Posa el any que es va fundar l'equip: ")
    sentenciaSQL = f"""UPDATE equipos SET nombre = '{nombreEquipo}', ciudad = '{ciudadEquipo}', estadio = '{estadioEquipo}', fundacion = {fundacionEquipo}
    WHERE idEquipo = {idEquipo}
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    conn.commit()
    conn.close()

def eliminarEquip():
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

    idEquipo = input("Posa la ID del equip que vols eliminar: ")

    sentenciaSQL = f"""DELETE FROM equipos
        WHERE idEquipo = {idEquipo}
        """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    conn.commit()
    conn.close()


def llistarEquips():

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

    sentenciaSQL = f"""SELECT * FROM equipos;
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    resultado = cur.fetchall()
    conn.close()
    for i in resultado:
        print(i)

def treballarEquips():
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

    sentenciaSQL = """CREATE TABLE IF NOT EXISTS equipos
    ( idEquipo INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(40) NOT NULL,
    ciudad VARCHAR(40) NOT NULL,
    estadio VARCHAR(40) NOT NULL,
    fundacion int NOT NULL,
    PRIMARY KEY (idEquipo),
    CONSTRAINT nombre_equipo UNIQUE (nombre)
    );
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    conn.commit()
    conn.close()

    while True:
        print("1- Mostrar una equip mitjançant el seu ID")
        print("2- Introduir un nou equip ")
        print("3- Modificar un equip ")
        print("4- Eliminar un equip")
        print("5- Llistar tots els equips (ID, NOM)")
        print("6- Sortir")
        resposta = int(input("Introdueix una opció: "))

        if resposta == 6:
            print("Menu Principal:\n")
            break

        if resposta == 1:
            mostrarEquip()

        if resposta == 2:
            introduirEquip()

        if resposta == 3:
            modificarEquip()

        if resposta == 4:
            eliminarEquip()

        if resposta == 5:
            llistarEquips()
