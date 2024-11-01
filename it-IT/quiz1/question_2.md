
--- question ---
---
legend: Domanda 2 di 3
---

Un progetto ha questo codice di `configurazione (setup)` per caricare un'immagine del pianeta e dire che le immagini dovrebbero essere posizionate al centro:

--- code ---
---
language: python
---

def setup():   
size(400, 400)   
image_mode(CENTER)   
global planet   
planet = load_image('planet.png')

--- /code ---

Le coordinate iniziano da (0, 0) nell'angolo in alto a sinistra. Nel progetto hai disegnato immagini di pianeti e razzi utilizzando la funzione `image(nome_file_immagine, coordinata-x, coordinata-y, larghezza-x, larghezza-y)`.

Questo codice dove posizionerà l’immagine del pianeta?

--- code ---
---
language: python
---

image(planet, 300, 100, 128, 128)

--- /code ---

--- choices ---

- ( ) ![Un'immagine del pianeta posizionata orizzontalmente a destra dello schermo e verticalmente al centro.](images/planet400200.png)

  --- feedback ---

Il secondo e il terzo input della funzione `image()` sono le coordinate `x` e `y` per il centro dell'immagine. Questo pianeta ha le coordinate `(400, 200)`.

  --- /feedback ---

- ( ) ![Un'immagine del pianeta posizionata al centro del quadrante in basso a sinistra.](images/planet100300.png)

  --- feedback ---

Il secondo e il terzo input della funzione `image()` sono le coordinate `x` e `y` per il centro dell'immagine. Questo pianeta ha le coordinate `(100, 300)`.

  --- /feedback ---

- (x) ![Un'immagine del pianeta posizionata al centro del quadrante in basso a destra.](images/planet300100.png)

  --- feedback ---

Corretto! Il secondo e il terzo input della funzione `image()` sono le coordinate `x` e `y` per il centro dell'immagine. Questa immagine ha le coordinate (300, 100), quindi è 300 (su 400) pixel da sinistra per la coordinata `x` e 100 (su 400) pixel verso il basso dalla sommità.

  --- /feedback ---

- () ![Un'immagine del pianeta posizionata al centro del quadrante in alto a sinistra.](images/planet128128.png)

  --- feedback ---

Il quarto e il quinto input danno la dimensione dell'immagine. Il secondo e il terzo input della funzione `image()` sono le coordinate `x` e `y` per il centro dell'immagine. Questo pianeta ha le coordinate `(128, 128)`.

  --- /feedback ---

--- /choices ---

--- /question ---
