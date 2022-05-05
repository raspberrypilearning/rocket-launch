## Het opzetten van de scene

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
De animatie heeft een ruimte achtergrond nodig met een planeet om de raket vanaf te lanceren.
</div>
<div>

![Een planeet tegen een zwarte achtergrond.](images/step_2.png){:width="300px"}

</div>
</div>

--- task ---

Open het [-projectsjabloon](https://trinket.io/python/f2199f5a8c){:target="_blank"}.

Als je een Trinket-account hebt, kun je op de knop **Remix** klikken om een kopie op te slaan in je `My Trinkets`-bibliotheek.

--- /task ---

Je gebruikt een `scherm_grootte` variabele om de grootte van het scherm en in berekeningen in te stellen. Variabelen die buiten functies zijn gedefinieerd, zijn **global**, dus je kunt ze overal in je programma gebruiken.

--- task ---

Zoek de opmerking `Globale variabelen instellen` en voeg een regel code toe om je `scherm_grootte` variabele te maken:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# Globale variabelen instellen
scherm_grootte = 400

--- /code ---

-- /task ---

--- task ---

Gebruik de `scherm_grootte` variabele om een vierkant van 400 bij 400 pixels te maken:

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 20
---

def setup():   
#Stel hier je animatie in   
size(scherm_grootte, scherm_grootte)


--- /code ---

--- /task ---

--- task ---

Het startproject heeft drie verschillende planeetafbeeldingen en de maan voor jou beschikbaar. Je kunt deze bekijken in de Trinket-afbeeldingen bibliotheek door de knop **View and Add Images** te selecteren.

![Een plusteken, een uploadsymbool en een afbeeldingssymbool. Het afbeeldingssymbool is gemarkeerd.](images/trinket_image.png)

**Kies:** Bepaal welke afbeelding je wilt gebruiken en noteer de bestandsnaam. Bijvoorbeeld `orange_planet.png`.

--- /task ---

Het is een goed idee om afbeeldingen in `setup()` te laden, zodat ze klaar zijn wanneer je ze moet gebruiken en je animatie snel zal worden uitgevoerd.

--- task ---

De regel `image_mode(CENTER)` zegt dat je afbeeldingen gaat positioneren door de coördinaten van het midden van de afbeelding op te geven (in plaats van de linkerbovenhoek).

Voeg ook code toe aan de functie `setup()` om de door jou gekozen afbeelding in een global variabele genaamd `planeet` te laden. De variabele moet global zijn, zodat je deze later kunt gebruiken wanneer je de planeet op het scherm toont.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 21-23
---

def setup():   
#Stel hier je animatie in   
size(scherm_grootte, scherm_grootte)   
image_mode(CENTER)   
global planeet   
planeet = load_image('planet.png') #Je gekozen planeet


--- /code ---

-- /task ---

--- task ---

Definieer een `teken_achtergrond()` functie, om de achtergrond te tekenen, onder de opmerking die je vertelt waar deze moet komen.

Gebruik `background(0)` om de achtergrondkleur op zwart te zetten en voeg een `image()` functie toe om de planeet te tekenen. De functie `image()` is als volgt ingedeeld:

`image(bestandsnaam afbeelding, x-coördinaat, y-coördinaat, afbeeldingsbreedte, afbeeldingshoogte)`

De `p5` bibliotheek stelt global variabelen `width` (breedte) en `height` (hoogte) in op basis van de grootte van het scherm. Gebruik deze in je code om de planeet te positioneren met het midden halverwege (`width/2`) en aan de onderkant (`height`) van het scherm.

--- code ---
---
language: python filename: main.py — draw_background() line_numbers: true line_number_start: 14
line_highlights: 15-17
---

# De functie teken_achtergrond komt hier
def teken_achtergrond():   
background(0) # Staat voor background(0, 0, 0) — zwart    
image(planeet, width/2, height, 300, 300) #Teken de afbeelding


--- /code ---

Door alle code voor het tekenen van de achtergrond in één functie te plaatsen, word je code gemakkelijker te begrijpen.

-- /task ---

--- task ---

Om de achtergrond te laten verschijnen, roep je `teken_achtergrond()` in `draw()` aan. Dit zorgt ervoor dat de achtergrond elke keer dat `draw()` wordt aangeroepen opnieuw wordt getekend, waarbij een oudere tekening wordt afgedekt:

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 28
line_highlights: 30
---

def draw():   
#Dingen om te doen in elk frame    
teken_achtergrond()

--- /code ---

-- /task ---

--- task ---

**Test:** Voer je code uit en controleer of deze een zwarte achtergrond tekent met onderaan een halve planeet.

-- /task ---

--- save ---
