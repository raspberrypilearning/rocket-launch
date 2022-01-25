
--- question ---
---
legend: Question 2 of 3
---

A project has this `setup` code to load a planet image and say that images should be positioned at their centre:

--- code ---
---
language: python
---

def setup():   
  size(400, 400)   
  image_mode(CENTER)   
  global planet   
  planet = load_image('planet.png')   

--- /code ---

Coordinates start from (0, 0) in the top-left corner. In the project you drew planet and rocket images using the `image(image_file, x-coord, y-coord, x-width, y-width)` function.

Where will this code position the planet image?

--- code ---
---
language: python
---

image(planet, 300, 100, 128, 128)

--- /code ---

--- choices ---

- ( ) 
![A planet image positioned horizontally off at the right of the screen and vertically in the middle.](images/planet400200.png)

  --- feedback ---

The second and third inputs to the `image()` function are the `x` and `y` coordinates for the centre of the image. This planet has the coordinates `(400, 200)`.
  
  --- /feedback ---

- ( ) 
![A planet image positioned in the middle of the bottom-left quadrant.](images/planet100300.png)

  --- feedback ---

The second and third inputs to the `image()` function are the `x` and `y` coordinates for the centre of the image. This planet has the coordinates `(100, 300)`.
  
  --- /feedback ---

- (x) 
![A planet image positioned in the middle of the top-right quadrant.](images/planet300100.png)

  --- feedback ---

Correct! The second and third inputs to the `image()` function are the `x` and `y` coordinates for the centre of the image. This image has the coordinates (300, 100) so it is 300 (out of 400) pixels from the left for the `x` coordinate and 100 (out of 400) pixels down from the top. 
 
  --- /feedback ---

- ()
![A planet image positioned in the top-left quadrant.](images/planet128128.png)

  --- feedback ---

The fourth and fifth inputs give the size of the image. The second and third inputs to the `image()` function are the `x` and `y` coordinates for the centre of the image. This planet has the coordinates `(128, 128)`. 
  
  --- /feedback ---

--- /choices ---

--- /question ---
