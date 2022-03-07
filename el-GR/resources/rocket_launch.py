#!/bin/python3

#Εισαγωγή του κώδικα της βιβλιοθήκης
from p5 import *
from random import randint

# Ορισμός καθολικών μεταβλητών
screen_size = 400
rocket_y = screen_size # ξεκινάει από το κάτω μέρος
καύση = 100 # πόσο καύσιμο καίγεται σε κάθε καρέ
orbit_radius = 250
orbit_y = screen_size - orbit_radius

# Η συνάρτηση draw_rocket πηγαίνει εδώ
def draw_rocket():

  global rocket_y, fuel, burn
  
  if fuel > burn and rocket_y > orbit_y: #Ακόμα πετάει
    rocket_y -= 1 # μετακίνησε τον πύραυλο
    καύσιμο -= καίω # καύση καυσίμου
    print('Υπολειπόμενο καύσιμο: ', fuel)
  
    no_stroke() #Απενεργοποίηση πινελιάς
  
    for i in range(25): # σχεδίαση 25 ελλείψεων για την καύση καυσαερίων
      fill(255, 255 - i*10, 0) # κίτρινο
      ellipse(width/2, rocket_y + i, 8, 3) # i αυξάνεται κάθε φορά που ο βρόχος επαναλαμβάνεται
    
    fill(200, 200, 200, 100) # διαφανές γκρι
    for i in range(20): # σχεδίαση 20 τυχαίων ελλείψεων καπνού
      ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))
  
  if fuel < burn and rocket_y > orbit_y: #Δεν υπάρχει καύσιμο και δεν είναι σε τροχιά
    tint(255, 0, 0) # Αποτυχία
  elif fuel < 1000 and rocket_y <= orbit_y:
    tint(0, 255, 0) # Επιτυχία
  elif fuel >= 1000 and rocket_y <= orbit_y: 
    tint(255, 200, 0) # Πάρα πολύ καύσιμο
  
  image(rocket, width/2, rocket_y, 64, 64)
  no_tint()
  

# Η συνάρτηση draw_background πηγαίνει εδώ
def draw_background():
  background(0) # short for background(0, 0, 0) - black 
  image(planet, width/2, height, 300, 300) # σχεδίαση της εικόνας
  
  no_fill() # Απενεργοποήση οποιουδήποτε γεμίσματος
  stroke(255) # Ορισμός μιας λευκής πινελιάς
  stroke_weight(2)
  ellipse(width/2, height, orbit_radius*2, orbit_radius*2)
  

def setup():
  # Ορισμός της κινούμενης εικόνας σου εδώ
  size(screen_size, screen_size)
  image_mode(CENTER)
  global planet, rocket
  planet = load_image('planet.png') # ο πλανήτης που επέλεξες
  rocket = load_image('rocket.png')


def draw():
  # Πράγματα που πρέπει να γίνονται σε κάθε καρέ
  draw_background()  
  draw_rocket()
  

fuel = int(input('Πόσα κιλά καυσίμου θέλεις να χρησιμοποιήσεις;'))
run()
