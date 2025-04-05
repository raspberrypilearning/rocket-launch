## Намалюй фон

--- task ---

Відкрий [початковий проєкт](https://editor.raspberrypi.org/uk-UA/projects/rocket-launch-starter){:target="_blank"}.

--- /task ---

Спочатку ти створиш чорне тло, — це буде космос.

--- task ---

Визнач функцію `draw_background()` і встанови чорний колір для тла.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12 
line_highlights: 13-14
---

# Тут буде функція draw_background
def draw_background():   
    background(0, 0, 0)

--- /code ---

--- /task ---

--- task ---

Додай цю функцію до списку дій, які будуть виконуватися у кожному кадрі (у функції `draw()`).

--- code ---
---
language: python
line_numbers: true
line_number_start: 25 
line_highlights: 27
---

def draw():
    # Що відбувається на кожному кадрі
    draw_background()

--- /code ---

--- /task ---

--- task ---

**Протестуй:** запусти код. Ти маєш побачити чорний квадрат.

--- /task ---



--- task ---

Додай рядок коду, який виводитиме зображення планети.

--- code ---
---
language: python
line_numbers: true
line_number_start: 13 
line_highlights: 15-16
---
def draw_background():  
    background(0,0,0)
    image(planet, screen_size/2, screen_size, 300, 300)

--- /code ---


Для функції `image()` потрібні такі дані:

- назва файлу зображення — ми вже завантажили зображення планети;
- координата x — ми вже встановили розмір екрана;
- координата y;
- ширина зображення;
- висота зображення.

--- /task ---

--- task ---

**Протестуй:** запусти свій код. Він має малювати чорне тло і пів планети внизу.

![Планета на чорному фоні.](images/step_2.png){:width="300px"}

--- /task ---

### Інша планета?

--- task ---

Натисни на значок зображення ліворуч, щоб переглянути галерею зображень.

![Вибрати іншу планету](images/image_gallery.png)

Якщо ти хочеш вибрати інше зображення планети, зміни `planet.png` у коді на назву файлу вибраної планети, наприклад, `orange_planet.png`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 17 
line_highlights: 22
---
def setup(): #
    Тут налаштуй анімацію
    size(screen_size, screen_size)
    image_mode(CENTER)
    global planet
    planet = load_image('planet.png')

--- /code ---

--- /task ---

