# Bibliotheekcode importeren
from p5 import *
from random import randint

# Global variabelen instellen
scherm_grootte = 400
omloopbaan_y = scherm_grootte - omloopbaan_straal


# De teken_raket functie komt hier
def teken_raket():
    global raket_y, brandstof, verbruik
    raket_y -= 1
    image(raket, width/2, height/2, 64, 64)
    fill(200, 200, 200, 100) # Transparant grijs
    no_stroke()
    for i in range(25):
        fill(255, 255 - i * 10, 0)
        ellipse(
            ellipse(width/2 + randint(-5, 5), raket_y +
            randint(20, 50), randint(5, 10), randint(5, 10))
            circle_size,
            circle_size,
        )


# De functie teken_achtergrond komt hier
def teken_achtergrond():
    background(0)
    image(planeet, width/2, height, 300, 300)


def setup():
    # Stel hier je animatie in
    size(scherm_grootte, scherm_grootte)
    image_mode(CENTER)
    global planeet, raket
    planeet = load_image('planet.png')
    raket = load_image('rocket.png')


def draw():
    # Dingen om te doen in elk frame
    teken_achtergrond()
    teken_raket()


run()
