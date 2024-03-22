#!/bin/python3

# Importuj kod biblioteki
from p5 import *
from random import randint

# Ustaw zmienne globalne
screen_size = 400
Rocket_y = screen_size # Zacznij od dołu
Spalanie = 100 # Ile paliwa jest spalane w każdej klatce
orbita_promień = 250
orbit_y = screen_size - orbit_radius
high_orbit_radius = 350
high_orbit_y = screen_size - high_orbit_radius
Prędkość = 1 # jak daleko rakieta leci w każdej klatce

# Funkcja draw_rocket pojawia się tutaj


def draw_rocket():
    global rocket_y, paliwo, spalanie

    IF fuel >= spal i ROCKET_y > high_orbit_y: # Nadal leci
        Rocket_y -= prędkość # Przesuń rakietę
        Paliwo -= spalanie # spalanie paliwa
        Print('Pozostało paliwo: ', paliwo)

        No_stroke() # Wyłącz obrys

        For i in range(25): # Rysuj 25 palące się elipsy wydechowe
            fill(255, 255 - i*10, 0) # żółty
            # i zwiększa się za każdym razem, gdy pętla się powtarza
            elipsa(width/2, rocket_y + i, 8, 3)

        fill(200, 200, 200, 100) # przezroczysty szary

        for i in range(20): # narysuj 20 losowych elips dymu
            elipsa(width/2 + randint(-5, 5), rocket_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    IF paliwo < burn and ROCKET_y > high_orbit_y: # Brak paliwa i nie na orbicie
        Tint(255, 0, 0) # Niepowodzenie
    elif rocket_y <= orbita_y i rocket_y > high_orbit_y:
        Tint(0, 255, 0) # sukces
    paliwo elif < 1000 i rocket_y <= wysoka_orbita_y:
        Tint(0, 100, 200) # sukces na wysokiej orbicie
    paliwo elif >= 1000 i rocket_y <= wysoka_orbita_y:
        Tint(255, 200, 0) # za dużo paliwa

    image(rakieta, width/2, rocket_y, 64, 64)
    no_tint()


# Funkcja draw_background pojawia się tutaj
def draw_background():
    Background(0) # Krótkie dla tła(0, 0, 0) - czarny
    image(planeta, szerokość/2, wysokość, 300, 300) # narysuj obraz

    # Narysuj dolną orbitę
    No_fill() # Wyłącz dowolne wypełnienie
    Stroke(255) # Ustaw biały obrys
    waga_uderzenia(2)
    elipsa(width/2, height, orbit_radius*2, orbit_radius*2)

    # Narysuj wyższą orbitę
    Stroke(0, 100, 200) # Ustaw niebieskawy skok
    waga_uderzenia(2)
    elipsa(width/2, height, high_orbit_radius*2, high_orbit_radius*2)


def setup():
    # Ustaw swoją animację tutaj
    rozmiar(screen_size, screen_size)
    Image_mode(ŚRODEK)
    globalna planeta, rakieta
    Planeta = load_image('orange_planet.png') # wybrana planeta
    rocket = load_image('rocket.png')


def draw():
    # Rzeczy do zrobienia w każdej klatce
    draw_background()
    draw_rocket()


Paliwo = int(input('Ile kilogramów paliwa chcesz użyć?'))
Burn = int(input('Ile paliwa powinna spalić rakieta każda klatka?'))
Prędkość = int(input("jak daleko rakieta powinna przejechać każdą klatkę?"))
run()
