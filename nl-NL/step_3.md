## Lancering!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Elke keer dat er een nieuw frame wordt getekend, moet de raket omhoog bewegen op het scherm om een animatie-effect te creëren.
</div>
<div>

![Een raket die met een constante snelheid van de onderkant naar de bovenkant van het scherm vliegt.](images/fly.gif){:width="300px"}

</div>
</div>

--- task ---

Het startproject heeft een raketafbeelding voor je.

![Afbeelding van de raket in de Trinket-beeldbibliotheek.](images/trinket_rocket_image.png)

--- /task ---

--- task ---

Voeg code toe aan de `setup()` functie om de raketafbeelding in een `raket` global variabele te laden.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 24, 26
---

def setup():   
#Stel je animatie hier in   
size(scherm_grootte, scherm_grootte)   
image_mode(CENTER)   
global planeet, raket   
planeet = load_image('planet.png')    
raket = load_image('rocket.png')

--- /code ---

--- /task ---

De `y` positie van de raket begint bij 400 (de schermhoogte) en neemt vervolgens af met 1 telkens wanneer een nieuw frame wordt getekend.

--- task ---

Voeg een global variabele `raket_y` toe om de `y` positie van de raket bij te houden.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9
---

# Global variabelen instellen
scherm_grootte = 400    
raket_y = scherm_grootte #Begin onderaan

--- /code ---

--- /task ---

--- task ---

Definieer een `teken_raket()` functie om de `y` positie van de raket te wijzigen en deze opnieuw te tekenen.

`raket_y -= 1` is een kortere manier om te zeggen `raket_y = raket_y - 1`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12-16
---

# De teken_raket functie komt hier
def teken_raket():

  global raket_y #Gebruik de global raket_y variabele    
raket_y -= 1 #Verplaats de raket    
image(raket, width/2, raket_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

Neem je nieuwe `teken_raket()` op in de `draw()` functie zodat de raket elk frame opnieuw wordt getekend.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 34
line_highlights: 37
---

def draw():   
#Dingen om te doen in elk frame   
teken_achtergrond()   
teken_raket()


--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit om te controleren of de raket onderaan het scherm begint en elk frame omhoog beweegt.

![Afbeelding van de raket halverwege het scherm.](images/trinket_rocket_fly.gif)

--- /task ---

--- save ---
