## Αναστοχασμός

Answer the three questions. There are hints to guide you to the correct answer.

Απάντησε στις τρεις ερωτήσεις παρακάτω για να διαπιστώσεις τι έμαθες.

Have fun!

--- question ---
---
legend: Ερώτηση 1 από 3
---

Which output would you expect if you ran the program below?

```python
for i in range(5):
  print("Βρόχος", i)
```

--- choices ---

- ( ) Βρόχος 1 <br> Βρόχος 2 <br> Βρόχος 3 <br> Βρόχος 4 <br> Βρόχος 5

  --- feedback ---

Not quite, a `for` loop in Python repeats its code once for each item in a sequence it's given, and here `range` creates a sequence starting from `0`.

  --- /feedback ---

- ( ) Βρόχος i

  --- feedback ---

Not quite, the **loop variable** from a `for` loop — in this case `i` — holds the current value from the sequence the loop is working through.

  --- /feedback ---

- (x) Βρόχος 0 <br> Βρόχος 1 <br> Βρόχος 2 <br> Βρόχος 3 <br> Βρόχος 4

  --- feedback ---

Correct. The loop runs once, in order, for each item `i` in the range [0, 1, 2, 3, 4].

  --- /feedback ---

- ( ) Βρόχος 4 <br> Βρόχος 3 <br> Βρόχος 2 <br> Βρόχος 1 <br> Βρόχος 0

  --- feedback ---

Not quite, a `for` loop runs through the sequence of items it is given in order. Because `range()` gives an ordered sequence from 0 to the number it is passed, that is the order you would expect to see printed out by this `for` loop.

  --- /feedback ---

--- /choices ---

--- /question ---
