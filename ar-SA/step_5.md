## حرق الوقود

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

من أهم الأشياء التي يجب أن تقررها عند إطلاق صاروخ هو مقدار الوقود الذي يجب تحميله فيه. 

للقيام بذلك ، تحتاج إلى محاكاة كمية الوقود التي سيتم حرقها في الرحلة.
</div>

! [البرنامج الذي يحتوي على سؤال في منطقة الإخراج يسأل عن كمية الوقود المطلوبة.] (images / burn_question_full.png) {: width = "300px"}

</div>

### Create a fuel variable

--- task ---

أضف متغيرًا لتتبع مقدار الوقود الذي يحرقه صاروخك (في الإطارات).

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 10
---

# تهيئة المتغيرات العامة
screen_size = 400   
rock_y = screen_size  
burn = 100 # كمية الوقود المحروقة في كل إطار

--- /code ---

--- /task ---


--- task ---

في الجزء السفلي من البرنامج ، أضف شفرة برمجية لسؤال المستخدم عن مقدار الوقود الذي يجب إضافته إلى الصاروخ وتخزين إجابته في متغير عالمي `وقود`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 52
line_highlights: 52
---

fuel = int(input (المدخلات ('كم كيلوغرامًا من الوقود تريد استخدامه؟')   
run()

--- /code ---

--- /task ---

### Check fuel against burn

يجب ألا يتحرك الصاروخ إلا إذا لم يحرق كل وقوده.

--- task ---

أضف الشفرة البرمجية إلى الدالة `draw_rocket ()` لتقليل المتبقي `fuel` بواسطة `burn` لكل إطار. استخدم `print ()` لإظهار مقدار الوقود المتبقي في كل إطار.

عليك أن تقول أنك تريد استخدام الوقود العالمي `fuel ` و `burn` متغيرات.

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 15, 17-18
---

    global rocket_y, fuel, burn<br x-id="3" />
      rocket_y -= 1<br x-id="3" />
      fuel -= burn #حرق الوقود<br x-id="3" />
      print('Fuel left: ', fuel)

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل البرنامج الخاص بك للتأكد من أن الرسوم المتحركة لا تبدأ حتى يتم الرد على السؤال `How many kilograms of fuel do you want to use?`. حاول إدخال `30000` كمقدار للوقود.

سيستمر الصاروخ في التحرك حتى لو لم يتبق له وقود.

![البرنامج الذي يحتوي على سؤال في منطقة الإخراج يسأل عن مقدار الوقود المطلوب.](images/burn_question.png)

--- /task ---

--- task ---

يجب أن يتحرك الصاروخ فقط في حالة وجود وقود كافٍ. أضف عبارة `if` للتحقق من أن `fuel >= burn`.

ستحتاج إلى مسافة بادئة لجميع أسطر الكود قبل استدعاء الدالة `image()`. للقيام بذلك ، قم بتمييز جميع الخطوط بالماوس ثم انقر فوق الزر <kbd>Tab</kbd> الموجود على لوحة المفاتيح لوضع مسافة بادئة لجميع الأسطر مرة واحدة.

لا يلزم وضع مسافة بادئة للسطر `image()` لأنك تريد دائمًا رسم الصاروخ.

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 16-31
---

    no_stroke() #اطفاء stroke   
    
    for i in range(25):   
      fill(255, 255 - i*10, 0)   
      ellipse(width/2, rocket_y + i, 8, 3)    
    
    fill(200, 200, 200, 100)   
    for i in range(20):   
      ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل البرنامج الخاص بك للتحقق من أن الصاروخ يتوقف عند عدم تبقي وقود.

![صورة صاروخ في منتصف الشاشة عليها عبارة "وقود متبقي: 0".](images/burn_empty.png){:width="300px"}

--- /task ---

Did your rocket stop when it ran out of fuel? Well done, you sent a rocket to outer space!

--- save ---

