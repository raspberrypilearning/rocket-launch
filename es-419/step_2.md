## Dibuja el fondo

--- task ---

Abre el [proyecto básico](https://editor.raspberrypi.org/en/projects/rocket-launch-starter){:target="_blank"}.

--- /task ---

Primero, crearás un fondo negro para representar el espacio.

--- task --- Define una función `dibujar_fondo()` y establece el color de fondo en negro.

--- code ---
---
language: python line_numbers: true line_number_start: 12
line_highlights: 13-14
---

# La función dibujar_fondo va aquí
def dibujar_fondo():   
background(0, 0, 0)

--- /code ---

--- /task ---

--- task ---

Añade esta función a la lista de cosas para `dibujar ()` en cada cuadro.

--- code ---
---
language: python line_numbers: true line_number_start: 25
line_highlights: 27
---

def dibujar(): #Cosas que hacer en cada cuadro dibujar_fondo()

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu código y deberías ver un cuadrado negro. --- /task ---



--- task ---

Añade una línea de código para mostrar una imagen de un planeta.

--- code ---
---
language: python line_numbers: true line_number_start: 13
line_highlights: 15-16
---
def dibujar_fondo():  
background(0,0,0) image(planet, screen_size/2, screen_size, 300, 300) --- /code ---

La función `image()` necesita los siguientes datos:

- nombre de archivo de la imagen: ya hemos cargado la imagen del planeta
- coordenada x: ya hemos establecido el tamaño de la pantalla
- coordenada y
- ancho de la imagen
- altura de la imagen

--- /task ---

--- task ---

**Prueba:** Ejecuta tu código y comprueba que dibuje un fondo negro con medio planeta en la parte inferior.

![Un planeta sobre un fondo negro.](images/step_2.png){:width="300px"}

--- /task ---

### ¿Un planeta diferente?

--- task ---

Haz clic en el icono de la imagen a la izquierda para ver la galería de imágenes.

![Elige un planeta diferente](images/image_gallery.png)

Si quieres cambiar la imagen del planeta, cambia `planet.png` en el código por el nombre de archivo del planeta elegido, por ejemplo, `orange_planet.png`.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 22
---
def setup(): #Configura tu animación aquí tamano(tamano_pantalla, tamano_pantalla) image_mode(CENTER) global planeta planeta = load_image('planet.png') #Tu planeta elegido

--- /task ---

