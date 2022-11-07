--- question ---
---
legend: Question 3 of 3
---

This code uses `tint()` to colour a rocket in a game to show the player how they are doing.

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

If the `points` variable has the value `99` and the `lives` variable has the value `1`, what will the rocket look like?

--- choices ---

- (x) 

![A rocket image with amber tint.](images/rocket_amber.png)
<div style="text-align: center;">Amber

 --- feedback ---

 Correct! The player has less than 100 points and only 1 life left. The rocket is coloured amber to let them know that this is their last chance to win!

 --- /feedback ---

- ( ) 

![A rocket image with no tint](images/rocket_original.png)
<div style="text-align: center;">No tint

 --- feedback ---

 Not quite, the rocket has a tint as one of the statements is true.

 --- /feedback ---

- ( ) 

![A rocket image with green tint](images/rocket_green.png)
<div style="text-align: center;">Green

 --- feedback ---

 Not quite, the player would need `>= 100` points to win and turn their rocket green. They have `99`, which is not enough. Check the conditions carefully.

 --- /feedback ---

- ( ) 

![A rocket image with red tint](images/rocket_red.png)
<div style="text-align: center;">Red

 --- feedback ---

 Not quite, the player has `< 100` points but lives does not equal `0`. Check the conditions carefully.

 --- /feedback ---

--- /choices ---

--- /question ---
