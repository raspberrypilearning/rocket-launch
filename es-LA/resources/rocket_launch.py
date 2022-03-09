#!/bin/python3

# Importar código de biblioteca
from p5 import *
from random import randint

# Configurar variables globales
tamano_pantalla = 400
cohete_y = tamano_pantalla # comienza en la parte inferior
quemar = 100 # cuánto combustible se quema en cada cuadro
orbita_radio = 250
orbita_y = tamano_pantalla - orbita_radio

# La función dibujar_cohete va aquí
def dibujar_cohete():

  global cohete_y, combustible, quemar
  
  if combustible >= quemar and cohete_y > orbita_y: # sigue volando
    cohete_y -= 1 # mueve el cohete
    combustible -= quemar # quemar combustible
    print('Combustible restante: ', combustible)
  
    no_stroke() # Desactiva el trazo
  
    for i in range(25): # dibujar 25 elipses de escape en llamas
      fill(255, 255 - i*10, 0) # amarillo
      ellipse(width/2, cohete_y + i, 8, 3) # i aumenta cada vez que se repite el bucle
    
    fill(200, 200, 200, 100) # gris transparente
    for i in range(20): # dibujar 20 elipses de humo al azar
      ellipse(width/2 + randint(-5, 5), cohete_y + randint(20, 50), randint(5, 10), randint(5, 10))
  
  if combustible < quemar and cohete_y > orbita_y: # No más combustible y no en órbita
    tint(255, 0, 0) # Fallo
  elif combustible < 1000 and cohete_y <= orbita_y:
    tint(0, 255, 0) # Éxito
  elif combustible >= 1000 and cohete_y <= orbita_y: 
    tint(255, 200, 0) # Demasiado combustible
  
  image(cohete, width/2, cohete_y, 64, 64)
  no_tint()
  

# La función dibujar_fondo va aquí
def dibujar_fondo():
  background(0) # abreviatura de fondo (0, 0, 0) - negro 
  image(planeta, width/2, height, 300, 300) # dibujar la imagen
  
  no_fill() # Desactiva cualquier relleno
  stroke(255) # Establecer un trazo blanco
  stroke_weight(2)
  ellipse(width/2, height, orbita_radio*2, orbita_radio*2)
  

def setup():
  # Configura tu animación aquí
  size(tamano_pantalla, tamano_pantalla)
  image_mode(CENTER)
  global planeta, cohete
  planeta = load_image('planet.png') # tu planeta elegido
  cohete = load_image('rocket.png')


def draw():
  # Cosas que hacer en cada cuadro
  dibujar_fondo()  
  dibujar_cohete()
  

combustible = int(input('¿Cuántos kilogramos de combustible quieres usar?'))
run()
