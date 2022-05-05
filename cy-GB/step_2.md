## Gosod yr olygfa

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Mae'r animeiddiad angen cefndir gofod gyda phlaned i lansio'r roced ohoni.
</div>
<div>

![Planed yn erbyn cefndir du.](images/step_2.png){:width="300px"}

</div>
</div>

--- task ---

Agorwch [dempled y prosiect](https://trinket.io/python/f2199f5a8c){:target="_blank"}.

Os oes gennych chi gyfrif Trinket, fe allwch chi glicio'r botwm **Remix** i gadw copi yn eich llyfrgell `My Trinkets`.

--- /task ---

Byddwch chi'n defnyddio newidyn `maint_sgrin` i osod maint y sgrin ac mewn cyfrifiadau. Mae newidynnau sy'n cael eu diffinio tu allan i swyddogaethau yn rhai **cyffredinol (global)** felly gallwch chi eu defnyddio unrhyw le yn eich rhaglen.

--- task ---

Dewch o hyd i'r sylw `Gosod newidynnau cyffredinol` ac ychwanegu llinell o god i greu eich newidyn `maint_sgrin`:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# Gosod newidynnau cyffredinol
screen_size = 400

--- /code ---

--- /task ---

--- task ---

Defnyddiwch y newidyn `maint_sgrin` i greu sgwâr 400 wrth 400 picsel:

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 20
---

def setup():   
#Setup your animation here   
size(screen_size, screen_size)


--- /code ---

--- /task ---

--- task ---

Mae gan y prosiect dechreuol dair delwedd wahanol o blaned a'r lleuad wedi'u llunio'n barod i chi. Fe allwch chi weld y rhain yn llyfrgell ddelweddau Trinket drwy ddewis y botwm **View and Add Images**.

![Symbol plws, symbol llwytho i fyny, a symbol delwedd. Mae'r symbol ddelwedd wedi'i amlygu.](images/trinket_image.png)

**Dewiswch:** Penderfynwch pa ddelwedd rydych chi am ei defnyddio a gwneud nodyn o enw'r ffeil. Er enghraifft, `orange_planet.png`.

--- /task ---

Mae'n syniad da llwytho delweddau yn `setup()` fel eu bod yn barod pan fyddwch chi angen eu defnyddio a bydd eich animeiddiad yn rhedeg yn gyflym.

--- task ---

Mae'r llinell `image_mode(CENTER)` yn dweud byddwch chi'n lleoli delweddau drwy roi cyfesurynnau canol y ddelwedd (yn hytrach na'r gornel chwith uchaf).

Hefyd, ychwanegwch god at y swyddogaeth `setup()` i lwytho'r ddelwedd o'ch dewis i newidyn cyffredinol `planed`. Rhaid i'r newidyn fod yn un cyffredinol er mwyn i chi allu ei ddefnyddio nes ymlaen wrth lunio'r blaned ar y sgrin.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 21-23
---

def setup():   
#Setup your animation here   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet   
planet = load_image('planet.png') #Your chosen planet


--- /code ---

--- /task ---

--- task ---

Diffiniwch swyddogaeth `llunio_cefndir()` i lunio'r cefndir o dan y sylw sy'n dweud wrthych chi ble dylai fynd.

Defnyddiwch `background(0)` i osod lliw'r cefndir i ddu ac ychwanegu swyddogaeth `image()` i lunio'r blaned. Mae'r swyddogaeth `image()` wedi'i gosod fel:

`image(image filename, x-coordinate, y-coordinate, image_width, image_height)`

Mae'r llyfrgell `p5` yn gosod newidynnau `width` a `height` cyffredinol ar sail maint y sgrin. Defnyddiwch y rhain yn eich cod i leoli'r blaned â'i chanol hanner ffordd ar draws (`width/2`) ac ar waelod (`height`) y sgrin.

--- code ---
---
language: python filename: main.py — draw_background() line_numbers: true line_number_start: 14
line_highlights: 15-17
---

# Mae'r swyddogaeth llunio_cefndir yn mynd fan hyn
def draw_background():   
background(0) #Short for background(0, 0, 0) — black    
image(planet, width/2, height, 300, 300) #Draw the image


--- /code ---

Mae rhoi'r holl god ar gyfer llunio'r cefndir mewn un swyddogaeth yn ei gwneud hi'n haws deall eich cod.

--- /task ---

--- task ---

I wneud i'r cefndir ymddangos, galwch `llunio_cefndir()` yn `draw()`. Bydd hyn yn ail-lunio'r cefndir bob tro mae `draw()` yn cael ei galw, gan orchuddio unrhyw luniad hŷn:

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 28
line_highlights: 30
---

def draw():   
#Things to do in every frame    
draw_background()

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich cod i wneud yn siŵr ei fod yn llunio cefndir du â hanner planed ar y gwaelod.

--- /task ---

--- save ---
