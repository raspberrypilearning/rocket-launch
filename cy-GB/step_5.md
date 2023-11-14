## Llosgi tanwydd

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Un o'r pethau pwysicaf i benderfynu arnyn nhw wrth lansio roced yw faint o danwydd i'w lwytho arni. 

I wneud hyn, rhaid i chi efelychu faint o danwydd fydd yn cael ei losgi yn ystod y daith.
</div>

![Y rhaglen gyda chwestiwn yn yr ardal allbwn yn gofyn faint o danwydd sydd ei angen.](images/burn_question_full.png){:width="300px"}

</div>

### Create a fuel variable

--- task ---

Ychwanegwch newidyn i gadw golwg ar faint o danwydd mae eich roced yn ei losgi (mewn fframiau).

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 10
---

# Gosod newidynnau cyffredinol
screen_size = 400   
roced_y = screen_size  
llosgi = 100 #Faint o danwydd sy'n cael ei losgi ym mhob ffrâm

--- /code ---

--- /task ---


--- task ---

Ar waelod eich rhaglen, ychwanegwch god i ofyn i'r defnyddiwr faint o danwydd i'w ychwanegu at y roced, a storio ei ateb mewn newidyn `tanwydd` cyffredinol.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 52
line_highlights: 52
---

fuel = int(input('How many kilograms of fuel do you want to use?'))   
run()

--- /code ---

--- /task ---

### Check fuel against burn

Dylai'r roced ddim ond symud os nad yw wedi llosgi ei holl danwydd.

--- task ---

Ychwanegwch god at y swyddogaeth `llunio_roced()` i leihau'r `tanwydd` sy'n weddill o werth `llosgi` bob ffrâm. Defnyddiwch `print()` i ddangos faint o danwydd sy'n weddill ym mhob ffrâm.

Rhaid i chi ddweud eich bod am ddefnyddio'r newidynnau `tanwydd` a `llosgi` cyffredinol.

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 15, 17-18
---

    no_stroke() #Diffodd y strôc   
    
    for i in range(25):   
      fill(255, 255 - i*10, 0)   
      ellipse(width/2, roced_y + i, 8, 3)    
    
    fill(200, 200, 200, 100)   
    for i in range(20):   
      ellipse(width/2 + randint(-5, 5), roced_y + randint(20, 50), randint(5, 10), randint(5, 10))

--- /code ---

--- /task ---

--- task ---

**Test:** Run your program to check that the animation doesn't start until `How many kilograms of fuel do you want to use?` has been answered. Try entering `30000` as the amount of fuel.

**Profi:** Rhedwch eich rhaglen i wneud yn siŵr nad yw'r animeiddiad yn dechrau nes bod `Sawl cilogram o danwydd ydych chi am ei ddefnyddio?` wedi'i ateb. Rhowch gynnig ar roi `30000` fel y cyfaint tanwydd.

![The program with a question in the output area asking how much fuel is required.](images/burn_question.png)

--- /task ---

--- task ---

The rocket should only move if it has enough fuel left. Add an `if` statement to check that `fuel >= burn`.

You will need to indent all of the lines of code before the `image()` function call. To do this, highlight all of the lines with the mouse and then tap the <kbd>Tab</kbd> on the keyboard to indent all the lines at once.

Bydd angen i chi fewnoli'r holl linellau cod cyn galw'r swyddogaeth `image()`. I wneud hyn, amlygwch yr holl linellau gyda'r llygoden a tharo <kbd>Tab</kbd> ar y fysellfwrdd i fewnoli'r holl linellau ar unwaith.

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 16-31
---

    global rocket_y, fuel, burn  
    
    if fuel >= burn:  # Still got fuel   
        rocket_y -= 1   
        fuel -= burn   
        print('Fuel left: ', fuel)   
    
        no_stroke()  # Turn off the stroke   
    
        for i in range(25):   
            fill(255, 255 - i*10, 0)   
            ellipse(width/2, rocket_y + i, 8, 3)    
    
        fill(200, 200, 200, 100)   
        for i in range(20):   
            ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))   
    
    image(rocket, width/2, rocket_y, 64, 64)

--- /code ---

--- /task ---

--- task ---

image(roced, width/2, roced_y, 64, 64)

![Image of a rocket in the middle of the screen with the statement 'Fuel left: 0'.](images/burn_empty.png){:width="300px"}

--- /task ---

Did your rocket stop when it ran out of fuel? Well done, you sent a rocket to outer space!

--- save ---

