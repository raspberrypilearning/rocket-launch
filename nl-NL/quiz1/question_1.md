## Snelle quiz

Beantwoord de drie vragen. Je wordt naar het juiste antwoord geleid.

Klik na het beantwoorden van elke vraag op **Indienen**.

Veel plezier!

--- question ---
---
legend: Vraag 1 van 3
---

Welke uitvoer zou je verwachten als je het onderstaande programma zou draaien?

```python
for i in range(5):
  print("Lus", i)
```

--- choices ---

- ( ) Lus 1 <br> Lus 2 <br> Lus 3 <br> Lus 4 <br> Lus 5

  --- feedback ---

Niet helemaal, een `for` lus in Python herhaalt zijn code in een gegeven reeks, en hier creëert `range` een reeks die begint bij `0`.

  --- /feedback ---

- ( ) i <br> i <br> i <br> i <br> i

  --- feedback ---

Niet helemaal, de **lus variabele** van een `for` lus - in dit geval `i` - bevat de huidige waarde uit de reeks waar de lus doorheen loopt.

  --- /feedback ---

- (x) Lus 0 <br> Lus 1 <br> Lus 2 <br> Lus 3 <br> Lus 4

  --- feedback ---

Juist. De lus loopt één keer, in volgorde, voor elk item `i` in het bereik [0, 1, 2, 3, 4].

  --- /feedback ---

- ( ) Lus 4 <br> Lus 3 <br> Lus 2 <br> Lus 1 <br> Lus 0

  --- feedback ---

Not quite. Unless you have specified otherwise, a `for` loop will start at 0 and count up the number of times specified in the range.

  --- /feedback ---

--- /choices ---

--- /question ---
