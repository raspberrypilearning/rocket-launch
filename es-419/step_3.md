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

![Imagen del cohete en la galería de imágenes del editor de código.](images/rocket_image.png)

--- /task ---

--- task ---

Agrega código a la función `setup()` para cargar la imagen del cohete en una variable global `cohete`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 24, 26
---

def setup():   
# Configura tu animación aquí   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet, roket   
planet = load_image('planet.png')     
rocket = load_image('rocket.png')

--- /code ---

--- /task ---

### Haz volar el cohete

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
rocket_y = screen_size # Comienza en la parte inferior

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
global rocket_y # Usar la variable global rocket_y    
rocket_y -= 1 # Mover el cohete    
image(rocket, width/2, rocket_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

Llama a tu nuevo `draw_rocket()` en la función `draw()` para que el cohete se vuelva a dibujar en cada cuadro.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 33
line_highlights: 36
---

def draw():   
# Cosas que hacer en cada cuadro   
draw_background()   
draw_rocket()


--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu código para verificar que el cohete comience en la parte inferior de la pantalla y suba en cada cuadro.

![Animación del cohete volando hasta la mitad de la pantalla.](images/rocket_fly.gif)

--- /task ---

--- save ---
