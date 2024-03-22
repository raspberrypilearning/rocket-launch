#!/bin/python3

# Importuj kod biblioteki
from p5 import *
from random import randint

# Ustaw zmienne globalne
screen_size = 400
rocket_y = 400
spalenie = 100
orbita_promień = 250
orbit_y = screen_size - orbit_radius


# Funkcja draw_rocket pojawia się tutaj
def draw_rocket():
    global rocket_y, paliwo, spalanie

    if fuel >= spal i rocket_y > orbit_y:
        rocket_y -= 1
        paliwo -= spalanie
        Print('Pozostało paliwo: ', paliwo)

        no_stroke()

        for i in range(25):
            fill(255, 255 - i * 10, 0)
            elipsa(width/2, rocket_y + i, 8, 3)

        Fill(200, 200, 200, 100) # Przezroczysty szary
        For i in range(20): # Rysuj 20 losowych elips dymu
            elipsa(width/2 + randint(-5, 5), rocket_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    if paliwo < burn and rocket_y > orbit_y:
        tint(255, 0, 0)
    paliwo elif < 1000 i rocket_y <= orbita_y:
        tint(0, 255, 0)
    paliwo elif >= 1000 i rocket_y <= orbit_y:
        tint(255, 200, 0)

    image(rakieta, width/2, rocket_y, 64, 64)
    no_tint()


# Funkcja draw_background pojawia się tutaj
def draw_background():
    background(0)
    obraz(planeta, szerokość/2, wysokość, 300, 300)

    no_fill()
    stroke(255)
    stroke_weight(2)
    elipsa(width/2, height, orbit_radius * 2, orbit_radius * 2)


def setup():
    # Ustaw swoją animację tutaj
    rozmiar(screen_size, screen_size)
    Image_mode(ŚRODEK)
    globalna planeta, rakieta
    planeta = load_image('planet.png')
    rocket = load_image('rocket.png')


def draw():
    # Rzeczy do zrobienia w każdej klatce
    draw_background()
    draw_rocket()


Paliwo = int(input('Ile kilogramów paliwa chcesz użyć?'))
run()
