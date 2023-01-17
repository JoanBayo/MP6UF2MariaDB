import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

import mariadb

# ESTA JA NO ÉS FA SERVIR JA QUE ARA ES TROBAR DINS DEL PROGRAMA GENERAL
class jugadors:
    idJugador = 0
    nombre = ""
    posicion = ""
    nacimiento = "1990-01-01"
    numero = 0
    altura = 0
    valorMercado = 0
    idEquipo = 0

    def __init__(self):
        pass


def descarregaWeb():
    url = 'https://www.transfermarkt.es/cd-teruel/kader/verein/19301/saison_id/2022/plus/1'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}

    req = urllib.request.Request(url, None, headers)
    with urllib.request.urlopen(req) as response:
        resposta = response.read().decode("utf-8")

    fitxer = open("jugadors.html", "wt", encoding="utf-8")
    fitxer.write(resposta)
    fitxer.close()


def carregarXML():
    tree = ET.parse("taula.xml")
    root = tree.getroot()
    llistajugadors = []
    # Numeros:
    for tr in root.iter('tbody'):
        for td in tr.iter('td'):
            for div in td.iter('div'):
                j1 = jugadors()
                j1.numero = div.text
                llistajugadors.append(j1)
    # Noms:
    comptador = 0
    for tbody in root.iter('tbody'):
        for a in tbody.iter('a'):
            if a.text is not None:
                llistajugadors[comptador].nombre = a.text
                llistajugadors[comptador].nombre = llistajugadors[comptador].nombre.strip()
                comptador += 1

    # Posició:
    comptador = 0
    for tbody in root.iter('tbody'):
        for table in tbody.iter('table'):
            for td in table.iter('td'):
                if td.text is not None:
                    valor = td.text
                    valor = valor.strip()
                    if len(valor) > 0:
                        llistajugadors[comptador].posicion = td.text
                        llistajugadors[comptador].posicion = llistajugadors[comptador].posicion.strip()
                        comptador += 1
                    else:
                        llistajugadors[comptador].posicion = "indeterminado"
    #nacimento
    cont = 0
    comptador = 0
    for tbody in root.iter('tbody'):
       for td in tbody.iter('td'):
            c = td.get('class')
            if c == 'zentriert':
                if cont%7 == 0:
                    if td.text is not None:
                        valor = td.text
                        valor = valor.strip()
                        if len(valor) > 0:
                            dia = td.text[0:2]
                            mes = td.text[3:5]
                            any = td.text[6:10]
                            naixement = any+"-"+mes+"-"+dia
                            llistajugadors[comptador].nacimiento = naixement
                            comptador += 1
                cont += 1


    #altura
    cont = 0
    comptador = 0
    for tbody in root.iter('tbody'):
        for td in tbody.iter('td'):
            c = td.get('class')
            if c == 'zentriert':
                if cont % 7 == 2:
                    if td.text is not None:
                        valor = td.text
                        valor = valor.strip()
                        if len(valor) > 0:
                            td.text = td.text.replace(',','')
                            td.text = td.text.replace('m','')
                            llistajugadors[comptador].altura = td.text
                            llistajugadors[comptador].altura = llistajugadors[comptador].altura
                            comptador += 1
                cont += 1

    #valorMercado
    comptador = 0
    for tbody in root.iter('tbody'):
        for td in tbody.iter('td'):
            c = td.get('class')
            if c == 'rechts hauptlink':
                if td.text is not None:
                    valor = td.text
                    valor = valor.strip()
                    if len(valor) > 0:
                        td.text = td.text.replace('€','')
                        td.text = td.text.replace('mil','')
                        td.text = int(td.text)
                        llistajugadors[comptador].valorMercado = td.text
                        llistajugadors[comptador].valorMercado = llistajugadors[comptador].valorMercado
                        comptador += 1


    for j in llistajugadors:
        j.idEquipo = 1
        print(j.posicion)
        print(j.numero + ". " + j.nombre)
        print(j.nacimiento)
        print("Alçada en cm: " + str(j.altura))
        print("Valor de mercat: " + str(j.valorMercado) + "mil €")
        print("ID del equip: " + str(j.idEquipo))
        print()

        # try:
        #     conn = mariadb.connect(
        #         user="pythonMaster",
        #         password="Admin1234",
        #         host="localhost",
        #         port=3306,
        #         database="proves"
        #     )
        # except mariadb.Error as e:
        #     print(f"Error conectando a la base de datos: {e}")
        #     sys.exit(1)
        #
        # sentenciaSQL = f"""UPDATE jugadores SET nombre = '{j.nombre}', posicion = '{j.posicion}', nacimiento = '{j.nacimiento}', numero = {j.numero}, altura = {j.altura}, valorMercado = {j.valorMercado}, equipos_id = {idEquipo} WHERE idjugador = {idJugador}
        # """
        # cur = conn.cursor()
        # cur.execute(sentenciaSQL)
        # conn.commit()
        # conn.close()


# descarregaWeb()
# llegirFitxer()
carregarXML()

