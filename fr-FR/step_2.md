## Dessiner l'arrière-plan

--- task ---

Ouvre le [projet de démarrage](https://editor.raspberrypi.org/en/projects/rocket-launch-starter){:target="_blank"}.

--- /task ---

Tu vas d'abord créer un arrière-plan pour représenter l'espace.

--- task ---

Crée une fonction `dessine_arriere_plan()` et définis la couleur d'arrière-plan sur noir.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# La fonction dessine_arriere_plan vient ici
def setup():   
# Configure ton animation ici   
size(taille_ecran, taille_ecran)

--- /code ---

--- /task ---

--- task ---

Ajoute cette fonction à la liste des éléments à `draw()` dans chaque image.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 28
line_highlights: 20
---

def draw():   
# Choses à faire dans chaque image    
dessine_arriere_plan()

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton code et tu devrais voir un carré noir.

--- /task ---



--- task ---

Ajoute une ligne de code pour afficher l'image d'une planète.

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 21-23
---
def draw_background():  
background(0,0,0) image(planet, screen_size/2, screen_size, 300, 300)

--- /code ---


La fonction `image()` doit avoir les données suivantes :

- nom du fichier image : nous avons déjà chargé l'image de la planète
- coordonnée x : nous avons déjà défini la taille de l'écran
- coordonnées y
- largeur de l'image
- hauteur de l'image

--- /task ---

--- task ---

**Test :** exécute ton code et vérifie qu'il dessine un arrière-plan noir avec une demi-planète en bas.

![Une planète sur un arrière-plan noir.](images/step_2.png){:width="300px"}

--- /task ---

### Une autre planète ?

--- task ---

Clique sur l'icône d'image à gauche pour voir la galerie d'images.

![Choisir une autre planète](images/image_gallery.png)

Par exemple, `orange_planet.png`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 15-17
---
def setup(): # Set up your animation here size(screen_size, screen_size) image_mode(CENTER) global planet planet = load_image('planet.png')

--- /code ---

--- /task ---

