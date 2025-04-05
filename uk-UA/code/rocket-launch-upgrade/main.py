#!/bin/python3

# Імпортуй код бібліотеки
from p5 import *
from random import randint

# Встанови глобальні змінні
screen_size = 400
rocket_y = screen_size  # Початок знизу
burn = 100  # Скільки палива спалюється у кожному кадрі
orbit_radius = 250
orbit_y = screen_size - orbit_radius
high_orbit_radius = 350
high_orbit_y = screen_size - high_orbit_radius
speed = 1  # Відстань, яку ракета пролітає за кожен кадр

# Тут буде функція draw_rocket


def draw_rocket():
    global rocket_y, fuel, burn

    if fuel >= burn and rocket_y > high_orbit_y:  # Досі летить
        rocket_y -= speed  # Ракета рухається
        fuel -= burn  # Спалюється паливо
        print('Залишилось палива: ', fuel)

        no_stroke()  # Вимкнути дим

        for i in range(25):  # Намалюй 25 еліпсів для вихлопних газів
            fill(255, 255 - i*10, 0)  # жовтий
            # i збільшується з кожним повторенням циклу
            ellipse(width/2, rocket_y + i, 8, 3)

        fill(200, 200, 200, 100)  # прозорий сірий

        for i in range(20):  # Намалюй 20 випадкових еліпсів для диму
            ellipse(width/2 + randint(-5, 5), rocket_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    if fuel < burn and rocket_y > high_orbit_y:  # Паливо закінчилось, не на орбіті
        tint(255, 0, 0)  # Невдача
    elif rocket_y <= orbit_y and rocket_y > high_orbit_y:
        tint(0, 255, 0)  # Успіх
    elif fuel < 1000 and rocket_y <= high_orbit_y:
        tint(0, 100, 200)  # Успіх на дальній орбіті
    elif fuel >= 1000 and rocket_y <= high_orbit_y:
        tint(255, 200, 0)  # Забагато палива

    image(rocket, width/2, rocket_y, 64, 64)
    no_tint()


# Тут буде функція draw_background
def draw_background():
    background(0)  # Короткий запис замість background(0, 0, 0) — чорний
    image(planet, width/2, height, 300, 300)  # намалюй зображення

    # Намалюй ближню орбіту
    no_fill()  # Вимкни заповнення
    stroke(255)  # Встанови білий колір лінії
    stroke_weight(2)
    ellipse(width/2, height, orbit_radius*2, orbit_radius*2)

    # Намалюй дальню орбіту
    stroke(0, 100, 200)  # Встанови блакитний колір лінії
    stroke_weight(2)
    ellipse(width/2, height, high_orbit_radius*2, high_orbit_radius*2)


def setup():
    # Тут налаштуй анімацію
    size(screen_size, screen_size)
    image_mode(CENTER)
    global planet, rocket
    planet = load_image('orange_planet.png')  # Вибрана планета
    rocket = load_image('rocket.png')


def draw():
    # Що відбувається на кожному кадрі
    draw_background()
    draw_rocket()


fuel = int(input('Скільки кілограмів пального ти хочеш використати?'))
burn = int(input('Скільки палива має спалювати ракета на кожному кадрі?'))
speed = int(input('Яку відстань має проходити ракета за кожен кадр?'))
run()
