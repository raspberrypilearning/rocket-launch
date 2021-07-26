## Liftoff!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Make your rocket fly, by creating a function that accepts a parameter.
</div>
<div>
![A rocket flying at a steady speed from the bottom to the top of the screen.](images/fly.gif){:width="300px"}
</div>
</div>

Functions that accept parameters as inputs are really useful tools: they let you create a piece of code that produces different outputs based on its inputs, which can be very useful in your programming. You've actually used lots of these kinds of functions already: the `print`, `sleep`, and `background` functions all accept parameters that change what gets printed, how long the program waits for, and what colour the background is, respectively. 

--- task ---

Create a function called `fly` that accepts a parameter called `frames`. You give a function parameters by placing them in the parentheses after the function's name when you define it with `def`. Have it set a variable called `how_far` to ten times `frames`. Then have it print that variable out.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 14 
line_highlights: 15-19
---
# The fly function goes here
def fly(frames):
  
  how_far = 10 * frames
  print(how_far)

--- /code ---

--- /task ---

--- task ---

Add a line to the `draw` function that calls your `fly` function and passes `frame_count` to it. `frame_count` is the number of frames of your animation that have been drawn.

---
language: python
filename: main.py
line_numbers: true
line_number_start: 54 
line_highlights: 57-59
---
def draw():
  # Things to do in every frame
  draw_bg()
  
  fly(frame_count)

--- /code ---

**Tip:** When you pass a variable into a function like this, you are passing its value at the moment you call the function. Changes you make to the value inside the function won't change the original variable.

--- save ---

**Test:** Run your program. After the countdown compleets, you should see numbers printing out, each 10 higher than the one before it. This will go on forever, so stop the program after you've seen this.
--- /task ---

These numbers, that your code prints out, can be used as the y-coordinates for drawing your rocket flying into orbit.

--- task ---

You'll need a rocket sprite, which you can create the same way you created the planet sprite. First, declare the global variable below the one for the planet, as well as one for the height of the rocket, below the `PLANET_RADIUS` variable.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10 
line_highlights: 11, 14-15
---
PLANET_RADIUS = 150
ROCKET_HEIGHT = 30

planet = None
rocket = None

--- /code ---

Then load the rocket as part of your `setup` function:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 46 
line_highlights: 48, 50-51
---
def setup():
  # Setup your animation here
  global planet, rocket
  planet = load_image('planet.png')
  rocket = load_image('rocket.png')

--- /code ---

--- /task ---

--- task ---

Now you need to draw your rocket sprite into your animation. To do this, you'll modify the fly function to delete the `print` statement and add `image` instead. By using `how_far` as part of the y-coordinate of the rocket, it will change every time the animation draws a new frame. If you subtract `how_far`, then the y-coordinate will get smaller, causing the rocket to move up the screen.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 17 
line_highlights: 20
---
def fly(frames):
  
  how_far = 10 * frames
  
  image(
    rocket, 
    SCREEN_WIDTH/2, 
    SCREEN_HEIGHT-(ROCKET_HEIGHT/2)-how_far, 
    rocket.width/(rocket.height/ROCKET_HEIGHT),
    ROCKET_HEIGHT
    )
--- /code ---

--- collapse ---
---
title: Controlling image size
---

`rocket.width/(rocket.height/ROCKET_HEIGHT)` uses the `width` and `height` properties of the image file you loaded to calculate the correct width for the image in proportion to your `ROCKET_HEIGHT` value. This lets you adjust the size of the rocket by changing a single variable. If you didn't do this, you would have to recalculate the image's width and height whenever you wanted to change its size, or end up with a squashed looking rocket!

--- /collapse ---

--- save ---

**Test:** Run your code and watch the rocket fly!

--- /task ---

That looks great, but maybe a little too fast? You can adjust how quickly your animation happens by changing the **frame rate** — the number of frames your animation draws every second. 

--- task ---

Add the `frame_rate` function to `setup` and use it to set your animation to ten frames per second:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 53 
line_highlights: 55
---
def setup():
  # Setup your animation here
  frame_rate(10)
  global planet, rocket
  planet = load_image('planet.png')
--- /code ---

--- save ---

**Test:** Run the program again, and see the difference.

**Choose:** You can adjust the frame rate if you think it's still too fast, or too slow. If you want it to go faster, you may reach the limits of your computer, or screen.

--- /task ---