--- question ---
---
legend: Pytanie 3 z 3
---

Ten kod używa ` tint()` do pokolorowania rakiety w grze, aby pokazać graczowi, jak sobie radzą.

--- code ---
---
language: python
---

if points >= 100:    
Tint(0, 255, 0) # punkty elif    
< 100 i żyje == 1:   
tint(255, 200, 0) #    
punkty elif < 100 i życia == 0:     
tint(255, 0, 0) #     
else:      
no_tint()

image(rakieta, width/2, height/2, 64, 64)

--- /code ---

Jeśli zmienna ` ` ma wartość ` `, a zmienna ` ` ma wartość ` `, to jak będzie wyglądała rakieta?

--- choices ---

- (x)

![Obraz rakiety z bursztynowym odcieniem.](images/rocket_amber.png) <div style="text-align: center;">Bursztynowy

 --- feedback ---

 Poprawna odpowiedź! Gracz ma mniej niż 100 punktów i pozostało tylko jedno życie. Rakieta ma kolor bursztynowy, aby poinformować ich, że jest to ich ostatnia szansa na wygraną!

 --- /feedback ---

- ( )

![Obraz rakiety bez odbarwienia](images/rocket_original.png) <div style="text-align: center;">Bez zabarwienia

 --- feedback ---

 Nie do końca, rakieta ma odcień, ponieważ jedno z twierdzeń jest prawdziwe.

 --- /feedback ---

- ( )

![Obraz rakiety z zielonym odcieniem](images/rocket_green.png) <div style="text-align: center;">Zielony

 --- feedback ---

 Nie do końca, gracz potrzebuje punktów `>= 100 `, aby wygrać i zmienić swoją rakietę na zieloną. Mają ` `, co nie wystarczy. Sprawdź dokładnie warunki.

 --- /feedback ---

- ( )

![Obraz rakiety z czerwonym odcieniem](images/rocket_red.png) <div style="text-align: center;">Czerwony

 --- feedback ---

 Nie do końca, gracz ma punkty `< 100 `, ale życie nie równa się ` 0 `. Sprawdź dokładnie warunki.

 --- /feedback ---

--- /choices ---

--- /question ---
