## Lancering!

Het startproject heeft een raketafbeelding voor je.

![Afbeelding van de raket in de code-editor beeldbibliotheek.](images/rocket_image.png)

--- task ---

Voeg code toe aan de `setup()` functie om de raketafbeelding in een `raket` global variabele te laden.

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 17
line_highlights: 21, 23
---

def setup():   
    # Stel hier je animatie in 
    size(scherm_grootte, scherm_grootte)   
    image_mode(CENTER)   
    global planeet, raket   
    planeet = load_image('planet.png')    
    raket = load_image('rocket.png')    

--- /code ---

--- /task ---

--- task ---

Voeg een global variabele `raket_positie` toe om de `y` positie van de raket bij te houden.

--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 7
---

# Globale variabelen instellen   
scherm_grootte = 400    
raket_positie = scherm_grootte  

--- /code ---

--- /task ---


De `y` positie van de raket begint bij 400 (de schermhoogte) en neemt vervolgens af met 1 telkens wanneer een nieuw frame wordt getekend.

--- task ---

Definieer een `teken_raket()` functie om de raket op het scherm te laten verschijnen.

--- code ---
---
language: python
line_numbers: true
line_number_start: 9 
line_highlights: 10-12 
---

# De functie teken_raket komt hier
def teken_raket():   
    global raket_positie      
    image(raket, width/2, raket_positie, 64, 64)    


--- /code ---

--- /task ---

--- task ---

Roep de functie `teken_raket()` aan.

--- code ---
---
language: python
line_numbers: true
line_number_start: 29 
line_highlights: 32 
---

def draw():
    # Dingen om te doen in elk frame
    teken_achtergrond()
    teken_raket() 


--- /code ---

--- /task ---

--- task ---  

**Test:** Voer je code uit en controleer of de raket onderaan de afbeelding verschijnt.

--- /task ---


Elke keer dat er een nieuw frame wordt getekend, moet de raket omhoog bewegen op het scherm om een animatie-effect te creëren.


--- task ---

De `raket_positie` van de raket begint bij 400 (de schermhoogte) en neemt vervolgens met 1 af telkens wanneer een nieuw frame wordt getekend.


--- code ---
---
language: python
line_numbers: true
line_number_start: 10 
line_highlights: 12
---

def teken_raket():   
    global raket_positie     
    raket_positie = raket_positie - 1    
    image(raket, width/2, raket_positie, 64, 64)    

--- /code ---

--- /task ---


--- task ---

**Test:** Voer je code uit om te controleren of de raket onderaan het scherm begint en elk frame omhoog beweegt.


![Een raket vliegt met een constante snelheid van de onderkant naar de bovenkant van het scherm.](images/fly.gif){:width="300px"}

--- /task ---

