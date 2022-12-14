import mariadb
import sys


def mostrarJugador():
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

    idJugador = input("Posa la ID del jugador que vols veure: ")

    sentenciaSQL = f"""SELECT * FROM jugadores
    WHERE idjugador = '{idJugador}';
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    resultado = cur.fetchall()
    conn.close()
    for i in resultado:
        print(i)


def introduirJugador():
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

    nombreJugador = input("Posa el nom del nou jugador: ")
    print("Posa la posició del jugador: "
          "\n1- Portero"
          "\n2- Defensa central"
          "\n3- Lateral izquierdo"
          "\n4- Lateral derecho"
          "\n5- Pivote"
          "\n6- Mediocentro"
          "\n7- Extremo izquierdo"
          "\n8- Extremo dercho"
          "\n9- Delantero centro")
    n = input("Escull un numero per triar la posició: ")
    if n == '1':
        pJugador = "portero"
    elif n == '2':
        pJugador = "defensa central"
    elif n == '3':
        pJugador = "lateral izquierdo"
    elif n == '4':
        pJugador = "lateral derecho"
    elif n == '5':
        pJugador = "pivote"
    elif n == '6':
        pJugador = "mediocentro"
    elif n == '7':
        pJugador = "extremo izquierdo"
    elif n == '8':
        pJugador = "extremo derecho"
    elif n == '9':
        pJugador = "delantero centro"

    nacimientoJugador = input("Posa la data de naixement (YYYY-MM-DD): ")
    numeroJugador = input("Posa el número del jugador: ")
    alturaJugador = input("Posa l'altura del jugador en centimetres: ")
    valorMercadoJugador = input("Posa el valor del mercat del jugador: ")
    idEquipo = input("Posa la ID del equip al que juga: ")
    sentenciaSQL = f"""INSERT INTO jugadores
    (nombre, posicion,nacimiento,numero,altura,valorMercado,equipos_id)
    VALUES
    ('{nombreJugador}','{pJugador}','{nacimientoJugador}',{numeroJugador},{alturaJugador},{valorMercadoJugador},{idEquipo});
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    conn.commit()
    conn.close()


def modificarJugador():
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
    idJugador = input("Posa la ID del jugador que vols modificar: ")
    nombreJugador = input("Posa el nom del nou jugador: ")
    print("Posa la posició del jugador: "
          "\n1- Portero"
          "\n2- Defensa central"
          "\n3- Lateral izquierdo"
          "\n4- Lateral derecho"
          "\n5- Pivote"
          "\n6- Mediocentro"
          "\n7- Extremo izquierdo"
          "\n8- Extremo dercho"
          "\n9- Delantero centro")
    n = input("Escull un numero per triar la posició: ")
    if n == '1':
        pJugador = "portero"
    elif n == '2':
        pJugador = "defensa central"
    elif n == '3':
        pJugador = "lateral izquierdo"
    elif n == '4':
        pJugador = "lateral derecho"
    elif n == '5':
        pJugador = "pivote"
    elif n == '6':
        pJugador = "mediocentro"
    elif n == '7':
        pJugador = "extremo izquierdo"
    elif n == '8':
        pJugador = "extremo derecho"
    elif n == '9':
        pJugador = "delantero centro"

    nacimientoJugador = input("Posa la data de naixement (YYYY-MM-DD): ")
    numeroJugador = input("Posa el número del jugador: ")
    alturaJugador = input("Posa l'altura del jugador en centimetres: ")
    valorMercadoJugador = input("Posa el valor del mercat del jugador: ")
    idEquipo = input("Posa la ID del equip al que juga: ")
    sentenciaSQL = f"""UPDATE jugadores SET nombre = '{nombreJugador}', posicion = '{pJugador}', nacimiento = '{nacimientoJugador}', numero = {numeroJugador}, altura = {alturaJugador}, valorMercado = {valorMercadoJugador}, equipos_id = {idEquipo} WHERE idjugador = {idJugador}
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    conn.commit()
    conn.close()


def eliminarJugador():

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
    idJugador = input("Posa la ID del jugador que vols eliminar: ")

    sentenciaSQL = f"""DELETE FROM jugadores WHERE idjugador = {idJugador}
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    conn.commit()
    conn.close()


def llistarJugadors():
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

    sentenciaSQL = f"""SELECT idJugador,nombre,posicion FROM jugadores
    """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    resultado = cur.fetchall()
    conn.close()
    for i in resultado:
        print(i)


def treballarJugadors():
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

    sentenciaSQL = """CREATE TABLE IF NOT EXISTS jugadores ( idJugador INT NOT NULL AUTO_INCREMENT, nombre VARCHAR(
    60) NOT NULL, posicion ENUM('Portero','Defensa central','Lateral izquierdo','Lateral derecho','Pivote',
    'Mediocentro','Extremo izquierdo','Extremo derecho','Delantero centro') NOT NULL, nacimiento DATE NOT NULL, 
    numero int NOT NULL, altura int NOT NULL, valorMercado int NOT NULL, equipos_id int NOT NULL, PRIMARY KEY (
    idJugador), FOREIGN KEY (equipos_id) REFERENCES equipos (idEquipo) ); """
    cur = conn.cursor()
    cur.execute(sentenciaSQL)
    conn.commit()

    while True:
        print("1- Mostrar un jugador mitjançant el seu ID")
        print("2- Introduir un nou jugador ")
        print("3- Modificar un jugador ")
        print("4- Eliminar un jugador")
        print("5- Llistar tots els jugador (ID, NOM, POSCICIO)")
        print("6- Sortir")
        resposta = int(input("Introdueix una opció: "))

        if resposta == 6:
            print("\nMenu Principal: ")
            break

        if resposta == 1:
            mostrarJugador()

        if resposta == 2:
            introduirJugador()

        if resposta == 3:
            modificarJugador()

        if resposta == 4:
            eliminarJugador()

        if resposta == 5:
            llistarJugadors()
