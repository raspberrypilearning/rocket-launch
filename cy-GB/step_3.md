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

![Delwedd o'r roced yn llyfrgell ddelweddau Trinket.](images/trinket_rocket_image.png)

--- /task ---

--- task ---

Ychwanegwch god at y swyddogaeth `setup()` i lwytho'r ddelwedd o roced i newidyn `roced` cyffredinol.

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 20
line_highlights: 24, 26
---

def setup():   
  #Gosodwch eich animeiddiad yma   
  size(screen_size, screen_size)   
  image_mode(CENTER)   
  global planed, roced   
  planed = load_image('planet.png')    
  roced = load_image('rocket.png')

--- /code ---

--- /task ---

Bydd safle `y` y roced yn dechrau ar 400 (uchder y sgrin) ac yn lleihau 1 bob tro mae ffrâm newydd yn cael ei llunio.

--- task ---

Ychwanegwch newidyn `roced_y` cyffredinol i gadw golwg ar safle `y` y roced.

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 7
line_highlights: 9
---

#Gosod newidynnau cyffredinol
screen_size = 400    
roced_y = screen_size #Dechrau ar y gwaelod

--- /code ---

--- /task ---

--- task ---

Diffiniwch swyddogaeth `llunio_roced()` i newid safle `y` y roced a'i hail-lunio.

Mae `rocket_y -= 1` yn ffordd fyrrach o ddweud `rocket_y = rocket_y - 1`.

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 11
line_highlights: 12-16
---

#Mae'r swyddogaeth llunio_roced yn mynd fan hyn
def llunio_roced():

  global roced_y #Defnyddio'r newidyn roced_y cyffredinol    
  roced_y -= 1 #Symud y roced    
  image(roced, width/2, roced_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

Galwch eich swyddogaeth `llunio_roced()` newydd yn y swyddogaeth `draw()` i ail-lunio'r roced bob ffrâm.

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 34
line_highlights: 37
---

def draw():   
  #Pethau i'w gwneud ym mhob ffrâm   
  llunio_cefndir()   
  llunio_roced()


--- /code ---

--- /task ---

--- task ---  

**Profi:** Rhedwch eich cod i wneud yn siŵr bod y roced yn dechrau ar waelod y sgrin ac yn symud i fyny bob ffrâm.

![Delwedd o'r roced hanner ffordd i fyny'r sgrin.](images/trinket_rocket_fly.gif)

--- /task ---

--- save ---
