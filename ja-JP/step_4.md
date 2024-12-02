## 排気効果

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Add some grey circles to simulate the exhaust trail. 
</div>
<div>

煙の効果の遅いアニメーション。
</div>
</div>

--- task --- Set the fill colour for the smoke to transparent grey.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 14
---

def draw_rocket():


--- /code ---

--- /task ---


--- task --- The outline around the circles is called the **stroke**. Add some code to turn it off.


--- code ---
---
language: python line_numbers: true line_number_start: 14
line_highlights: 15
---

    fill(200, 200, 200, 100) 
    no_stroke()


--- /code ---

--- /task ---


--- task ---

Generate a random number between 5 and 10 for the size of the circle, then draw it at the bottom of the rocket.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 16-22
---

no_stroke() circle_size = randint(5,10) ellipse( screen_size/2, rocket_position, circle_size, circle_size )

--- /code ---

--- /task ---

--- task ---

**テスト：** プログラムを実行し、排気ガスが見えることを確認します。

--- /task ---

--- task ---

Indent the code you used to draw the circle, and add a loop which will run the code 20 times.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 12
images/rocket_exhaust.png
---

fill(200, 200, 200, 100) #透明な灰色   
for i in range(20): #排煙をランダムに20回描画    
ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))


--- /code ---

--- /task ---

--- task ---

**テスト：** コードを実行して、ロケットに新しい排気ガスの軌跡があることを確認します。 You will still see a flashing grey circle at the bottom of the rocket - all of the circles have been drawn on top of each other!

--- /task ---

--- task --- Generate a random number and add it to the x and y position of each circle so they aren't all drawn in the same place.


--- code ---
---
for i in range(25):   
fill(255, 255 - i * 10, 0) #緑の量を減らす    
ellipse(width/2, rocket_y + i, 8, 3)
line_highlights: 23-26
---

for i in range(25):  
fill(255, 255 - i * 10, 0)   
ellipse(width/2, rocket_y + i, 8, 3)

--- /code ---

--- /task ---




--- task --- **Test:** Run your program and you should see lots of grey circles in random places at the bottom of the rocket. --- /task ---