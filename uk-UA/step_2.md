## Створення фону

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Для анімації потрібен космічний фон з зображенням планети, з якої стартує ракета.
</div>
<div>

![Планета на чорному фоні.](images/step_2.png){:width="300px"}

</div>
</div>

--- task ---

Відкрий [шаблон проєкту](https://trinket.io/python/77c37dd931){:target="_blank"}.

Якщо у тебе є обліковий запис в Trinket, ти можеш натиснути на кнопку **Remix**, щоб зберегти копію у свою бібліотеку `My Trinkets`.

--- /task ---

Ти будеш використовувати змінну `screen_size`, щоб встановити розмір екрана та провести розрахунки. Змінні, які визначаються за межами функцій, є **глобальними**, завдяки чому ти можеш використовувати їх будь-де у своїй програмі.

--- task ---

Знайди коментар `Налаштування глобальних змінних` та додай рядок коду для створення змінної `screen_size`:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7 
line_highlights: 8
---

#Налаштування глобальних змінних    
screen_size = 400   

--- /code ---

--- /task ---

--- task ---

Використовуй змінну `screen_size`, щоб створити квадрат розміром 400 на 400 пікселів:

--- code ---
---
language: python
filename: main.py — setup()
line_numbers: true
line_number_start: 18
line_highlights: 20
---

def setup():   
  #Налаштувати анімацію можна тут   
  size(screen_size, screen_size) 


--- /code ---

--- /task ---

--- task ---

Стартовий проєкт пропонує три різні зображення планет та Місяця. Ти можеш переглянути їх у бібліотеці зображень Trinket, натиснувши кнопку **View and Add Images**.

![Символ "плюс", символ "завантажити" та символ "зображення". Символ "зображення" підсвічується.](images/trinket_image.png)

**Обирай:** Виріши, яке зображення хочеш використати, та запиши ім'я файлу. Наприклад, `orange_planet.png`.

--- /task ---

Зображення зручно завантажувати в `setup()`, щоб вони завжди були напоготові, коли тобі потрібно буде їх використати, а твоя анімація буде швидко запускатись.

--- task ---

Рядок `image_mode(CENTER)` вказує на те, що ти будеш розміщувати зображення, вказавши координати центру зображення (замість лівого верхнього кута).

Також, додай код до функції `setup()`, щоб завантажити вибране зображення в глобальну змінну `planet`. Змінна повинна бути глобальною, щоб її можна було використати пізніше, коли ти будеш малювати планету на екрані.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18 
line_highlights: 21-23
---

def setup():   
  #Налаштувати анімацію можна тут   
  size(screen_size, screen_size)   
  image_mode(CENTER)   
  global planet   
  planet = load_image('planet.png') #Твоя обрана планета


--- /code ---

--- /task ---

--- task ---

Визнач функцію `draw_background()`, щоб намалювати фон, внизу коментаря, який підказує, куди його треба поставити.

Використовуй `background(0)`, щоб встановити колір фону на чорний, та додати функцію `image()`, яка намалює планету. Функція `image()` викладена:

`image(image filename, x-coordinate, y-coordinate, image_width, image_height)`

Бібліотека `p5` встановлює глобальні змінні `width` та `height`, залежно від розміру екрана. Використовуй їх у своєму коді, щоб розташувати планету посередині (`width/2`) та внизу екрану (`height`).

--- code ---
---
language: python
filename: main.py — draw_background()
line_numbers: true
line_number_start: 14 
line_highlights: 15-17
---

#Функція draw_background викликається тут   
def draw_background():   
  background(0) #Скорочено від background(0, 0, 0) - чорний    
  image(planet, width/2, height, 300, 300) #Малювання зображення
  

--- /code ---

Якщо весь код для малювання фону помістити в одну функцію, тоді твій код буде легше зрозуміти.

--- /task --- 

--- task ---

Для того, щоб фон з'явився, потрібно викликати `draw_background()` у `draw()`. Таким чином, щоразу, коли буде викликано `draw()`, фон буде перемальовуватися, перекриваючи будь-які попередні малюнки:

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 28 
line_highlights: 30
---

def draw():   
  #Що відбувається на кожному кадрі    
  draw_background()

--- /code ---

--- /task ---

--- task ---

**Тест:** Запусти свій код та переконайся, що він малює чорний фон та пів планети внизу.

--- /task ---

--- save ---
