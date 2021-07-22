## Step title

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
What is a sprite. How to load a sprite. How to position and size a sprite relative to screen.

Use gifs — use OBS > easygif workflow
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

Open a [new Scratch project](http://rpf.io/scratch-new){:target="_blank"}. Scratch will open in another browser tab.

[[[working-offline]]]

--- /task ---

--- task ---

Step content... 
Can use:
**Test:**
**Choose:**
**Tip:**

--- /task ---

--- save ---


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