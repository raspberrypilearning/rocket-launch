#!/bin/python3

# Bibliotheekcode importeren
from p5 import *
from random import randint

# Global variabelen instellen
scherm_grootte = 400
raket_y = 400
verbruik = 100
omloopbaan_straal = 250
omloopbaan_y = scherm_grootte - omloopbaan_straal


# De teken_raket functie komt hier
def teken_raket():
    global raket_y, brandstof, verbruik

    if brandstof >= verbruik and raket_y > omloopbaan_y:
        raket_y = 1
        brandstof -= verbruik
        print('Brandstof over: ', brandstof)

        no_stroke()

        for i in range(25):
            fill(255, 255 - i * 10, 0)
            ellipse(width/2, raket_y + i, 8, 3)

        fill(200, 200, 200, 100) # Transparant grijs
        for i in range(20): # Teken 20 willekeurige rook ellipsen
            ellipse(width/2 + randint(-5, 5), raket_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    if brandstof < verbruik and raket_y > omloopbaan_y:
        tint(255, 0, 0)
    elif brandstof < 1000 en raket_y <= omloopbaan_y:
        tint(0, 255, 0)
    elif brandstof >= 1000 en raket_y <= omloopbaan_y:
        tint(255, 200, 0)

    image(raket, width/2, height/2, 64, 64)
    no_tint()


# De functie teken_achtergrond komt hier
def teken_achtergrond():
    background(0)
    image(planeet, width/2, height, 300, 300)

    no_fill()
    stroke(255)
    stroke_weight(2)
    ellipse(width/2, height, omloopbaan_straal*2, omloopbaan_straal*2)


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


brandstof = int(input('Hoeveel kilogram brandstof wil je gebruiken?'))
run()
