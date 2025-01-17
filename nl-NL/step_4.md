## Uitlaat effecten

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Add some grey circles to simulate the exhaust trail. 
</div>
<div>

Een langzame animatie van het rookeffect.
</div>
</div>

--- task --- Set the fill colour for the smoke to transparent grey.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 14
---

def teken_raket(): global raket_y   
raket_y -= 1


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

**Test:** Voer je programma uit en controleer of de uitlaatgassen zichtbaar zijn.

--- /task ---

--- task ---

Indent the code you used to draw the circle, and add a loop which will run the code 20 times.

--- code ---
---
Verander de aanroep in `fill()` om de hoeveelheid groen in te stellen op `255 - i*10` zodat de eerste ellips evenveel rood en groen heeft en de laatste ellips heel weinig groen.
line_highlights: 16-23
---

no_stroke() # Schakel de lijn uit for i in range(25): # Teken 25 brandende uitlaatellipsen fill(255, 255, 0) # Geel ellipse(width/2, raket_y + i, 8, 3) # i neemt toe elke keer dat de lus wordt herhaald image(raket, width/2, raket_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit om te controleren of de raket een nieuw uitlaatspoor heeft. You will still see a flashing grey circle at the bottom of the rocket - all of the circles have been drawn on top of each other!

--- /task ---

--- task --- Generate a random number and add it to the x and y position of each circle so they aren't all drawn in the same place.


--- code ---
---
for i in range(25): fill(255, 255 - i * 10, 0) # Verminder de hoeveelheid groen ellipse(width/2, raket_y + i, 8, 3)
line_highlights: 25-26
---

for i in range(25): fill(255, 255 - i * 10, 0) ellipse(width/2, raket_y + i, 8, 3) fill(200, 200, 200, 100) # Transparant grijs for i in range(20): # Teken 20 willekeurige rookellipsen ellipse(width/2 + randint(-5, 5), raket_y + randint(20, 50), randint(5, 10), randint(5, 10)) image(raket, width/2, raket_y, 64, 64)

--- /code ---

--- /task ---




--- task --- **Test:** Run your program and you should see lots of grey circles in random places at the bottom of the rocket. --- /task ---