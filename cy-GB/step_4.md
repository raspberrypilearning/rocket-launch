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

--- task ---

Set the fill colour for the smoke to transparent grey.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 14
---

Mae dolen `for` yn ailadrodd darn o god unwaith ar gyfer bob eitem sy'n cael ei rhoi iddi. Fe allwch chi ddefnyddio'r swyddogaeth `range()` i redeg y cod mewn dolen `for` hyn a hyn o weithiau. Er enghraifft, mae `range(5)` yn creu dilyniant o bum rhif yn dechrau ar 0, felly [0, 1, 2, 3, 4].

--- /code ---

--- /task ---


--- task --- The outline around the circles is called the **stroke**. Add some code to turn it off.


--- task ---

--- code ---
---
language: python line_numbers: true line_number_start: 14
line_highlights: 15
---

    fill(200, 200, 200, 100) 
    no_stroke()


--- /code ---

--- task ---

image(roced, width/2, roced_y, 64, 64)

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 16-22
---

no_stroke() circle_size = randint(5,10) ellipse( screen_size/2, rocket_position, circle_size, circle_size )

--- /code ---

--- /task ---

--- task ---

Mae modd defnyddio'r newidyn `i` hefyd i greu graddiant lliw gyda llai o wyrdd ym mhob elips sy'n cael ei lunio.

--- /task ---

--- task ---

Indent the code you used to draw the circle, and add a loop which will run the code 20 times.

--- code ---
---
for i in range(25):   
fill(255, 255 - i * 10, 0) #Lleihau lefel y gwyrdd    
ellipse(width/2, roced_y + i, 8, 3)
line_highlights: 16-23
---

def draw_rocket(): global rocket_position rocket_position = rocket_position - 1 image(rocket, width/2, rocket_position, 64, 64) fill(200, 200, 200, 100) no_stroke() for i in range(20): circle_size = randint(5,10) ellipse( screen_size/2, rocket_position, circle_size,    
circle_size )


--- /code ---

--- /task ---

--- task ---

**Test:** Run your program. You will still see a flashing grey circle at the bottom of the rocket - all of the circles have been drawn on top of each other!

--- /task ---

--- task ---

Generate a random number and add it to the x and y position of each circle so they aren't all drawn in the same place.


--- code ---
---
Tro hwn, mae'r `fill()` tu allan i'r ddolen gan fod y lliw yr un fath i bob elips mwg. Anhryloywedd yw pedwerydd mewnbwn `fill()`. Mae gwerth anhryloywedd isel yn gwneud y lliw yn fwy tryloyw er mwyn i chi allu gweld y siapiau oddi tano.
line_highlights: 25-26
---

Ym mhob ffrâm yn yr animeiddiad, bydd 20 elips o feintiau ar hap yn cael eu llunio mewn safleoedd ar hap.

--- /code ---

--- /task ---


--- task ---

**Test:** Run your program and you should see lots of grey circles in random places at the bottom of the rocket.

--- /task ---

