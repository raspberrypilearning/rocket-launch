## Prepara la scena

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
L'animazione necessita di uno sfondo spaziale con un pianeta da cui lanciare il razzo.
</div>
<div>

![Un pianeta su sfondo nero.](images/step_2.png){:width="300px"}

</div>
</div>

--- task ---

Apri il [template del progetto](https://editor.raspberrypi.org/en/projects/rocket-launch-starter){:target="_blank"}.

### Crea lo schermo

--- /task ---

Utilizzerai una variabile `screen_size` per impostare la dimensione dello schermo e nei calcoli. Le variabili definite all'esterno delle funzioni sono **globali** quindi puoi usarle ovunque nel tuo programma.

--- task ---

Trova il commento `Imposta le variabili globali` e aggiungi una riga di codice per creare la variabile `screen_size`:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# Imposta le variabili globali
screen_size = 400

--- /code ---

--- /task ---

--- task ---

Utilizza la variabile `screen_size` per creare un quadrato di 400 x 400 pixel:

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 20
---

def setup():   
# Imposta qui la tua animazione   
size(screen_size, screen_size)


--- /code ---

--- /task ---

### Scegli un'immagine

--- task ---

Il progetto iniziale prevede tre diverse immagini del pianeta e della luna. Puoi visualizzarli nella **Galleria immagini** sul lato sinistro dell'editor di codice.

![Uno screenshot dell'editor del codice, con la galleria di immagini evidenziata contenente immagini di pianeti e della luna.](images/image_gallery.png)

**Scegli:** Decidi quale immagine vuoi utilizzare e prendi nota del nome del file. Ad esempio, `orange_planet.png`.

--- /task ---

--- task ---

Aggiungi il codice alla funzione `setup()` per caricare e posizionare la tua immagine.

La riga `image_mode(CENTER)` dice che posizionerai le immagini fornendo le coordinate del centro dell'immagine (invece dell'angolo in alto a sinistra).

Successivamente carica la tua immagine nella variabile globale `planet`. La variabile deve essere globale in modo da poterla utilizzare in seguito quando disegni il pianeta sullo schermo.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 21-23
---

def setup():   
# Imposta qui la tua animazione   
size(screen_size, screen_size)   
image_mode(CENTER) # Posiziona l'immagine al centro global planet   
planet = load_image('planet.png') # Il pianeta scelto


--- /code ---

--- /task ---

### Disegna lo sfondo

--- task ---

Definisci una funzione `draw_background()`, per disegnare lo sfondo, sotto il commento che ti dice dove dovrebbe andare.

Usa `background(0)` per impostare il colore di sfondo su nero e aggiungi una funzione `image()` per disegnare il pianeta. La funzione `image()` è così strutturata:

`image(nome immagine, coordinata x, coordinata y, larghezza, altezza)`

La riga di codice `from p5 import *` fornisce le variabili globali `width` e `height` in base alla dimensione dello schermo. Usali nel tuo codice per posizionare il pianeta con il suo centro a metà strada (`width/2`) e nella parte inferiore (`height`) del schermo.

--- code ---
---
language: python filename: main.py — draw_background() line_numbers: true line_number_start: 14
line_highlights: 15-17
---

# La funzione draw_background va qui
def draw_background():   
background(0)  # Abbreviazione per background(0, 0, 0) — black    
image(planet, width/2, height, 300, 300)  # Disegna l'immagine


--- /code ---

Inserire tutto il codice per disegnare lo sfondo in un'unica funzione semplifica la comprensione del codice.

--- /task ---

--- task ---

Per far apparire lo sfondo, richiama `draw_background()` in `draw()`. Ciò farà sì che lo sfondo venga ridisegnato ogni volta che viene chiamata `draw()`, coprendo qualsiasi disegno precedente:

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 28
line_highlights: 30
---

def draw():   
# Cose da fare in ogni fotogramma    
draw_ background()

--- /code ---

--- /task ---

--- task ---

**Test:** Esegui il codice e controlla che disegni uno sfondo nero con mezzo pianeta in basso.

--- /task ---

Se disponi di un account Raspberry Pi, puoi fare clic sul pulsante **Salva** per salvarne una copia tra i tuoi progetti.

--- save ---
