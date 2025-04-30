## Décollage !

Le projet de démarrage a une image de fusée qui t'est fournie.

![Image de la fusée dans la galerie d'images du Code Editor.](images/rocket_image.png)

--- task ---

Ajoute du code à la fonction `setup()` pour charger l'image de la fusée dans une variable globale `fusee`.

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 17
line_highlights: 21, 23
---

def setup():   
    # Configure ton animation ici 
    size(taille_ecran, taille_ecran)   
    image_mode(CENTER)   
    global planete, fusee   
    planete = load_image('planet.png')    
    fusee = load_image('rocket.png')    

--- /code ---

--- /task ---

--- task ---

Ajoute une variable globale `position_fusee` pour suivre la position `y` de la fusée.

--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 7
---

# Set up global variables    
taille_ecran = 400    
position_fusee = taille_ecran  

--- /code ---

--- /task ---


La position `y` de la fusée commencera à 400 (la hauteur de l'écran) puis diminuera de 1 à chaque fois qu'une nouvelle image est dessinée.

--- task ---

Définis une fonction `dessine_fusee()` pour faire apparaître la fusée à l'écran.

--- code ---
---
language: python
line_numbers: true
line_number_start: 9 
line_highlights: 10-12 
---

# La fonction dessine_fusee vient ici
def dessine_fusee():   
    global position_fusee      
    image(fusee, width/2, position_fusee, 64, 64)    


--- /code ---

--- /task ---

--- task ---

Appelle la fonction `dessine_fusee()` .

--- code ---
---
language: python
line_numbers: true
line_number_start: 29 
line_highlights: 32 
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
language: python
line_numbers: true
line_number_start: 10 
line_highlights: 12
---

def dessine_fusee():   
    global position_fusee     
    position_fusee = position_fusee - 1    
    image(fusee, width/2, position_fusee, 64, 64)    

--- /code ---
--- /task ---


--- task ---

**Test :** exécute ton code pour vérifier que la fusée décolle bien du bas de l'écran.


![Une fusée volant à une vitesse constante du bas vers le haut de l'écran.](images/fly.gif){:width="300px"}

--- /task ---

