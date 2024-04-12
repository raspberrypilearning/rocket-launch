#!/bin/python3

# Importa la libreria di codice
from p5 import *
from random import randint

# Imposta le variabili globali
screen_size = 400
rocket_y = screen_size # Inizia dal basso
burn = 100 # Quanto carburante viene bruciato in ogni frame
orbit_radius = 250
orbit_y = screen_size - orbit_radius
high_orbit_radius = 350
high_orbit_y = screen_size - high_orbit_radius
speed = 1 # Quanto lontano vola il razzo per ogni fotogramma

# La funzione draw_rocket va qui


def draw_rocket():
    global rocket_y, fuel, burn

    if fuel >= burn and rocket_y > high_orbit_y:  # Sta ancora volando
        rocket_y -= speed  # Muovi il razzo
        fuel -= burn  # Brucia il carburante
        print('Carburante rimanente: ', fuel)

        no_stroke()  # Disattiva il disegno della linea

        for i in range(25):  # Disegna 25 ellissi di gas di scarico
            fill(255, 255 - i*10, 0)  # giallo
            # i aumenta ogni volta che il ciclo si ripete
            ellipse(width/2, rocket_y + i, 8, 3)

        fill(200, 200, 200, 100)  # grigio trasparente

        for i in range(20):  # disegna 20 ellissi casuali di fumo
            ellipse(width/2 + randint(-5, 5), rocket_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    if fuel < burn and rocket_y > high_orbit_y:  # Carburante esaurito e non ancora in orbita
        tint(255, 0, 0)  # Errore
    elif rocket_y <= orbit_y and rocket_y > high_orbit_y:
        tint(0, 255, 0)  # Successo
    elif fuel < 1000 and rocket_y <= high_orbit_y:
        tint(0, 100, 200)  # Orbita alta-Successo
    elif fuel >= 1000 and rocket_y <= high_orbit_y:
        tint(255, 200, 0)  # Troppo carburante

    image(rocket, width/2, rocket_y, 64, 64)
    no_tint()


# La funzione draw_ background va qui
def draw_background():
    background(0)  # Abbreviazione di background(0, 0, 0) - nero
    image(planet, width/2, height, 300, 300)  # disegna l'immagine

    # Disegna l'orbita inferiore
    no_fill() # Disattiva qualsiasi riempimento
    stroke(255)  # Imposta un tratto bianco
    stroke_weight(2)
    ellipse(width/2, height, orbit_radius*2, orbit_radius*2)

    # Disegna l'orbita più alta
    stroke(0, 100, 200)  # Imposta una linea blu
    stroke_weight(2)
    ellipse(width/2, height, high_orbit_radius*2, high_orbit_radius*2)


def setup():
    # Imposta la tua animazione qui
    size(screen_size, screen_size)
    image_mode(CENTER)
    global planet, rocket
    planet = load_image('orange_planet.png')  # Il pianeta che hai scelto tu
    rocket = load_image('rocket.png')


def draw():
    # Cose da fare in ogni fotogramma
    draw_background()
    draw_rocket()


fuel = int(input('Quanti kg di carburante vuoi usare?'))
burn = int(input('Quanto carburante dovrebbe bruciare il razzo per ogni fotogramma?'))
speed = int(input('Quanto lontano dovrà andare il razzo ad ogni fotogramma?'))
run()
