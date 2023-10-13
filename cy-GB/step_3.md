## Ffwrdd â ni!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Bob tro mae ffrâm newydd yn cael ei llunio, mae angen i'r roced symud i fyny'r sgrin i greu effaith animeiddio.
</div>
<div>

![Roced yn hedfan ar gyflymder cyson o waelod y sgrin i'r brig.](images/fly.gif){:width="300px"}

</div>
</div>

--- task ---

Mae'r prosiect dechreuol wedi darparu delwedd o roced i chi.

![Image of the rocket in the code editor image gallery.](images/rocket_image.png)

--- /task ---

--- task ---

Ychwanegwch god at y swyddogaeth `setup()` i lwytho'r ddelwedd o roced i newidyn `roced` cyffredinol.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 24, 26
---

def setup():   
# Setup your animation here   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet, rocket   
planet = load_image('planet.png')    
rocket = load_image('rocket.png')

--- /code ---

--- /task ---

### Make the rocket fly

Bydd safle `y` y roced yn dechrau ar 400 (uchder y sgrin) ac yn lleihau 1 bob tro mae ffrâm newydd yn cael ei llunio.

--- task ---

Ychwanegwch newidyn `roced_y` cyffredinol i gadw golwg ar safle `y` y roced.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9
---

# Gosod newidynnau cyffredinol
screen_size = 400    
rocket_y = screen_size  # Start at the bottom

--- /code ---

--- /task ---

--- task ---

Diffiniwch swyddogaeth `llunio_roced()` i newid safle `y` y roced a'i hail-lunio.

Mae `rocket_y -= 1` yn ffordd fyrrach o ddweud `rocket_y = rocket_y - 1`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12-16
---

# Mae'r swyddogaeth llunio_roced yn mynd fan hyn
def draw_rocket():   
global rocket_y  # Use the global rocket_y variable    
rocket_y -= 1  # Move the rocket    
image(rocket, width/2, rocket_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

Call your new `draw_rocket()` in the `draw()` function so that the rocket gets redrawn every frame.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 33
line_highlights: 36
---

def draw():   
# Things to do in every frame   
draw_background()   
draw_rocket()


--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to check that the rocket starts at the bottom of the screen and moves up each frame.

![Animation of the rocket flying half way up the screen.](images/rocket_fly.gif)

--- /task ---

--- save ---
