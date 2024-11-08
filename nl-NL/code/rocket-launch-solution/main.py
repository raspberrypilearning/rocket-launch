# Bibliotheekcode importeren
from p5 import *
from random import randint

# Set up global variables
scherm_grootte = 400
rocket_position = screen_size


# De teken_raket functie komt hier
def teken_raket():
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


# De functie teken_achtergrond komt hier
def teken_achtergrond():
    background(0, 0, 0)
    image(planet, screen_size / 2, screen_size, 300, 300)


def setup():
    # Set up your animation here
    size(scherm_grootte, scherm_grootte)
    image_mode(CENTER)
    global planeet, raket
    planet = load_image("purple_planet.png")
    rocket = load_image("rocket.png")


def draw():
    # Dingen om te doen in elk frame
    teken_achtergrond()
    teken_raket()


run()
