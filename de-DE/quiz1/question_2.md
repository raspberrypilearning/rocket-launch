
--- question ---
---
legend: Frage 2 von 3
---

Ein Projekt hat diesen `setup`-Code, um ein Planetenbild zu laden und anzugeben, dass Bilder in dessen Mitte positioniert werden sollen:

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

Die Koordinaten beginnen bei (0, 0) in der oberen linken Ecke. Im Projekt hast Du Planeten- und Raketenbilder mit der Funktion `image(bild_datei, x-Koordinate, y-Koordinate, x-Breite, y-Breite)` gezeichnet.

Wo wird dieser Code das Planetenbild positionieren?

--- code ---
---
language: python
---

image(planet, 300, 100, 128, 128)

--- /code ---

--- choices ---

- ( ) ![Ein Planetenbild, das horizontal rechts auf dem Bildschirm und vertikal in der Mitte positioniert ist.](images/planet400200.png)

  --- feedback ---

Die zweiten und dritten Eingaben der Funktion `image()` sind die Koordinaten `x` und `y` für die Bildmitte. Dieser Planet hat die Koordinaten `(400, 200)`.

  --- /feedback ---

- ( ) ![Ein Planetenbild in der Mitte des unteren linken Quadranten.](images/planet100300.png)

  --- feedback ---

Die zweiten und dritten Eingaben der Funktion `image()` sind die Koordinaten `x` und `y` für die Bildmitte. Dieser Planet hat die Koordinaten `(100, 300)`.

  --- /feedback ---

- (x) ![Ein Planetenbild in der Mitte des oberen rechten Quadranten.](images/planet300100.png)

  --- feedback ---

Korrekt! Die zweiten und dritten Eingaben der Funktion `image()` sind die Koordinaten `x` und `y` für die Bildmitte. Dieses Bild hat die Koordinaten (300, 100), es liegt also 300 (von 400) Pixel von links für die Koordinate `x` und 100 (von 400) Pixel von oben.

  --- /feedback ---

- () ![Ein Planetenbild im oberen linken Quadranten.](images/planet128128.png)

  --- feedback ---

Der vierte und fünfte Eingaben geben die Größe des Bildes an. Die zweiten und dritten Eingaben der Funktion `image()` sind die Koordinaten `x` und `y` für die Bildmitte. Dieser Planet hat die Koordinaten `(128, 128)`.

  --- /feedback ---

--- /choices ---

--- /question ---
