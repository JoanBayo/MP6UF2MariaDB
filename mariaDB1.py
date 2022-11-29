from equips import treballarEquips
from jugadors import treballarJugadors

while True:
    print("1- Treballar amb Equips")
    print("2- Treballar amb Jugadors")
    print("3- Soritr")
    resposta = int(input("Introdueix una opció: "))

    if resposta == 3:
        print("Andusiauuu!")
        break

    if resposta == 1:
        treballarEquips()
        print("Benvingut al menu de Equips")

    if resposta == 2:
        treballarJugadors()
        print("Benvingut al menu de Jugadors")


