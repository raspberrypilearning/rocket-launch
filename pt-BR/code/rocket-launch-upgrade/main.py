#!/bin/python3

# Importar código da biblioteca
from p5 import *
from random import randint

# Configurar variáveis globais
tamanho_da_tela = 400
foguete_y = tamanho_tela #Comece na parte inferior
queimar = 100 # Quanto combustível é queimado em cada quadro
raio_orbita = 250
orbita_y = tamanho_da_tela - raio_orbita
raio_orbita_alto = 350
orbita_y_alto = tamanho_da_tela - raio_orbita_alto
velocidade = 1 # Quão longe o foguete voa em cada quadro

# A função desenhar_foguete vai aqui


def desenha_foguete():
    global foguete_y, combustivel, queimar

    if combustivel >= queimar and foguete_y > orbita_y_alto: # Ainda voando
        foguete_y -= velocidade # Mova o foguete
        combustivel -= queimar # Queima combustível
        print('Combustível restante: ', combustivel)

        no_stroke()  # Desligue o lançamento

        for i in range(25):  # Desenhe 25 elipses de combustão em chamas
            fill(255, 255 - i*10, 0)  # amarelo
            # i aumenta cada vez que o ciclo se repete
            elipse (largura/2, foguete_y + i, 8, 3)

        fill(200, 200, 200, 100) # Cinza transparente

        for i in range(20): # desenha 20 elipses de fumaça aleatórias
            elipse(largura/2 + randint(-5, 5), foguete_y +
                    randint(20, 50), randint(5, 10), randint(5, 10))

    if combustivel < queimar and foguete_y > orbita_y_alto:  # Não há mais combustível e não em órbita
        tint(255, 0, 0)  # Fracasso
    elif foguete_y <= orbita_y and foguete_y > orbita_y_alto:
        tint(0, 255, 0)  # Successo
    elif combustivel < 1000 and foguete_y <= orbita_y_alto:
        tint(0, 100, 200) # Sucesso em órbita alta
    elif combustivel >= 1000 and foguete_y <= orbita_y_alto:
        tint(255, 200, 0)  # Excesso de combustível

    image(foguete, largura/2, foguete_y, 64, 64)
    no_tint()


# A função desenhar_fundo vai aqui
def desenhar_plano_de_fundo():
    background(0)  # Abreviação de plano de fundo (0, 0, 0) — preto
    image(planeta, largura/2, altura, 300, 300) # desenhe a imagem

    # Desenhe a órbita inferior
    no_fill()  # Desligue qualquer preenchimento
    stroke(255)  # Defina um traço branco
    stroke_weight(2)
    ellipse(largura/2, altura, raio_orbita * 2, raio_orbita * 2)

    # Desenhe a órbita mais alta
    stroke(0, 100, 200) # Define um traço azulado
    stroke_weight(2)
    ellipse(largura/2, altura, raio_orbita_alto * 2, raio_orbita_alto * 2)


def setup():
    # Configure sua animação aqui
    size(tamanho_da_tela, tamanho_da_tela)
    image_mode(CENTER)
    global planeta, foguete
    planeta = load_image('orange_planet.png')  # Seu planeta escolhido
    foguete = load_image('rocket.png')


def draw():
    # Coisas para fazer em cada quadro
    desenhar_plano_de_fundo()
    desenhar_foguete()


combustivel = int(input('Quantos quilogramas de combustível você quer usar?'))
queimar = int(input('Quanto combustível o foguete deve queimar em cada quadro?'))
velocidade = int(input('Qual a distância que o foguete deve percorrer em cada quadro?'))
run()
