## Erreichen der Umlaufbahn

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Der Sinn des Raketenstarts besteht darin, einen Satelliten in die Umlaufbahn zu bringen. 

Eine Umlaufbahn, oder Orbit, ist eine gekrümmte Bahn, die ein Objekt aufgrund der Schwerkraft um ein anderes zurücklegt.

Die Rakete kann ihre Farbe ändern, um anzuzeigen, wie erfolgreich der Start war. 

</div>
<div>

![Drei nebeneinander liegende Bilder zeigen erfolgreiche (Grünstich), überbetankte (Gelbstich) und versagte (Rotstich) Starts.](images/check_orbit.png){:width="400px"}

</div>
</div>

### Zeichne eine Umlaufbahnlinie

--- task ---

Erstelle zwei neue globale Variablen, um den Radius des Umlaufkreises und die `y` Koordinate der Umlaufbahn bis zu dem Punkt festzulegen, den das Raketenzentrum erreichen muss, um den Satelliten zu starten.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11-12
---

# Globale Variablen einrichten
bildschirm_groesse = 400   
rakete_y = bildschirm_groesse   
verbrennen = 100   
orbit_radius = 250   
orbit_y = bildschirm_groesse - orbit_radius

--- /code ---

--- /task ---

--- task ---

Erweitere die Funktion `zeichne_hintergrund()` um eine Ellipse, welche die Satellitenumlaufbahn darstellt, die die Rakete erreichen muss.

--- code ---
---
language: python filename: main.py - draw_background() line_numbers: true line_number_start: 38
line_highlights: 42-45
---

def zeichne_hintergrund():   
background(0) # Kurzform für background(0, 0, 0) — schwarz   
image(planet, width/2, height, 300, 300)   

    no_fill() # Jegliche Füllung ausschalten  
    stroke(255) # Einen weißen Strich setzen   
    stroke_weight(2)   
    ellipse(width/2, height, orbit_radius * 2, orbit_radius * 2)

--- /code ---

--- /task ---

--- task ---

**Test:** Führe dein Programm aus und überprüfe, ob eine weiße Orbitlinie gezeichnet wird.

![Der Bildschirm mit Planeten und neuer Umlaufbahnlinie.](images/draw_orbit.png){:width="300px"}

--- /task ---

### Bringe die Rakete in die Umlaufbahn

Die Rakete sollte anhalten, wenn sie die Umlaufbahn des Satelliten erreicht – das wäre das Ende der Mission.

--- task ---

Erweitere den Code `if treibstoff >= verbrennen`, um auch zu überprüfen, dass die Rakete die Umlaufbahn noch nicht erreicht hat.

Du kannst `and` (engl.: "und") in `if` -Anweisungen verwenden, um zu überprüfen, ob zwei oder mehr Bedingungen erfüllt sind.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 19
---

# Die Funktion „zeichne_rakete“ kommt hierher
def zeichne_rakete():   
global rakete_y, treibstoff, verbrennen

        if treibstoff >= verbrennen and rakete_y > orbit_y: # fliegt immer noch

--- /code ---

--- /task ---

--- task ---

**Test:** Führe dein Projekt aus und gib `50000` als Treibstoffmenge ein. Dies sollte ausreichend Treibstoff sein, um die Umlaufbahn zu erreichen. Sobald die Rakete die Umlaufbahn erreicht, sollte sie zum Stillstand kommen.

--- /task ---

### Überprüfe, ob der Start erfolgreich war

Die Rakete sollte rot gefärbt werden, wenn ihr der Treibstoff ausgeht, bevor sie hoch genug gekommen ist, um den Satelliten zu starten.

--- task ---

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 30
line_highlights: 34-35
---

    fill(200, 200, 200, 100)   
    for i in range(20):   
        ellipse(width/2 + randint(-5, 5), rakete_y + randint(20, 50), randint(5, 10), randint(5, 10))
    
    if treibstoff < verbrennen and rakete_y > orbit_y:  # Kein Treibstoff mehr und noch nicht im Orbit   
        tint(255, 0, 0)  # Versagen

--- /code ---

--- /task ---

--- task ---

