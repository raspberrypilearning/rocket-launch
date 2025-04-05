## Gosod yr olygfa

--- task ---

Agorwch [dempled y prosiect](https://trinket.io/python/58565016a2){:target="_blank"}.

--- /task ---

First, you will create a black background to represent space.

--- task ---

Define a `draw_background()` function, and set the background colour to black.

--- code ---
---
Dewch o hyd i'r sylw `Gosod newidynnau cyffredinol` ac ychwanegu llinell o god i greu eich newidyn `maint_sgrin`:
line_highlights: 8
---

# Mae'r swyddogaeth llunio_cefndir yn mynd fan hyn
def draw_background():   
background(0, 0, 0)

--- /code ---

--- /task ---

--- task ---

Add this function to the list of things to `draw()` in every frame.

--- code ---
---
Defnyddiwch y newidyn `maint_sgrin` i greu sgwâr 400 wrth 400 picsel:
line_highlights: 20
---

def draw(): # Things to do in every frame draw_background()

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and you should see a black square.

--- /task ---



--- task ---

**Dewiswch:** Penderfynwch pa ddelwedd rydych chi am ei defnyddio a gwneud nodyn o enw'r ffeil. Er enghraifft, `orange_planet.png`.

--- code ---
---
**Dewiswch:** Penderfynwch pa ddelwedd rydych chi am ei defnyddio a gwneud nodyn o enw'r ffeil. Er enghraifft, `orange_planet.png`.
line_highlights: 21-23
---
def draw_background():  
background(0,0,0) image(planet, screen_size/2, screen_size, 300, 300)

--- /code ---


Hefyd, ychwanegwch god at y swyddogaeth `setup()` i lwytho'r ddelwedd o'ch dewis i newidyn cyffredinol `planed`. Rhaid i'r newidyn fod yn un cyffredinol er mwyn i chi allu ei ddefnyddio nes ymlaen wrth lunio'r blaned ar y sgrin.

- image filename - we have already loaded the planet image
- x coordinate - we have already set the screen size
- y coordinate
- image width
- image height

--- /task ---

--- task ---

def setup():   
#Gosodwch eich animeiddiad yma   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planed   
planed = load_image('planet.png') #Y blaned o'ch dewis

![A planet against a black background.](images/step_2.png){:width="300px"}

--- /task ---

### A different planet?

--- task ---

Diffiniwch swyddogaeth `llunio_cefndir()` i lunio'r cefndir o dan y sylw sy'n dweud wrthych chi ble dylai fynd.

![Choose a different planet](images/image_gallery.png)

If you want to change the planet image, change `planet.png` in the code to the filename of your chosen planet, for example, `orange_planet.png`.

--- code ---
---
Defnyddiwch `background(0)` i osod lliw'r cefndir i ddu ac ychwanegu swyddogaeth `image()` i lunio'r blaned. Mae'r swyddogaeth `image()` wedi'i gosod fel:
line_highlights: 15-17
---
def setup(): # Set up your animation here size(screen_size, screen_size) image_mode(CENTER) global planet planet = load_image('planet.png')

--- /code ---

--- /task ---

