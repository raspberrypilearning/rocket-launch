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

Abre la [plantilla de proyecto](https://trinket.io/python/f2199f5a8c){:target="_blank"}.

Si tienes una cuenta Trinket, puede hacer clic en el botón **Remix** para guardar una copia en tu biblioteca `My Trinkets`.

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
tamano_pantalla = 400

--- /code ---

--- /task ---

--- task ---

Usa la variable `tamano_pantalla` para crear un cuadrado de 400 por 400 píxeles:

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 20
---

def setup():   
#Configura tu animación aquí   
tamano(tamano_pantalla, tamano_pantalla)


--- /code ---

--- /task ---

--- task ---

El proyecto de inicio tiene tres imágenes de planetas diferentes y la luna proporcionadas para tí. Puedes verlos en la biblioteca de imágenes de Trinket seleccionando el botón **View and Add Images**.

![Un símbolo de más, un símbolo de carga y un símbolo de imagen. El símbolo de la imagen está resaltado.](images/trinket_image.png)

**Elige:** Decide qué imagen deseas utilizar y toma nota del nombre del archivo. Por ejemplo, `planet.png`.

--- /task ---

Es una buena idea cargar imágenes en `setup()` para que estén listas cuando necesites usarlas y su animación se ejecute rápidamente.

--- task ---

La línea `image_mode(CENTER)` dice que colocarás las imágenes dando las coordenadas del centro de la imagen (en lugar de la esquina superior izquierda).

También agrega código a la función `setup()` para cargar tu imagen elegida en una variable global `planeta`. La variable debe ser global para que puedas usarla más tarde cuando dibujes el planeta en la pantalla.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 21-23
---

def setup():   
#Configura tu animación aquí   
tamano(tamano_pantalla, tamano_pantalla)   
image_mode(CENTER)   
global planeta   
planeta = load_image('planet.png') #Tu planeta elegido


--- /code ---

--- /task ---

--- task ---

Define una función `draw_background()` para dibujar el fondo, debajo del comentario que te indica dónde debe ir.

Usa `background(0)` para establecer el color de fondo en negro y agrega una función `image()` para dibujar el planeta. La función `image()` se presenta:

`image(image filename, x-coordinate, y-coordinate, image_width, image_height)`

La biblioteca `p5` establece variables globales `width` y `height` según el tamaño de la pantalla. Úsalos en tu código para colocar el planeta con su centro en la mitad (`width/2`) y en la parte inferior (`height`) de la pantalla.

--- code ---
---
language: python filename: main.py — draw_background() line_numbers: true line_number_start: 14
line_highlights: 15-17
---

# La función dibujar_fondo va aquí
def dibujar_fondo():   
fondo(0) #Abreviatura de fondo(0, 0, 0) — negro    
imagen(planeta, width/2, height, 300, 300) #Dibuja la imagen


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

def dibujar():   
#Cosas que hacer en cada cuadro    
dibujar_fondo()

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu código y comprueba que dibuje un fondo negro con medio planeta en la parte inferior.

--- /task ---

--- save ---
