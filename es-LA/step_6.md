## Alcanzando la órbita

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

El objetivo de lanzar el cohete es impulsar un satélite a la órbita. 

Una órbita es una trayectoria curva que un objeto toma alrededor de otro debido a la gravedad.

El cohete puede cambiar de color para mostrar el éxito del lanzamiento. 

</div>
<div>

![Tres imágenes una al lado de la otra que muestran lanzamientos exitosos (tinte verde), con exceso de combustible (tinte ámbar) y fallidos (tinte rojo).](images/check_orbit.png){:width="400px"}

</div>
</div>

--- task ---

Crea dos nuevas variables globales para establecer el radio del círculo de la órbita y la coordenada `y` de la órbita hasta el punto al que debe llegar el centro del cohete para lanzar el satélite.

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 7
line_highlights: 11-12
---

#Configurar variables globales
tamano_pantalla = 400   
cohete_y = tamano_pantalla   
quemar = 100   
orbita_radio = 250   
orbita_y = tamano_pantalla - orbita_radio

--- /code ---

--- /task ---

--- task ---

Actualiza la función `dibujar_fondo()` para dibujar una elipse que represente la órbita del satélite que el cohete debe alcanzar.

--- code ---
---
language: python 
filename: main.py - dibujar_fondo() 
line_numbers: true 
line_number_start: 37
line_highlights: 42-45
---

def dibujar_fondo():   
  fondo(0) #Abreviatura de fondo(0, 0, 0) — negro   
  image(planeta, width/2, height, 300, 300)

  no_fill() #Desactivar cualquier relleno  
  stroke(255) #Establecer un trazo blanco   
  stroke_weight(2)   
  ellipse(width/2, height, orbita_radio * 2, orbita_radio * 2)

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu programa y verifica que se dibuje una línea de órbita blanca.

![La pantalla con el planeta y la nueva línea de órbita.](images/draw_orbit.png){:width="300px"}

--- /task ---

El cohete debe detenerse cuando alcance la órbita del satélite: el final de la misión.

--- task ---

Actualiza tu código `if combustible >= quemar` para verificar también que el cohete no haya alcanzado la órbita.

Puedes usar un `and` en declaraciones `if` para verificar si dos o más condiciones son verdaderas.

--- code ---
---
language: python 
filename: main.py - dibujar_cohete() 
line_numbers: true 
line_number_start: 14
line_highlights: 19
---

#La función dibujar_cohete va aquí
def dibujar_cohete():

  global cohete_y, combustible, quemar

    if combustible >= quemar and cohete_y > orbita_y: #Sigue volando

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu proyecto e ingresa `50000` como la cantidad de combustible. Esto debería ser suficiente combustible para alcanzar la órbita. El cohete debería dejar de moverse cuando alcance la órbita.

--- /task ---

El cohete debería tornarse color rojo si se queda sin combustible antes de alcanzar la altura suficiente para lanzar el satélite.

--- task ---

--- code ---
---
language: python 
filename: main.py — dibujar_cohete() 
line_numbers: true 
line_number_start: 30
line_highlights: 34-35
---

    fill(200, 200, 200, 100)   
    for i in range(20):   
      ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

  if combustible < quemar and cohete_y > orbita_y: #No más combustible y no en órbita 
    tint(255, 0, 0) #Fallo

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu código e ingresa `20000` como la cantidad de combustible. Comprueba que el cohete se vuelve rojo cuando se detiene por debajo de la órbita.

![Un cohete rojo que se ha quedado sin combustible antes del círculo de la órbita. El planeta también se ha vuelto rojo.](images/orbit_failure.png){:width="300px"}

¡Oh no, el planeta se ha vuelto rojo!

--- /task ---

--- task ---

La función `tint()` establece el color de tinte para todas las imágenes que se dibujan hasta que cambie el tinte o use `no_tint()` para apagarlo.

**Elige:** Agrega una llamada a `no_tint()` después de dibujar la imagen para que el planeta no se tiña de rojo en el siguiente cuadro, ¡o déjalo si deseas que el planeta se vuelva rojo!

--- code ---
---
language: python 
filename: main.py - dibujar_cohete() 
line_numbers: true 
line_number_start: 34
line_highlights: 38
---

if combustible < quemar and cohete_y > orbita_y: 
  tint(255, 0, 0) #Fallo

image(cohete, width/2, cohete_y, 64, 64)   
no_tint() #¡Así que el planeta no está teñido de rojo en el siguiente cuadro!


--- /code ---

--- /task ---

--- task ---

Usa la función `tint()` nuevamente, esta vez para colorear el cohete de verde si el cohete tiene suficiente combustible para alcanzar la órbita del satélite:

--- code ---
---
language: python 
filename: main.py - dibujar_cohete() 
line_numbers: true 
line_number_start: 34
line_highlights: 36-37
---

if combustible < quemar and cohete_y > orbita_y: 
  tint(255, 0, 0) #Fallo   
elif cohete_y <= orbita_y:   
  tint(0, 255, 0) #Exitoso

image(cohete, width/2, cohete_y, 64, 64)   
no_tint()

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu proyecto e ingresa `50000` como la cantidad de combustible. Comprueba que tu cohete se vuelve verde cuando alcanza la órbita del satélite.

![Un cohete verde que ha alcanzado el círculo orbital y le queda combustible.](images/orbit_success.png){:width="300px"}

--- /task ---

Ahora tienes una simulación que puede usarse para mostrar cuánto combustible se necesita como mínimo para alcanzar la órbita del satélite. Genial; sin embargo, podrías tomar una gran cantidad de combustible y aún así tener éxito, ¡pero esto es costoso y resulta en un desperdicio!

--- task ---

Modifica las condiciones en tu código de éxito para que el cohete solo se vuelva verde si alcanza la órbita `y` le quedan menos de 1,000 kg de combustible.

Agrega un código para colorear el cohete de amarillo si al cohete le quedan más de 1000 kg de combustible cuando alcanza la órbita.

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 34
line_highlights: 36, 38-39
---

if combustible < quemar and cohete_y > orbita_y: 
  tint(255, 0, 0) #Fallo   
elif combustible < 1000 and cohete_y <= orbita_y:   
  tint(0, 255, 0) #Exitoso   
elif combustible >= 1000 and cohete_y <= orbita_y:    
  tint(255, 200, 0) #Demasiado combustible

image(cohete, width/2, cohete_y, 64, 64)    
no_tint() #¡De esta manera el planeta no está teñido de rojo en el siguiente cuadro!

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu programa varias veces con diferentes números; por ejemplo, 25.000 kg de combustible debería ser la cantidad necesaria para que el cohete se vuelva verde, pero también verifica que el tinte amarillo funcione usando un número mayor.

![Un cohete amarillo que ha llegado al círculo de la órbita y le queda combustible.](images/orbit_meh.png){:width="300px"}

--- /task ---

--- save ---
