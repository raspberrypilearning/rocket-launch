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

Mae gan y prosiect dechreuol dair delwedd wahanol o blaned a'r lleuad wedi'u llunio'n barod i chi. Fe allwch chi weld y rhain yn llyfrgell ddelweddau Trinket drwy ddewis y botwm **View and Add Images**.

--- code ---
---
**Dewiswch:** Penderfynwch pa ddelwedd rydych chi am ei defnyddio a gwneud nodyn o enw'r ffeil. Er enghraifft, `orange_planet.png`.
line_highlights: 21-23
---
def draw_background():  
background(0,0,0) image(planet, screen_size/2, screen_size, 300, 300)

--- /code ---


Mae'n syniad da llwytho delweddau yn `setup()` fel eu bod yn barod pan fyddwch chi angen eu defnyddio a bydd eich animeiddiad yn rhedeg yn gyflym.

- image filename - we have already loaded the planet image
- x coordinate - we have already set the screen size
- y coordinate
- image width
- image height

--- /task ---

--- task ---

Hefyd, ychwanegwch god at y swyddogaeth `setup()` i lwytho'r ddelwedd o'ch dewis i newidyn cyffredinol `planed`. Rhaid i'r newidyn fod yn un cyffredinol er mwyn i chi allu ei ddefnyddio nes ymlaen wrth lunio'r blaned ar y sgrin.

![A planet against a black background.](images/step_2.png){:width="300px"}

--- /task ---

### A different planet?

--- task ---

Click on the image icon to the left to view the image gallery.

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

