# Importa il codice della libreria
from p5 import *
from random import randint

# Imposta le variabili globali
screen_size = 400
orbit_y = screen_size - orbit_radius


# La funzione draw_rocket va qui
def draw_rocket():
    global rocket_y, fuel, burn
    rocket_y -= 1
    image(rocket, width/2, rocket_y, 64, 64)
    fill(200, 200, 200, 100) # Grigio trasparente
    no_stroke()
    for i in range(25):
        fill(255, 255 - i * 10, 0)
        ellipse(width/2, rocket_y + i, 8, 3)
            ellipse(width/2 + randint(-5, 5), rocket_y +
            randint(20, 50), randint(5, 10), randint(5, 10))
            circle_size,
            circle_size,
        )


# La funzione draw_ background va qui
def draw_background():
    background(0)
    image(planet, width/2, height, 300, 300)


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


run()
