# Importer le code de la bibliothèque
from p5 import *
from random import randint

# Set up global variables
taille_ecran = 400
rocket_position = screen_size


# La fonction dessine_fusee vient ici
def dessine_fusee():
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


# La fonction dessine_arriere_plan vient ici
def dessine_arriere_plan():
    background(0, 0, 0)
    image(planet, screen_size / 2, screen_size, 300, 300)


def setup():
    # Set up your animation here
    size(taille_ecran, taille_ecran)
    image_mode(CENTER)
    global planete, fusee
    planet = load_image("purple_planet.png")
    rocket = load_image("rocket.png")


def draw():
    # Choses à faire dans chaque image
    dessine_arriere_plan()
    dessine_fusee()


run()
