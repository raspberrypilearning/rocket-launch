## Décollage !

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Chaque fois qu'une nouvelle image est dessinée, la fusée doit remonter l'écran pour créer un effet d'animation.
</div>
<div>

![Une fusée volant à vitesse constante du bas vers le haut de l'écran.](images/fly.gif){:width="300px"}

</div>
</div>

--- task ---

Le projet de démarrage a une image de fusée qui t'est fournie.

![Image de la fusée dans la galerie d'images de l'éditeur de code.](images/rocket_image.png)

--- /task ---

--- task ---

Ajoute du code à la fonction `configuration()` pour charger l'image de la fusée dans une variable globale `fusee`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 24, 26
---

def configuration():   
# Configure ton animation ici   
size(taille_ecran, taille_ecran)   
image_mode(CENTER)   
global planete, fusee   
planete = load_image('planet.png')    
fusee = load_image( 'rocket.png')

--- /code ---

--- /task ---

### Faire voler la fusée

La position `y` de la fusée commencera à 400 (la hauteur de l'écran) puis diminuera de 1 à chaque fois qu'une nouvelle image est dessinée.

--- task ---

Ajoute une variable globale `fusee_y` pour suivre la position `y` de la fusée.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9
---

# Configurer les variables globales
taille_ecran = 400    
fusee_y = taille_ecran #Commence en bas

--- /code ---

--- /task ---

--- task ---

Définis une fonction `dessine_fusee()` pour changer la position `y` de la fusée et la redessiner.

`fusee_y -= 1` est une manière plus courte de dire `fusee_y = fusee_y - 1`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12-16
---

# La fonction dessine_fusee vient ici
def dessine_fusee():   
global fusee_y # Utilise la variable globale fusee_y    
fusee_y -= 1 # Déplace la fusée    
image(fusee, width/2, fusee_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

Appelle ton nouveau `dessine_fusee()` dans la fonction `dessin()` afin que la fusée soit redessinée à chaque image.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 33
line_highlights: 36
---

def dessin():   
# Choses à faire dans chaque image   
dessine_arriere_plan()   
dessine_fusee()


--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton code pour vérifier que la fusée démarre en bas de l'écran et remonte à chaque image.

![Animation de la fusée volant à mi-hauteur de l'écran.](images/rocket_fly.gif)

--- /task ---

--- save ---
