from crearWebPlantilla import crearWebPlantilla
from equips import treballarEquips
from importarEquips import importarJugadors
from jugadors import treballarJugadors

while True:
    print("1- Treballar amb Equips")
    print("2- Treballar amb Jugadors")
    print("3- Importar Equips")
    print("4- Crear paguina Web de un equip")
    print("5- Soritr")
    resposta = int(input("Introdueix una opció: "))

    if resposta == 5:
        print("Andusiauuu!")
        break

    if resposta == 4:
        crearWebPlantilla()

    if resposta == 3:
        print("\nBenvingut al menu de Importació de Equips al complet")
        importarJugadors()

    if resposta == 2:
        print("\nBenvingut al menu de Jugadors")
        treballarJugadors()

    if resposta == 1:
        print("\nBenvingut al menu de Equips")

        treballarEquips()



