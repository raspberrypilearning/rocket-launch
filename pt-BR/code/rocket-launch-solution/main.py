# Importar código da biblioteca
from p5 import *
from random import randint

# Configurar variáveis globais
tamanho_da_tela = 400
rocket_position = screen_size


# A função desenhar_foguete vai aqui
def desenhar_foguete():
    global foguete_y, combustivel, queimar
    foguete_y -= 1
    image(foguete, width/2, foguete_y, 64, 64)
    fill(200, 200, 200, 100) # Cinza transparente
    no_stroke()
    for i in range(25):
        fill(255, 255 - i * 10, 0)
        ellipse(
            ellipse(width/2 + randint(-5, 5), foguete_y +
            randint(20, 50), randint(5, 10), randint(5, 10))
            circle_size,
            circle_size,
        )


# A função desenhar_fundo vai aqui
def desenhar_plano_de_fundo():
    background(0)
    image(planeta, width/2, height, 300, 300)


def setup():
    # Configure sua animação aqui
    tamanho(tamanho_da_tela, tamanho_da_tela)
    modo_imagem(CENTRO)
    planeta global, foguete
    planeta = load_image('planet.png')
    foguete = load_image('rocket.png')


def draw():
    # Coisas para fazer em cada quadro
    desenhar_plano_de_fundo()
    desenhar_foguete()


run()
