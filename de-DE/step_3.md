## Abheben!

Das Starterprojekt stellt dir ein Raketenbild zur Verfügung.

![Bild der Rakete in der Bildergalerie des Code-Editors.](images/rocket_image.png)

Füge der Funktion `setup()` Code hinzu, um das Raketenbild in eine globale Variable `rakete` zu laden.

<div class="c-project-code">

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 24, 26
---

def setup():   
# Richte hier Deine Animation ein   
size(bildschirm_groesse, bildschirm_groesse)   
image_mode(CENTER)   
global planet, rakete   
planet = load_image('planet.png')    
rakete = load_image('rocket.png')

--- /code --- --- /task ---

--- task ---

Füge eine globale Variable `rakete_y` hinzu, um die `y` Position der Rakete im Auge zu behalten.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9
---

# Globale Variablen einrichten
bildschirm_groesse = 400    
rakete_y = bildschirm_groesse # unten starten

--- /code ---

--- /task ---


Die Position `y` der Rakete beginnt bei 400 (der Bildschirmhöhe) und verringert sich dann bei jedem gezeichneten Frame um 1.


--- task ---

Definiere eine `zeichne_rakete()`-Funktion, um die `y` Position der Rakete zu ändern und sie neu zu zeichnen.

--- code ---
---
--- save ---
line_highlights: 12-16
---

# Die Funktion „zeichne_rakete“ kommt hierher
Lass die Rakete fliegen


--- /code ---

--- /task ---

--- task ---

Rufe deine neue `zeichne_rakete()` in der Funktion `draw()` auf, damit die Rakete in jedem Frame neu gezeichnet wird.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 33
line_highlights: 36
---

def draw():   
# Dinge die in jedem Frame passieren   
zeichne_hintergrund()   
zeichne_rakete()


--- /code ---

--- /task ---

--- task ---

`rakete_y -= 1` ist eine kürzere Art zu sagen: `rakete_y = rakete_y - 1`.


--- /task ---


Jedes Mal, wenn ein neues Bild gezeichnet wird, muss sich die Rakete auf dem Bildschirm nach oben bewegen, um einen Animationseffekt zu erzeugen.


--- task ---

!\[Eine Rakete, die mit gleichmäßiger Geschwindigkeit vom unteren zum oberen Bildschirmrand fliegt.\](images/fly.gif){:width="300px"}

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12
---

def zeichne_rakete():   
global rakete_y  # Benutze die globale Variable rakete_y    
rakete_y -= 1  # Bewege die Rakete    
image(rakete, width/2, rakete_y, 64, 64)

--- /task ---


--- task ---

**Test:** Führe deinen Code aus, um zu überprüfen, ob die Rakete am unteren Bildschirmrand startet und sich mit jedem Frame nach oben bewegt.


![Animation der Rakete, die auf halber Höhe des Bildschirms fliegt.](images/fly.gif){:width="300px"}

--- /task ---