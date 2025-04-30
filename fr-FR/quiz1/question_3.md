--- question ---
---
legend: Question 3 sur 3
---

Ce code utilise `tint()` pour colorer une fusée dans un jeu afin de montrer au joueur comment il se débrouille.

--- code ---
---
language: python
---

if points >= 100:    
    tint(0, 255, 0) #Vert   
elif points < 100 and vies == 1:   
    tint(255, 200, 0) #Orange    
elif points < 100 and vies == 0:     
    tint(255, 0, 0) #Rouge     
else:      
    no_tint()

image(fusee, width/2, height/2, 64, 64)

--- /code ---

Si la variable `points` a la valeur `99` et la variable `vies` a la valeur `1`, à quoi ressemblera la fusée ?

--- choices ---

- (x)

![Une image de fusée avec une teinte orange.](images/rocket_amber.png)
<div style="text-align: center;">Orange

 --- feedback ---

 Correct ! Le joueur a moins de 100 points et seulement 1 vie restante. La fusée est de couleur orange pour leur faire savoir que c'est leur dernière chance de gagner !

 --- /feedback ---

- ( )

![Une image de fusée sans teinte](images/rocket_original.png)
<div style="text-align: center;">Pas de teinte

 --- feedback ---

 Pas tout à fait, la fusée a une teinte car l'une des affirmations est vraie.

 --- /feedback ---

- ( )

![Une image de fusée avec une teinte verte](images/rocket_green.png)
<div style="text-align: center;">Vert

 --- feedback ---

 Pas tout à fait, le joueur aurait besoin de `>= 100` points pour gagner et passer la fusée au vert. Ils ont `99`, ce qui n'est pas suffisant. Vérifie bien les conditions.

 --- /feedback ---

- ( )

![Une image de fusée avec une teinte rouge](images/rocket_red.png)
<div style="text-align: center;">Rouge

 --- feedback ---

 Pas tout à fait, le joueur a `< 100` points mais la vie n'est pas égale à `0`. Vérifie bien les conditions.

 --- /feedback ---

--- /choices ---

--- /question ---
