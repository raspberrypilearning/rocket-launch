
--- question ---
---
legend: Question 2 sur 3
---

Un projet a ce code `configuration` pour charger une image de planète et dire que les images doivent être positionnées en leur centre :

--- code ---
---
language: python
---

def setup():   
  size(400, 400)   
  image_mode(CENTER)   
  global planete   
  planete = load_image('planet.png')   

--- /code ---

Les coordonnées commencent à partir de (0, 0) dans le coin supérieur gauche. Dans le projet, tu as dessiné des images de planètes et de fusées à l'aide de la fonction `image(image_file, x-coord, y-coord, x-width, y-width)`.

Où ce code positionnera-t-il l'image de la planète ?

--- code ---
---
language: python
---

image(planete, 300, 100, 128, 128)

--- /code ---

--- choices ---

- ( )
![Une image de planète positionnée horizontalement à droite de l'écran et verticalement au milieu.](images/planet400200.png)

  --- feedback ---

Les deuxième et troisième entrées de la fonction `image()` sont les coordonnées `x` et `y` pour le centre de l'image. Cette planète a pour coordonnées `(400, 200)`.

  --- /feedback ---

- ( )
![Une image de la planète positionnée au milieu du quadrant inférieur gauche.](images/planet100300.png)

  --- feedback ---

Les deuxième et troisième entrées de la fonction `image()` sont les coordonnées `x` et `y` pour le centre de l'image. Cette planète a pour coordonnées `(100, 300)`.

  --- /feedback ---

- (x)
![Une image de la planète positionnée au milieu du quadrant supérieur droit.](images/planet300100.png)

  --- feedback ---

Correct ! Les deuxième et troisième entrées de la fonction `image()` sont les coordonnées `x` et `y` pour le centre de l'image. Cette image a les coordonnées (300, 100) donc elle est à 300 (sur 400) pixels de la gauche pour la coordonnée `x` et 100 (sur 400) pixels du haut.

  --- /feedback ---

- ()
![Une image de planète positionnée dans le quadrant supérieur gauche.](images/planet128128.png)

  --- feedback ---

Les quatrième et cinquième entrées donnent la taille de l'image. Les deuxième et troisième entrées de la fonction `image()` sont les coordonnées `x` et `y` pour le centre de l'image. Cette planète a pour coordonnées `(128, 128)`.

  --- /feedback ---

--- /choices ---

--- /question ---
