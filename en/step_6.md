## Fuel weight
<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Time to make your rocket more realistic. One of the most important things to decide when building a rocket is how much fuel to load into it.
</div>
</div>

<iframe src="https://trinket.io/embed/python/fa55405c62?outputOnly=true&runOption=run" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

--- task ---

Add some variables at the start of your program to keep track of how much fuel your rocket has, how fast that fuel burns (in frames), and how far the rocket has travelled.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 15 
line_highlights: 17-20
---
planet = None
rocket = None
how_far = 0 # how far the rocket has travelled
burn = 1000 # burn how much fuel every frame?
fuel = 25000 # start with how many kgs of fuel?

--- /code ---

--- /task ---

--- task ---

Declare `how_far` as a `global` variable, to keep it from being erased every time the `draw()` function calls `fly()` as part of creating a frame.

--- code ---
---
language: python
filename: main.py — fly()
line_numbers: true
line_number_start: 22
line_highlights: 24
---
def fly(frames):
  
  global how_far 
  
  how_far = 10 * frames
  
--- /code ---

--- /task ---

--- task ---

Check if burning for the number of frames that have passed would have used up all the rocket's fuel. You can test this by checking if `frames` times `burn` is less than or equal to (≤) the total amount of fuel the rocket started with. Chang your code for `how_far` so it uses `if` and `<=` to only update if the rocket still has fuel.

--- code ---
---
language: python
filename: main.py — fly()
line_numbers: true
line_number_start: 22
line_highlights: 26-27
---
def fly(frames):
  
  global how_far 
  
  if (frames * burn) <= fuel: 
    how_far = 10 * frames
  
--- /code ---

--- /task ---

--- /task ---

--- task ---

To finish off the fuel burning code, add a test in `fly()` to check if the rocket will never reach orbit, due to running out of fuel, and tint it red if so. 

--- code ---
---
language: python
filename: main.py — fly()
line_numbers: true
line_number_start: 29 
line_highlights: 33-34
---
  # Reached orbit?
  if how_far >= ORBIT_RADIUS:
    tint(0, 200, 0)
  
  elif (frames * burn) >= fuel:
    tint(200, 0, 0)
--- /code ---

--- save ---

--- /task ---

--- task ---

**Test:** Run your program and watch the rocket launch!

--- /task ---

--- task ---

Finally, let users of your program set the fuel value when the program starts by updating `setup()` to include `fuel` as `global`, and to use the `input()` function to ask the user to set it.

--- code ---
---
language: python
filename: main.py — fly()
line_numbers: true
line_number_start: 91 
line_highlights: 94, 100
---
def setup():
  # Setup your animation here
  frame_rate(10)
  global planet, rocket, fuel
  planet = load_image('planet.png')
  rocket = load_image('rocket.png')
  
  size(SCREEN_WIDTH, SCREEN_HEIGHT)
  
  fuel = int(input('How many kilograms of fuel do you want to use?'))
  
  countdown()
  
  
--- /code ---

**Tip:** You have to surround `input()` with `int()` to turn what the user types into a number you can do maths with.

--- /task ---

--- task ---

**Test:** Try launching your rocket with enough fuel to reach orbit, and to fail to reach orbit. To reach orbit, use 25000 kg of fuel. To fail to reach orbit, use 24000 kg, or less.

--- /task ---

Your results should look something like this:

![A rocket launches from a planet and flys straight up, passing a green line and becoming green.](images/fuel_orbit_success.gif){:width="300px"}

![A rocket launches from a planet and flys straight up, falling short of a green line and becoming red.](images/fuel_orbit_fail.gif){:width="300px"}