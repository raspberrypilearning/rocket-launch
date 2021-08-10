
--- question ---

---
legend: Question 2 of 3
---

![A planet inside a grey square is shown on a grid. At the top-left corner of the square, the coordinates (210, 50) are shown. At the top-right corner of the square, the coordinates (310, 50) are shown. At the bottom-right corner of the square, the coordinates (310, 150) are shown. At the bottom-left corner of the square, the coordinates (210, 150) are shown.](images/quiz_planet.png)

Which code would position the planet sprite where it is shown in this image?

--- choices ---

- ( ) 
```python
image(
  planet,
  310,
  50,
  100,
  100
  )
```

  --- feedback ---
The `image()` function needs to be given the coordinates for the top-left corner of the image. `(310, 50)` are the coordinates for the top-right corner.
  --- /feedback ---

- ( ) 
```python
image(
  planet,
  0,
  0,
  100,
  100
  )
```

  --- feedback ---
`(0, 0)` are the coordinates of the top-left corner of the grid you are drawing on, and the planet is positioned down and to the right.
  --- /feedback ---

- ( ) 
```python
translate(210, 50)

image(
  planet,
  210,
  50,
  100,
  100
  )
```

  --- feedback ---
`translate()` moves the entire grid by the amount it is given for x and y. In this example, it would have moved the grid so the new `(0, 0)` is at the old `(210, 50)`. The new `(210, 50)` — where this code tries to draw the planet — is at the old `(420, 100)` and so totally off screen!
  --- /feedback ---

- (x)

```python
translate(210, 50)

image(
  planet,
  0,
  0,
  100,
  100
  )
```

  --- feedback ---
Correct. By moving the grid `(0, 0)` by `(210, 50)` you can draw the image at `(0, 0)` and get the result you want.
  --- /feedback ---

--- /choices ---

--- /question ---
