# Importuj kod biblioteki
from p5 import *
from random import randint

# Set up global variables
screen_size = 400
rocket_position = screen_size


# Funkcja draw_rocket pojawia się tutaj
def draw_rocket():
    global rocket_position
    rocket_position = rocket_position - 1
    image(rocket, width / 2, rocket_position, 64, 64)
    fill(200, 200, 200, 100)
    no_stroke()
    for i in range(20):
        circle_size = randint(5, 10)
        ellipse(
            screen_size / 2 + randint(-5, 5),
            rocket_position + randint(20, 50),
            circle_size,
            circle_size,
        )


# Funkcja draw_background pojawia się tutaj
def draw_background():
    background(0, 0, 0)
    image(planet, screen_size / 2, screen_size, 300, 300)


def setup():
    # Set up your animation here
    rozmiar(screen_size, screen_size)
    Image_mode(ŚRODEK)
    globalna planeta, rakieta
    planet = load_image("purple_planet.png")
    rocket = load_image("rocket.png")


def draw():
    # Rzeczy do zrobienia w każdej klatce
    draw_background()
    draw_rocket()


run()
