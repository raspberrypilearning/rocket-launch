## Quick quiz

Answer the three questions. There are hints to guide you to the correct answer.

When you have answered each question, click on **Check my answer**.

Have fun!

--- question ---
---
legend: Vraag 1 van 3
---

Which output would you expect if you ran the program below?

```python
for i in range(5):
  print("Lus", i)
```

--- choices ---

- ( ) Lus 1 <br> Lus 2 <br> Lus 3 <br> Lus 4 <br> Lus 5

  --- feedback ---

Not quite, a `for` loop in Python repeats its code once for each item in a sequence it's given, and here `range` creates a sequence starting from `0`.

  --- /feedback ---

- ( ) Lus i

  --- feedback ---

Not quite, the **loop variable** from a `for` loop — in this case `i` — holds the current value from the sequence the loop is working through.

  --- /feedback ---

- (x) Lus 0 <br> Lus 1 <br> Lus 2 <br> Lus 3 <br> Lus 4

  --- feedback ---

Correct. The loop runs once, in order, for each item `i` in the range [0, 1, 2, 3, 4].

  --- /feedback ---

- ( ) Lus 4 <br> Lus 3 <br> Lus 2 <br> Lus 1 <br> Lus 0

  --- feedback ---

Nto quite, a `for` loop runs through the sequence of items it is given in order. Because `range()` gives an ordered sequence from 0 to the number it is passed, that is the order you would expect to see printed out by this `for` loop.

  --- /feedback ---

--- /choices ---

--- /question ---
