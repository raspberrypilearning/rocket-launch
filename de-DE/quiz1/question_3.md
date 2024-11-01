--- question ---
---
legend: Frage 3 von 3
---

Dieser Code verwendet `tint()`, um eine Rakete in einem Spiel einzufärben und anzuzeigen, wie es gerade läuft.

--- code ---
---
language: python
---

if punkte >= 100:    
    tint(0, 255, 0) #Grün   
elif punkte < 100 and leben == 1:   
    tint(255, 200, 0) #Gelb    
elif punkte < 100 and leben == 0:     
    tint(255, 0, 0) #Rot     
else:      
    no_tint()

image(rocket, width/2, height/2, 64, 64)

--- /code ---

Wenn die Variable `punkte` den Wert `99` und die Variable `leben` den Wert `1`hat, wie wird die Rakete aussehen?

--- choices ---

- (x)

![Ein Raketenbild mit gelben Farbton.](images/rocket_amber.png)
<div style="text-align: center;">Gelb

 --- feedback ---

 Korrekt! Der Spieler hat weniger als 100 Punkte und nur noch 1 Leben. Die Rakete ist gelb, um anzuzeigen, dass dies die letzte Chance ist, zu gewinnen!

 --- /feedback ---

- ( )

![Ein Raketenbild ohne Tönung](images/rocket_original.png)
<div style="text-align: center;">Keine Tönung

 --- feedback ---

 Nicht ganz, die Rakete hat eine Tönung, da eine der Aussagen wahr ist.

 --- /feedback ---

- ( )

![Ein Raketenbild mit grünem Farbton](images/rocket_green.png)
<div style="text-align: center;">Grün

 --- feedback ---

 Nicht ganz, es wären `>= 100` Punkte nötig, um zu gewinnen und die Rakete grün zu färben. Hier ist die Punktezahl `99`, was nicht genug ist. Prüfe die Bedingungen sorgfältig.

 --- /feedback ---

- ( )

![Ein Raketenbild mit rotem Farbton](images/rocket_red.png)
<div style="text-align: center;">Rot

 --- feedback ---

 Nicht ganz, es wurden `< 100` Punkte erzielt, aber Anzahl Leben ist nicht `0`. Prüfe die Bedingungen sorgfältig.

 --- /feedback ---

--- /choices ---

--- /question ---
