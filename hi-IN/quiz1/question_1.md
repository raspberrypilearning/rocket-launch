## Quick quiz

Answer the three questions. There are hints to guide you to the correct answer.

When you have answered each question, click on **Check my answer**.

Have fun!

--- question ---
---
प्रश्न १ का ३
---

Which output would you expect if you ran the program below?

```python
for i in range(5):
  print("Looping", i)
```

--- choices ---

- ( ) 1 <br> looping 2 <br> looping 3 <br> looping 4 <br> looping 5

  --- feedback ---

Not quite, a `for` loop in Python repeats its code once for each item in a sequence it's given, and here `range` creates a sequence starting from `0`.

  --- /feedback ---

- ( ) लूपिंग I

  --- feedback ---

Not quite, the **loop variable** from a `for` loop — in this case `i` — holds the current value from the sequence the loop is working through.

  --- /feedback ---

- (x) लूपिंग 0 <br> लूपिंग 1 <br> लूपिंग 2 <br> looping 3 <br> looping 4

  --- feedback ---

Correct. The loop runs once, in order, for each item `i` in the range [0, 1, 2, 3, 4].

  --- /feedback ---

- ( ) 4 <br> looping 3 <br> looping 2 <br> looping 1 <br> looping 0

  --- feedback ---

Not quite, a `for` loop runs through the sequence of items it is given in order. Because `range()` gives an ordered sequence from 0 to the number it is passed, that is the order you would expect to see printed out by this `for` loop.

  --- /feedback ---

--- /choices ---

--- /question ---
