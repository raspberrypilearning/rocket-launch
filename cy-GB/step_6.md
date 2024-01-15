## Cyrraedd orbit

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Pwrpas lansio'r roced yw gyrru lloeren i orbit. 

Mae orbit yn llwybr crwn mae un gwrthrych yn ei ddilyn o amgylch gwrthrych arall o ganlyniad i ddisgyrchiant.

Mae'r roced yn gallu newid lliw i ddangos pa mor llwyddiannus oedd y lansiad. 

</div>
<div>

![Tair delwedd ochr yn ochr yn dangos lansiadau llwyddiannus (arlliw gwyrdd), gormod o danwydd (arlliw melyngoch) ac aflwyddiannus (arlliw coch).](images/check_orbit.png){:width="400px"}

</div>
</div>

### Draw an orbit line

--- task ---

Ewch ati i greu dau newidyn cyffredinol newydd i osod radiws y cylch orbit a chyfesuryn `y` yr orbit i'r pwynt mae canol y roced angen ei gyrraedd i lansio'r lloeren.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11-12
---

# Gosod newidynnau cyffredinol
screen_size = 400   
roced_y = screen_size   
llosgi = 100   
radiws_orbit = 250   
orbit_y = screen_size - radiws_orbit

--- /code ---

--- /task ---

--- task ---

Diweddarwch y swyddogaeth `llunio_cefndir()` i lunio elips i gynrychioli orbit y lloeren mae angen i'r roced ei gyrraedd.

--- code ---
---
language: python filename: main.py - llunio_cefndir() line_numbers: true line_number_start: 37
line_highlights: 42-45
---

def llunio_cefndir():   
background(0) #Byr ar gyfer cefndir(0, 0, 0) — black   
image(planed, width/2, height, 300, 300)   

    if tanwydd >= llosgi and roced_y > orbit_y: #Dal yn hedfan

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

Diweddarwch eich cod `if tanwydd >= llosgi` hefyd i wneud yn siŵr nad yw'r roced wedi cyrraedd yr orbit.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 19
---

# Mae'r swyddogaeth llunio_roced yn mynd fan hyn
language: python filename: main.py - llunio_roced() line_numbers: true line_number_start: 14

        fill(200, 200, 200, 100)   
    for i in range(20):   
      ellipse(width/2 + randint(-5, 5), roced_y + randint(20, 50), randint(5, 10), randint(5, 10))

--- /code ---

--- /task ---

--- task ---

**Test:** Run your project and enter `50000` as the amount of fuel. This should be plenty of fuel to reach orbit. The rocket should stop moving when it reaches orbit.

--- /task ---

### Check if the launch is successful

**Profi:** Rhedwch eich prosiect a rhoi `50000` fel y cyfaint tanwydd. Dylai hyn fod yn ddigon o danwydd i gyrraedd orbit. Dylai'r roced stopio symud pan fydd yn cyrraedd orbit.

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

O na, mae'r blaned wedi troi'n goch!

**Choose:** Add a call to `no_tint()` after drawing the image so that the planet isn't tinted red in the next frame — or leave it if you like the planet turning red!

--- code ---
---
Mae'r swyddogaeth `tint()` yn gosod yr arlliw ar gyfer bob delwedd sy'n cael ei llunio nes eich bod yn newid yr arlliw neu'n defnyddio `no_tint()` i'w diffodd.
line_highlights: 38
---

    if fuel < burn and rocket_y > orbit_y:    
        tint(255, 0, 0)  # Failure
    
    image(rocket, width/2, rocket_y, 64, 64)   
    no_tint()  # So the planet isn't tinted red in the next frame!


--- /code ---

--- /task ---

--- task ---

if tanwydd < llosgi and roced_y > orbit_y: tint(255, 0, 0) #Methiant

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

Newidiwch yr amodau yn eich cod llwyddiant er mwyn i'r roced ddim ond troi'n wyrdd os yw'n cyrraedd yr orbit a bod ganddi lai na 1,000kg o danwydd yn weddill.

![A yellow rocket that has reached the orbit circle and has fuel left.](images/orbit_meh.png){:width="300px"}

--- /task ---

--- save ---
