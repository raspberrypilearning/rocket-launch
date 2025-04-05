## Створення фону

--- task ---

Відкрий [шаблон проєкту](https://trinket.io/python/77c37dd931){:target="_blank"}.

--- /task ---

First, you will create a black background to represent space.

--- task ---

Define a `draw_background()` function, and set the background colour to black.

--- code ---
---
Знайди коментар `Налаштування глобальних змінних` та додай рядок коду для створення змінної `screen_size`:
line_highlights: 8
---

# Налаштування глобальних змінних
def draw_background():   
background(0, 0, 0)

--- /code ---

--- /task ---

--- task ---

Add this function to the list of things to `draw()` in every frame.

--- code ---
---
Використовуй змінну `screen_size`, щоб створити квадрат розміром 400 на 400 пікселів:
line_highlights: 20
---

def draw(): # Things to do in every frame draw_background()

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and you should see a black square.

--- /task ---



--- task ---

Add a line of code to display an image of a planet.

--- code ---
---
language: python line_numbers: true line_number_start: 13
line_highlights: 21-23
---
def draw_background():  
background(0,0,0) image(planet, screen_size/2, screen_size, 300, 300)

--- /code ---


Зображення зручно завантажувати в `setup()`, щоб вони завжди були напоготові, коли тобі потрібно буде їх використати, а твоя анімація буде швидко запускатись.

- image filename - we have already loaded the planet image
- x coordinate - we have already set the screen size
- y coordinate
- image width
- image height

--- /task ---

--- task ---

def setup():   
#Налаштувати анімацію можна тут   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet   
planet = load_image('planet.png') #Твоя обрана планета

![A planet against a black background.](images/step_2.png){:width="300px"}

--- /task ---

### A different planet?

--- task ---

Визнач функцію `draw_background()`, щоб намалювати фон, внизу коментаря, який підказує, куди його треба поставити.

![Choose a different planet](images/image_gallery.png)

If you want to change the planet image, change `planet.png` in the code to the filename of your chosen planet, for example, `orange_planet.png`.

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 15-17
---
def setup(): # Set up your animation here size(screen_size, screen_size) image_mode(CENTER) global planet planet = load_image('planet.png')

--- /code ---

--- /task ---

