--- question ---
---
legenda: Vraag 3 van 3
---

Deze code gebruikt `tint()` om een raket in een spel te kleuren om de speler te laten zien hoe het gaat.

--- code ---
---
language: python
---

if punten >= 100:    
tint(0, 255, 0) #Groen   
elif punten < 100 en levens == 1:   
tint(255, 200, 0) #Amber    
elif punten < 100 en levens == 0:     
tint(255, 0, 0) #Rood     
else:      
no_tint()

image(raket, width/2, height/2, 64, 64)

--- /code ---

Als de variabele `punten` de waarde `99` heeft en de variabele `levens` de waarde `1`heeft, hoe ziet de raket er dan uit?

--- choices ---

- (x)

![Een raketafbeelding met amberkleurige tint.](images/rocket_amber.png) <div style="text-align: center;">Amber

 --- feedback ---

 Correct! De speler heeft minder dan 100 punten en heeft nog maar 1 leven over. De raket is amber gekleurd om te laten weten dat dit de laatste kans is om te winnen!

 --- /feedback ---

- ( )

![Een raketafbeelding zonder tint](images/rocket_original.png) <div style="text-align: center;">Geen tint

 --- feedback ---

 Niet helemaal, de raket heeft een tint als een van de uitspraken waar is.

 --- /feedback ---

- ( )

![Een raketafbeelding met groene tint](images/rocket_green.png) <div style="text-align: center;">Groen

 --- feedback ---

 Niet helemaal, de speler zou `>= 100` punten nodig hebben om te winnen en zijn raket groen te maken. Hij heeft `99`, wat niet genoeg is. Controleer de voorwaarden zorgvuldig.

 --- /feedback ---

- ( )

![Een raketafbeelding met rode tint](images/rocket_red.png) <div style="text-align: center;">Rood

 --- feedback ---

 Niet helemaal, de speler heeft `< 100` punten maar levens zijn niet gelijk aan `0`. Controleer de voorwaarden zorgvuldig.

 --- /feedback ---

--- /choices ---

--- /question ---
