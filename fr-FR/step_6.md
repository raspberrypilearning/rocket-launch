## Atteindre l'orbite

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Le but du lancement de la fusée est de propulser un satellite en orbite. 

Une orbite est une trajectoire courbe qu'un objet emprunte autour d'un autre sous l'effet de la gravité.

La fusée peut changer de couleur pour montrer le succès du lancement. 

</div>
<div>

![Trois images côte à côte montrant des lancements réussis (teinte verte), suralimentés (teinte orange) et infructueux (teinte rouge).](images/check_orbit.png){:width="400px"}

</div>
</div>

### Tracer une ligne d'orbite

--- task ---

Crée deux nouvelles variables globales pour définir le rayon du cercle d'orbite et la coordonnée `y` de l'orbite au point que le centre de la fusée doit atteindre pour lancer le satellite.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11-12
---

# Configurer les variables globales
taille_ecran = 400   
fusee_y = taille_ecran   
brule = 100   
rayon_orbite = 250   
orbite_y = taille_ecran - rayon_orbite

--- /code ---

--- /task ---

--- task ---

Mets à jour la fonction `dessine_arriere_plan()` pour dessiner une ellipse représentant l'orbite du satellite que la fusée doit atteindre.

--- code ---
---
language: python filename: main.py - dessine_arriere_plan() line_numbers: true line_number_start: 38
line_highlights: 42-45
---

def dessine_arriere_plan():   
background(0) # Raccourci pour background(0, 0, 0) — noir   
image(planete, width/2, height, 300, 300)   

    no_fill() # Désactive tout remplissage  
      stroke(255) # Définis un trait blanc   
      stroke_weight(2)   
      ellipse(width/2, height, rayon_orbite * 2, rayon_orbite * 2)

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton programme et vérifie qu'une ligne d'orbite blanche est tracée.

![L'écran avec la planète et la nouvelle ligne d'orbite.](images/draw_orbit.png){:width="300px"}

--- /task ---

### Lancer la fusée en orbite

La fusée doit s'arrêter lorsqu'elle atteint l'orbite du satellite, c'est-à-dire à la fin de la mission.

--- task ---

Mets à jour ton code `if carburant >= brule` pour vérifier également que la fusée n'a pas atteint l'orbite.

Tu peux utiliser les instructions `and` dans les instructions `if` pour vérifier si deux conditions ou plus sont vraies.

--- code ---
---
language: python filename: main.py - dessine_fusee() line_numbers: true line_number_start: 15
line_highlights: 19
---

# La fonction dessine_fusee vient ici
def dessine_fusee():   
global fusee_y, carburant, brule

        if carburant >= brule and fusee_y > orbite_y : # Toujours en vol

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton projet et entre `50000` comme quantité de carburant. Cela devrait être suffisant pour atteindre l'orbite. La fusée devrait cesser de bouger lorsqu'elle atteint l'orbite.

--- /task ---

### Vérifier si le lancement est réussi

La fusée doit être colorée en rouge si elle manque de carburant avant d'être suffisamment haute pour lancer le satellite.

--- task ---

--- code ---
---
language: python filename: main.py — dessine_fusee() line_numbers: true line_number_start: 30
line_highlights: 34-35
---

    fill(200, 200, 200, 100)   
    for i in range(20):   
        ellipse(width/2 + randint(-5, 5), fusee_y + randint(20, 50), randint(5, 10), randint(5, 10))
    
    if carburant < brule and fusee_y > orbite_y:  # Plus de carburant et pas en orbite   
        tint(255, 0, 0)  # Échec

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton code et entre `20000` comme quantité de carburant. Vérifie que la fusée devient rouge lorsqu'elle s'arrête sous l'orbite.

![Une fusée rouge à court de carburant avant le cercle orbital. La planète est également devenue rouge.](images/orbit_failure.png){:width="300px"}

Oh non, la planète est devenue rouge !

--- /task ---

--- task ---

La fonction `tint()` définit la couleur de teinte pour toutes les images dessinées jusqu'à ce que tu changes la teinte ou que tu utilises `no_tint()` pour la désactiver.

**Choisir :** ajoute un appel à `no_tint()` après avoir dessiné l'image pour que la planète ne soit pas teintée en rouge dans l'image suivante - ou laisse-le si tu aimes que la planète devienne rouge !

--- code ---
---
language: python filename: main.py - dessine_fusee() line_numbers: true line_number_start: 34
line_highlights: 38
---

    if carburant < brule and fusee_y > orbite_y:    
        tint(255, 0, 0)  # Échec
    
    image(fusee, width/2, fusee_y, 64, 64)   
    no_tint()  # La planète n'est donc pas teintée de rouge dans l'image suivante !


--- /code ---

--- /task ---

--- task ---

Utilise à nouveau la fonction `tint()`, cette fois pour colorer la fusée en vert si la fusée a suffisamment de carburant pour atteindre l'orbite du satellite :

--- code ---
---
language: python filename: main.py - dessine_fusee() line_numbers: true line_number_start: 34
line_highlights: 36-37
---

    if carburant < brule and fusee_y > orbite_y:    
        tint(255, 0, 0)  # Échec   
    elif fusee_y <= orbite_y:   
        tint(0, 255, 0)  # Succès   
    
    image(fusee, width/2, fusee_y, 64, 64)   
    no_tint()

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton projet et entre `50000` comme quantité de carburant. Vérifie que ta fusée devient verte lorsqu'elle atteint l'orbite du satellite.

![Une fusée verte qui a atteint le cercle orbital et qui a encore du carburant.](images/orbit_success.png){:width="300px"}

--- /task ---

Tu as maintenant une simulation qui peut être utilisée pour montrer quelle quantité carburant est nécessaire au minimum pour atteindre l'orbite du satellite. C'est génial ; cependant, tu pourrais prendre une énorme quantité de carburant et réussir quand même, mais c'est coûteux et inutile !

--- task ---

Modifie les conditions de ton code de réussite afin que la fusée ne devienne verte que si elle atteint l'orbite `et` a moins de 1 000 kg de carburant restant.

Ajoute du code pour colorer la fusée en jaune s'il reste plus de 1 000 kg de carburant à la fusée lorsqu'elle atteint l'orbite.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 34
line_highlights: 36, 38-39
---

    if carburant < brule and fusee_y > orbite_y:   
        tint(255, 0, 0)  # Échec      
    elif carburant < 1000 and fusee_y <= orbite_y:   
        tint(0, 255, 0)  # Succès   
    elif carburant >= 1000 and fusee_y <= orbite_y:    
        tint(255, 200, 0)  # Trop de carburant   
    
    image(fusee, width/2, fusee_y, 64, 64)    
    no_tint()  # La planète n'est donc pas teintée dans l'image suivante !

--- /code ---

--- /task ---

--- task ---

**Test :** exécute plusieurs fois ton programme avec des nombres différents ; par exemple, 25 000 kg de carburant devraient être la quantité nécessaire pour rendre la fusée verte, mais vérifie également que la teinte jaune fonctionne également en utilisant un nombre plus grand.

![Une fusée jaune qui a atteint le cercle orbital et qui a encore du carburant.](images/orbit_meh.png){:width="300px"}

--- /task ---

--- save ---
