## Quick quiz

Answer the three questions. There are hints to guide you to the correct answer.

When you have answered each question, click on **Check my answer**.

Have fun!

--- question ---
---
legend: Cwestiwn 1 o 3
---

Which output would you expect if you ran the program below?

```python
for i in range(5):
  print("Looping", i)
```

--- choices ---

- ( ) Gwneud dolen 1 <br> Gwneud dolen 2 <br> Gwneud dolen 3 <br> Gwneud dolen 4 <br> Gwneud dolen 5

  --- feedback ---

Not quite, a `for` loop in Python repeats its code once for each item in a sequence it's given, and here `range` creates a sequence starting from `0`.

  --- /feedback ---

- ( ) Gwneud dolen i

  --- feedback ---

Not quite, the **loop variable** from a `for` loop — in this case `i` — holds the current value from the sequence the loop is working through.

  --- /feedback ---

- (x) Gwneud dolen 0 <br> Gwneud dolen 1 <br> Gwneud dolen 2 <br> Gwneud dolen 3 <br> Gwneud dolen 4

  --- feedback ---

Correct. The loop runs once, in order, for each item `i` in the range [0, 1, 2, 3, 4].

  --- /feedback ---

- ( ) Gwneud dolen 4 <br> Gwneud dolen 3 <br> Gwneud dolen 2 <br> Gwneud dolen 1 <br> Gwneud dolen 0

  --- feedback ---

Nto quite, a `for` loop runs through the sequence of items it is given in order. Because `range()` gives an ordered sequence from 0 to the number it is passed, that is the order you would expect to see printed out by this `for` loop.

  --- /feedback ---

--- /choices ---

--- /question ---
