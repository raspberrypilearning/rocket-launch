## آثار العادم

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

سيبدو الصاروخ أكثر واقعية مع بعض المؤثرات الخاصة لمحاكاة مسار العادم. 

يمكنك إنشاء تأثيرات رائعة باستخدام حلقة `for` لرسم الكثير من الأشكال في كل إطار.

</div>
<div>

![سقوط الصاروخ مع مسار عادم.](images/flying_rocket.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
تستخدم الشفرة البرمجية لعمل <span style="color: #0faeb0">**تأثيرات رسومية**</span> للأفلام والألعاب. إن كتابة الشفرة البرمجية أسرع بكثير من رسم كل إطار من الرسوم المتحركة على حدة. </p>

يؤدي رسم الكثير من الأشكال البيضاوية الصفراء في مواضع مختلفة من `y` إلى إنشاء مسار العادم.

--- task ---

تكرر الحلقة `for` جزءًا من الشفرة البرمجية مرة واحدة لكل عنصر يتم تقديمه. لتشغيل الشفرة البرمجية في حلقة `for` لعدد معين من المرات ، يمكنك استخدام الدالة `range()`. على سبيل المثال ، يُنشئ النطاق `(5)range` سلسلة من خمسة أرقام تبدأ من 0 ، [0, 1, 2, 3, 4].

في كل مرة تتكرر فيها الحلقة `for` ، فإنها تحدد متغيرًا للعنصر الحالي بحيث يمكنك استخدامه في الحلقة.

قم بتحديث الدالة `draw_rocket()` لتشمل حلقة `for` التي تكرر رسم `25` علامات للعادم. تتم إضافة متغير الحلقة **متغير الحلقة** `i` إلى `rocket_y`لرسم التاثيرات الحركية للعادم اسفل الصاروخ.

--- code ---
---
language: python 
filename: main.py - draw_rocket() 
line_numbers: true 
line_number_start: 12
line_highlights: 16-22
---

def draw_rocket():

  global rocket_y   
  rocket_y -= 1

  no_stroke() #أوقف السكتة الدماغية

  for i in range(25): #ارسم 25 شكلًا بيضاويًا محترقًا في العادم   
    fill(255, 255, 0) #أصفر   
    ellipse(width/2, rocket_y + i, 8, 3) #يزيد في كل مرة تتكرر فيها الحلقة

  image(rocket, width/2, rocket_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

**الاختبار:** لنقم بتشغيل الشفرة البرمجية للتحقق من أن الصاروخ يحتوي على مسار عادم جديد.

![لقطة مقرّبة للصاروخ مع أثر عادم.](images/rocket_exhaust.png){:width="300px"}

--- /task ---

يمكن أيضًا استخدام المتغير `i` لإنشاء تدرج لوني أقل من اللون الأخضر في كل شكل بيضاوي يتم رسمه.

--- task ---

قم بتغيير الاستدعاء إلى `fill()` لتعيين مقدار اللون الأخضر إلى `255 - i*10` بحيث يكون للشكل البيضوي الأول كميات متساوية من الأحمر والأخضر ويكون آخر شكل أخضر قليلًا جدًا.

--- code ---
---
language: python 
filename: main.py - draw_rocket() 
line_numbers: true 
line_number_start: 19
line_highlights: 20
---

  for i in range(25):   
    fill(255, 255 - i * 10, 0) #تقليل مقدار القطع الناقص الأخضر    
    ellipse(width/2, rocket_y + i, 8, 3)

--- /code ---

--- /task ---

--- task ---

**اختبار:** تأكد من حصولك على أثر من الأشكال البيضاوية يتغير تدريجيًا من الأصفر إلى الأحمر.

--- /task ---

يتم إنشاء مسار عادم الدخان عن طريق رسم الكثير من الأشكال البيضاوية الرمادية الشفافة قليلاً في مواضع مختلفة في كل إطار.

![رسم متحرك بطيء لتأثير الدخان.](images/rocket_smoke.gif)

--- task ---

هذه المرة ، تكون التعبئة`fill()` خارج الحلقة حيث أن اللون هو نفسه لكل شكل بيضاوي من الدخان. الإدخال الرابع لـ `fill()` هو العتامة ، قيمة عتامة منخفضة تجعل اللون أكثر شفافية حتى تتمكن من رؤية الأشكال الموجودة تحته.

في كل إطار من إطارات الرسوم المتحركة ، سيتم رسم 20 علامة بيضاوية بأحجام عشوائية في مواضع عشوائية.

--- code ---
---
language: python 
filename: main.py - draw_rocket() 
line_numbers: true 
line_number_start: 19
line_highlights: 23-26
---

  for i in range(25):  
    fill(255, 255 - i * 10, 0)   
    ellipse(width/2, rocket_y + i, 8, 3)

  fill(200, 200, 200, 100) #Transparent grey   
  for i in range(20): #Draw 20 random smoke ellipses    
    ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

  image(rocket, width/2, rocket_y, 64, 64)

--- /code ---

--- /task ---

--- task ---

**اختبار:** لنقم بتشغيل البرنامج ونتحقق من أن أبخرة العادم مرئية.

![لقطة مقرّبة للصاروخ ومسار العادم مع إضافة دخان.](images/rocket_exhaust_circles.gif)

--- /task ---

--- save ---
