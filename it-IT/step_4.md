## Effetto gas di scarico

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Add some grey circles to simulate the exhaust trail. 
</div>
<div>

Un'animazione lenta dell'effetto fumo.
</div>
</div>

--- task ---

Set the fill colour for the smoke to transparent grey.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 14
---

def draw_rocket(): global rocket_y   
rocket_y -= 1

--- /code ---

--- /task ---


--- task --- The outline around the circles is called the **stroke**. Add some code to turn it off.


--- task ---

--- code ---
---
language: python line_numbers: true line_number_start: 14
line_highlights: 15
---

    fill(200, 200, 200, 100) 
    no_stroke()


--- /code ---

--- task ---

Generate a random number between 5 and 10 for the size of the circle, then draw it at the bottom of the rocket.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 16-22
---

for i in range(25): fill(255, 255 - i * 10, 0)  # Riduce la quantità di verde ellipse(width/2, rocket_y + i, 8, 3)

--- /code ---

--- /task ---

--- task ---

**Test:** Esegui il programma e verifica che i fumi di scarico siano visibili.

--- /task ---

--- task ---

Indent the code you used to draw the circle, and add a loop which will run the code 20 times.

--- code ---
---
Cambia la chiamata della funzione `fill()` per impostare la quantità di verde al valore di `255 - i * 10` in modo che la prima ellisse abbia la stessa quantità di rosso e verde e l'ultima ellisse ha pochissimo verde.
line_highlights: 16-23
---

no_stroke()  # Fa in modo che non venga disegnata la linea for i in range(25):  # Disegna 25 ellissi di gas di scarico fill(255, 255, 0)  # Giallo ellipse(width/2, rocket_y + i, 8, 3)  # aumenta I ad ogni ciclo image(rocket, width/2, rocket_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

**Test:** Esegui il codice per verificare che il razzo abbia una nuova scia di scarico. You will still see a flashing grey circle at the bottom of the rocket - all of the circles have been drawn on top of each other!

--- /task ---

--- task ---

Generate a random number and add it to the x and y position of each circle so they aren't all drawn in the same place.


--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 18
line_highlights: 25-26
---

for i in range(25): fill(255, 255 - i * 10, 0) ellipse(width/2, rocket_y + i, 8, 3) fill(200, 200, 200, 100)  # Grigio trasparente for i in range(20):  # Disegna 20 ellissi di fumo ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10)) image(rocket, width/2, rocket_y, 64, 64)

--- /code ---

--- /task ---


--- task ---

**Test:** Run your program and you should see lots of grey circles in random places at the bottom of the rocket.

--- /task ---

