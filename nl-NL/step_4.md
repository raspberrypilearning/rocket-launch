## Uitlaat effecten

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Voeg wat grijze cirkels toe om het uitlaatspoor te simuleren. 
</div>
<div>

![Een langzame animatie van het rookeffect.](images/rocket_smoke.gif)
</div>
</div>

--- task ---

Stel de opvulkleur voor de rook in op transparant grijs.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 14
---

def draw_rocket(): global rocket_position rocket_position = rocket_position - 1 image(rocket, width/2, rocket_position, 64, 64) fill(200, 200, 200, 100)

--- /code ---

--- /task ---


--- task ---

De omtrek rond de cirkels wordt de **stroke**genoemd. Voeg wat code toe om het uit te schakelen.


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

Genereer een willekeurig getal tussen 5 en 10 dat de grootte van de cirkel aangeeft en teken dit onderaan de raket.

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

Laat de code die je hebt gebruikt om de cirkel te tekenen inspringen, en voeg een lus toe die de code 20 keer uitvoert.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 16-23
---

def draw_rocket(): global rocket_position rocket_position = rocket_position - 1 image(rocket, width/2, rocket_position, 64, 64) fill(200, 200, 200, 100) no_stroke() for i in range(20): circle_size = randint(5,10) ellipse( screen_size/2, rocket_position, circle_size,    
circle_size )


--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit om te controleren of de raket een nieuw uitlaatspoor heeft. Je ziet nog steeds één knipperende grijze cirkel onderaan de raket - alle cirkels zijn boven op elkaar getekend!

--- /task ---

--- task ---

Genereer een willekeurig getal en voeg dit toe aan de x- en y-positie van elke cirkel, zodat ze niet allemaal op dezelfde plaats worden getekend.


--- code ---
---
language: python line_numbers: true line_number_start: 24
line_highlights: 25-26
---

ellipse( screen_size/2 + randint(-5,5), rocket_position + randint(20,50), circle_size, circle_size )

--- /code ---

--- /task ---


--- task ---

**Test:** Voer je programma uit, je zou nu op willekeurige plekken aan de onderkant van de raket een heleboel grijze cirkels moeten zien.

--- /task ---

