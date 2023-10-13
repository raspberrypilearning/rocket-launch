## Alcançando a órbita

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

O objetivo do lançamento do foguete é colocar um satélite em órbita. 

Uma órbita é um caminho curvo que um objeto percorre em torno de outro devido à gravidade.

O foguete pode mudar de cor para mostrar o sucesso do lançamento. 

</div>
<div>

![Three side-by-side images showing successful (green tint), over-fueled (amber tint), and unsuccessful (red tint) launches.](images/check_orbit.png){:width="400px"}

</div>
</div>

### Draw an orbit line

--- task ---

Crie duas novas variáveis globais para definir o raio do círculo da órbita e a coordenada `y` da órbita para o ponto que o centro do foguete precisa alcançar para lançar o satélite.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11-12
---

# Configurar variáveis globais
screen_size = 400   
rocket_y = screen_size   
burn = 100   
orbit_radius = 250   
orbit_y = screen_size - orbit_radius

--- /code ---

--- /task ---

--- task ---

Atualize a função `desenhar_plano_de_fundo()` para desenhar uma elipse para representar a órbita do satélite que o foguete precisa alcançar.

--- code ---
---
language: python filename: main.py - draw_background() line_numbers: true line_number_start: 38
line_highlights: 42-45
---

def draw_background():   
background(0)  # Short for background(0, 0, 0) — black   
image(planet, width/2, height, 300, 300)   

    no_fill()  # Turn off any fill  
    stroke(255)  # Set a white stroke   
    stroke_weight(2)   
    ellipse(width/2, height, orbit_radius * 2, orbit_radius * 2)

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

You can use an `and` in `if` statements to check if two, or more, conditions are true.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 19
---

# A função desenhar_foguete vai aqui
def draw_rocket():   
global rocket_y, fuel, burn

        if fuel >= burn and rocket_y > orbit_y:  # Still flying

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

The `tint()` function sets the tint colour for all images that are drawn until you change the tint or use `no_tint()` to turn it off.

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

Use the `tint()` function again, this time to colour the rocket green if the rocket has enough fuel to reach the satellite orbit:

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
