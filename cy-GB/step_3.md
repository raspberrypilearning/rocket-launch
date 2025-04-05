## Ffwrdd â ni!

Mae'r prosiect dechreuol wedi darparu delwedd o roced i chi.

![Delwedd o'r roced yn llyfrgell ddelweddau Trinket.](images/rocket_image.png)

--- task ---

Add code to the `setup()` function to load the rocket image into a `rocket` global variable.

<div class="c-project-code">

--- code ---
---
Ychwanegwch god at y swyddogaeth `setup()` i lwytho'r ddelwedd o roced i newidyn `roced` cyffredinol.
line_highlights: 24, 26
---

def setup():   
# Set up your animation here   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet, rocket   
planet = load_image('planet.png')    
rocket = load_image('rocket.png')

--- /code ---

--- /task ---

--- task ---

Bydd safle `y` y roced yn dechrau ar 400 (uchder y sgrin) ac yn lleihau 1 bob tro mae ffrâm newydd yn cael ei llunio.

--- code ---
---
Bydd safle `y` y roced yn dechrau ar 400 (uchder y sgrin) ac yn lleihau 1 bob tro mae ffrâm newydd yn cael ei llunio.
line_highlights: 9
---

# Gosod newidynnau cyffredinol
screen_size = 400    
rocket_position = screen_size

--- /code ---

--- /task ---


Bydd safle `y` y roced yn dechrau ar 400 (uchder y sgrin) ac yn lleihau 1 bob tro mae ffrâm newydd yn cael ei llunio.

--- task ---

Define a `draw_rocket()` function to make the rocket appear on the screen.

--- code ---
---
language: python line_numbers: true line_number_start: 9
line_highlights: 12-16
---

# Mae'r swyddogaeth llunio_roced yn mynd fan hyn
Diffiniwch swyddogaeth `llunio_roced()` i newid safle `y` y roced a'i hail-lunio.


--- /code ---

--- /task ---

--- task ---

def llunio_roced():

--- code ---
---
language: python line_numbers: true line_number_start: 29
line_highlights: 37
---

def draw(): # Things to do in every frame draw_background() draw_rocket()


--- /code ---

--- /task ---

--- task ---

language: python filename: main.py line_numbers: true line_number_start: 34

--- /task ---


Each time a new frame is drawn, you need to move the rocket one pixel up the screen to create an animation effect.


--- task ---

The `rocket_position` of the rocket will start at 400 (the screen height) and then decrease by 1 each time a new frame is drawn.


--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 12
---

def draw_rocket():   
global rocket_position     
rocket_position = rocket_position - 1    
image(rocket, width/2, rocket_position, 64, 64)

--- /code ---

--- /task ---


--- task ---

**Test:** Run your code to check that the rocket blasts off from the bottom of the screen.


![A rocket flying at a steady speed from the bottom to the top of the screen.](images/fly.gif){:width="300px"}

--- /task ---

