
--- question ---
---
legend: Pregunta 2 de 3
---

Un proyecto tiene este `setup` para cargar una imagen de planeta y decir que las imágenes deben colocarse en su centro:

--- code ---
---
language: python
---

def setup():   
  tamano(400, 400)   
  image_mode(CENTER)   
  global planeta   
  planeta = load_image ('planet.png')

--- /code ---

Las coordenadas comienzan desde (0, 0) en la esquina superior izquierda. En el proyecto, dibujaste imágenes de planetas y cohetes usando la función `image(nombre de archivo de imagen, coordenada x, coordenada y, ancho_imagen, altura_imagen)`.

¿Dónde colocará este código la imagen del planeta?

--- code ---
---
language: python
---

image(planet, 300, 100, 128, 128)

--- /code ---

--- choices ---

- ( ) ![Una imagen de planeta posicionada horizontalmente a la derecha de la pantalla y verticalmente en el medio.](images/planet400200.png)

  --- feedback ---

Las entradas segunda y tercera a la función `image()` son las coordenadas `x` y `y` para el centro de la imagen. Este planeta tiene las coordenadas `(400, 200)`.

  --- /feedback ---

- ( ) ![Una imagen del planeta colocada en el centro del cuadrante inferior izquierdo.](images/planet100300.png)

  --- feedback ---

Las entradas segunda y tercera a la función `image()` son las coordenadas `x` y `y` para el centro de la imagen. Este planeta tiene las coordenadas `(100, 300)`.

  --- /feedback ---

- (x) ![Una imagen del planeta colocada en el medio del cuadrante superior derecho.](images/planet300100.png)

  --- feedback ---

¡Correcto! Las entradas segunda y tercera a la función `image()` son las coordenadas `x` y `y` para el centro de la imagen. Esta imagen tiene las coordenadas (300, 100), por lo que tiene 300 (de 400) píxeles desde la izquierda para la coordenada `x` y 100 (de 400) píxeles hacia abajo desde la parte superior.

  --- /feedback ---

- () ![Una imagen de planeta posicionada en el cuadrante superior izquierdo.](images/planet128128.png)

  --- feedback ---

La cuarta y quinta entradas dan el tamaño de la imagen. La segunda y tercera entradas a la función `image()` son las coordenadas `x` y `y` para el centro de la imagen. Este planeta tiene las coordenadas `(128, 128)`.

  --- /feedback ---

--- /choices ---

--- /question ---
