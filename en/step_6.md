## Fuel weight
<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Time to make your rocket more realistic. One of the most important things to decide when building a rocket is how to balance the amount of fuel your rocket has to burn before it runs out, with how much that fuel weighs. Every extra kilogram of fuel is another kilogram of weight the rocket has to lift. Too little fuel, and you can't burn the engine long enough to reach orbit. Too much fuel, and the rocket is too heavy to fly.
</div>
</div>
<iframe src="https://trinket.io/embed/python/ced6bff454?toggleCode=true&runOption=run&start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

--- task ---

Add some variables to keep track of how much fuel your rocket has, how fast that fuel burns (in frames), and how far the rocket has travelled. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 14 
line_highlights: 16-20
---
planet = None
rocket = None
speed = 0
how_far = 0
burn = 0
fuel = 0

--- /code ---

--- /task ---

--- task ---

Now update the code in `fly` that calculates how far the rocket has flown. Add an `if` statement to check if burning for the number of frames that have passed would have used up all the rocket's fuel.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 22
line_highlights: 23-28
---
def fly(frames):
  
  global how_far 
  
  if frames * burn <= fuel: 
    how_far = frames * speed
  
--- /code ---

**Tip:** You're using a `global` variable here to keep `how_far` from being erased every time the `draw` function calls `fly` as part of creating a frame. This keeps the rocket in place even once the fuel test starts to fail.

--- /task ---

--- task ---

To finish off the fuel burning code, add a test to check if the rocket will never reach orbit, due to running out of fuel, and tint it red if so. 

<mark> I realised you don't need an elif here, due to the nature of the conditions, so I just used another if. Also, will they have seen and by now?</mark>

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 29 
line_highlights: 33-34
---
  # Reached orbit?
  if how_far >= ORBIT_RADIUS:
    tint(0, 200, 0)
  
  if frames * burn >= fuel and how_far < ORBIT_RADIUS:
    tint(200, 0, 0)
--- /code ---

--- save ---

--- /task ---

--- task ---

**Test:** Try getting your rocket into orbit, and failing to do so, to check that both work correctly.

To reach orbit:

 + Set `speed` to `50`
 + Set `burn` to `1000`
 + Set `fuel` to `6000`

To fail to reach orbit:

 + Leave `speed` at `50`
 + Leave `burn` at `1000`
 + Change `fuel` to `4000`

--- /task ---

Your results should look something like this:

![A rocket launches from a planet and flys straight up, passing a green line and becoming green.](images/fuel_orbit_success.png){:width="300px"}

![A rocket launches from a planet and flys straight up, falling short of a green line and becoming red.](images/fuel_orbit_fail.png){:width="300px"}

--- task ---

Once you've completed both tests, set the variables you changed back to `0`.

--- /task ---

<mark>This feels like the natural break point if we're splitting this step.</mark>

Now your rocket burns fuel, and can fail to reach orbit if it runs out. However, unlike real rockets, the weight of that fuel still doesn't affect the rocket's speed. One more function and a few small changes will fix that.

--- task ---

Create a `how_fast` function where the comment indicates, and have it accept three parameters:

 + `power` — the basic power of the engine (how far the rocket will fly each frame), without including the weight of the fuel
 + `fuel_loss` — how much power the engine loses for each kg of fuel included
 + `fuel` — how many kgs of fuel to load on the rocket

The function should calculate the rocket's speed by subtracting the total loss of power due to fuel weight from the engine power.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 46 
line_highlights: 47-52
---
# The how_fast function goes here
def how_fast(power, fuel, fuel_loss):
  
  global speed
  
  speed = power - (fuel_loss * fuel)

--- /code ---

--- /task ---

--- task ---

Setting up the parameters that influence the rocket's speed, and calling `how_fast`, should happen in the `setup` function. You'll need to:

 + Make `fuel` and `burn` `global`, so you can change their values in `setup`.
 + Set the values of `power`, `fuel_loss`, `burn`, and `fuel`. You should let the user choose the value for `fuel` using `input`.
 + Call `how_fast`, passing it those values, so as it can set `speed`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 86 
line_highlights: 89, 
---
def setup():
  # Setup your animation here
  frame_rate(10)
  global planet, rocket, fuel, burn
  planet = load_image('planet.png')
  rocket = load_image('rocket.png')
  
  size(SCREEN_WIDTH, SCREEN_HEIGHT)
  
  fuel = int(input('How much fuel do you want to use?'))
  power = 100
  fuel_loss = 0.01
  burn = 1000

  how_fast(power, fuel, fuel_loss)

  countdown()
  
--- /code ---

**Tip:** When setting `fuel`, you surround `input()` with `int()` to force the result to be a number instead of text. This will let `how_fast` use it in maths without problems.

--- save ---

**Test:** Test your program with fuel values of `5000`, `8000`, and `12000`. 

--- /task ---

Notice the three different results you got from your test: orbit, failure to reach orbit, and failure to launch. The first two are well communicated by your program, the last one might be confusing to the user.

--- task ---

Add an `if` statement to the `countdown` function that checks whether the rocket will launch (`speed > 0`) and, if it won't, tells the user this instead of saying 'We have liftoff!':

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 54 
line_highlights: 60-65
---
def countdown():

  for t_minus in range(10,-1,-1):
    print('T minus', t_minus) # Print out the countdown at each step
    sleep(1)

  if speed > 0:
    print('We have liftoff!')
    print('🚀🚀🚀🚀🚀')
  else:
    print('The rocket is too heavy to fly!')

--- /code ---

--- save ---

**Test:** Run your program and try a fuel value of `12000` again, to check the message displays correctly.

--- /task ---