--- question ---
---
legend: Domanda 3 di 3
---

Questo codice utilizza `tint()` per colorare un razzo in un gioco e mostrare al giocatore come sta andando.

--- code ---
---
language: python
---

if points >= 100:    
    tint(0, 255, 0) # Verde   
elif points < 100 and lives == 1:   
    tint(255, 200, 0) # Giallo    
elif points < 100 and lives == 0:     
    tint(255, 0, 0) # Rosso     
else:      
    no_tint()

image(rocket, width/2, height/2, 64, 64)

--- /code ---

Se la variabile `points` ha il valore `99` e la variabile `lives` ha il valore `1`, come sarà il razzo?

--- choices ---

- (x)

![Un'immagine di un razzo colorato di giallo.](images/rocket_amber.png) <div style="text-align: center;">Giallo

 --- feedback ---

 Corretto! Il giocatore ha meno di 100 punti e solo 1 vita rimasta. Il razzo è colorato di giallo per far sapere al giocatore che questa è la sua ultima possibilità di vincere!

 --- /feedback ---

- ( )

![Un'immagine di un razzo senza colore](images/rocket_original.png) <div style="text-align: center;">No tint

 --- feedback ---

 Non proprio, il razzo ha un colore perché una delle affermazioni è vera.

 --- /feedback ---

- ( )

![Un'immagine di un razzo colorato di verde](images/rocket_green.png) <div style="text-align: center;">Verde

 --- feedback ---

 Non proprio, il giocatore avrebbe bisogno di `>= 100` punti per vincere e far diventare verde il suo razzo. Ha `99`, il che non è sufficiente. Controlla attentamente le condizioni.

 --- /feedback ---

- ( )

![Un'immagine di un razzo colorato di rosso](images/rocket_red.png) <div style="text-align: center;">Rosso

 --- feedback ---

 Non proprio, il giocatore ha `< 100` punti ma le vite non sono a `0`. Controlla attentamente le condizioni.

 --- /feedback ---

--- /choices ---

--- /question ---
