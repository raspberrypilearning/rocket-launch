#!/bin/python3

# Importar código da biblioteca
from p5 import *
from random import randint

# Configurar variáveis globais
tamanho_da_tela = 400
foguete_y = 400
queimar = 100
raio_orbita = 250
orbita_y = tamanho_da_tela - raio_orbita


# A função desenhar_foguete vai aqui
def desenhar_foguete():
    global foguete_y, combustível, queimar

    if combustivel >= queimar and foguete_y > orbita_y:
        foguete_y -= 1
        combustível -= queimar
        print('Combustível restante: ', combustivel)

        no_stroke()

        for i in range(25):
            fill(255, 255 - i * 10, 0)
            elipse (largura/2, foguete_y + i, 8, 3)

        fill(200, 200, 200, 100) # Cinza transparente
        for i in range(20): # Desenha 20 elipses de fumaça aleatórias
            elipse(largura/2 + randint(-5, 5), foguete_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    if combustível < queimar and foguete_y >orbita_y:
        tint(255, 0, 0)
    elif combustivel <1000 and foguete_y <= orbita_y:
        tint(0, 255, 0)
    elif combustivel >= 1000 and foguete_y <= orbita_y:
        tint(255, 200, 0)

    imagem(foguete, largura/2, foguete_y, 64, 64)
    no_tint()


# A função desenhar_fundo vai aqui
def desenhar_plano_de_fundo():
    background(0)
    image(planeta, largura/2, altura, 300, 300)

    no_fill()
    stroke(255)
    stroke_weight(2)
    ellipse(largura/2, altura, raio_orbita * 2, raio_orbita * 2)


def setup():
    # Configure sua animação aqui
    tamanho(tamanho_da_tela, tamanho_da_tela)
    modo_imagem(CENTRO)
    planeta global, foguete
    planeta = carregar_imagem('planeta.png')
    foguete = carregar_imagem('rocket.png')


def draw():
    # Coisas para fazer em cada quadro
    desenhar_plano_de_fundo()
    desenhar_foguete()


combustivel = int(input('Quantos quilogramas de combustível você quer usar?'))
run()
