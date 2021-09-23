## Set the scene

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
The animation needs a space backdrop with a planet to launch the rocket from.</div>
<div>
![A planet against a black background](images/step_2.png){:width="300px"}
</div>

--- task ---

Open the [project template](https://trinket.io/python/f2199f5a8c){:target="_blank"}.

If you have a Trinket account you can click on the **Remix** button to save a copy to your ‘My Trinkets’ library.

--- /task ---

You will use a `screen_size` variable to set the size of the screen and in calculations. Variables defined outside functions are **global** so you will be able to use them anywhere in your program.

--- task ---

Find the comment `Setup global variables` and add a line of code to create your `screen_size` variable:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7 
line_highlights: 8
---
# Setup global variables 
screen_size = 400 

--- /code ---

--- /task ---

--- task ---

Use the `screen_size` variable to create a square 400 by 400 screen size:

--- code ---
---
language: python
filename: main.py — setup()
line_numbers: true
line_number_start: 18
line_highlights: 20
---
def setup():
  # Setup your animation here
  size(screen_size, screen_size)
  

--- /code ---

--- /task ---

--- task ---

The starter project has three different planet images and the moon provided for you. You can view these in the Trinket image library by selecting the 'View and add images' button.

![A plus, an upload symbol, and an image symbol. The image symbol is highlighted.](images/trinket_image.png)

**Choose:** Decide which image you want to use and make a note of the filename. For example, `orange_planet.png`.

--- /task ---

It's a good idea to load images in `setup()` so that they are ready when you need to use them and your animation will run quickly.

--- task ---

The `image_mode(CENTER)` line says that you will be positioning images by giving the coordinates of the centre of the image (instead of the top left corner).

Add code to the `setup()` function to load your chosen image into a `planet` global variable. The variable needs to be global so you can use it later when you draw the planet to the screen.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18 
line_highlights: 21-23
---
def setup():
  # Setup your animation here
  size(screen_size, screen_size)
  image_mode(CENTER)
  global planet
  planet = load_image('planet.png') # your chosen planet


--- /code ---

--- /task ---

--- task ---

Define a `draw_background()` function, to draw the background, below the comment that tells you where it should go. 

Use `background(0)` to set the background colour to black and add an `image()` function to draw the planet.

The `p5` library sets `width` and `height` variables based on the size of the screen. Use these in your code to position the planet with its centre half-way across (`width/2`) and at the bottom (`height`) of the screen.

--- code ---
---
language: python
filename: main.py — draw_background()
line_numbers: true
line_number_start: 14 
line_highlights: 15-17
---
# The draw_background function goes here
def draw_background():
  background(0) # short for background(0, 0, 0) - black 
  image(planet, width/2, height, 300, 300) # draw the image
  

--- /code ---

Putting all the code for drawing the background into one function makes your code easier to understand.

--- /task --- 

--- task ---

To make the background appear, call `draw_background()` in `draw()`. This will cause the background to be re-drawn every time `draw()` is called, covering over any older drawing:

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 28 
line_highlights: 30
---
def draw():
  # Things to do in every frame
  draw_background()
  
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and check that it draws a black background with half a planet at the bottom.

--- /task ---

--- save ---