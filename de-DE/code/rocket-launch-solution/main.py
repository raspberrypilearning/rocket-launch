#!/bin/python3

# Bibliothekscode importieren
from p5 import *
from random import randint

# Globale Variablen einrichten
bildschirm_groesse = 400
rakete_y = 400
verbrennen = 100
orbit_radius = 250
orbit_y = bildschirm_groesse - orbit_radius


# Die Funktion „zeichne_rakete“ kommt hierher
def zeichne_rakete():
    global rakete_y, treibstoff, verbrennen

    if treibstoff >= verbrennen and rakete_y > orbit_y:
        rakete_y -= 1
        treibstoff -= verbrennen
        print('Verbleibender Treibstoff: ', treibstoff)

        no_stroke()

        for i in range(25):
            fill(255, 255 - i * 10, 0)
            ellipse(width/2, rakete_y + i, 8, 3)

        fill(200, 200, 200, 100) # Transparent grau
        for i in range(20): # Zeichne 20 zufällige Rauchellipsen
            ellipse(width/2 + randint(-5, 5), rakete_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    if treibstoff < verbrennen and rakete_y > orbit_y:
        tint(255, 0, 0)
    elif treibstoff < 1000 and rakete_y <= orbit_y:
        tint(0, 255, 0)
    elif treibstoff >= 1000 and rakete_y <= orbit_y:
        tint(255, 200, 0)

    image(rakete, width/2, rakete_y, 64, 64)
    no_tint()


# Die Funktion „zeichne_hintergrund“ kommt hierher
def zeichne_hintergrund():
    background(0)
    image(planet, width/2, height, 300, 300)

    no_fill()
    stroke(255)
    stroke_weight(2)
    ellipse(width/2, height, orbit_radius * 2, orbit_radius * 2)


def setup():
    # Richte hier Deine Animation ein
    size(bildschirm_groesse, bildschirm_groesse)
    image_mode(CENTER)
    global planet, rakete
    planet = load_image('planet.png')
    rakete = load_image('rocket.png')


def draw():
    # Dinge die in jedem Frame passieren
    zeichne_hintergrund()
    zeichne_rakete()


treibstoff = int(input('Wie viele Kilogramm Treibstoff willst Du verbrauchen?'))
run()
