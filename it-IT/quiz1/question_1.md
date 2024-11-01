## Quiz veloce

Rispondi alle tre domande. Ci sono alcuni suggerimenti per aiutarti a trovare la risposta corretta.

Dopo aver risposto a ciascuna domanda, fai clic su **Controlla la mia risposta**.

Divertiti!

--- question ---
---
legend: Domanda 1 di 3
---

Quale risultato ti aspetteresti se eseguissi il programma seguente?

```python
for i in range(5):
  print("Ciclo", i)
```

--- choices ---

- ( ) Ciclo 1 <br> Ciclo 2 <br> Ciclo 3 <br> Ciclo 4 <br> Ciclo 5

  --- feedback ---

Non proprio, un ciclo `for` in Python ripete il suo codice una volta nella sequenza stabilita, e qui `range` inizia la sequenza partendo da `0`.

  --- /feedback ---

- ( ) Ciclo i

  --- feedback ---

Non proprio,  **la variabile del ciclo** che varia ad ogni ciclo `for` — in questo caso `i` — memorizza il valore corrente per la sequenza in esecuzione.

  --- /feedback ---

- (x) Ciclo 0 <br> Ciclo 1 <br> Ciclo 2 <br> Ciclo 3 <br> Ciclo 4

  --- feedback ---

Corretto. Il ciclo viene eseguito una volta, in ordine, per ogni elemento `i` nell'intervallo [0, 1, 2, 3, 4].

  --- /feedback ---

- ( ) Ciclo 4 <br> Ciclo 3 <br> Ciclo 2 <br> Ciclo 1 <br> Ciclo 0

  --- feedback ---

Dato che `range()` restituisce una sequenza ordinata di numeri da 0 al numero che gli è stato passato, questo è l'ordine che dovrai aspettarti che verrà stampato ad un ciclo di `for`. Dato che`range()` restituisce una sequenza ordinata di numeri da 0 al numero che gli è stato passato, questo è l'ordine che dovrai aspettarti che verrà stampato ad un ciclo di `for`.

  --- /feedback ---

--- /choices ---

--- /question ---
