--- question ---
---
السؤال 3 من 3
---

تستخدم هذه الشفرة البرمجية `tint ()` لتلوين صاروخ في لعبة لإظهار اللاعب كيف يفعل.

--- code ---
---
language: python
---

if points >= 100:    
tint(0, 255, 0) #Green   
elif points < 100 and lives == 1:   
tint(255, 200, 0) #Amber    
elif points < 100 and lives == 0:     
tint(255, 0, 0) #Red     
else:      
no_tint()

image(rocket, width/2, height/2, 64, 64)

--- /code ---

إذا كان المتغير `points` له القيمة `99` والمتغير `lives` له القيمة `1`، فكيف سيبدو الصاروخ؟

--- choices ---

- (x)

![صورة صاروخية بلون كهرماني خفيف.](images/rocket_amber.png) <div style="text-align: center;">العنبر

 --- feedback ---

 صحيح! اللاعب لديه أقل من 100 نقطة وحياة واحدة فقط متبقية. The rocket is coloured amber to let them know that this is their last chance to win!

 --- /feedback ---

- ( )

![صورة صاروخية بدون لون خفيف](images/rocket_original.png) <div style="text-align: center;">بدون لون خفيف

 --- feedback ---

 ليس تمامًا ، الصاروخ له لون خفيف لأن أحد العبارات صحيح.

 --- /feedback ---

- ( )

![صورة صاروخية بلون أخضر](images/rocket_green.png) <div style="text-align: center;">أخضر

 --- feedback ---

 ليس تمامًا ، سيحتاج اللاعب إلى `>= 100` نقطة للفوز وتحويل صاروخه إلى اللون الأخضر. لديهم `99`، وهذا لا يكفي. تحقق من الشروط بعناية.

 --- /feedback ---

- ( )

![صورة صاروخية بلون أحمر](images/rocket_red.png) <div style="text-align: center;">أحمر

 --- feedback ---

 ليس تمامًا ، يمتلك اللاعب `< 100` لكن الأرواح لا تساوي `0`. تحقق من الشروط بعناية.

 --- /feedback ---

--- /choices ---

--- /question ---
