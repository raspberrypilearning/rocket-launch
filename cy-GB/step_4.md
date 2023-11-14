## Effeithiau'r ecsôst

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Bydd y roced yn edrych yn fwy realistig gyda rhywfaint o effeithiau arbennig i efelychu ôl yr ecsôst. 

Fe allwch chi greu effeithiau cŵl drwy ddefnyddio dolen `for` i lunio nifer o siapiau ym mhob ffrâm.

</div>
<div>

![Y roced wrth hedfan gydag ôl ecsôst.](images/flying_rocket.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Mae codio'n cael ei ddefnyddio i wneud <span style="color: #0faeb0">**effeithiau graffeg**</span> ar gyfer ffilmiau a gemau. Mae'n gyflymach o lawer ysgrifennu cod na llunio pob ffrâm mewn animeiddiad yn unigol. </p>

### Draw your exhaust

Mae llunio nifer o elipsau melyn mewn gwahanol safleoedd `y` yn creu ôl ecsôst gyda gwaelod crwn.

--- task ---

Update your `draw_rocket()` function to include a `for` loop that repeats the drawing of `25` exhaust ellipses. The **loop variable** `i` gets added to `rocket_y` to draw each ellipse further below the rocket.

--- code ---
---
Diweddarwch eich swyddogaeth `llunio_roced()` i gynnwys dolen `for` sy'n ailadrodd y lluniad o `25` elips ecsôst. Mae'r **newidyn dolen** `i` yn cael ei ychwanegu at `roced_y` i lunio pob elips yn bellach o dan y roced.
line_highlights: 16-22
---

def draw_rocket(): global rocket_y   
rocket_y -= 1   

    no_stroke()  # Turn off the stroke
    
    for i in range(25):  # Draw 25 burning exhaust ellipses   
        fill(255, 255, 0)  # Yellow   
        ellipse(width/2, rocket_y + i, 8, 3)  # i increases each time the loop repeats    
    
    image(rocket, width/2, rocket_y, 64, 64)


--- /code ---

--- /task ---

global roced_y   
roced_y -= 1

To run the code in a `for` loop a certain number of times, you can use the `range()` function. For example, `range(5)` creates a sequence of five numbers starting from 0, so [0, 1, 2, 3, 4].

for i in range(25): #Llunio 25 o elipsau ecsôst sy'n llosgi   
fill(255, 255, 0) #Melyn   
ellipse(width/2, roced_y + i, 8, 3) #i yn cynyddu bob tro mae'r ddolen yn ailadrodd

--- task ---

**Test:** Run your code to check the rocket has a new exhaust trail.

![A close-up of the rocket with an exhaust trail.](images/rocket_exhaust.png){:width="300px"}

--- /task ---

### Add a gradient

**Profi:** Rhedwch eich cod i wneud yn siŵr bod gan y roced ôl ecsôst newydd.

--- task ---

Change the call to `fill()` to set the amount of green to `255 - i * 10` so that the first ellipse has equal amounts of red and green and the last ellipse has very little green.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 18
line_highlights: 20
---

    for i in range(25):   
        fill(255, 255 - i * 10, 0)  # Reduce the amount of green    
        ellipse(width/2, rocket_y + i, 8, 3)

--- /code ---

--- /task ---

--- task ---

for i in range(25):   
fill(255, 255 - i * 10, 0) #Lleihau lefel y gwyrdd    
ellipse(width/2, roced_y + i, 8, 3)

--- /task ---

### Create a smoke effect

The smoke exhaust trail is created by drawing lots of slightly transparent grey ellipses at different positions in each frame.

![A slow animation of the smoke effect.](images/rocket_smoke.gif)

--- task ---

This time the `fill()` is outside the loop as the colour is the same for each smoke ellipse. The fourth input to `fill()` is the opacity, a low opacity value makes the colour more transparent so you can see the shapes underneath.

Mae'r ôl mwg ecsôst yn cael ei greu drwy lunio nifer o elips llwyd sydd ychydig yn dryloyw mewn safle gwahanol ym mhob ffrâm.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 18
line_highlights: 23-26
---

    for i in range(25):  
        fill(255, 255 - i * 10, 0)   
        ellipse(width/2, rocket_y + i, 8, 3)    
    
    fill(200, 200, 200, 100)  # Transparent grey   
    for i in range(20):  # Draw 20 random smoke ellipses    
        ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))    
    
    image(rocket, width/2, rocket_y, 64, 64)

--- /code ---

--- /task ---

--- task ---

language: python filename: main.py - llunio_roced() line_numbers: true line_number_start: 19

![An animation of the rocket and exhaust trail with added smoke.](images/rocket_exhaust_circles.gif)

--- /task ---

--- save ---
