## Step 5

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Add variables to setup
Add input for fuel
Add how_fast function to calculate speed
Add liftoff failure message to countdown
type casting str ==> int

Calculate the sweet spot for around 10 frames to orbit on the various variables
floats
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
ORBIT_RADIUS = PLANET_RADIUS + 100

planet = None
rocket = None
speed = None
how_far = 0
burn = 0
fuel = 0

def fly(frames):
  
  global how_far 
  
  if frames * burn <= fuel: # Problem — what if they use a fuel quantity that's a fraction of the burn rate?
    how_far = frames * speed

  # Reached orbit
  if how_far >= ORBIT_RADIUS:
    tint(0, 200, 0)

  elif frames * burn >= fuel and how_far < ORBIT_RADIUS:
    tint(200, 0, 0)
  
  image(
      rocket, 
      SCREEN_WIDTH/2, 
      SCREEN_HEIGHT-(ROCKET_HEIGHT/2)-how_far, 
      ROCKET_WIDTH, 
      ROCKET_HEIGHT
      )
  
  no_tint()

def how_fast(power, fuel, fuel_loss):
  
  global speed
  
  speed = power - (fuel_loss * fuel)

def countdown():

  for t_minus in range(10, -1, -1):
    print('T minus', t_minus)
    sleep(1)

  if speed > 0:
    print('We have liftoff!')
    print('🚀🚀🚀🚀🚀')
  else:
    print('The rocket is too heavy to fly!')

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

  # Draw an orbit around the planet
  no_fill()
  stroke(0, 200, 0)
  ellipse(
      SCREEN_WIDTH/2, 
      SCREEN_HEIGHT, 
      ORBIT_RADIUS*2,
      ORBIT_RADIUS*2
    )
  no_stroke()

def setup():
  global planet, rocket, burn, fuel
  
  frame_rate(10)

  # Load the sprite from file
  planet = load_image('planet.png')
  rocket = load_image('rocket.png')
  
  # The endless void of space
  size(SCREEN_WIDTH, SCREEN_HEIGHT)

  power = 140
  fuel_loss = 1
  burn = 1000
  fuel = int(input('How much fuel do you want to use?'))

  how_fast(power, fuel, fuel_loss)

  countdown()

def draw():
  
  draw_bg()

  fly(frame_count)
  
run()


```