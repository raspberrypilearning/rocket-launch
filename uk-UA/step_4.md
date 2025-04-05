## Ефекти вихлопних газів

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Додай кілька сірих кіл, які будуть створювати вихлопний слід. 
</div>
<div>

![Повільна анімація ефекту диму.](images/rocket_smoke.gif)
</div>
</div>

--- task ---

Встанови колір заливки диму на прозоро-сірий.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 14
---

def draw_rocket(): global rocket_position rocket_position = rocket_position - 1 image(rocket, width/2, rocket_position, 64, 64) fill(200, 200, 200, 100)

--- /code ---

--- /task ---


--- task ---

Функція **stroke** керує контуром кіл. За допомогою рядка коду можна вимкнути контур.


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

Згенеруй випадкове число від 5 до 10 для розміру кола, а потім намалюй його внизу ракети.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 16-22
---

no_stroke() circle_size = randint(5,10) ellipse( screen_size/2, rocket_position, circle_size, circle_size )

--- /code ---

--- /task ---

--- task ---

**Протестуй:** запусти свою програму. Ти маєш побачити сіре коло внизу ракети.

--- /task ---

--- task ---

Зроби відступ у коді, яким ти малюєш коло, і додай цикл, який запускатиме код 20 разів.

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

**Протестуй:** запусти свою програму. Ти все одно побачиш миготливе сіре коло у нижній частині ракети – усі кола намалювались одне на одному!

--- /task ---

--- task ---

Згенеруй випадкове число і додай його до положень x і y кожного кола, щоб вони не малювалися в одному місці.


--- code ---
---
language: python line_numbers: true line_number_start: 24
line_highlights: 25-26
---

ellipse( screen_size/2 + randint(-5,5), rocket_position + randint(20,50), circle_size, circle_size )

--- /code ---

--- /task ---


--- task ---

**Протестуй:** запусти свою програму. Ти маєш побачити багато сірих кіл у випадкових місцях внизу ракети.

--- /task ---

