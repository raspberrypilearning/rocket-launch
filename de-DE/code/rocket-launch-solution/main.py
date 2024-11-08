# Bibliothekscode importieren
from p5 import *
from random import randint

# Set up global variables
bildschirm_groesse = 400
rocket_position = screen_size


# Die Funktion „zeichne_rakete“ kommt hierher
def zeichne_rakete():
    global rocket_position
    rocket_position = rocket_position - 1
    image(rocket, width / 2, rocket_position, 64, 64)
    fill(200, 200, 200, 100)
    no_stroke()
    for i in range(20):
        circle_size = randint(5, 10)
        ellipse(
            screen_size / 2 + randint(-5, 5),
            rocket_position + randint(20, 50),
            circle_size,
            circle_size,
        )


# Die Funktion „zeichne_hintergrund“ kommt hierher
def zeichne_hintergrund():
    background(0, 0, 0)
    image(planet, screen_size / 2, screen_size, 300, 300)


def setup():
    # Set up your animation here
    size(bildschirm_groesse, bildschirm_groesse)
    image_mode(CENTER)
    global planet, rakete
    planet = load_image("purple_planet.png")
    rocket = load_image("rocket.png")


def draw():
    # Dinge die in jedem Frame passieren
    zeichne_hintergrund()
    zeichne_rakete()


run()
