## Reflection

Well done, you have learned a lot! Now it's time to reflect - reflecting is an important part of learning because it helps make new connections in your brain.

Answer the three questions below to reflect on what you've learned.

After each question, press submit. You will be guided towards the correct answer. You can do this activity as many times as you want to.

Have fun!

--- question ---

---
legend: Question 1 of 3
---

Which output would you expect if you ran the program below?

```python
count = range(5)

for counter in count:
  print("Looping", counter)
```
--- choices ---

- ( ) Looping 0

  --- feedback ---
A `for` loop in Python repeats its code once for each item in a sequence it's given.
  --- /feedback ---

- ( ) Looping counter

  --- feedback ---
The **loop variable** from a `for` loop — in this case `counter` — holds the current value from the sequence the loop is working through. In the case of this loop, counter would hold 0, 1, 2, 3, and 4 in that order, as that is the sequence created by `range(5)` and stored in `count`.
  --- /feedback ---

- (x) Looping 0 <br> Looping 1 <br> Looping 2 <br> Looping 3 <br> Looping 4

  --- feedback ---
Correct. The loop runs once, in order, for each item in the sequence stored in `count`.
  --- /feedback ---

- ( ) Looping 0 <br> Looping 3 <br> Looping 2 <br> Looping 4 <br> Looping 1

  --- feedback ---
A `for` loop runs through the sequence of items it is given in order. Because `range()` gives an ordered sequence from 0 to the number it is passed, that is the order you would expect to see printed out by this `for` loop.
  --- /feedback ---

--- /choices ---

--- /question ---
