#!/bin/python3

# Importer le code de la bibliothèque
from p5 import *
from random import randint

# Configurer les variables globales
taille_ecran = 400
fusee_y = taille_ecran # commencer en bas
brule = 100 # combien de carburant est brûlé dans chaque image
rayon_orbite = 250
orbite_y = taille_ecran - rayon_orbite

# La fonction dessine_fusee vient ici
def dessine_fusee():

  global fusee_y, carburant, brule
  
  if carburant >= brule and fusee_y > orbite_y : # toujours en vol
    fusee_y -= 1 # déplace la fusée
    carburant -= brule # brûler du carburant
    print('Carburant restant : ', carburant)
  
    no_stroke() # Désactive le trait
  
    for i in range(25): # dessiner 25 ellipses d'échappement brûlant
      fill(255, 255 - i*10, 0) # jaune
      ellipse(width/2, fusee_y + i, 8, 3) # i augmente à chaque fois que la boucle se répète
    
    fill(200, 200, 200, 100) # gris transparent
    for i in range(20): # dessiner 20 ellipses de fumée aléatoire
      ellipse(width/2 + randint(-5, 5), fusee_y + randint(20, 50), randint(5, 10), randint(5, 10))
  
  if carburant < brule and fusee_y > orbit_y: # Plus de carburant et pas en orbite
    tint(255, 0, 0) # Échec
  elif carburant < 1000 and fusee_y <= orbite_y:
    tint(0, 255, 0) # Succès
  elif carburant >= 1000 and fusee_y <= orbite_y: 
    tint(255, 200, 0) # Trop de carburant
  
  image(fusee, width/2, fusee_y, 64, 64)
  no_tint()
  

# La fonction dessine_arriere_plan vient ici
def dessine_arriere_plan():
  background(0) # raccourci pour background(0, 0, 0) - noir 
  image(planete, width/2, height, 300, 300) # dessine l'image
  
  no_fill() # Désactive tout remplissage
  stroke(255) # Définir un trait blanc
  stroke_weight(2)
  ellipse(width/2, height, rayon_orbite*2, rayon_orbite*2)
  

def configuration():
  # Configure ton animation ici
  size(taille_ecran, taille_ecran)
  image_mode(CENTER)
  global planete, fusee
  planete = load_image('planet.png') # ta planète choisie
  fusee = load_image('rocket.png')


def dessin():
  # Choses à faire dans chaque image
  dessine_arriere_plan()   
  dessine_fusee()
  

carburant = int(input('Combien de kilos de carburant veux-tu utiliser ?'))
run()
