## Teken achtergrond

--- task ---

Open het [projectsjabloon](https://editor.raspberrypi.org/en/projects/rocket-launch-starter){:target="_blank"}.

--- /task ---

Eerst maak je een zwarte achtergrond om de ruimte weer te geven.

--- task ---

Definieer een `teken_achtergrond()` functie, en stel de achtergrondkleur in op zwart.

--- code ---
---
language: python line_numbers: true line_number_start: 12
line_highlights: 13-14
---

# De functie teken_achtergrond komt hier
def draw_background():   
background(0, 0, 0)

--- /code ---

--- /task ---

--- task ---

Voeg deze functie toe aan de lijst met dingen om te tekenen (`draw()`) in elk frame.

--- code ---
---
language: python line_numbers: true line_number_start: 25
line_highlights: 27
---

def draw(): # Things to do in every frame draw_background()

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit, je zou een zwart vierkant moeten zien.

--- /task ---



--- task ---

Voeg een regel code toe om een afbeelding van een planeet weer te geven.

--- code ---
---
language: python line_numbers: true line_number_start: 13
line_highlights: 15-16
---
def draw_background():  
background(0,0,0) image(planet, screen_size/2, screen_size, 300, 300)

--- /code ---


De functie `image()` heeft de volgende gegevens nodig:

- afbeelding bestandnaam - we hebben de planeetafbeelding al geladen
- x-coördinaat - we hebben de schermgrootte al ingesteld
- y-coördinaat
- breedte afbeelding
- hoogte afbeelding

--- /task ---

--- task ---

**Test:** Voer je code uit en controleer of deze een zwarte achtergrond tekent met onderaan een halve planeet.

![Een planeet tegen een zwarte achtergrond.](images/step_2.png){:width="300px"}

--- /task ---

### Een andere planeet?

--- task ---

Klik op het afbeeldingsicoontje links om de galerij met afbeeldingen te bekijken.

![Kies een andere planeet](images/image_gallery.png)

Als u de afbeelding van de planeet wilt wijzigen, vervangt u `planet.png` in de code door de bestandsnaam van de door u gekozen planeet, bijvoorbeeld `orange_planet.png`.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 22
---
def setup(): # Set up your animation here size(screen_size, screen_size) image_mode(CENTER) global planet planet = load_image('planet.png')

--- /code ---

--- /task ---

