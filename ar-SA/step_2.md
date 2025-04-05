## Draw the background

--- task ---

افتح[ نموذج المشروع](https://trinket.io/python/bd7592097e){:target="_blank"}.

--- /task ---

First, you will create a black background to represent space.

--- task ---

حدد دالة `draw_background()` ، لرسم الخلفية ، أسفل التعليق الذي يخبرك إلى أين يجب أن تذهب.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# يتم وضع دالة draw_background هنا
def setup():   
#Setup your animation here   
size(screen_size, screen_size)

--- /code ---

--- /task ---

--- task ---

Add this function to the list of things to `draw()` in every frame.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 28
line_highlights: 20
---

def draw():   
#أشياء يجب القيام بها في كل إطار    
draw_background()

--- /code ---

--- /task ---

--- task ---

إذا كان لديك حساب Trinket ، فيمكنك النقر فوق الزر **Remix** لحفظ نسخة في مكتبة `My Trinkets`.

--- /task ---



--- task ---

Add a line of code to display an image of a planet.

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 21-23
---
def draw_background():  
background(0,0,0) image(planet, screen_size/2, screen_size, 300, 300)

--- /code ---


تم وضع الدالة `image()`:

- image filename - we have already loaded the planet image
- x coordinate - we have already set the screen size
- y coordinate
- image width
- image height

--- /task ---

--- task ---

**اختبار:** قوموا بتشغيل الشفرة البرمجية الخاصة بكم وتحققوا من أنه يرسم خلفية سوداء مع نصف كوكب في الأسفل.

![A planet against a black background.](images/step_2.png){:width="300px"}

--- /task ---

### A different planet?

--- task ---

Click on the image icon to the left to view the image gallery.

![Choose a different planet](images/image_gallery.png)

أضف أيضًا الشفرة البرمجية إلى الدالة `setup()` لتحميل الصورة التي اخترتها في متغير عام `planet`. يجب أن يكون المتغير عامًا حتى تتمكن من استخدامه لاحقًا عند رسم الكوكب على الشاشة.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 15-17
---
def setup(): # Set up your animation here size(screen_size, screen_size) image_mode(CENTER) global planet planet = load_image('planet.png')

--- /code ---

--- /task ---

