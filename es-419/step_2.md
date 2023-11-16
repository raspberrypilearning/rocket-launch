## Establece la escena

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
La animación necesita un fondo espacial con un planeta desde el cual lanzar el cohete.
</div>
<div>

![Un planeta contra un fondo negro.](images/step_2.png){:width="300px"}

</div>
</div>

--- task ---

Abre la [plantilla de proyecto](https://editor.raspberrypi.org/en/projects/rocket-launch-starter){:target="_blank"}.

### Crea la pantalla

--- /task ---

Utilizarás una variable `screen_size` para establecer el tamaño de la pantalla y en los cálculos. Las variables definidas fuera de las funciones son **globales**, por lo que puedes usarlas en cualquier parte de tu programa.

--- task ---

Busca el comentario `Configurar variables globales` y agrega una línea de código para crear tu variable `screen_size`:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# Configurar variables globales
screen_size = 400

--- /code ---

--- /task ---

--- task ---

Usa la variable `screen_size` para crear un cuadrado de 400 por 400 píxeles:

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 20
---

def setup():   
#Configura tu animación aquí   
size(screen_size, screen_size)


--- /code ---

--- /task ---

### Elige una imagen

--- task ---

El proyecto de inicio te proporciona tres imágenes diferentes de planetas y la luna. Puedes verlos en la **Galería de imágenes** en el lado izquierdo del editor de código.

![Una captura de pantalla del editor de código, con la galería de imágenes conteniendo imágenes de planetas y la luna resaltada.](images/image_gallery.png)

**Elige:** Decide qué imagen deseas utilizar y toma nota del nombre del archivo. Por ejemplo, `orange_planet.png`.

--- /task ---

--- task ---

Agrega código a la función `setup()` para cargar y posicionar tu imagen.

La línea `image_mode(CENTER)` dice que posicionará las imágenes dando las coordenadas del centro de la imagen (en lugar de la esquina superior izquierda).

Luego carga tu imagen en una variable global `planeta`. La variable debe ser global para que puedas usarla más tarde cuando dibujes el planeta en la pantalla.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 21-23
---

def setup():   
# Configura tu animación aquí   
size(screen_size, screen_size)   
image_mode(CENTER) # Coloca la imagen en el centro global planet   
planet = load_image('planet.png') # El planeta que elegiste


--- /code ---

--- /task ---

### Dibujar fondo

--- task ---

Define una función `draw_background()` para dibujar el fondo, debajo del comentario que te indica dónde debe ir.

Usa `background(0)` para establecer el color de fondo en negro y agrega la función `image()` para dibujar el planeta. La función `image()` es asi:

`image(image filename, x-coordinate, y-coordinate, image_width, image_height)`

La línea de código `from p5 import *` te proporciona variables globales `width` (ancho) y `height` (largo) según el tamaño de la pantalla. Úsalos en tu código para colocar el planeta con su centro en la mitad (`width/2`) y en la parte inferior (`height`) de la pantalla.

--- code ---
---
language: python filename: main.py — draw_background() line_numbers: true line_number_start: 14
line_highlights: 15-17
---

# La función dibujar_fondo va aquí
def draw_background():   
background(0)  # Abreviatura de background(0, 0, 0) — black    
image(planet, width/2, height, 300, 300)  # Dibuja la imagen


--- /code ---

Poner todo el código para dibujar el fondo en una sola función hace que tu código sea más fácil de entender.

--- /task ---

--- task ---

Para que aparezca el fondo, llama a `draw_background()` en `draw()`. Esto hará que el fondo se vuelva a dibujar cada vez que se llame a `draw()`, cubriendo cualquier dibujo anterior:

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 28
line_highlights: 30
---

def draw():   
# Cosas que hacer en cada cuadro    
draw_background()

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu código y comprueba que dibuje un fondo negro con medio planeta en la parte inferior.

--- /task ---

Si tienes una cuenta Raspberry Pi, en tu editor de código puedes hacer clic en el botón **Guardar** para guardar una copia detsu proyecto en Proyectos.

--- save ---
