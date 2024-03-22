## Uitlaat effecten

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

De raket ziet er realistischer uit met enkele speciale effecten om het uitlaatspoor te simuleren. 

Je kunt coole effecten creëren door een `for`-lus te gebruiken om veel vormen in elk frame te tekenen.

</div>
<div>

![De raket halverwege de vlucht met een uitlaatspoor.](images/flying_rocket.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Coderen wordt gebruikt om <span style="color: #0faeb0">**grafische effecten**</span> te maken voor films en games. Het is veel sneller om code te schrijven dan om elk frame van een animatie afzonderlijk te tekenen. </p>

### Teken je uitlaat

Door veel gele ellipsen op verschillende `y`-posities te tekenen, ontstaat een uitlaatspoor met een ronde onderkant.

--- task ---

Werk je `teken_raket()` functie bij om een `for`-lus op te nemen die het tekenen van `25` uitlaatellipsen herhaalt. De **lusvariabele** `i` wordt opgeteld bij `raket_y` om elke ellips verder onder de raket te tekenen.

--- code ---
---
language: python filename: main.py - teken_raket() line_numbers: true line_number_start: 12
line_highlights: 16-22
---

def teken_raket(): global raket_y   
raket_y -= 1   

    no_stroke() # Schakel de lijn uit
    
    for i in range(25): # Teken 25 brandende uitlaatellipsen
        fill(255, 255, 0) # Geel
        ellipse(width/2, raket_y + i, 8, 3) # i neemt toe elke keer dat de lus wordt herhaald
    
    image(raket, width/2, raket_y, 64, 64)


--- /code ---

--- /task ---

fill(200, 200, 200, 100) #Transparant grijs   
for i in range(20): #Teken 20 willikeurige rook ellipsen    
ellipse(width/2 + randint(-5, 5), raket_y + randint(20, 50), randint(5, 10), randint(5, 10))

Om de code in een `for` lus een aantal malen uit te voeren, kun je de `range()` functie gebruiken. Bijvoorbeeld, `range(5)` creëert een reeks van vijf getallen beginnend bij 0, dus [0, 1, 2, 3, 4].

Elke keer dat de `for`-lus wordt herhaald, stelt het een variabele in op het huidige item, zodat je het in de lus kunt gebruiken.

--- task ---

**Test:** Voer je code uit om te controleren of de raket een nieuw uitlaatspoor heeft.

![Een close-up van de raket met een uitlaatspoor.](images/rocket_exhaust.png){:width="300px"}

--- /task ---

### Voeg een verloop toe

De variabele `i` kan ook worden gebruikt om een kleurverloop te maken met minder groen in elke ellips die wordt getekend.

--- task ---

Verander de aanroep in `fill()` om de hoeveelheid groen in te stellen op `255 - i*10` zodat de eerste ellips evenveel rood en groen heeft en de laatste ellips heel weinig groen.

--- code ---
---
language: python filename: main.py - teken_raket() line_numbers: true line_number_start: 19
line_highlights: 20
---

    for i in range(25):
        fill(255, 255 - i * 10, 0) # Verminder de hoeveelheid groen
        ellipse(width/2, raket_y + i, 8, 3)

--- /code ---

--- /task ---

--- task ---

**Test:** Controleer of je een spoor van ellipsen krijgt die geleidelijk veranderen van geel naar rood.

--- /task ---

### Creëer een rookeffect

Het rookafvoerspoor wordt gecreëerd door veel licht transparante grijze ellipsen op verschillende posities in elk frame te tekenen.

![Een langzame animatie van het rookeffect.](images/rocket_smoke.gif)

--- task ---

Deze keer bevindt de `fill()` zich buiten de lus omdat de kleur voor elke rook ellips hetzelfde is. De vierde invoer voor `fill()` is de doorzichtigheid, een lage doorzichtigheidswaarde maakt de kleur transparanter, zodat je de vormen eronder kunt zien.

In elk frame van de animatie worden 20 ellipsen van willekeurige grootte op willekeurige posities getekend.

--- code ---
---
language: python filename: main.py - teken_raket() line_numbers: true line_number_start: 19
line_highlights: 23-26
---

    for i in range(25):
        fill(255, 255 - i * 10, 0)
        ellipse(width/2, raket_y + i, 8, 3)
    
    fill(200, 200, 200, 100) # Transparant grijs
    for i in range(20): # Teken 20 willekeurige rookellipsen
      ellipse(width/2 + randint(-5, 5), raket_y + randint(20, 50), randint(5, 10), randint(5, 10))
    
    image(raket, width/2, raket_y, 64, 64)

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je programma uit en controleer of de uitlaatgassen zichtbaar zijn.

![Een animatie van de raket en het uitlaatspoor met toegevoegde rook.](images/rocket_exhaust_circles.gif)

--- /task ---

--- save ---
