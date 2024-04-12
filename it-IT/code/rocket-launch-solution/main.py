#!/bin/python3

# Importa il codice della libreria
from p5 import *
from random import randint

# Imposta le variabili globali
screen_size = 400
rocket_y = 400
burn = 100
orbit_radius = 250
orbit_y = screen_size - orbit_radius


# La funzione draw_rocket va qui
def draw_rocket():
    global rocket_y, fuel, burn

    if fuel >= burn and rocket_y > orbit_y:
        rocket_y -= 1
        fuel -= burn
        print('Carburante rimanente: ', fuel)

        no_stroke()

        for i in range(25):
            fill(255, 255 - i * 10, 0)
            ellipse(width/2, rocket_y + i, 8, 3)

        fill(200, 200, 200, 100) # Grigio trasparente
        for i in range(20): # Disegna 20 ellissi di fumo casuali
            ellipse(width/2 + randint(-5, 5), rocket_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    if fuel < burn and rocket_y > orbit_y:
        tint(255, 0, 0)
    elif fuel < 1000 and rocket_y <= orbit_y:
        tint(0, 255, 0)
    elif fuel >= 1000 and rocket_y <= orbit_y:
        tint(255, 200, 0)

    image(rocket, width/2, rocket_y, 64, 64)
    no_tint()


# La funzione draw_ background va qui
def draw_background():
    background(0)
    image(planet, width/2, height, 300, 300)

    no_fill()
    stroke(255)
    stroke_weight(2)
    ellipse(width/2, height, orbit_radius * 2, orbit_radius * 2)


def setup():
    # Imposta la tua animazione qui
    size(screen_size, screen_size)
    image_mode(CENTER)
    global planet, rocket
    planet = load_image('planet.png')
    rocket = load_image('rocket.png')


def draw():
    # Cose da fare in ogni fotogramma
    draw_background()
    draw_rocket()


fuel = int(input('Quanti chilogrammi di carburante vuoi usare?'))
run()
