# Bibliotheekcode importeren
from p5 import *
from random import randint

# Global variabelen instellen
scherm_grootte = 400
raket_positie = scherm_grootte


# De teken_raket functie komt hier
def teken_raket():
    global raket_positie
    raket_positie = raket_positie - 1
    image(raket, width / 2, raket_positie, 64, 64)
    fill(200, 200, 200, 100)
    no_stroke()
    for i in range(20):
        cirkel_grootte = randint(5, 10)
        ellipse(
            scherm_grootte / 2 + randint(-5, 5),
            raket_positie + randint(20, 50),
            cirkel_grootte,
            cirkel_grootte,
        )


# De functie teken_achtergrond komt hier
def teken_achtergrond():
    background(0, 0, 0)
    image(planeet, scherm_grootte / 2, scherm_grootte, 300, 300)


def setup():
    # Stel hier je animatie in
    size(scherm_grootte, scherm_grootte)
    image_mode(CENTER)
    global planeet, raket
    planeet = load_image("purple_planet.png")
    raket = load_image("rocket.png")


def draw():
    # Dingen om te doen in elk frame
    teken_achtergrond()
    teken_raket()


run()
