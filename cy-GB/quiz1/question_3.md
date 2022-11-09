--- question ---
---
legend: Cwestiwn 3 o 3
---

Mae'r cod hwn yn defnyddio `tint()` i liwio roced mewn gêm i ddangos i'r chwaraewr sut hwyl mae'n ei gael.

--- code ---
---
language: python
---

if points >= 100:    
tint(0, 255, 0) #Green   
elif points < 100 and lives == 1:   
tint(255, 200, 0) #Amber    
elif points < 100 and lives == 0:     
tint(255, 0, 0) #Red     
else:      
no_tint()

image(rocket, width/2, height/2, 64, 64)

--- /code ---

Os oes gan y newidyn `pwyntiau` werth o `99` a bod gan y newidyn `bywydau` werth o `1`, sut fydd y roced yn edrych?

--- choices ---

- (x)

![Delwedd o roced gydag arlliw melyngoch.](images/rocket_amber.png) <div style="text-align: center;">Melyngoch

 --- feedback ---

 Cywir! Mae gan y chwaraewr lai na 100 o bwyntiau a dim ond 1 bywyd yn weddill. The rocket is coloured amber to let them know that this is their last chance to win!

 --- /feedback ---

- ( )

![Delwedd o roced heb arlliw](images/rocket_original.png) <div style="text-align: center;">Dim arlliw

 --- feedback ---

 Ddim yn hollol, mae gan y roced arlliw oherwydd bod un o'r datganiadau'n wir.

 --- /feedback ---

- ( )

![Delwedd o roced gydag arlliw gwyrdd](images/rocket_green.png) <div style="text-align: center;">Gwyrdd

 --- feedback ---

 Ddim yn hollol, bydd angen `>= 100` o bwyntiau ar y chwaraewr i ennill a throi eu roced yn wyrdd. Mae ganddyn nhw `99`, sydd ddim yn ddigon. Gwiriwch yr amodau'n ofalus.

 --- /feedback ---

- ( )

![Delwedd o roced gydag arlliw coch](images/rocket_red.png) <div style="text-align: center;">Coch

 --- feedback ---

 Ddim yn hollol, mae gan y chwaraewr `< 100` o bwyntiau ond nid yw'r bywydau'n hafal i `0`. Gwiriwch yr amodau'n ofalus.

 --- /feedback ---

--- /choices ---

--- /question ---
