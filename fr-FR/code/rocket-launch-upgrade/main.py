#!/bin/python3

# Importer le code de la bibliothèque
from p5 import *
from random import randint

# Configuration des variables globales
taille_ecran = 400
fusee_y = taille_ecran # commencer en bas
brule = 100 # quelle est la quantité de carburant brûlée dans chaque image
rayon_orbite = 250
orbite_y = taille_ecran - rayon_orbite
rayon_orbite_haut = 350
orbite_haut_y = taille_ecran - rayon_orbite_haut
vitesse = 1 # Jusqu'où la fusée vole à chaque image

# La fonction dessine_fusee vient ici


def dessine_fusee():
    global fusee_y, carburant, brule

    if carburant >= brule and fusee_y > orbite_haut_y: # toujours en vol
        fusee_y -= vitesse # Déplace la fusée
        carburant -= brule # brûler du carburant
        print('Carburant restant : ', carburant)

        no_stroke() # Désactive le trait

        for i in range(25): # dessiner 25 ellipses d'échappement en combustion
            fill(255, 255 - i*10, 0) # jaune
            # i augmente à chaque fois que la boucle se répète
            ellipse(width/2, fusee_y + i, 8, 3)

        fill(200, 200, 200, 100) # gris transparent

        for i in range(20): # dessiner 20 ellipses de fumée aléatoire
            ellipse(width/2 + randint(-5, 5), fusee_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    if carburant < brule and fusee_y > orbite_haut_y: # Plus de carburant et pas en orbite
        tint(255, 0, 0)  # Échec
    elif fusee_y <= orbite_y and fusee_y > orbite_haut_y:
        tint(0, 255, 0)  # Succès
    elif carburant < 1000 and fusee_y <= orbite_haut_y:
        tint(0, 100, 200)  # succès orbite haute
    elif carburant >= 1000 and fusee_y <= orbite_haut_y:
        tint(255, 200, 0) # Trop de carburant

    image(fusee, width/2, fusee_y, 64, 64)
    no_tint()


# La fonction dessine_arriere_plan vient ici
def dessine_arriere_plan():
    background(0) # raccourci pour background(0, 0, 0) - noir
    image(planete, width/2, height, 300, 300) # dessine l'image

    # Dessine l'orbite basse
    no_fill() # Désactive tout remplissage
    stroke(255) # Définir un trait blanc
    stroke_weight(2)
    ellipse(width/2, height, rayon_orbite*2, rayon_orbite*2)

    # Dessine l'orbite haute
    stroke(0, 100, 200) # Définir un trait bleuâtre
    stroke_weight(2)
    ellipse(width/2, height, rayon_orbite_haut*2, rayon_orbite_haut*2)


def setup():
    # Configure ton animation ici
    size(taille_ecran, taille_ecran)
    image_mode(CENTER)
    global planete, fusee
    planete = load_image('orange_planet.png') # ta planète choisie
    fusee = load_image('rocket.png')


def draw():
    # Choses à faire dans chaque image
    dessine_arriere_plan()
    dessine_fusee()


carburant = int(input('Combien de kilos de carburant veux-tu utiliser ?'))
brule = int(input('Quelle quantité de carburant la fusée doit-elle brûler à chaque image ?'))
vitesse = int(input('Quelle distance la fusée doit-elle parcourir à chaque image ?'))
run()
