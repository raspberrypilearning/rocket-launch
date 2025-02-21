## ¡Despegar!

El proyecto de inicio tiene una imagen de cohete provista para tí.

![Imagen del cohete en la galería de imágenes del editor de código.](images/rocket_image.png)

--- task ---

Add code to the `setup()` function to load the rocket image into a `rocket` global variable.

<div class="c-project-code">

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 17
line_highlights: 21, 23
---

def setup():   
#Configura tu animación aquí   
tamano(tamano_pantalla, tamano_pantalla)   
image_mode(CENTER)   
global planeta, cohete   
planeta = load_image('planet.png')    
cohete = load_image( 'rocket.png')

--- /code ---

--- /task ---

--- task ---

Agrega una variable global `posicion_cohete` para realizar un seguimiento de la posición `y` del cohete.

--- code ---
---
language: python line_numbers: true line_number_start: 5
line_highlights: 7
---

# Configurar variables globales
tamano_de_pantalla = 400    
posición_del_cohete = tamano_de_pantalla

--- /code ---

--- /task ---


La posición `y` del cohete comenzará en 400 (la altura de la pantalla) y luego disminuirá en 1 cada vez que se dibuje un nuevo fotograma.

--- task ---

Define una función `dibujar_cohete()` para hacer que el cohete aparezca en la pantalla.

--- code ---
---
language: python line_numbers: true line_number_start: 9
line_highlights: 10-12
---

# La función draw_rocket va aquí
def dibujar_cohete():   
posicion_cohete global      
image(cohete, ancho/2, posicion_cohete, 64, 64)


--- /code ---

--- /task ---

--- task ---

Llama a la función `dibujar_cohete()`.

--- code ---
---
language: python line_numbers: true line_number_start: 29
line_highlights: 32
---

def dibujar(): #Cosas a hacer en cada fotograma dibujar_fondo() dibujar_cohete()


--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu código y verifica que el cohete aparece en la parte inferior de la imagen.

--- /task ---


Cada vez que se dibuja un nuevo cuadro, el cohete debe moverse hacia arriba en la pantalla para crear un efecto de animación.


--- task ---

La `posicion_cohete` comenzará en 400 (la altura de la pantalla) y luego disminuirá en 1 cada vez que se dibuje un nuevo cuadro.


--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 12
---

def draw_rocket():   
global rocket_position     
rocket_position = rocket_position - 1    
image(rocket, width/2, rocket_position, 64, 64)

--- /code ---

--- /task ---


--- task ---

**Prueba:** Ejecuta tu código para verificar que el cohete despegue desde la parte inferior de la pantalla.


![Un cohete que vuela a una velocidad constante desde la parte inferior hasta la parte superior de la pantalla.](images/fly.gif){:width="300px"}

--- /task ---

