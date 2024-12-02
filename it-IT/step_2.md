## Disegna lo sfondo

--- task ---

Apri il [template del progetto](https://editor.raspberrypi.org/it-IT/projects/rocket-launch-starter){:target="_blank"}.

--- /task ---

First, you will create a black background to represent space.

Definisci una funzione `draw_ background()` , per disegnare lo sfondo, sotto il commento che ti dice dove dovrebbe andare.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# La funzione draw_background va qui
def setup():   
# Imposta qui la tua animazione   
size(screen_size, screen_size)

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
# Cose da fare in ogni fotogramma    
draw_background()

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
def draw_background():   
background(0)  # Abbreviazione per background(0, 0, 0) — black    
image(planet, width/2, height, 300, 300)  # Disegna l'immagine

La funzione `image()` è così strutturata:

- image filename - we have already loaded the planet image
- x coordinate - we have already set the screen size
- y coordinate
- image width
- image height

--- /task ---

--- task ---

**Test:** Esegui il codice e controlla che disegni uno sfondo nero con mezzo pianeta in basso.

![![Un pianeta su sfondo nero.](images/step_2.png){:width="300px"}](images/step_2.png){:width="300px"}

--- /task ---

### A different planet?

--- task ---

Click on the image icon to the left to view the image gallery.

![Choose a different planet](images/image_gallery.png)

Ad esempio, `orange_planet.png`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 15-17
---
def setup():   
# Imposta qui la tua animazione   
size(screen_size, screen_size)   
image_mode(CENTER) # Posiziona l'immagine al centro global planet   
planet = load_image('planet.png') # Il pianeta scelto

--- /task ---

