## Зліт!

Ми вже додали зображення ракети у початковий проєкт.

![Зображення ракети в бібліотеці зображень редактора коду Code Editor.](images/rocket_image.png)

--- task ---

Додай код до функції `setup()`, щоб завантажити зображення ракети у глобальну змінну `rocket`.

<div class="c-project-code">

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 17
line_highlights: 21, 23
---

def setup():   
# Тут налаштуй анімацію   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet, rocket   
planet = load_image('planet.png')    
rocket = load_image('rocket.png')

--- /code ---

--- /task ---

--- task ---

Додай глобальну змінну `rocket_position`, щоб відстежувати положення ракети за віссю `y`.

--- code ---
---
language: python line_numbers: true line_number_start: 5
line_highlights: 7
---

# Встанови глобальні змінні
screen_size = 400    
rocket_position = screen_size

--- /code ---

--- /task ---


Положення ракети за віссю `y` буде починатися з 400 (висота екрану), а потім буде зменшуватися на 1 щоразу, коли малюватиметься новий кадр.

--- task ---

Визнач функцію `draw_rocket()`, щоб ракета з’явилася на екрані.

--- code ---
---
language: python line_numbers: true line_number_start: 9
line_highlights: 10-12
---

# Тут буде функція draw_rocket
def draw_rocket():   
global rocket_position      
image(rocket, width/2, rocket_position, 64, 64)


--- /code ---

--- /task ---

--- task ---

Виклич функцію `draw_rocket()`.

--- code ---
---
language: python line_numbers: true line_number_start: 29
line_highlights: 32
---

def draw(): # Що відбувається на кожному кадрі draw_background() draw_rocket()


--- /code ---

--- /task ---

--- task ---

**Протестуй:** запусти свій код і переконайся, що внизу зображення зʼявляється ракета.

--- /task ---


Щоразу, як малюється новий кадр, ти маєш перемістити ракету на один піксель вгору, щоб створити ефект анімації.


--- task ---

Положення ракети `rocket_position` буде починатися з 400 (висота екрану), а потім буде зменшуватися на 1 щоразу, коли малюватиметься новий кадр.


--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 12
---

def draw_rocket():   
global rocket_position     
rocket_position = rocket_position - 1    
image(rocket, width/2, rocket_position, 64, 64)

--- /code ---

--- /task ---


--- task ---

**Протестуй:** запусти свій код і переконайся, що ракета злітає з нижньої частини екрану вгору.


![Ракета, що летить з постійною швидкістю від низу до верху екрану.](images/fly.gif){:width="300px"}

--- /task ---

