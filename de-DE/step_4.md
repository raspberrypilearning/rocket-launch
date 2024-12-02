## Abgaseffekte

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Add some grey circles to simulate the exhaust trail. 
</div>
<div>

Eine langsame Animation des Raucheffekts.
</div>
</div>

--- task --- Set the fill colour for the smoke to transparent grey.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 14
---

def zeichne_rakete(): global rakete_y   
rakete_y -= 1


--- /code ---

--- /task ---


--- task --- The outline around the circles is called the **stroke**. Add some code to turn it off.


--- code ---
---
language: python line_numbers: true line_number_start: 14
line_highlights: 15
---

    fill(200, 200, 200, 100) 
    no_stroke()


--- /code ---

--- /task ---


--- task ---

Generate a random number between 5 and 10 for the size of the circle, then draw it at the bottom of the rocket.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 16-22
---

no_stroke() circle_size = randint(5,10) ellipse( screen_size/2, rocket_position, circle_size, circle_size )

--- /code ---

--- /task ---

--- task ---

**Test:** Führe dein Programm aus und prüfe, ob die Abgase sichtbar sind.

--- /task ---

--- task ---

Indent the code you used to draw the circle, and add a loop which will run the code 20 times.

--- code ---
---
Ändere den Aufruf in `fill()`, um den Grünanteil auf `255 - i * 10` festzulegen, sodass die erste Ellipse gleiche Mengen Rot und Grün aufweist und die letzte Ellipse sehr wenig Grün.
line_highlights: 16-23
---

no_stroke() # Schaltet Zeichnen aus for i in range(25): # Zeichne 25 brennende Abgasellipsen fill(255, 255, 0) # Gelb ellipse(width/2, rakete_y + i, 8, 3) # i erhöht sich bei jeder Wiederholung der Schleife image(rakete, width/2, rakete_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

**Test:** Führe deinen Code aus, um zu überprüfen, ob die Rakete eine neue Abgasspur hat. You will still see a flashing grey circle at the bottom of the rocket - all of the circles have been drawn on top of each other!

--- /task ---

--- task --- Generate a random number and add it to the x and y position of each circle so they aren't all drawn in the same place.


--- code ---
---
for i in range(25): fill(255, 255 - i * 10, 0)  # Grünanteil reduzieren ellipse(width/2, rakete_y + i, 8, 3)
line_highlights: 25-26
---

for i in range(25): fill(255, 255 - i * 10, 0) ellipse(width/2, rakete_y + i, 8, 3) fill(200, 200, 200, 100)  # Transparent grau for i in range(20):  # Zeichne 20 zufällige Rauchellipsen ellipse(width/2 + randint(-5, 5), rakete_y + randint(20, 50), randint(5, 10), randint(5, 10)) image(rakete, width/2, rakete_y, 64, 64)

--- /code ---

--- /task ---




--- task --- **Test:** Run your program and you should see lots of grey circles in random places at the bottom of the rocket. --- /task ---