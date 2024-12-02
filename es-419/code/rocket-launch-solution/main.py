# Importar código de biblioteca
from p5 import *
from random import randint

# Configurar variables globales
tamano_pantalla = 400
posicion_cohete = tamano_pantalla


# Aquí va la función dibujar_cohete
def dibujar_cohete():
    global posicion_cohete
    posicion_cohete = posicion_cohete - 1
    image(cohete, ancho/2, cohete_y, 64, 64)
    fill(200, 200, 200, 100)
    no_stroke()
    for i in range(20):
        tamano_circulo = randint(5, 10)
        elipse(
            tamano_pantalla / 2 + randint(-5, 5),
            posicion_cohete + randint(20, 50),
            tamano_circulo
            tamano_circulo,
        )


# Aquí va la función dibujar_fondo
def dibujar_fondo():
    background(0, 0, 0)
    image(planeta, tamano_pantalla / 2, tamano_pantalla, 300, 300)


def setup():
    # Configura tu animación aquí
    size(tamano_pantalla, tamano_pantalla)
    image_mode(CENTER)
    global planeta, cohete
    planeta = load_image("purple_planet.png")
    cohete = load_image("rocket.png")


def draw():
    # Cosas que hacer en cada cuadro
    dibujar_fondo()
    dibujar_cohete()


run()
