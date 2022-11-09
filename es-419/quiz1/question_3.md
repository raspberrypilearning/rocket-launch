--- question ---
---
legend: Pregunta 3 de 3
---

Este programa usa `tint()` para colorear un cohete en un juego para mostrarle al jugador cómo lo está haciendo.

--- code ---
---
language: python
---

if puntos >= 100:    
tint(0, 255, 0) #Green   
elif puntos < 100 and vidas == 1:   
tint(255, 200, 0) #Amber    
elif puntos < 100 and vidas == 0:     
tint(255, 0, 0) #Red     
else:      
no_tint()

imagen(cohete, width/2, alto/2, 64, 64)

--- /code ---

Si la variable `puntos` tiene el valor `99` y la variable `vidas` tiene el valor `1`, ¿cómo se verá el cohete?

--- choices ---

- (x)

![Una imagen de cohete con tinte ámbar.](images/rocket_amber.png) <div style="text-align: center;">Ámbar

 --- feedback ---

 ¡Correcto! El jugador tiene menos de 100 puntos y solo le queda 1 vida. The rocket is coloured amber to let them know that this is their last chance to win!

 --- /feedback ---

- ( )

![Una imagen de cohete sin tinte](images/rocket_original.png) <div style="text-align: center;">Sin tinte

 --- feedback ---

 No del todo, el cohete tiene un matiz ya que una de las afirmaciones es cierta.

 --- /feedback ---

- ( )

![Una imagen de cohete con tinte verde](images/rocket_green.png) <div style="text-align: center;">Verde

 --- feedback ---

 No del todo, el jugador necesitaría `>= 100` puntos para ganar y convertir su cohete en verde. Tienen `99`, que no es suficiente. Revisa bien las condiciones.

 --- /feedback ---

- ( )

![Una imagen de cohete con tinte rojo](images/rocket_red.png) <div style="text-align: center;">Rojo

 --- feedback ---

 No del todo, el jugador tiene `< 100` puntos pero vidas no es igual a `0`. Revisa bien las condiciones.

 --- /feedback ---

--- /choices ---

--- /question ---
