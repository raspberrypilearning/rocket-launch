## Effets d'échappement

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Add some grey circles to simulate the exhaust trail. 
</div>
<div>

Une animation lente de l'effet de fumée.
</div>
</div>

--- task --- Set the fill colour for the smoke to transparent grey.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 14
---

def draw_rocket(): global rocket_position rocket_position = rocket_position - 1 image(rocket, width/2, rocket_position, 64, 64) fill(200, 200, 200, 100)


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

**Test :** exécute ton programme et vérifie que les gaz d'échappement sont visibles.

--- /task ---

--- task ---

Indent the code you used to draw the circle, and add a loop which will run the code 20 times.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 12
line_highlights: 16-23
---

def draw_rocket(): global rocket_position rocket_position = rocket_position - 1 image(rocket, width/2, rocket_position, 64, 64) fill(200, 200, 200, 100) no_stroke() for i in range(20): circle_size = randint(5,10) ellipse( screen_size/2, rocket_position, circle_size,    
circle_size )


--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton code pour vérifier que la fusée a une nouvelle traînée d'échappement. You will still see a flashing grey circle at the bottom of the rocket - all of the circles have been drawn on top of each other!

--- /task ---

--- task --- Generate a random number and add it to the x and y position of each circle so they aren't all drawn in the same place.


--- code ---
---
for i in range(25): fill(255, 255 - i * 10, 0) # Réduis la quantité de vert ellipse(width/2, fusee_y + i, 8, 3)
line_highlights: 25-26
---

for i in range(25): fill(255, 255 - i * 10, 0) ellipse(width/2, fusee_y + i, 8, 3) fill(200, 200, 200, 100)  # Gris transparent for i in range(20):  # Dessine 20 ellipses de fumée ellipse(width/2 + randint(-5, 5), fusee_y + randint(20, 50), randint(5, 10), randint(5, 10)) image(fusee, width/2, fusee_y, 64, 64)

--- /code ---

--- /task ---




--- task --- **Test:** Run your program and you should see lots of grey circles in random places at the bottom of the rocket. --- /task ---