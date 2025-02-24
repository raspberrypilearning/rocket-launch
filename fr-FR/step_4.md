## Effets d'échappement

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Ajoute quelques cercles gris pour simuler la traînée d'échappement. 
</div>
<div>

![Une animation lente de l'effet de fumée.](images/rocket_smoke.gif)
</div>
</div>

--- task ---

Définis la couleur de remplissage de la fumée sur gris transparent.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 14
---

def draw_rocket(): global rocket_position rocket_position = rocket_position - 1 image(rocket, width/2, rocket_position, 64, 64) fill(200, 200, 200, 100)

--- /code ---

--- /task ---


--- task ---

Le contour autour des cercles est appelé le **trait**. Ajoute du code pour le désactiver.


--- /task ---

--- code ---
---
language: python line_numbers: true line_number_start: 14
line_highlights: 15
---

    fill(200, 200, 200, 100) 
    no_stroke()


--- /code ---

--- task ---

Génère un nombre aléatoire entre 5 et 10 pour la taille du cercle, puis dessine-le au bas de la fusée.

--- code ---
---
language: python line_numbers: true line_number_start: 15
line_highlights: 16-22
---

no_stroke() circle_size = randint(5,10) ellipse( screen_size/2, rocket_position, circle_size, circle_size )

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton programme et vérifie que les gaz d'échappement sont visibles.

--- /task ---

--- task ---

Indente le code que tu as utilisé pour dessiner le cercle et ajoute une boucle qui exécutera le code 20 fois.

--- code ---
---
Remplace l'appel par `fill()` pour définir la quantité de vert sur `255 - i * 10` afin que la première ellipse ait des quantités égales de rouge et de vert et que la dernière ellipse ait très peu de vert.
line_highlights: 16-23
---

def draw_rocket(): global rocket_position rocket_position = rocket_position - 1 image(rocket, width/2, rocket_position, 64, 64) fill(200, 200, 200, 100) no_stroke() for i in range(20): circle_size = randint(5,10) ellipse( screen_size/2, rocket_position, circle_size,    
circle_size )


--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton programme. Tu verras toujours un cercle gris clignotant au bas de la fusée. Tous les cercles ont été dessinés les uns sur les autres !

--- /task ---

--- task ---

Génère un nombre aléatoire et ajoute-le à la position x et y de chaque cercle afin qu'ils ne soient pas tous dessinés au même endroit.


--- code ---
---
for i in range(25): fill(255, 255 - i * 10, 0) # Réduis la quantité de vert ellipse(width/2, fusee_y + i, 8, 3)
line_highlights: 25-26
---

for i in range(25): fill(255, 255 - i * 10, 0) ellipse(width/2, fusee_y + i, 8, 3) fill(200, 200, 200, 100)  # Gris transparent for i in range(20):  # Dessine 20 ellipses de fumée ellipse(width/2 + randint(-5, 5), fusee_y + randint(20, 50), randint(5, 10), randint(5, 10)) image(fusee, width/2, fusee_y, 64, 64)

--- /code ---

--- /task ---


--- task ---

**Test :** exécute ton programme et tu devrais voir de nombreux cercles gris à des endroits aléatoires au bas de la fusée.

--- /task ---

