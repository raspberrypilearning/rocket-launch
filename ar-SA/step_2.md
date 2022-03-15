## جهز المشهد

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
تحتاج الرسوم المتحركة إلى خلفية فضائية مع كوكب لإطلاق الصاروخ منه.
</div>
<div>

![كوكب على خلفية سوداء.](images/step_2.png){:width="300px"}

</div>
</div>

--- task ---

افتح[ نموذج المشروع](https://trinket.io/python/bd7592097e){:target="_blank"}.

إذا كان لديك حساب Trinket ، فيمكنك النقر فوق الزر **Remix** لحفظ نسخة في مكتبة `My Trinkets`.

--- /task ---

سوف تستخدم متغير `screen_size` لتعيين حجم الشاشة وفي العمليات الحسابية. المتغيرات المعرفة دوالة خارجية هي **global** لذا يمكنك استخدامها في أي مكان في برنامجك.

--- task ---

ابحث عن التعليق `Setup global variables` وأضف سطرًا من الشفرة البرمجية لإنشاء متغير `screen_size`:

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 7
line_highlights: 8
---

#تهيئة المتغيرات العامة
screen_size = 400

--- /code ---

--- /task ---

--- task ---

استخدم المتغير `screen_size` لإنشاء مربع 400 × 400 بكسل:

--- code ---
---
language: python 
filename: main.py — setup() 
line_numbers: true 
line_number_start: 18
line_highlights: 20
---

def setup():   
  #Setup your animation here   
  size(screen_size, screen_size)


--- /code ---

--- /task ---

--- task ---

يحتوي مشروع البداية على ثلاث صور مختلفة للكوكب وقد تم توفير القمر لك. يمكنك عرض هذه في مكتبة صور Trinket عن طريق تحديد الزر **View and Add Images**.

![رمز زائد ورمز تحميل ورمز صورة. يتم تمييز رمز الصورة.](images/trinket_image.png)

**اختر:** حدد الصورة التي تريد استخدامها وقم بتدوين اسم الملف. على سبيل المثال ، `orange_planet.png`.

--- /task ---

إنها لفكرة جيدة أن تقوم بتحميل الصور في `setup()` بحيث تكون جاهزة عندما تحتاج إلى استخدامها وسيتم تشغيل الرسوم المتحركة الخاصة بك بسرعة.

--- task ---

يشير السطر `image_mode(CENTER)` إلى أنك ستضع الصور عن طريق إعطاء إحداثيات مركز الصورة (بدلاً من الزاوية اليسرى العلوية).

أضف أيضًا الشفرة البرمجية إلى الدالة `setup()` لتحميل الصورة التي اخترتها في متغير عام `planet`. يجب أن يكون المتغير عامًا حتى تتمكن من استخدامه لاحقًا عند رسم الكوكب على الشاشة.

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 18
line_highlights: 21-23
---

def setup():   
    #إعداد الرسوم المتحركة هنا 
    size(screen_size, screen_size)   
    image_mode(CENTER)   
    global planet   
    planet = load_image('planet.png') #الكوكب الذي اخترته


--- /code ---

--- /task ---

--- task ---

حدد دالة `draw_background()` ، لرسم الخلفية ، أسفل التعليق الذي يخبرك إلى أين يجب أن تذهب.

استخدم `background(0)` لتعيين لون الخلفية إلى الأسود وإضافة دالة `image()`لرسم الكوكب. تم وضع الدالة `image()`:

`image(ملف الصورة ,تنسيق x, تنسيق y, العرض ,الارتفاع)`

تحدد مكتبة `p5` المتغيرات العامة،`width` و`height` متغيرات عامة بناءً على حجم الشاشة. استخدموا الدوال التاليتان في الشفرة البرمجية الخاصة بك لوضع الكوكب في منتصف الشاشة(`width/2`) وفي الجزء السفلي من الشاشة (`height`).

--- code ---
---
language: python 
filename: main.py — draw_background() 
line_numbers: true 
line_number_start: 14
line_highlights: 15-17
---

#يتم وضع دالة draw_background هنا
def draw_background():   
    background(0) #مختصر الخلفية (0, 0, 0) — اسود    
    image(planet, width/2, height, 300, 300) #ارسم الصورة


--- /code ---

يؤدي وضع كل الشفرة البرمجية لرسم الخلفية في دالة واحدة إلى تسهيل فهم الشفرة البرمجية الخاص بك.

--- /task --- 

--- task ---

لإظهار الخلفية ،call `draw_background()` in `draw()`. سيؤدي هذا إلى إعادة رسم الخلفية في كل مرة يتم استدعاء `draw()` ، بحيث تغطي أي رسم قديم:

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 28
line_highlights: 30
---

def draw():   
    #أشياء يجب القيام بها في كل إطار    
    draw_background()

--- /code ---

--- /task ---

--- task ---

**اختبار:** قوموا بتشغيل الشفرة البرمجية الخاصة بكم وتحققوا من أنه يرسم خلفية سوداء مع نصف كوكب في الأسفل.

--- /task ---

--- save ---
