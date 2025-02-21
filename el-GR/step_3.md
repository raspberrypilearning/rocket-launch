## Απογείωση!

Το αρχικό έργο σου προσφέρει μια εικόνα πυραύλου.

![Εικόνα του πυραύλου στη βιβλιοθήκη εικόνων Trinket.](images/rocket_image.png)

--- task --- Add code to the `setup()` function to load the rocket image into a `rocket` global variable.

<div class="c-project-code">

--- code ---
---
Πρόσθεσε επίσης κώδικα στη συνάρτηση `setup()` για να φορτώσεις την εικόνα του πύραυλου σε μια καθολική μεταβλητή `rocket`.
line_highlights: 24, 26
---

def setup():   
# Set up your animation here   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet, rocket   
planet = load_image('planet.png')    
rocket = load_image('rocket.png')

language: python filename: main.py line_numbers: true line_number_start: 20

--- task ---

Add a `rocket_position` global variable to keep track of the rocket's `y` position.

--- code ---
---
Η θέση `y` του πυραύλου θα ξεκινά από το 400 (το ύψος της οθόνης) και στη συνέχεια θα μειώνεται κατά 1 κάθε φορά που σχεδιάζεται ένα νέο καρέ.
line_highlights: 9
---

# Ρύθμιση καθολικών μεταβλητών
screen_size = 400    
rocket_position = screen_size

--- /code ---

--- /task ---


Η θέση `y` του πυραύλου θα ξεκινά από το 400 (το ύψος της οθόνης) και στη συνέχεια θα μειώνεται κατά 1 κάθε φορά που σχεδιάζεται ένα νέο καρέ.

--- task ---

Define a `draw_rocket()` function to make the rocket appear on the screen.

--- code ---
---
language: python line_numbers: true line_number_start: 9
line_highlights: 12-16
---

# Η συνάρτηση draw_rocket πηγαίνει εδώ
Όρισε μια συνάρτηση `draw_rocket()` για να αλλάξεις τη θέση του `y` του πυραύλου και σχεδίασέ τον ξανά.


--- /code ---

--- /task ---

--- task ---

def draw_rocket():

--- code ---
---
language: python line_numbers: true line_number_start: 29
line_highlights: 37
---

def draw(): # Things to do in every frame draw_background() draw_rocket()


--- /code ---

--- /task ---

--- task ---

language: python filename: main.py line_numbers: true line_number_start: 34

--- /task ---


Each time a new frame is drawn, you need to move the rocket one pixel up the screen to create an animation effect.


--- task ---

The `rocket_position` of the rocket will start at 400 (the screen height) and then decrease by 1 each time a new frame is drawn.


--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 12
---

def draw_rocket():   
global rocket_position     
rocket_position = rocket_position - 1    
image(rocket, width/2, rocket_position, 64, 64)

--- /code ---

--- /task ---


--- task ---

**Test:** Run your code to check that the rocket blasts off from the bottom of the screen.


![A rocket flying at a steady speed from the bottom to the top of the screen.](images/fly.gif){:width="300px"}

--- /task ---

