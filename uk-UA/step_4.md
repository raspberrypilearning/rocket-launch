## Ефекти вихлопних газів

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Add some grey circles to simulate the exhaust trail. 
</div>
<div>

![Ракета посередині шляху зі слідом вихлопних газів.](images/flying_rocket.gif){:width="300px"}
</div>
</div>

--- task ---

Намалювавши багато жовтих овалів у різних позиціях `y`, можна створити вихлопний слід із заокругленим кінцем.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 14
---

def draw_rocket(): global rocket_position rocket_position = rocket_position - 1 image(rocket, width/2, rocket_position, 64, 64) fill(200, 200, 200, 100)

--- /code ---

--- /task ---


--- task ---

The outline around the circles is called the **stroke**. Add some code to turn it off.


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

image(rocket, width/2, rocket_y, 64, 64)

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 16-22
---

no_stroke() circle_size = randint(5,10) ellipse( screen_size/2, rocket_position, circle_size, circle_size )

--- /code ---

--- /task ---

--- task ---

Зміни виклик функції `fill()`, встановивши кількість зеленого кольору на `255 - i*10` так, щоб у першому колі було однакова кількість червоного та зеленого кольорів, а в останньому - дуже мало зеленого.

--- /task ---

--- task ---

for i in range(25):   
fill(255, 255 - i * 10, 0) #Зменшити кількість зеленого кольору    
ellipse(width/2, rocket_y + i, 8, 3)

--- code ---
---
for i in range(25):   
fill(255, 255 - i * 10, 0) #Зменшити кількість зеленого кольору    
ellipse(width/2, rocket_y + i, 8, 3)
line_highlights: 16-23
---

def draw_rocket(): global rocket_position rocket_position = rocket_position - 1 image(rocket, width/2, rocket_position, 64, 64) fill(200, 200, 200, 100) no_stroke() for i in range(20): circle_size = randint(5,10) ellipse( screen_size/2, rocket_position, circle_size,    
circle_size )


--- /code ---

--- /task ---

--- task ---

**Test:** Run your program. You will still see a flashing grey circle at the bottom of the rocket - all of the circles have been drawn on top of each other!

--- /task ---

--- task ---

На кожному кадрі анімації буде намальовано 20 овалів випадкових розмірів на випадкових позиціях.


--- code ---
---
language: python line_numbers: true line_number_start: 24
line_highlights: 25-26
---

На кожному кадрі анімації буде намальовано 20 овалів випадкових розмірів на випадкових позиціях.

--- /code ---

--- /task ---


--- task ---

**Test:** Run your program and you should see lots of grey circles in random places at the bottom of the rocket.

--- /task ---

