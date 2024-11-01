## Einrichten der Szene

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Für die Animation wird ein Weltraumhintergrund mit einem Planeten benötigt, von dem aus die Rakete gestartet werden kann.
</div>
<div>

![Ein Planet vor einem schwarzen Hintergrund.](images/step_2.png){:width="300px"}

</div>
</div>

--- task ---

Öffne die [Projektvorlage](https://editor.raspberrypi.org/de-DE/projects/rocket-launch-starter){:target="_blank"}.

### Erstelle die Bildfläche

--- /task ---

Du verwendest eine Variable `bildschirm_groesse` für die Bildschirmgröße und für Berechnungen. Variablen, die außerhalb von Funktionen definiert werden, sind **global**, dass du sie von überall in deinem Programm verwenden kannst.

--- task ---

Suche den Kommentar `Globale Variablen einrichten` und füge eine Codezeile hinzu, um deine Variable `bildschirm_groesse` zu erstellen:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7 
line_highlights: 8
---

# Globale Variablen einrichten
bildschirm_groesse = 400

--- /code ---

--- /task ---

--- task ---

Benutze die Variable `bildschirm_groesse`, um ein Quadrat mit 400 x 400 Pixeln zu erstellen:

--- code ---
---
language: python
filename: main.py — setup()
line_numbers: true
line_number_start: 18
line_highlights: 20
---

def setup():   
    # Richte hier Deine Animation ein   
    size(bidschirm_groesse, bildschirm_groesse)


--- /code ---

--- /task ---

### Wähle ein Bild

--- task ---

Im Starterprojekt stehen dir drei verschiedene Planetenbilder und der Mond zur Verfügung. Du kannst diese in der **Bildergalerie** (engl.: "Image gallery") auf der linken Seite des Code-Editors ansehen.

![Ein Screenshot des Code-Editors mit hervorgehobener Bildergalerie mit Bildern von Planeten und dem Mond.](images/image_gallery.png)

**Wähle:** Entscheide welches Bild du verwenden möchtest und notiere den Dateinamen. Beispiel: `orange_planet.png`.

--- /task ---

--- task ---

Füge der Funktion `setup()` Code hinzu, um dein Bild zu laden und zu positionieren.

Die Zeile `image_mode(CENTER)` besagt, dass Bilder anhand von Koordinaten der Bildmitte positioniert werden (anstelle der oberen linken Ecke).

Lade als Nächstes dein Bild in eine globale Variable `planet`. Die Variable muss global sein, damit du sie später verwenden kannst, wenn du den Planeten auf dem Bildschirm zeichnest.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18 
line_highlights: 21-23
---

def setup():   
    # Richte hier Deine Animation ein   
    size(bildschirm_groesse, bildschirm_groesse)   
    image_mode(CENTER)  # Positioniert das Bild in der Mitte
    global planet   
    planet = load_image('planet.png')  # Dein gewählter Planet


--- /code ---

--- /task ---

### Hintergrund zeichnen

--- task ---

Definiere eine Funktion `zeichne_hintergrund()` unter dem entsprechenden Kommentar, um den Hintergrund zu zeichnen.

Verwende `background(0)`, um die Hintergrundfarbe auf Schwarz festzulegen, und füge eine `image()` Funktion hinzu, um den Planeten zu zeichnen. Die Funktion `image()` ist wie folgt aufgebaut:

`image(Bilddateiname, X-Koordinate, Y-Koordinate, Bildbreite, Bildhöhe)`

Die Codezeile `from p5 import *` gibt dir die globalen Variablen `width` (Breite) und `height` (Höhe) basierend auf der Bildschirmgröße. Verwende diese in deinem Code, um den Planeten mit seinem Mittelpunkt auf halber Breite (`width/2`) und am unteren Rand (`height`) des Bildschirms zu positionieren.

--- code ---
---
language: python
filename: main.py — draw_background()
line_numbers: true
line_number_start: 14 
line_highlights: 15-17
---

# Die Funktion „zeichne_hintergrund“ kommt hierher
def zeichne_hintergrund():   
    background(0) # Kurzform für background(0, 0, 0) — schwarz    
    image(planet, width/2, height, 300, 300) # Zeichnet das Bild


--- /code ---

Wenn du den gesamten Code zum Zeichnen des Hintergrunds in einer Funktion bündelst, wird dein Code leichter verständlich.

--- /task --- 

--- task ---

Um den Hintergrund anzuzeigen, rufe `zeichne_hintergrund()` in `draw()` (engl. "to draw" = "zeichnen") auf. Dies führt dazu, dass der Hintergrund bei jedem Aufruf von `draw()` neu gezeichnet wird und alle älteren Zeichnungen überdeckt:

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 28 
line_highlights: 30
---

def draw():   
    # Dinge die in jedem Frame passieren    
    zeichne_hintergrund()

--- /code ---

--- /task ---

--- task ---

**Test:** Führe deinen Code aus und prüfe, ob er einen schwarzen Hintergrund mit einem halben Planeten darunter zeichnet.

--- /task ---

Wenn Du ein Raspberry Pi Konto hast, kannst Du auf **Speichern** klicken, um eine Kopie in Deinen Projekten zu speichern.

--- save ---
