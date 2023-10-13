## ¡Despegue!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Cada vez que se dibuja un nuevo cuadro, el cohete debe moverse hacia arriba en la pantalla para crear un efecto de animación.
</div>
<div>

![Un cohete que vuela a una velocidad constante desde la parte inferior hasta la parte superior de la pantalla.](images/fly.gif){:width="300px"}

</div>
</div>

--- task ---

El proyecto de inicio tiene una imagen de cohete provista para tí.

![Image of the rocket in the code editor image gallery.](images/rocket_image.png)

--- /task ---

--- task ---

Agrega código a la función `setup()` para cargar la imagen del cohete en una variable global `cohete`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 24, 26
---

def setup():   
# Setup your animation here   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet, rocket   
planet = load_image('planet.png')    
rocket = load_image('rocket.png')

--- /code ---

--- /task ---

### Make the rocket fly

La posición `y` del cohete comenzará en 400 (la altura de la pantalla) y luego disminuirá en 1 cada vez que se dibuje un nuevo fotograma.

--- task ---

Agrega una variable global `rocket_y` para realizar un seguimiento de la posición `y` del cohete.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9
---

# Configurar variables globales
screen_size = 400    
rocket_y = screen_size  # Start at the bottom

--- /code ---

--- /task ---

--- task ---

Define una función `draw_rocket()` para cambiar la posición `y` del cohete y volver a dibujarlo.

`rocket_y -= 1` es una forma más corta de decir `rocket_y = rocket_y - 1`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12-16
---

# La función draw_rocket va aquí
def draw_rocket():   
global rocket_y  # Use the global rocket_y variable    
rocket_y -= 1  # Move the rocket    
image(rocket, width/2, rocket_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

Call your new `draw_rocket()` in the `draw()` function so that the rocket gets redrawn every frame.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 33
line_highlights: 36
---

def draw():   
# Things to do in every frame   
draw_background()   
draw_rocket()


--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to check that the rocket starts at the bottom of the screen and moves up each frame.

![Animation of the rocket flying half way up the screen.](images/rocket_fly.gif)

--- /task ---

--- save ---
