## Step 4

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create a paramatised function
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>


```python
#!/bin/python3
from p5 import *
from time import sleep

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 400
PLANET_RADIUS = 150
ROCKET_HEIGHT = 34.4 ### Can we just ask processing for the width and height?
ROCKET_WIDTH = 20


planet = None
rocket = None

def fly(frames):
  
  distance_travelled = 10 * frames
  
  image(
      rocket, 
      SCREEN_WIDTH/2, 
      SCREEN_HEIGHT-(ROCKET_HEIGHT/2)-distance_travelled, 
      ROCKET_WIDTH, 
      ROCKET_HEIGHT
      )


def countdown():

  for t_minus in range(10, -1, -1):
    print('T minus', t_minus)
    sleep(1)

  print('We have liftoff!')
  print('🚀🚀🚀🚀🚀')

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
  global planet, rocket
  
  frame_rate(10)

  # Load the sprite from file
  planet = load_image('planet.png')
  rocket = load_image('rocket.png')
  
  # The endless void of space
  size(SCREEN_WIDTH, SCREEN_HEIGHT)

    countdown()

def draw():
  
  draw_bg()

  fly(frame_count)
  
run()


```