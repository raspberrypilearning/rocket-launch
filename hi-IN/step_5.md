## ईंधन बर्न करें

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

रॉकेट को कब लॉन्च करना है, यह तय करने के लिए सबसे महत्वपूर्ण चीजों में से एक यह है कि इसमें कितना ईंधन लोड करना है। 

ऐसा करने के लिए, आपको यह अनुरूपण करने की आवश्यकता है कि यात्रा में कितना ईंधन जलाया जाएगा।
</div>

![आउटपुट क्षेत्र में एक प्रश्न के साथ प्रोग्राम यह पूछ रहा है कि कितना ईंधन चाहिए।](images/code_question_full.png){:width="300px"}

</div>

--- task ---

आपके रॉकेट में कितना ईंधन बर्न होता है इसका ट्रैक रखने के लिए एक वेरिएबल जोड़ें (फ्रेम में)।

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 10
---

# वैश्विक वेरिएबल सेटअप करें
screen_size = 400   
rocket_y = screen_size  
burn = 100 #How much fuel is burned in each frame

--- /code ---

--- /task ---


--- task ---

अपने प्रोग्राम के निचले भाग में, उपयोगकर्ता से यह पूछने के लिए कोड जोड़ें कि रॉकेट में कितना ईंधन जोड़ना है और अपने उत्तर को `fuel` वैश्विक वेरिएबल में संग्रहीत करें।

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 52
line_highlights: 52
---

fuel = int(input('How many kilograms of fuel do you want to use?'))   
run()

--- /code ---

--- /task ---

रॉकेट को तभी चलना चाहिए जब उसने अपने सभी ईंधन को नहीं जलाया हो।

--- task ---

प्रत्येक फ्रेम के `burn` द्वारा शेष `fuel` को कम करने के लिए `drawing_rotरॉकेट()` फंक्शन में कोड जोड़ें। प्रत्येक फ्रेम में कितना ईंधन बचा है यह दिखाने के लिए `print()` का उपयोग करें।

आपको यह कहना होगा कि आप वैश्विक `fuel` और `breast` वेरिएबल्स का उपयोग करना चाहते हैं।

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 15, 17-18
---

  global rocket_y, fuel, burn   
rocket_y -= 1   
fuel -= burn #Burn fuel   
print('Fuel left: ', fuel)

--- /code ---

--- /task ---

--- task ---

**परीक्षण:** यह जांचने के लिए अपना प्रोग्राम चलाएँ कि एनीमेशन तब तक शुरू नहीं होता जब तक `आप कितने किलोग्राम ईंधन का उपयोग करना चाहते हैं?` का उत्तर नहीं दिया गया है। ईंधन की मात्रा के रूप में `30000` दर्ज करने का प्रयास करें।

रॉकेट तब भी चलता रहेगा जब उसके पास कोई ईंधन नहीं बचा हो।

![आउटपुट क्षेत्र में एक प्रश्न के साथ प्रोग्राम यह पूछता है कि कितना ईंधन चाहिए।](images/burn_question.png)

--- /task ---

--- task ---

रॉकेट को तभी चलना चाहिए जब उसके पास पर्याप्त ईंधन बचा हो। `fuel>= बर्न` जांचने के लिए एक `if` स्टेटमेंट जोड़ें।

आपको `image()` फ़ंक्शन कॉल से पहले कोड की सभी पंक्तियों को इंडेंट करने की आवश्यकता होगी। ऐसा करने के लिए, माउस के साथ सभी पंक्तियों को हाइलाइट करें और फिर सभी पंक्तियों को एक बार में इंडेंट करने के लिए कीबोर्ड पर <kbd>tab</kbd> पर टैप करें।

`image()` पंक्ति को इंडेंट करने की आवश्यकता नहीं है क्योंकि आप हमेशा रॉकेट बनाना चाहते हैं।

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 16-31
---

  global rocket_y, fuel, burn

  if fuel >= burn: #Still got fuel   
rocket_y -= 1   
fuel -= burn   
print('Fuel left: ', fuel)   

    no_stroke() #Turn off the stroke   
    
    for i in range(25):   
      fill(255, 255 - i*10, 0)   
      ellipse(width/2, rocket_y + i, 8, 3)    
    
    fill(200, 200, 200, 100)   
    for i in range(20):   
      ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

  image(rocket, width/2, rocket_y, 64, 64)

--- /code ---

--- /task ---

--- task ---

**परीक्षण:** यह जांचने के लिए अपना प्रोग्राम चलाएं कि जब कोई ईंधन नहीं बचा तो रॉकेट रुक जाए।

!['Fuel left: 0' कथन के साथ स्क्रीन के बीच में एक रॉकेट की छवि।](images/burn_empty.png){:width="300px"}

--- /task ---

यह कंप्यूटर सिमुलेशन बहुत सटीक नहीं है, लेकिन यह हमारे एनीमेशन के लिए पर्याप्त है।

--- save ---

