## Efeitos da combustão

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Add some grey circles to simulate the exhaust trail. 
</div>
<div>

Uma animação lenta do efeito de fumaça.
</div>
</div>

--- task ---

Set the fill colour for the smoke to transparent grey.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 14
---

def desenhar_foguete(): global foguete_y   
foguete_y -= 1

--- /code ---

--- /task ---


--- task ---

The outline around the circles is called the **stroke**. Add some code to turn it off.


--- /task ---

--- code ---
---
language: python line_numbers: true line_number_start: 14
line_highlights: 15
---

    fill(200, 200, 200, 100) 
    no_stroke()


--- /code ---

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

**Teste:** Execute o seu programa e verifique que os gases de escape estão visíveis.

--- /task ---

--- task ---

Indent the code you used to draw the circle, and add a loop which will run the code 20 times.

--- code ---
---
Altere a chamada para `fill()` para definir a quantidade de verde para `255 - i*10` para que a primeira elipse tenha quantidades iguais de vermelho e verde e a última elipse tenha muito pouco verde.
line_highlights: 16-23
---

no_stroke()  # Desliga o traço for i in range(25): # Desenhe 25 elipses de combustão em chamas fill(255, 255, 0) # Amarelo ellipse(width/2, foguete_y + i, 8, 3) # i aumenta cada vez que o ciclo se repete image(rocket, width/2, foguete_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu código para verificar que o foguete tem um novo rastro de combustão. You will still see a flashing grey circle at the bottom of the rocket - all of the circles have been drawn on top of each other!

--- /task ---

--- task ---

Generate a random number and add it to the x and y position of each circle so they aren't all drawn in the same place.


--- code ---
---
for i in range(25):  
fill(255, 255 - i * 10, 0)   
ellipse(width/2, foguete_y + i, 8, 3)
line_highlights: 25-26
---

fill(200, 200, 200, 100)  # Cinza transparente   
for i in range(20):  # Desenhar 20 elipses de fumaça aleatórias    
ellipse(width/2 + randint(-5, 5), foguete_y + randint(20, 50), randint(5, 10), randint(5, 10))

--- /code ---

--- /task ---


--- task ---

**Test:** Run your program and you should see lots of grey circles in random places at the bottom of the rocket.

--- /task ---

