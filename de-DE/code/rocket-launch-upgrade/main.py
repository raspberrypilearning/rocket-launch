#!/bin/python3

# Bibliothekscode importieren
from p5 import *
from random import randint

# Globale Variablen einrichten
bildschirm_groesse = 400
rakete_y = bildschirm_groesse # unten starten
verbrennen = 100 # Wieviel Treibstoff wird in jedem Frame verbrannt
orbit_radius = 250
orbit_y = bildschirm_groesse - orbit_radius
hoher_orbit_radius = 350
hoher_orbit_y = bildschirm_groesse - hoher_orbit_radius
geschwindigkeit = 1 # Wie weit die Rakete in jedem Frame fliegt

# Die Funktion „zeichne_rakete“ kommt hierher


def zeichne_rakete():
    global rakete_y, treibstoff, verbrennen

    if treibstoff >= verbrennen and rakete_y > hoher_orbit_y: # fliegt immer noch
        rakete_y -= geschwindigkeit # Bewege die Rakete
        treibstoff -= verbrennen # Treibstoff verbrennen
        print('Verbleibender Treibstoff: ', treibstoff)

        no_stroke() # Schaltet Zeichnen aus

        for i in range(25): # Zeichne 25 brennende Abgasellipsen
            fill(255, 255 - i*10, 0) # gelb
            # i erhöht sich bei jeder Wiederholung der Schleife
            ellipse(width/2, rakete_y + i, 8, 3)

        fill(200, 200, 200, 100) # Transparent grau

        for i in range(20): # Zeichne 20 zufällige Rauchellipsen
            ellipse(width/2 + randint(-5, 5), rakete_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    if treibstoff < verbrennen and rakete_y > hoher_orbit_y: # kein Treibstoff mehr und nicht im Orbit
        tint(255, 0, 0) # Versagen
    elif rakete_y <= orbit_y and rakete_y > hoher_orbit_y:
        tint(0, 255, 0) # Erfolg
    elif treibstoff < 1000 and rakete_y <= hoher_orbit_y:
        tint(0, 100, 200) # Erfolg: hoher Orbit
    elif treibstoff >= 1000 and rakete_y <= hoher_orbit_y:
        tint(255, 200, 0) # Zu viel Treibstoff

    image(rakete, width/2, rakete_y, 64, 64)
    no_tint()


# Die Funktion „zeichne_hintergrund“ kommt hierher
def zeichne_hintergrund():
    background(0) # Kurzform für background(0, 0, 0) - schwarz
    image(planet, width/2, height, 300, 300)  # zeichne das Bild

    # Zeichne die untere Umlaufbahn
    no_fill() # Jegliche Füllung ausschalten
    stroke(255) # Setzt einen weißen Strich
    stroke_weight(2)
    ellipse(width/2, height, orbit_radius * 2, orbit_radius * 2)

    # Zeichne die höhere Umlaufbahn
    stroke(0, 100, 200) # Setzt einen bläulichen Strich
    stroke_weight(2)
    ellipse(width/2, height, hoher_orbit_radius * 2, hoher_orbit_radius * 2)


def setup():
    # Richte hier Deine Animation ein
    size(bildschirm_groesse, bildschirm_groesse)
    image_mode(CENTER)
    global planet, rakete
    planet = load_image('orange_planet.png') # Dein gewählter Planet
    rakete = load_image('rocket.png')


def draw():
    # Dinge die in jedem Frame passieren
    zeichne_hintergrund()
    zeichne_rakete()


treibstoff = int(input('Wie viele Kilogramm Treibstoff willst Du verbrauchen?'))
verbrennen = int(input('Wie viel Treibstoff soll die Rakete pro Frame verbrennen?'))
geschwindigkeit = int(input('Wie weit soll die Rakete pro Frame fliegen?'))
run()
