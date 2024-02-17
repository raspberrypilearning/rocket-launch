## Effetti dei gas di scarico

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Il razzo apparirà più realistico con alcuni effetti speciali per simulare la scia di scarico. 

Puoi creare fantastici effetti utilizzando un ciclo "for" per disegnare molte forme in ciascun fotogramma.

</div>
<div>

![The rocket mid flight with an exhaust trail.](images/flying_rocket.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Il coding viene utilizzato per creare <span style="color: #0faeb0">**effetti grafici**</span> per film e giochi. È molto più veloce scrivere il codice che disegnare individualmente ciascun fotogramma di un'animazione. </p>

### Disegna i tuoi gas di scarico

Disegnare molte ellissi gialle in diverse posizioni `y` crea una scia di scarico con un fondo rotondo.

--- task ---

Aggiorna la tua funzione `draw_rocket()` per includere un ciclo `for` che ripete il disegno di `25` ellissi di scarico. La  **variabile del ciclo** `i` viene aggiunta a `rocket_y` per disegnare ciascuna ellisse più in basso del razzo.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 12
line_highlights: 16-20
---

def draw_rocket(): global rocket_y   
rocket_y -= 1   

    no_stroke()  # Fa in modo che non venga disegnata la linea
    
    for i in range(25):  # Disegna 25 ellissi di gas di scarico
        fill(255, 255, 0)  # Giallo
        ellipse(width/2, rocket_y + i, 8, 3)  # aumenta I ad ogni ciclo 
    
    image(rocket, width/2, rocket_y, 64, 64)


--- /code ---

--- /task ---

Un ciclo `for` ripete un pezzo di codice una volta per ogni elemento fornito.

Per eseguire il codice in un ciclo `for` un certo numero di volte, puoi utilizzare la funzione `range()`. Ad esempio, `range(5)` crea una sequenza di cinque numeri a partire da 0, quindi [0, 1, 2, 3, 4].

Ogni volta che il ciclo `for` si ripete, imposta una variabile sull'elemento corrente in modo da poterlo utilizzare nel ciclo.

--- task ---

**Test:** Esegui il codice per verificare che il razzo abbia una nuova scia di scarico.

![A close-up of the rocket with an exhaust trail.](images/rocket_exhaust.png){:width="300px"}

--- /task ---

### Aggiungi una sfumatura

La variabile `i` può essere utilizzata anche per creare una sfumatura di colore con meno verde in ogni ellisse disegnata.

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
