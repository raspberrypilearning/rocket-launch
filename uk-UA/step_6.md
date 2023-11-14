## Вихід на орбіту

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Мета запуску ракети - вивести супутник на орбіту. 

Орбіта - це зігнута лінія, по якій рухається один об'єкт навколо іншого під дією сили тяжіння.

Ракета може змінювати колір, щоб показати успішність свого запуску. 

</div>
<div>

![Три зображення, які демонструють: успіх (зелений колір), перевантаження паливом (янтарний колір) та невдалий запуск (червоний колір).](images/check_orbit.png){:width="400px"}

</div>
</div>

### Draw an orbit line

--- task ---

Створи дві нові глобальні змінні, щоб встановити радіус кола орбіти та координату орбіти `y` до точки, якої повинен досягти центр ракети, щоб запустити супутник.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11-12
---

# Налаштування глобальних змінних
screen_size = 400   
rocket_y = screen_size   
burn = 100   
orbit_radius = 250   
orbit_y = screen_size - orbit_radius

--- /code ---

--- /task ---

--- task ---

Онови функцію `draw_background()`, щоб намалювати овал, який буде відображати орбіту супутника, яку ракета повинна досягти.

--- code ---
---
language: python filename: main.py - draw_background() line_numbers: true line_number_start: 37
line_highlights: 42-45
---

def draw_background():   
background(0) #Скорочено від background(0, 0, 0) - чорний   
image(planet, width/2, height, 300, 300)   

    if fuel >= burn and rocket_y > orbit_y: #Продовжує летіти

--- /code ---

--- /task ---

--- task ---

**Test:** Run your program and check that a white orbit line is drawn.

![The screen with planet and new orbit line.](images/draw_orbit.png){:width="300px"}

--- /task ---

### Launch the rocket to the orbit

The rocket should stop when it reaches the satellite orbit — the end of the mission.

--- task ---

Update your `if fuel >= burn` code to also check that the rocket hasn't reached the orbit.

Онови свій код `if fuel >= burn`, щоб також перевіряти, якщо ракета не буде досягати орбіти.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 19
---

# Функція draw_rocket викликається тут
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 14

        fill(200, 200, 200, 100)   
    for i in range(20):   
      ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

--- /code ---

--- /task ---

--- task ---

**Test:** Run your project and enter `50000` as the amount of fuel. This should be plenty of fuel to reach orbit. The rocket should stop moving when it reaches orbit.

--- /task ---

### Check if the launch is successful

The rocket should be coloured red if it runs out of fuel before getting high enough to launch the satellite.

--- task ---

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 30
line_highlights: 34-35
---

    fill(200, 200, 200, 100)   
    for i in range(20):   
        ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))
    
    if fuel < burn and rocket_y > orbit_y:  # No more fuel and not in orbit   
        tint(255, 0, 0)  # Failure

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and enter `20000` as the amount of fuel. Check that the rocket turns red when it stops below the orbit.

![A red rocket that has run out of fuel before the orbit circle. The planet has also turned red.](images/orbit_failure.png){:width="300px"}

Oh no, the planet has turned red!

--- /task ---

--- task ---

О ні, планета теж стала червоною!

**Choose:** Add a call to `no_tint()` after drawing the image so that the planet isn't tinted red in the next frame — or leave it if you like the planet turning red!

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 34
line_highlights: 38
---

    if fuel < burn and rocket_y > orbit_y:    
        tint(255, 0, 0)  # Failure
    
    image(rocket, width/2, rocket_y, 64, 64)   
    no_tint()  # So the planet isn't tinted red in the next frame!


--- /code ---

--- /task ---

--- task ---

if fuel < burn and rocket_y > orbit_y: tint(255, 0, 0) #Провал

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 34
line_highlights: 36-37
---

    if fuel < burn and rocket_y > orbit_y:    
        tint(255, 0, 0)  # Failure   
    elif rocket_y <= orbit_y:   
        tint(0, 255, 0)  # Success   
    
    image(rocket, width/2, rocket_y, 64, 64)   
    no_tint()

--- /code ---

--- /task ---

--- task ---

**Test:** Run your project and enter `50000` as the amount of fuel. Check that your rocket turns green when it reaches the satellite orbit.

![A green rocket that has reached the orbit circle and has fuel left.](images/orbit_success.png){:width="300px"}

--- /task ---

You now have a simulation that can be used to show how much fuel is needed as a minimum to reach the satellite orbit. That's great; however, you could take a huge amount of fuel and still be successful, but this is costly and wasteful!

--- task ---

Amend the conditions in your success code so that the rocket only turns green if it reaches the orbit `and` has less than 1,000kg of fuel left.

Add code to colour the rocket yellow if the rocket has more than 1,000kg of fuel left when it reaches orbit.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 34
line_highlights: 36, 38-39
---

    if fuel < burn and rocket_y > orbit_y:   
        tint(255, 0, 0)  # Failure   
    elif fuel < 1000 and rocket_y <= orbit_y:   
        tint(0, 255, 0)  # Success   
    elif fuel >= 1000 and rocket_y <= orbit_y:    
        tint(255, 200, 0)  # Too much fuel   
    
    image(rocket, width/2, rocket_y, 64, 64)    
    no_tint()  # So the planet isn't tinted in the next frame!

--- /code ---

--- /task ---

--- task ---

**Test:** Run your program several times with different numbers; for example, 25,000kg of fuel should be the amount needed to turn the rocket green, but also check that the yellow tint works too by using a bigger number.

![A yellow rocket that has reached the orbit circle and has fuel left.](images/orbit_meh.png){:width="300px"}

--- /task ---

--- save ---
