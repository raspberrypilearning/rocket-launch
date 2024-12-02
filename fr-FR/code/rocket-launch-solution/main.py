# Importer le code de la bibliothèque
from p5 import *
from random import randint

# Configuration des variables globales
taille_ecran = 400
orbite_y = taille_ecran - rayon_orbite


# La fonction dessine_fusee vient ici
def dessine_fusee():
    global fusee_y, carburant, brule
    rocket_position = rocket_position - 1
    image(fusee, width/2, fusee_y, 64, 64)
    fill(200, 200, 200, 100) # gris transparent
    no_stroke()
    for i in range(25):
        fill(255, 255 - i * 10, 0)
        ellipse(width/2, fusee_y + i, 8, 3)
            ellipse(width/2 + randint(-5, 5), fusee_y +
            randint(20, 50), randint(5, 10), randint(5, 10))
            circle_size,
            circle_size,
        )


# La fonction dessine_arriere_plan vient ici
def dessine_arriere_plan():
    background(0)
    image(planete, width/2, height, 300, 300)


def setup():
    # Configure ton animation ici
    size(taille_ecran, taille_ecran)
    image_mode(CENTER)
    global planete, fusee
    planete = load_image('planet.png')
    fusee = load_image('rocket.png')


def draw():
    # Choses à faire dans chaque image
    dessine_arriere_plan()
    dessine_fusee()


run()
