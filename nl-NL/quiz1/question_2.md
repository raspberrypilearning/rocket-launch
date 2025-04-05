
--- question ---
---
legenda: Vraag 2 van 3
---

Een project heeft deze `setup` code om een planeetafbeelding te laden en te zeggen dat afbeeldingen in hun midden moeten worden geplaatst:

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

Coördinaten beginnen bij (0, 0) in de linkerbovenhoek. In het project heb je afbeeldingen van planeten en raketten getekend met de functie `image(bestandsnaam afbeelding, x-coördinaat, y-coördinaat, afbeeldingsbreedte, afbeeldingshoogte)`.

Waar zal deze code het planeetbeeld positioneren?

--- code ---
---
language: python
---

image(planet, 300, 100, 128, 128)

--- /code ---

--- choices ---

- ( ) ![Een planeetafbeelding horizontaal rechts van het scherm en verticaal in het midden.](images/planet400200.png)

  --- feedback ---

De tweede en derde invoer voor de functie `image()` zijn de `x` en `y` coördinaten voor het midden van de afbeelding. Deze planeet heeft de coördinaten `(400, 200)`.

  --- /feedback ---

- ( ) ![Een planeetafbeelding in het midden van het kwadrant linksonder.](images/planet100300.png)

  --- feedback ---

De tweede en derde invoer voor de functie `image()` zijn de `x` en `y` coördinaten voor het midden van de afbeelding. Deze planeet heeft de coördinaten `(100, 300)`.

  --- /feedback ---

- (x) ![Een planeetafbeelding in het midden van het kwadrant rechtsboven.](images/planet300100.png)

  --- feedback ---

Correct! De tweede en derde invoer voor de functie `image()` zijn de `x` en `y` coördinaten voor het midden van de afbeelding. Deze afbeelding heeft de coördinaten (300, 100) dus het is 300 (van de 400) pixels van links voor de `x` coördinaat en 100 (van de 400) pixels naar beneden vanaf de bovenkant.

  --- /feedback ---

- () ![Een planeetafbeelding in het kwadrant linksboven.](images/planet128128.png)

  --- feedback ---

De vierde en vijfde invoer geven de grootte van de afbeelding aan. De tweede en derde invoer voor de functie `image()` zijn de `x` en `y` coördinaten voor het midden van de afbeelding. Deze planeet heeft de coördinaten `(128, 128)`.

  --- /feedback ---

--- /choices ---

--- /question ---
