## Efectos de escape

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

El cohete se verá más realista con algunos efectos especiales para simular el rastro de escape. 

Puedes crear efectos geniales usando un bucle `for` para dibujar muchas formas en cada cuadro.

</div>
<div>

![El cohete en pleno vuelo con un rastro de escape.](images/flying_rocket.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
La codificación se usa para hacer <span style="color: #0faeb0">**efectos gráficos**</span> para películas y juegos. Es mucho más rápido escribir código que dibujar cada cuadro de una animación individualmente. </p>

### Draw your exhaust

Dibujar muchas elipses amarillas en diferentes posiciones `y` crea un rastro de escape con un fondo redondo.

--- task ---

Update your `draw_rocket()` function to include a `for` loop that repeats the drawing of `25` exhaust ellipses. The **loop variable** `i` gets added to `rocket_y` to draw each ellipse further below the rocket.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 12
line_highlights: 16-20
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

A `for` loop repeats a piece of code once for every item it is given.

To run the code in a `for` loop a certain number of times, you can use the `range()` function. For example, `range(5)` creates a sequence of five numbers starting from 0, so [0, 1, 2, 3, 4].

Each time the `for` loop repeats, it sets a variable to the current item so that you can use it in the loop.

--- task ---

**Test:** Run your code to check the rocket has a new exhaust trail.

![A close-up of the rocket with an exhaust trail.](images/rocket_exhaust.png){:width="300px"}

--- /task ---

### Add a gradient

The `i` variable can also be used to create a colour gradient with less green in each ellipse that gets drawn.

--- task ---

Change the call to `fill()` to set the amount of green to `255 - i * 10` so that the first ellipse has equal amounts of red and green and the last ellipse has very little green.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 18
line_highlights: 19
---

    for i in range(25):   
        fill(255, 255 - i * 10, 0)  # Reduce the amount of green    
        ellipse(width/2, rocket_y + i, 8, 3)

--- /code ---

--- /task ---

--- task ---

**Test:** Check that you get a trail of ellipses gradually changing from yellow to red.

--- /task ---

### Create a smoke effect

The smoke exhaust trail is created by drawing lots of slightly transparent grey ellipses at different positions in each frame.

![A slow animation of the smoke effect.](images/rocket_smoke.gif)

--- task ---

This time the `fill()` is outside the loop as the colour is the same for each smoke ellipse. The fourth input to `fill()` is the opacity, a low opacity value makes the colour more transparent so you can see the shapes underneath.

In each frame of the animation, 20 ellipses of random sizes will be drawn at random positions.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 18
line_highlights: 22-24
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

**Test:** Run your program and check the exhaust fumes are visible.

![An animation of the rocket and exhaust trail with added smoke.](images/rocket_exhaust_circles.gif)

--- /task ---

--- save ---
