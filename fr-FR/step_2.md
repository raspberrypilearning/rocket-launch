## Dessiner l'arrière-plan

--- task ---

Ouvre le [projet de démarrage](https://editor.raspberrypi.org/fr-FR/projects/rocket-launch-starter){:target="_blank"}.

--- /task ---

Tu vas d'abord créer un arrière-plan pour représenter l'espace.

--- task ---

Crée une fonction `dessine_arriere_plan()` et définis la couleur d'arrière-plan sur noir.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12 
line_highlights: 13-14
---

# La fonction dessine_arriere_plan vient ici  
def dessine_arriere_plan():   
    background(0, 0, 0)    
  
--- /code ---

--- /task ---

--- task ---

Ajoute cette fonction à la liste des éléments à `draw()` dans chaque image.

--- code ---
---
language: python
line_numbers: true
line_number_start: 25 
line_highlights: 27
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
language: python
line_numbers: true
line_number_start: 13 
line_highlights: 15-16
---
def dessine_arriere_plan():  
    background(0,0,0)
    image(planete, taille_ecran/2, taille_ecran, 300, 300)

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

Si tu souhaites modifier l'image de la planète, remplace `planet.png` dans le code par le nom de fichier de la planète choisie, par exemple, `orange_planet.png`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 17 
line_highlights: 22
---
def setup():
    # Configure ton animation ici
    size(taille_ecran, taille_ecran)
    image_mode(CENTER)
    global planete
    planete = load_image('planet.png')

--- /code ---

--- /task ---

