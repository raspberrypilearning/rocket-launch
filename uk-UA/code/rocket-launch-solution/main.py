# Імпортуй код бібліотеки
from p5 import *
from random import randint

# Встанови глобальні змінні
screen_size = 400
rocket_position = screen_size


# Тут буде функція draw_rocket
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


# Тут буде функція draw_background
def draw_background():
    background(0, 0, 0)
    image(planet, screen_size / 2, screen_size, 300, 300)


def setup():
    # Тут налаштуй анімацію
    size(screen_size, screen_size)
    image_mode(CENTER)
    global planet, rocket
    planet = load_image("purple_planet.png")
    rocket = load_image("rocket.png")


def draw():
    # Що відбувається на кожному кадрі
    draw_background()
    draw_rocket()


run()
