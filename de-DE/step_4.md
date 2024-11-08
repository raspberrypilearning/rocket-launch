## Abgaseffekte

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Mit einigen Spezialeffekten zur Simulation der Abgasspur wird die Rakete realistischer aussehen. 

Du kannst coole Effekte erstellen, indem du mit einer „for“-Schleife viele Formen in jeden Frame zeichnest.

</div>
<div>

![Die Rakete mitten im Flug mit einer Abgasspur.](images/flying_rocket.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Mithilfe von Programmierung werden <span style="color: #0faeb0">**Grafikeffekte**</span> für Filme und Spiele erstellt. Es ist viel schneller, Code zu schreiben, als jedes Bild einer Animation einzeln zu zeichnen. </p>

### Zeichne dein Abgas

Durch das Zeichnen vieler gelber Ellipsen an verschiedenen `y` Positionen entsteht eine Abgasspur mit runder Unterseite.

--- task ---

Verfeinere deine Funktion `zeichne_rakete()` mit einer `for`-Schleife, die das Zeichnen von `25` Abgasellipsen wiederholt. Die **Schleifenvariable** `i` wird zu `rakete_y` addiert, um jede Ellipse weiter unterhalb der Rakete zu zeichnen.

--- code ---
---
language: python
filename: main.py - draw_rocket()
line_numbers: true
line_number_start: 12
line_highlights: 16-20
---

def zeichne_rakete():
    global rakete_y   
    rakete_y -= 1   

    no_stroke() # Schaltet Zeichnen aus
    
    for i in range(25): # Zeichne 25 brennende Abgasellipsen   
        fill(255, 255, 0) # Gelb   
        ellipse(width/2, rakete_y + i, 8, 3) # i erhöht sich bei jeder Wiederholung der Schleife    
    
    image(rakete, width/2, rakete_y, 64, 64)


--- /code ---

--- /task ---

Eine `for`-Schleife wiederholt einen Codeabschnitt einmal für jedes ihr übergebene Element.

Um den Code in einer `for`-Schleife eine bestimmte Anzahl von Malen auszuführen, kannst du die Funktion `range()` verwenden. Beispielsweise erstellt `range(5)` eine Folge von fünf Zahlen, beginnend bei 0, also [0, 1, 2, 3, 4].

Bei jeder Wiederholung der `for`-Schleife wird eine Variable auf das aktuelle Element gesetzt, sodass du sie in der Schleife verwenden kannst.

--- task ---

**Test:** Führe deinen Code aus, um zu überprüfen, ob die Rakete eine neue Abgasspur hat.

![Eine Nahaufnahme der Rakete mit einer Rauchspur.](images/rocket_exhaust.png){:width="300px"}

--- /task ---

### Füge einen Farbverlauf hinzu

Die Variable `i` kann auch verwendet werden, um einen Farbverlauf mit weniger Grün in jeder gezeichneten Ellipse zu erstellen.

--- task ---

Ändere den Aufruf in `fill()`, um den Grünanteil auf `255 - i * 10` festzulegen, sodass die erste Ellipse gleiche Mengen Rot und Grün aufweist und die letzte Ellipse sehr wenig Grün.

--- code ---
---
language: python
filename: main.py - draw_rocket()
line_numbers: true
line_number_start: 18
line_highlights: 19
---

    for i in range(25):   
        fill(255, 255 - i * 10, 0)  # Grünanteil reduzieren    
        ellipse(width/2, rakete_y + i, 8, 3)

--- /code ---

--- /task ---

--- task ---

**Test:** Überprüfe, ob du eine Spur von Ellipsen erhältst, deren Farbe allmählich von Gelb nach Rot wechselt.

--- /task ---

### Erzeuge einen Raucheffekt

Die Rauchspur wird durch das Zeichnen vieler leicht transparenter grauer Ellipsen an unterschiedlichen Positionen in jedem Frame erstellt.

![Eine langsame Animation des Raucheffekts.](images/rocket_smoke.gif)

--- task ---

Dieses Mal liegt `fill()` außerhalb der Schleife, da die Farbe für jede Rauchellipse gleich ist. Die vierte Eingabe für `fill()` ist die Deckkraft. Ein niedriger Deckkraftwert macht die Farbe transparenter, sodass du die darunter liegenden Formen sehen kannst.

In jedem Frame der Animation werden 20 Ellipsen zufälliger Größe an zufälligen Positionen gezeichnet.

--- code ---
---
language: python
filename: main.py - draw_rocket()
line_numbers: true
line_number_start: 18
line_highlights: 22-24
---

    for i in range(25):  
        fill(255, 255 - i * 10, 0)   
        ellipse(width/2, rakete_y + i, 8, 3)    
    
    fill(200, 200, 200, 100)  # Transparent grau   
    for i in range(20):  # Zeichne 20 zufällige Rauchellipsen    
        ellipse(width/2 + randint(-5, 5), rakete_y + randint(20, 50), randint(5, 10), randint(5, 10))    
    
    image(rakete, width/2, rakete_y, 64, 64)

--- /code ---

--- /task ---

--- task ---

**Test:** Führe dein Programm aus und prüfe, ob die Abgase sichtbar sind.

![Eine Animation der Rakete und der Rauchspur mit zusätzlichem Rauch.](images/rocket_exhaust_circles.gif)

--- /task ---

--- save ---
