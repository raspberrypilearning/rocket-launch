## Efectos de escape

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Añade algunos círculos grises para simular el rastro del escape. 
</div>
<div>

![Una animación lenta del efecto humo.](images/rocket_smoke.gif)
</div>
</div>

--- task ---

Set the fill colour for the smoke to transparent grey.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 14
---

def dibujar_cohete(): posicion_cohete global posicion_cohete = posicion_cohete - 1 image(cohete, ancho/2, posicion_cohete, 64, 64) fill(200, 200, 200, 100)

--- /code ---

--- /task ---


--- task ---

The outline around the circles is called the **stroke**. Añade código para desactivarlo.


--- /task ---

--- code ---
---
language: python line_numbers: true line_number_start: 14
line_highlights: 15
---

    fill(200, 200, 200, 100) 
    no_stroke()


--- /code ---

--- task ---

Genera un número aleatorio entre 5 y 10 para el tamaño del círculo, luego dibújalo en la parte inferior del cohete.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 16-22
---

no_stroke() circle_size = randint(5,10) ellipse( screen_size/2, rocket_position, circle_size, circle_size )

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu programa y debería ver aparecer un círculo gris en la parte inferior del cohete.

--- /task ---

--- task ---

Sangra el código que usaste para dibujar el círculo y agrega un bucle que ejecutará el código 20 veces.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 16-23
---

def dibujar_cohete(): global posicion_cohete posicion_cohete = posicion_cohete - 1 image(cohete, width/2, posicion_cohete, 64, 64) fill(200, 200, 200, 100) no_stroke() for i in range(20): medida_circulo = randint(5,10) ellipse( medida_pantalla/2, rposicion_cohete, medida_circulo ,    
medida_circulo )


--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu programa. Todavía verás un círculo gris intermitente en la parte inferior del cohete: ¡todos los círculos se han dibujado uno encima del otro!

--- /task ---

--- task ---

Generate a random number and add it to the x and y position of each circle so they aren't all drawn in the same place.


--- code ---
---
language: python line_numbers: true line_number_start: 24
line_highlights: 25-26
---

ellipse( medida_pantalla/2 + randint(-5,5), posicion_cohete + randint(20,50), medida_circulo , medida_circulo )

--- /code ---

--- /task ---


--- task ---

**Test:** Run your program and you should see lots of grey circles in random places at the bottom of the rocket.

--- /task ---

