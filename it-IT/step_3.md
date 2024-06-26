## Decollo!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ogni volta che viene disegnato un nuovo fotogramma, il razzo deve spostarsi verso l'alto sullo schermo per creare un effetto di animazione.
</div>
<div>

![Un razzo che vola a velocità costante dal basso verso l'alto dello schermo.](images/fly.gif){:width="300px"}

</div>
</div>

--- task ---

Il progetto iniziale include l'immagine di un razzo.

![Immagine del razzo nella galleria immagini dell'editor di codice.](images/rocket_image.png)

--- /task ---

--- task ---

Aggiungi il codice alla funzione `setup()` per caricare l'immagine del razzo in una variabile globale `rocket` .

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 24, 26
---

def setup():   
    # Imposta qui la tua animazione   
    size(screen_size, screen_size)   
    image_mode(CENTER)   
    global planet, rocket   
    planet = load_image('planet.png')    
    rocket = load_image('rocket.png')

--- /code ---

--- /task ---

### Fai volare il razzo

La posizione `y` del razzo inizierà a 400 (l'altezza dello schermo) e poi diminuirà di 1 ogni volta che viene disegnato un nuovo fotogramma.

--- task ---

Aggiungi una variabile globale `rocket_y` per tenere traccia della posizione `y` del razzo.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7 
line_highlights: 9
---

# Imposta le variabili globali
screen_size = 400    
rocket_y = screen_size # Inizia dal basso

--- /code ---

--- /task ---

--- task ---

Definisci una funzione `draw_rocket()` per modificare la posizione `y` del razzo e ridisegnarlo.

`rocket_y -= 1`è un modo più breve per dire `rocket_y = rocket_y - 1`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 11 
line_highlights: 12-16 
---

# La funzione draw_rocket va qui
def draw_rocket():   
    global rocket_y  # Usa la variabile globale rocket_y variable    
    rocket_y -= 1  # Muove il razzo    
    image(rocket, width/2, rocket_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

Richiama la tua nuova funzione `draw_rocket()` nella funzione `draw()` in modo che il razzo venga ridisegnato a ogni fotogramma.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 33 
line_highlights: 36
---

def draw():   
    # Cose da fare ad ogni cambio di frame   
    draw_background()   
    draw_rocket()


--- /code ---

--- /task ---

--- task ---  

**Test:** Esegui il codice per verificare che il razzo parta dalla parte inferiore dello schermo e si muova verso l'alto in ogni fotogramma.

![Animazione del razzo che vola a metà dello schermo.](images/rocket_fly.gif)

--- /task ---

--- save ---
