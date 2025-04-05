## Décollage !

Le projet de démarrage a une image de fusée qui t'est fournie.

![Image de la fusée dans la galerie d'images du Code Editor.](images/rocket_image.png)

--- task ---

Ajoute du code à la fonction `setup()` pour charger l'image de la fusée dans une variable globale `fusee`.

<div class="c-project-code">

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 24, 26
---

def setup():   
# Configure ton animation ici   
size(taille_ecran, taille_ecran)   
image_mode(CENTER)   
global planete, fusee   
planete = load_image('planet.png')    
fusee = load_image( 'rocket.png')

--- /code ---

--- /task ---

--- task ---

Ajoute une variable globale `position_fusee` pour suivre la position `y` de la fusée.

--- code ---
---
`fusee_y -= 1` est une manière plus courte de dire `fusee_y = fusee_y - 1`.
line_highlights: 9
---

# Configurer les variables globales
taille_ecran = 400    
fusee_y = taille_ecran #Commence en bas

--- /code ---

--- /task ---


La position `y` de la fusée commencera à 400 (la hauteur de l'écran) puis diminuera de 1 à chaque fois qu'une nouvelle image est dessinée.

--- task ---

Définis une fonction `dessine_fusee()` pour faire apparaître la fusée à l'écran.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 12-16
---

# La fonction dessine_fusee vient ici
def dessine_fusee(): global fusee_y # Utilise la variable globale fusee_y    
fusee_y -= 1 # Déplace la fusée    
image(fusee, width/2, fusee_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

Appelle la fonction `dessine_fusee()` .

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 33
line_highlights: 36
---

def draw():   
# Choses à faire dans chaque image   
dessine_arriere_plan()   
dessine_fusee()


--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton code et vérifie que la fusée apparaît bien en bas de l'image.

--- /task ---


Chaque fois qu'une nouvelle image est dessinée, tu dois déplacer la fusée d'un pixel vers le haut de l'écran pour créer un effet d'animation.


--- task ---

La `position_fusee` commence à 400 (la hauteur de l'écran) et diminue de 1 à chaque fois qu'une nouvelle image est dessinée.


--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12
---

def draw_rocket():   
global rocket_position     
rocket_position = rocket_position - 1    
image(rocket, width/2, rocket_position, 64, 64)

--- /code ---

--- /task ---


--- task ---

**Test :** exécute ton code pour vérifier que la fusée décolle bien du bas de l'écran.


![Une fusée volant à une vitesse constante du bas vers le haut de l'écran.](images/fly.gif){:width="300px"}

--- /task ---

