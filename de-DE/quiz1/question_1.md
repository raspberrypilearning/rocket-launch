## Kurzes Quiz

Beantworte die drei Fragen. Hinweise helfen dir beim Finden der richtigen Antwort.

Nach dem Beantworten jeder Frage wähle **Meine Antwort prüfen**.

Viel Spaß!

--- question ---
---
legend: Frage 1 von 3
---

Welche Ausgabe würdest du erwarten, wenn du das folgende Programm ausführen würdest?

```python
for i in range(5):
  print("Schleife", i)
```

--- choices ---

- ( ) Schleife 1 <br> Schleife 2 <br> Schleife 3 <br> Schleife 4 <br> Schleife 5

  --- feedback ---

Nicht ganz, eine `for`-Schleife in Python wiederholt ihren Code einmal für jedes Element in einer gegebenen Sequenz, und hier erstellt `range` eine Sequenz, die bei `0`beginnt.

  --- /feedback ---

- ( ) i <br> i <br> i <br> i <br> i

  --- feedback ---

Nicht ganz, die **Schleifenvariable** aus einer `for`-Schleife – in diesem Fall `i` – enthält den aktuellen Wert aus der Sequenz, die die Schleife durchläuft.

  --- /feedback ---

- (x) Schleife 0 <br> Schleife 1 <br> Schleife 2 <br> Schleife 3 <br> Schleife 4

  --- feedback ---

Korrekt. Die Schleife wird der Reihe nach einmal für jedes Element `i` in der Sequenz [0, 1, 2, 3, 4] ausgeführt.

  --- /feedback ---

- ( ) Schleife 4 <br> Schleife 3 <br> Schleife 2 <br> Schleife 1 <br> Schleife 0

  --- feedback ---

Not quite. Unless you have specified otherwise, a `for` loop will start at 0 and count up the number of times specified in the range.

  --- /feedback ---

--- /choices ---

--- /question ---
