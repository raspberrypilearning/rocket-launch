# Importer le code de la bibliothèque
from p5 import *
from random import randint

# Configuration des variables globales
taille_ecran = 400
position_fusee = taille_ecran


# La fonction dessine_fusee vient ici
def dessine_fusee():
    position_fusee globale
    position_fusee = position_fusee - 1
    image(fusee, width / 2, position_fusee, 64, 64)
    fill(200, 200, 200, 100)
    no_stroke()
    for i in range(20):
        taille_cercle = randint(5, 10)
        ellipse(
            taille_ecran / 2 + randint(-5, 5),
            position_fusee + randint(20, 50),
            taille_cercle,
            taille_cercle,
        )


# La fonction dessine_arriere_plan vient ici
def dessine_arriere_plan():
    background(0, 0, 0)
    image(planete, taille_ecran / 2, taille_ecran, 300, 300)


def setup():
    # Configure ton animation ici
    size(taille_ecran, taille_ecran)
    image_mode(CENTER)
    global planete, fusee
    planete = load_image("purple_planet.png")
    fusee = load_image("rocket.png")


def draw():
    # Choses à faire dans chaque image
    dessine_arriere_plan()
    dessine_fusee()


run()
