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
language: python
line_numbers: true
line_number_start: 10
line_highlights: 14
---

def dessine_fusee():
    global position_fusee
    position_fusee = position_fusee - 1
    image(fusee, width/2, position_fusee, 64, 64)
    fill(200, 200, 200, 100) 

--- /code ---

--- /task ---


--- task ---

Le contour autour des cercles est appelé le **trait**. Ajoute du code pour le désactiver.


--- /task ---

--- code ---
---
language: python
line_numbers: true
line_number_start: 14
line_highlights: 15
---

    fill(200, 200, 200, 100) 
    no_stroke()
    

--- /code ---

--- task ---

Génère un nombre aléatoire entre 5 et 10 pour la taille du cercle, puis dessine-le au bas de la fusée.

--- code ---
---
language: python
line_numbers: true
line_number_start: 15
line_highlights: 16-22
---

no_stroke()
taille_cercle = randint(5,10) 
ellipse(
    taille_ecran/2, 
    position_fusee, 
    taille_cercle, 
    taille_cercle
)   

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton programme et tu devrais voir un cercle gris apparaître au bas de la fusée.

--- /task ---

--- task ---

Indente le code que tu as utilisé pour dessiner le cercle et ajoute une boucle qui exécutera le code 20 fois.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 16-23
---

def dessine_fusee():
    global position_fusee
    position_fusee = position_fusee - 1
    image(fusee, width/2, position_fusee, 64, 64)
    fill(200, 200, 200, 100) 
    no_stroke()
    for i in range(20):
        taille_cercle = randint(5,10)
        ellipse(
            taille_ecran/2, 
            position_fusee, 
            taille_cercle,    
            taille_cercle
        )
    

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton programme. Tu verras toujours un cercle gris clignotant au bas de la fusée. Tous les cercles ont été dessinés les uns sur les autres !

--- /task ---

--- task ---

Génère un nombre aléatoire et ajoute-le à la position x et y de chaque cercle afin qu'ils ne soient pas tous dessinés au même endroit.


--- code ---
---
language: python
line_numbers: true
line_number_start: 24
line_highlights: 25-26
---

ellipse(
    taille_ecran/2 + randint(-5,5), 
    position_fusee + randint(20,50), 
    taille_cercle, 
    taille_cercle
)   

--- /code ---

--- /task ---


--- task ---

**Test :** exécute ton programme et tu devrais voir de nombreux cercles gris à des endroits aléatoires au bas de la fusée.

--- /task ---

