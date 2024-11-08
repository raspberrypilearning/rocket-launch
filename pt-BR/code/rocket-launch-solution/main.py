# Importar código da biblioteca
from p5 import *
from random import randint

# Set up global variables
tamanho_da_tela = 400
rocket_position = screen_size


# A função desenhar_foguete vai aqui
def desenhar_foguete():
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


# A função desenhar_fundo vai aqui
def desenhar_plano_de_fundo():
    background(0, 0, 0)
    image(planet, screen_size / 2, screen_size, 300, 300)


def setup():
    # Set up your animation here
    tamanho(tamanho_da_tela, tamanho_da_tela)
    modo_imagem(CENTRO)
    planeta global, foguete
    planet = load_image("purple_planet.png")
    rocket = load_image("rocket.png")


def draw():
    # Coisas para fazer em cada quadro
    desenhar_plano_de_fundo()
    desenhar_foguete()


run()
