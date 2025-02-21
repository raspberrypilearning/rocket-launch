## Teken achtergrond

--- task ---

Open het [projectsjabloon](https://editor.raspberrypi.org/nl-NL/projects/rocket-launch-starter){:target="_blank"}.

--- /task ---

First, you will create a black background to represent space.

--- task ---

Define a `draw_background()` function, and set the background colour to black.

--- code ---
---
language: python line_numbers: true line_number_start: 12
line_highlights: 13-14
---

# De functie teken_achtergrond komt hier
def draw_background():   
background(0, 0, 0)

--- /code ---

--- /task ---

--- task ---

Add this function to the list of things to `draw()` in every frame.

--- code ---
---
language: python line_numbers: true line_number_start: 25
line_highlights: 27
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
line_highlights: 15-16
---
def draw_background():  
background(0,0,0) image(planet, screen_size/2, screen_size, 300, 300)

--- /code ---


De functie `image()` is als volgt ingedeeld:

- image filename - we have already loaded the planet image
- x coordinate - we have already set the screen size
- y coordinate
- image width
- image height

--- /task ---

--- task ---

**Test:** Voer je code uit en controleer of deze een zwarte achtergrond tekent met onderaan een halve planeet.

![![Een planeet tegen een zwarte achtergrond.](images/step_2.png){:width="300px"}](images/step_2.png){:width="300px"}

--- /task ---

### A different planet?

--- task ---

Click on the image icon to the left to view the image gallery.

![Choose a different planet](images/image_gallery.png)

Bijvoorbeeld `orange_planet.png`.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 22
---
def setup(): # Set up your animation here size(screen_size, screen_size) image_mode(CENTER) global planet planet = load_image('planet.png')

--- /code ---

--- /task ---

