## Hintergrund zeichnen

--- task ---

Öffne die [Projektvorlage](https://editor.raspberrypi.org/de-DE/projects/rocket-launch-starter){:target="_blank"}.

--- /task ---

First, you will create a black background to represent space.

Definiere eine Funktion `zeichne_hintergrund()` unter dem entsprechenden Kommentar, um den Hintergrund zu zeichnen.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# Die Funktion „zeichne_hintergrund“ kommt hierher
def setup():   
# Richte hier Deine Animation ein   
size(bidschirm_groesse, bildschirm_groesse)

--- /code ---

--- /task ---

--- task ---

Add this function to the list of things to `draw()` in every frame.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 28
line_highlights: 20
---

def draw():   
# Dinge die in jedem Frame passieren    
zeichne_hintergrund()

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and you should see a black square. --- /task ---



--- task ---

Add a line of code to display an image of a planet.

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 21-23
---
def zeichne_hintergrund():   
background(0) # Kurzform für background(0, 0, 0) — schwarz    
image(planet, width/2, height, 300, 300) # Zeichnet das Bild

Die Funktion `image()` ist wie folgt aufgebaut:

- image filename - we have already loaded the planet image
- x coordinate - we have already set the screen size
- y coordinate
- image width
- image height

--- /task ---

--- task ---

**Test:** Führe deinen Code aus und prüfe, ob er einen schwarzen Hintergrund mit einem halben Planeten darunter zeichnet.

![A planet against a black background.](images/step_2.png){:width="300px"}

--- /task ---

### A different planet?

--- task ---

Click on the image icon to the left to view the image gallery.

![Choose a different planet](images/image_gallery.png)

Lade als Nächstes dein Bild in eine globale Variable `planet`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 15-17
---
def setup():   
# Richte hier Deine Animation ein   
size(bildschirm_groesse, bildschirm_groesse)   
image_mode(CENTER)  # Positioniert das Bild in der Mitte global planet   
planet = load_image('planet.png')  # Dein gewählter Planet

--- /task ---

