#!/bin/python3

# Bibliotheekcode importeren
from p5 import *
from random import randint

# Globale variabelen instellen
scherm_grootte = 400
raket_y = scherm_grootte # begin onderaan
verbruik = 100 # hoeveel brandstof wordt er in elk frame verbrand
omloopbaan_straal = 250
omloopbaan_y = scherm_grootte - omloopbaan_straal

# De teken_raket functie komt hier
def teken_raket():

  global raket_y, brandstof, verbruik
  
  if brandstof >= verbruik and raket_y > omloopbaan_y: # vliegt nog steeds
    raket_y -= 1 # verplaats de raket
    brandstof -= verbruik # brandstof verbruik
    print('Brandstof over: ', brandstof)
  
    no_stroke() # Zet de lijn uit
  
    for i in range(25): # teken 25 brandende uitstoot ellipsen
      fill(255, 255 - i*10, 0) # geel
      ellipse(width/2, raket_y + i, 8, 3) # i neemt toe elke keer dat de lus wordt herhaald
    
    fill(200, 200, 200, 100) # transparant grijs
    for i in range(20): # teken 20 willekeurige rook ellipsen
      ellipse(width/2 + randint(-5, 5), raket_y + randint(20, 50), randint(5, 10), randint(5, 10))
  
  if brandstof < verbruik and raket_y > omloopbaan_y: # Geen brandstof meer en niet in een omloopbaan
    tint(255, 0, 0) # Mislukt
  elif brandstof < 1000 and raket_y <= omloopbaan_y:
    tint(0, 255, 0) # Gelukt
  elif brandstof >= 1000 and raket_y <= omloopbaan_y: 
    tint(255, 200, 0) # Te veel brandstof
  
  image(raket, width/2, height/2, 64, 64)
  no_tint()
  

# De functie teken_achtergrond komt hier
def teken_achtergrond():
  background(0) # afkorting voor background(0, 0, 0) - zwart 
  image(planeet, width/2, height, 300, 300) # teken de afbeelding
  
  no_fill() # Zet elke vulling uit
  stroke(255) # Stel een witte lijn in
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
run()