**Test:** Führe dein Projekt aus und gib `20000` als Treibstoffmenge ein. Überprüfe, ob die Rakete rot wird, wenn sie unterhalb der Umlaufbahn zum Stehen kommt.

![Eine rote Rakete, der vor Erreichen der Umlaufbahn der Treibstoff ausgegangen ist. Auch der Planet ist rot geworden.](images/orbit_failure.png){:width="300px"}

Oh nein, der Planet ist rot geworden!

--- /task ---

--- task ---

Die Funktion `tint()` legt die Farbtönung für alle gezeichneten Bilder fest, bis du die Tönung änderst oder sie mit `no_tint()` ausschaltest.

**Wähle:** Füge nach dem Zeichnen des Bildes einen Aufruf von `no_tint()` hinzu, damit der Planet im nächsten Frame nicht rot gefärbt wird – oder lass es, wenn du möchtest, dass der Planet rot wird!

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 34
line_highlights: 38
---

    if treibstoff < verbrennen and rakete_y > orbit_y:    
        tint(255, 0, 0)  # Versagen
    
    image(rakete, width/2, rakete_y, 64, 64)   
    no_tint()  # Damit der Planet im nächsten Frame nicht rot gefärbt wird!


--- /code ---

--- /task ---

--- task ---

Verwende erneut die Funktion `tint()` - dieses Mal um die Rakete grün zu färben, wenn sie genug Treibstoff hat, um die Satellitenumlaufbahn zu erreichen:

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 34
line_highlights: 36-37
---

    if treibstoff < verbrennen and rakete_y > orbit_y:    
        tint(255, 0, 0)  # Versagen   
    elif rakete_y <= orbit_y:   
        tint(0, 255, 0)  # Erfolg   
    
    image(rakete, width/2, rakete_y, 64, 64)   
    no_tint()

--- /code ---

--- /task ---

--- task ---

**Test:** Führe dein Projekt aus und gib `50000` als Treibstoffmenge ein. Überprüfe, ob deine Rakete grün wird, wenn sie die Satellitenumlaufbahn erreicht.

![Eine grüne Rakete, die den Orbit erreicht hat und noch Treibstoff übrig hat.](images/orbit_success.png){:width="300px"}

--- /task ---

Nun steht eine Simulation zur Verfügung, mit der sich darstellen lässt, wie viel Treibstoff mindestens benötigt wird, um die Umlaufbahn des Satelliten zu erreichen. Das ist großartig. Du könntest jedoch auch große Mengen Treibstoff mitnehmen und trotzdem erfolgreich sein, aber das ist kostspielig und verschwenderisch!

--- task ---

Passe die Bedingungen in deinem "Erfolg"-Code so an, dass die Rakete nur dann grün wird, wenn sie die Umlaufbahn erreicht `und` weniger als 1.000 kg Treibstoff übrig hat.

Füge Code hinzu, um die Rakete gelb zu färben, wenn sie beim Erreichen der Umlaufbahn noch über mehr als 1.000 kg Treibstoff verfügt.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 34
line_highlights: 36, 38-39
---

    if treibstoff < verbrennen and rakete_y > orbit_y:   
        tint(255, 0, 0)  # Versagen   
    elif treibstoff < 1000 and rakete_y <= orbit_y:   
        tint(0, 255, 0)  # Erfolg   
    elif treibstoff >= 1000 and rakete_y <= orbit_y:    
        tint(255, 200, 0)  # Zu viel Treibstoff   
    
    image(rakete, width/2, rakete_y, 64, 64)    
    no_tint()  # Damit der Planet im nächsten Frame nicht eingefärbt ist!

--- /code ---

--- /task ---

--- task ---

**Test:** Führe dein Programm mehrere Male mit unterschiedlichen Zahlen aus. Beispielsweise sollten 25.000 kg Treibstoff die Menge sein, die benötigt wird, um die Rakete grün zu färben. Überprüfe aber auch mit einer größeren Zahl, ob der Gelbton ebenfalls funktioniert.

![Eine gelbe Rakete, die den Orbit erreicht hat und noch Treibstoff hat.](images/orbit_meh.png){:width="300px"}

--- /task ---

--- save ---
