## Effets d'échappement

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

La fusée aura l'air plus réaliste avec quelques effets spéciaux pour simuler la traînée d'échappement. 

Tu peux créer des effets sympas en utilisant une boucle "for" pour dessiner de nombreuses formes dans chaque image.

</div>
<div>

![La fusée en plein vol avec une traînée d'échappement.](images/flying_rocket.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Le codage est utilisé pour créer des <span style="color: #0faeb0">**effets graphiques**</span> pour les films et les jeux. Il est beaucoup plus rapide d'écrire du code que de dessiner chaque image d'une animation individuellement. </p>

Dessiner beaucoup d'ellipses jaunes à différentes positions `y` crée une traînée d'échappement avec un fond rond.

--- task ---

Une boucle `for` répète un morceau de code une fois pour chaque élément qui lui est donné. Pour exécuter le code dans une boucle `for` un certain nombre de fois, tu peux utiliser la fonction `range()`. Par exemple, `range(5)` crée une séquence de cinq nombres à partir de 0, donc [0, 1, 2, 3, 4].

Chaque fois que la boucle `for` se répète, elle définit une variable sur l'élément actuel afin que tu puisses l'utiliser dans la boucle.

Mets à jour ta fonction `dessine_fusee()` pour inclure une boucle `for` qui répète le dessin de `25` ellipses d'échappement. La **variable de boucle** `i` est ajoutée à `fusee_y` pour dessiner chaque ellipse plus loin sous la fusée.

--- code ---
---
language: python 
filename: main.py - dessine_fusee() 
line_numbers: true 
line_number_start: 12
line_highlights: 16-22
---

def dessine_fusee():

  global fusee_y   
  fusee_y -= 1

  no_stroke() # Désactive le trait

  for i in range(25): #Dessine 25 ellipses d'échappement brûlants   
    fill(255, 255, 0) #Jaune   
    ellipse(width/2, fusee_y + i, 8, 3) #i augmente chaque fois que la boucle se répète

  image(fusee, width/2, fusee_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton code pour vérifier que la fusée a une nouvelle traînée d'échappement.

![Un gros plan de la fusée avec une traînée d'échappement.](images/rocket_exhaust.png){:width="300px"}

--- /task ---

La variable `i` peut également être utilisée pour créer un dégradé de couleur avec moins de vert dans chaque ellipse dessinée.

--- task ---

Remplace l'appel par `fill()` pour définir la quantité de vert sur `255 - i*10` afin que la première ellipse ait des quantités égales de rouge et de vert et que la dernière ellipse ait très peu de vert.

--- code ---
---
language: python 
filename: main.py - dessine_fusee() 
line_numbers: true 
line_number_start: 19
line_highlights: 20
---

  for i in range(25):   
    fill(255, 255 - i * 10, 0) #Réduire la quantité de vert    
    ellipse(width/2, fusee_y + i, 8, 3)

--- /code ---

--- /task ---

--- task ---

**Test :** Vérifie que tu obtiens une traînée d'ellipses passant progressivement du jaune au rouge.

--- /task ---

La traînée de fumée est créée en dessinant de nombreuses ellipses grises légèrement transparentes à différents endroits de chaque image.

![Une animation lente de l'effet de fumée.](images/rocket_smoke.gif)

--- task ---

Cette fois, le `fill()` est en dehors de la boucle car la couleur est la même pour chaque ellipse de fumée. La quatrième entrée de `fill()` est l'opacité, une faible valeur d'opacité rend la couleur plus transparente afin que tu puisses voir les formes en dessous.

Dans chaque image de l'animation, 20 ellipses de tailles aléatoires seront dessinées à des positions aléatoires.

--- code ---
---
language: python 
filename: main.py - dessine_fusee() 
line_numbers: true 
line_number_start: 19
line_highlights: 23-26
---

  for i in range(25):  
    fill(255, 255 - i * 10, 0)   
    ellipse(width/2, fusee_y + i, 8, 3)

  fill(200, 200, 200, 100) #Gris transparent   
    for i in range(20): #Dessine 20 ellipses de fumée aléatoires    
    ellipse(width/2 + randint(-5, 5), fusee_y + randint(20 , 50), randint(5, 10), randint(5, 10))

  image(fusee, width/2, fusee_y, 64, 64)

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton programme et vérifie que les gaz d'échappement sont visibles.

![Un gros plan de la fusée et de la traînée d'échappement avec de la fumée supplémentaire.](images/rocket_exhaust_circles.gif)

--- /task ---

--- save ---
