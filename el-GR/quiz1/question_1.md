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

Not quite, a `for` loop in Python starts from 0, unless otherwise specified.

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

Not quite. Unless you have specified otherwise, a `for` loop will start at 0 and count up the number of times specified in the range.

  --- /feedback ---

--- /choices ---

--- /question ---
