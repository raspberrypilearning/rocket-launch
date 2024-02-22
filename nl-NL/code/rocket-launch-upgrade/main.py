#!/bin/python3

# Bibliotheekcode importeren
from p5 import *
from random import randint

# Globale variabelen instellen
scherm_grootte = 400
raket_y = scherm_grootte # begin onderaan
verbruik = 100 # hoeveel brandstof wordt er in elk frame verbruikt
omloopbaan_straal = 250
omloopbaan_y = scherm_grootte - omloopbaan_straal
hoge_omloopbaan_straal = 350
hoge_omloopbaan_y = scherm_grootte - hoge_omloopbaan_straal
snelheid = 1 # Hoe ver de raket elk frame vliegt

# De teken_raket functie komt hier


def teken_raket():
    global raket_y, brandstof, verbruik

    if brandstof >= verbruik and raket_y > hoge_omloopbaan_y: # vliegt nog steeds
        raket_y -= snelheid # Verplaats de raket
        brandstof -= verbruik # brandstof verbruik
        print('Brandstof over: ', brandstof)

        no_stroke() # Zet de lijn uit

        for i in range(25): # teken 25 brandende uitstoot ellipsen
            fill(255, 255 - i*10, 0) # geel
            # i neemt toe elke keer dat de lus wordt herhaald
            ellipse(width/2, raket_y + i, 8, 3)

        fill(200, 200, 200, 100) # Transparant grijs

        for i in range(20): # Teken 20 willekeurige rook ellipsen
            ellipse(width/2 + randint(-5, 5), raket_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    if brandstof < verbruik and raket_y > omloopbaan_y: # Geen brandstof meer en niet in een omloopbaan
        tint(255, 0, 0) # Mislukt
    elif raket_y <= orbit_y and raket_y > high_orbit_y:
        tint(0, 255, 0) # Gelukt
    elif brandstof < 1000 and raket_y <= omloopbaan_y:
        tint(0, 100, 200) # Succes met hoge baan
    elif brandstof >= 1000 and raket_y <= omloopbaan_y:
        tint(255, 200, 0) # Te veel brandstof

    image(raket, width/2, height/2, 64, 64)
    no_tint()


# De functie teken_achtergrond komt hier
def teken_achtergrond():
    achtergrond(0) # afkorting voor achtergrond(0, 0, 0) - zwart
    image(planeet, width/2, height, 300, 300) # teken de afbeelding

    # Teken de onderste baan
    no_fill() # Zet elke vulling uit
    stroke(255) # Stel een witte lijn in
    stroke_weight(2)
    ellipse(width/2, height, omloopbaan_straal*2, omloopbaan_straal*2)

    # Teken de hogere baan
    stroke(0, 100, 200) # Stel een blauwachtige streek in
    stroke_weight(2)
    ellipse(width/2, height, omloopbaan_straal*2, omloopbaan_straal*2)


def setup():
    # Stel hier je animatie in
    size(scherm_grootte, scherm_grootte)
    image_mode(CENTER)
    global planeet, raket
    planeet = load_image('planet.png') # jouw gekozen planeet
    raket = load_image('rocket.png')


def draw():
    # Dingen om te doen in elk frame
    teken_achtergrond()
    teken_raket()


brandstof = int(input('Hoeveel kilogram brandstof wil je gebruiken?'))
verbruik = int(input('Hoeveel brandstof moet de raket per frame verbruiken?'))
snelheid = int(input('Hoe ver moet de raket per frame reizen?'))
run()
