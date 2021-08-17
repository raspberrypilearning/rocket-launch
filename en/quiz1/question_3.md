
--- question ---

---
legend: Question 3 of 3
---

If you wanted your program to output:

```
I like pizza
But I prefer ice cream
```

How would you call the `favourites()` function, defined in the code below?

```python
def favourites(food, prefercence):
  print("I like", food)
  print("But I prefer", preference)
```

--- choices ---

- ( ) `favourites`


  --- feedback ---
This is just the name of the function. Any function needs to be called with parentheses to run the code inside it: `my_function()` 
  --- /feedback ---

- ( ) `favourites()`

  --- feedback ---
This would work for a function that did not expect any inputs. However, `favourites()` expects to be passed values for `food` and `preference` when it is called.
  --- /feedback ---

- (x) `favourites('pizza','ice cream')`


  --- feedback ---
This is correct. `favourites()` needs to be passed `'pizza'` and `'ice cream'`, in that order, to get the result you want.
  --- /feedback ---

- ( ) `favourites('ice cream', 'pizza')`


  --- feedback ---
Close, but the parameters are in the wrong order. Passing them this way sets `food` to `'ice cream'` and `preference` to `'pizza'`, which will lead to:

```
I like ice cream
But I prefer pizza
```
  --- /feedback ---

--- /choices ---

--- /question ---
