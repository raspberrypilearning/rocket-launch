#!/bin/python3

# Importar código de biblioteca
from p5 import *
from random import randint

# Configuración de variables globales
tamano_pantalla = 400
cohete_y = tamano_pantalla # comienza en la parte inferior
quemar = 100 # cuánto combustible se quema en cada cuadro
orbita_radio = 250
orbita_y = tamano_pantalla - orbita_radio
orbita_radio_mayor = 350
orbita_radio_y = tamano_pantalla - orbita_radio_mayor
velocidad = 1 # Qué tan lejos vuela el cohete en cada cuadro

# La función dibujar_cohete va aquí


def dibujar_cohete():
    global cohete_y, combustible, quemar

    if combustible >= quemar and cohete_y > orbita_y: # sigue volando
        cohete_y -= velocidad # mueve el cohete
        combustible -= quemar # quemar combustible
        print('Combustible restante: ', combustible)

        no_stroke() # Desactiva el trazo

        for i in range(25): # dibujar 25 elipses humo de escape
            fill(255, 255 - i*10, 0) # amarillo
            # i aumenta cada vez que se repite el bucle
            elipse(ancho/2, cohete_y + i, 8, 3)

        fill(200, 200, 200, 100) # gris transparente

        for i in range(20): # dibujar 20 elipses de humo al azar
            elipse(ancho/2 + randint(-5, 5), cohete_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    if combustible < quemar and cohete_y > orbita_y_mayor: # No más combustible y no en órbita
        tint(255, 0, 0) # Fallo
    elif cohete_y <= orbita_y y cohete_y > orbita_y_mayor:
        tint(0, 255, 0) # Éxito
    elif combustible < 1000 and cohete_y <= orbita_y_mayor:
        tint(0, 100, 200) # Éxito de órbita alta
    elif combustible < 1000 and cohete_y <= orbita_y_mayor:
        tint(255, 200, 0) # Demasiado combustible

    image(cohete, ancho/2, cohete_y, 64, 64)
    no_tint()


# Aquí va la función dibujar_fondo
def dibujar_fondo():
    fondo(0) # abreviatura de fondo (0, 0, 0) - negro
    image(planeta, ancho/2, altura, 300, 300) # dibujar la imagen

    # Dibuja la órbita inferior
    no_fill() # Desactiva el relleno
    stroke(255) # Establece un trazo blanco
    stroke_weight(2)
    elipse(ancho/2, alto, radio_órbita*2, radio_órbita*2)

    # Dibuja la órbita superior
    stroke(0, 100, 200) # Establece un trazo azulado
    stroke_weight(2)
    elipse(ancho/2, alto, radio_órbita*2, radio_órbita*2)


def setup():
    # Configura tu animación aquí
    tamano(tamano_pantalla, tamano_pantalla)
    image_mode(CENTER)
    global planeta, cohete
    planeta = load_image('orange_planet.png') # Tu planeta elegido
    cohete = load_image('rocket.png')


def draw():
    # Cosas que hacer en cada cuadro
    dibujar_fondo()
    dibujar_cohete()


combustible = int(input('¿Cuántos kilogramos de combustible quieres usar?'))
burn = int(input('¿Cuánto combustible debe quemar el cohete en cada cuadro?'))
velocidad = int(input('¿Qué distancia debe recorrer el cohete en cada cuadro?'))
run()
