## Step title

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
You will now create your program, and add a sprite for the planet your rocket will be launching from.
</div>
<div>
![A planet against a black background](images/step_2.png){:width="300px"}
</div>
</div>

--- task ---

Open the [project template](https://trinket.io/python/b0f4874ac4){:target="_blank"} and remix it.

--- save ---

--- /task ---

First, setup the black background of space.

--- task ---

Add some variables for your animation's width and height where the comments tell you to create global variables:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 6 
line_highlights: 7-9
---
# Setup global variables 
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 400

--- /code ---

Then use those variables to set the animation's size in the `setup` function:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18 
line_highlights: 20
---
def setup():
  # Setup your animation here
  size(SCREEN_WIDTH, SCREEN_HEIGHT)
--- /code ---

--- save ---

--- /task ---

--- task ---

Create a `draw_bg` function below the comment that tells you where it should go. Use `background` to set the background colour to black.

```python
# The draw_bg function goes here
def draw_bg()
  background(0,0,0)
```

**Tip:** Placing the instructions for drawing the background into their own function means that you can easily re-draw the background in every frame of your animation by calling `draw_bg`.
--- /task ---

Now you need to add the planet image to your animation.

--- task ---

First, you need to 

--- /task ---

```python
#!/bin/python3
from p5 import *


SCREEN_WIDTH = 480
SCREEN_HEIGHT = 400
PLANET_RADIUS = 150

planet = None

def draw_bg():
  background(0, 0, 0)

  # Draw an origin planet
  image(
  planet, # sprite
  (SCREEN_WIDTH/2)-PLANET_RADIUS, # x top-left corner
  SCREEN_HEIGHT-PLANET_RADIUS, # y top-left corner
  PLANET_RADIUS*2, # sprite width
  PLANET_RADIUS*2 # sprite height
  )


def setup():
  global planet
  
  frame_rate(10)

  # Load the sprite from file
  planet = load_image('planet.png')
  
  # The endless void of space
  size(SCREEN_WIDTH, SCREEN_HEIGHT)

def draw():
  
  draw_bg()
  
run()
```