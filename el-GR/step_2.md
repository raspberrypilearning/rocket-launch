## Στήνοντας τη σκηνή

--- task --

Ανοίξτε το [πρότυπο έργου](https://trinket.io/python/c7454ed7a8){:target="_blank"}.

--- /task ---

First, you will create a black background to represent space.

--- task ---

Define a `draw_background()` function, and set the background colour to black.

--- code ---
---
Βρες το σχόλιο `Ρύθμιση καθολικών μεταβλητών` και πρόσθεσε μια γραμμή κώδικα για να δημιουργήσεις τη μεταβλητή `screen_size`:
line_highlights: 8
---

# Η συνάρτηση draw_background πηγαίνει εδώ
def draw_background():   
background(0, 0, 0)

--- /code ---

--- /task ---

--- task ---

Add this function to the list of things to `draw()` in every frame.

--- code ---
---
Χρησιμοποίησε τη μεταβλητή `screen_size` για να δημιουργήσεις ένα τετράγωνο με 400 επί 400 εικονοστοιχεία:
line_highlights: 20
---

def draw(): # Things to do in every frame draw_background()

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and you should see a black square.

--- /task ---



--- task ---

Add a line of code to display an image of a planet.

--- code ---
---
language: python line_numbers: true line_number_start: 13
line_highlights: 21-23
---
def draw_background():  
background(0,0,0) image(planet, screen_size/2, screen_size, 300, 300)

--- /code ---


Είναι καλή ιδέα να φορτώνεις εικόνες στο `setup()`, ώστε να είναι έτοιμες όταν χρειαστεί να τις χρησιμοποιήσεις και η κινούμενη εικόνα σου να εκτελείται γρήγορα.

- image filename - we have already loaded the planet image
- x coordinate - we have already set the screen size
- y coordinate
- image width
- image height

--- /task ---

--- task ---

**Test:** Run your code and check that it draws a black background with half a planet at the bottom.

![A planet against a black background.](images/step_2.png){:width="300px"}

--- /task ---

### A different planet?

--- task ---

Click on the image icon to the left to view the image gallery.

![Choose a different planet](images/image_gallery.png)

If you want to change the planet image, change `planet.png` in the code to the filename of your chosen planet, for example, `orange_planet.png`.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 15-17
---
def setup(): # Set up your animation here size(screen_size, screen_size) image_mode(CENTER) global planet planet = load_image('planet.png')

--- /code ---

--- /task ---

