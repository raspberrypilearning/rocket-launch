# Bibliothekscode importieren
from p5 import *
from random import randint

# Globale Variablen einrichten
bildschirm_groesse = 400
orbit_y = bildschirm_groesse - orbit_radius


# Die Funktion „zeichne_rakete“ kommt hierher
def zeichne_rakete():
    global rakete_y, treibstoff, verbrennen
    rakete_y -= 1
    image(rakete, width/2, rakete_y, 64, 64)
    fill(200, 200, 200, 100) # Transparent grau
    no_stroke()
    for i in range(25):
        fill(255, 255 - i * 10, 0)
        ellipse(
            ellipse(width/2 + randint(-5, 5), rakete_y +
            randint(20, 50), randint(5, 10), randint(5, 10))
            circle_size,
            circle_size,
        )


# Die Funktion „zeichne_hintergrund“ kommt hierher
def zeichne_hintergrund():
    background(0)
    image(planet, width/2, height, 300, 300)


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


run()
