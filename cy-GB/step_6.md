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

--- task ---

Ewch ati i greu dau newidyn cyffredinol newydd i osod radiws y cylch orbit a chyfesuryn `y` yr orbit i'r pwynt mae canol y roced angen ei gyrraedd i lansio'r lloeren.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11-12
---

# Gosod newidynnau cyffredinol
screen_size = 400   
rocket_y = screen_size   
burn = 100   
orbit_radius = 250   
orbit_y = screen_size - orbit_radius

--- /code ---

--- /task ---

--- task ---

Diweddarwch y swyddogaeth `llunio_cefndir()` i lunio elips i gynrychioli orbit y lloeren mae angen i'r roced ei gyrraedd.

--- code ---
---
language: python filename: main.py - draw_background() line_numbers: true line_number_start: 37
line_highlights: 42-45
---

def draw_background():   
background(0) #Short for background(0, 0, 0) — black   
image(planet, width/2, height, 300, 300)

  no_fill() #Turn off any fill  
stroke(255) #Set a white stroke   
stroke_weight(2)   
ellipse(width/2, height, orbit_radius * 2, orbit_radius * 2)

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich rhaglen a gwneud yn siŵr bod llinell orbit wen yn cael ei llunio.

![Y sgrin gyda phlaned a llinell orbit newydd.](images/draw_orbit.png){:width="300px"}

--- /task ---

Dylai'r roced stopio pan fydd yn cyrraedd orbit y lloeren — diwedd y daith.

--- task ---

Diweddarwch eich cod `if tanwydd >= llosgi` hefyd i wneud yn siŵr nad yw'r roced wedi cyrraedd yr orbit.

Fe allwch chi ddefnyddio datganiadau `and` yn `if` i wirio bod dau amod neu fwy yn wir.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 14
line_highlights: 19
---

# Mae'r swyddogaeth llunio_roced yn mynd fan hyn
def draw_rocket():

  global rocket_y, fuel, burn

    if fuel >= burn and rocket_y > orbit_y: #Still flying

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich prosiect a rhoi `50000` fel y cyfaint tanwydd. Dylai hyn fod yn ddigon o danwydd i gyrraedd orbit. Dylai'r roced stopio symud pan fydd yn cyrraedd orbit.

--- /task ---

Dylai'r roced fod yn goch os yw ei thanwydd yn dod i ben cyn iddi gyrraedd yn ddigon uchel i lansio'r lloeren.

--- task ---

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 30
line_highlights: 34-35
---

    fill(200, 200, 200, 100)   
    for i in range(20):   
      ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

  if fuel < burn and rocket_y > orbit_y: #No more fuel and not in orbit tint(255, 0, 0) #Failure

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich cod a rhoi `20000` fel y cyfaint tanwydd. Gwnewch yn siŵr bod y roced yn troi'n goch pan fydd yn stopio o dan yr orbit.

![Roced goch sydd wedi rhedeg allan o danwydd cyn cylch yr orbit. Mae'r blaned wedi troi'n goch hefyd.](images/orbit_failure.png){:width="300px"}

O na, mae'r blaned wedi troi'n goch!

--- /task ---

--- task ---

Mae'r swyddogaeth `tint()` yn gosod yr arlliw ar gyfer bob delwedd sy'n cael ei llunio nes eich bod yn newid yr arlliw neu'n defnyddio `no_tint()` i'w diffodd.

**Dewiswch:** Ychwanegwch alwad at `no_tint()` ar ôl llunio'r ddelwedd er mwyn atal y blaned rhag cael arlliw coch yn y ffrâm nesaf — neu ei adael os ydych chi'n dymuno i'r blaned droi'n goch!

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 34
line_highlights: 38
---

if fuel < burn and rocket_y > orbit_y: tint(255, 0, 0) #Failure

image(rocket, width/2, rocket_y, 64, 64)   
no_tint() #So the planet isn't tinted red in the next frame!


--- /code ---

--- /task ---

--- task ---

Defnyddiwch y swyddogaeth `tint()` eto, y tro hwn i liwio'r roced yn wyrdd os oes gan y roced ddigon o danwydd i gyrraedd orbit y lloeren:

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 34
line_highlights: 36-37
---

if fuel < burn and rocket_y > orbit_y: tint(255, 0, 0) #Failure   
elif rocket_y <= orbit_y:   
tint(0, 255, 0) #Success

image(rocket, width/2, rocket_y, 64, 64)   
no_tint()

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich prosiect a rhoi `50000` fel y cyfaint tanwydd. Gwnewch yn siŵr bod eich roced yn troi'n wyrdd pan fydd yn cyrraedd orbit y lloeren.

![Roced werdd sydd wedi cyrraedd y cylch orbit ac sydd â thanwydd yn weddill.](images/orbit_success.png){:width="300px"}

--- /task ---

Nawr mae gennych chi efelychiad gellir ei ddefnyddio i ddangos faint o danwydd sydd ei angen fan leiaf i gyrraedd orbit y lloeren. Gwych; fodd bynnag, fe allech chi fynd â llwyth o danwydd a llwyddo, ond mae hynny'n gostus ac yn wastraffus!

--- task ---

Newidiwch yr amodau yn eich cod llwyddiant er mwyn i'r roced ddim ond troi'n wyrdd os yw'n cyrraedd yr orbit a bod ganddi lai na 1,000kg o danwydd yn weddill.

Ychwanegwch god i liwio'r roced yn felyn os oes gan y roced fwy na 1,000kg o danwydd yn weddill pan fydd yn cyrraedd orbit.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 34
line_highlights: 36, 38-39
---

if fuel < burn and rocket_y > orbit_y: tint(255, 0, 0) #Failure   
elif fuel < 1000 and rocket_y <= orbit_y:   
tint(0, 255, 0) #Success   
elif fuel >= 1000 and rocket_y <= orbit_y:    
tint(255, 200, 0) #Too much fuel

image(rocket, width/2, rocket_y, 64, 64)    
no_tint() #So the planet isn't tinted in the next frame!

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich cod nifer o weithiau gyda gwahanol rifau; er enghraifft, dylai 25,000kg fod y cyfaint sydd ei angen i droi'r roced yn wyrdd, ond gwnewch yn siŵr bod yr arlliw melyn yn gweithio hefyd drwy ddefnyddio rhif mwy.

![Roced felen sydd wedi cyrraedd y cylch orbit gyda thanwydd yn weddill.](images/orbit_meh.png){:width="300px"}

--- /task ---

--- save ---
