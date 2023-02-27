## दृश्य को स्थापित करें

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
एनीमेशन को एक अंतरिक्ष पृष्ठभूमि की आवश्यकता है जिसमें से रॉकेट लॉन्च करने के लिए एक ग्रह है।
</div>
<div>

![एक ग्रह जो एक काली पृष्ठभूमि के खिलाफ है।](images/step_2.png){:width="300px"}

</div>
</div>

--- task ---

[project टेम्प्लेट](https://trinket.io/python/f2199f5a8c){:target="_blank"} खोलें।

यदि आपके पास एक Trinket खाता है, तो आप अपने `My Trinkets` लाइब्रेरी में कॉपी सहेजने के लिए **Remix** बटन पर क्लिक कर सकते हैं।

--- /task ---

आप स्क्रीन का आकार और गणना में सेट करने के लिए `Screen_size` वेरिएबल का उपयोग करेंगे। बाहरी फंक्शन परिभाषित वेरिएबल **global** हैं ताकि आप अपने प्रोग्राम में कहीं भी उनका उपयोग कर सकें।

--- task ---

टिप्पणी `Setup global variables` ढूंढें और अपना `Screen_size` वेरिएबल बनाने के लिए कोड की एक पंक्ति जोड़ें:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# वैश्विक वेरिएबल सेटअप करें
screen_size = 400

--- /code ---

--- /task ---

--- task ---

एक वर्ग 400 गुणा 400 पिक्सेल बनाने के लिए `Screen_size` वेरिएबल का उपयोग करें:

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 20
---

def setup():   
#Setup your animation here   
size(screen_size, screen_size)


--- /code ---

--- /task ---

--- task ---

स्टार्टर प्रोजेक्ट में तीन अलग-अलग ग्रह चित्र और आपके लिए प्रदान किया गया चंद्रमा होता है। आप इन्हें **दृश्य और चित्र जोड़ें** बटन का चयन करके Trinket इमेज लाइब्रेरी में देख सकते हैं।

![एक धन प्रतीक, एक अपलोड प्रतीक, और एक छवि प्रतीक। छवि प्रतीक हाइलाइट किया गया है।](images/trinket_image.png)

**choose:** यह तय करें कि आप किस चित्र का उपयोग करना चाहते हैं और फ़ाइल नाम का एक नोट बनाएं। उदाहरण के लिए, `norge_planet.png`।

--- /task ---

`setup()` में चित्र लोड करना एक अच्छा विचार है ताकि जब आपको इनका उपयोग करने की आवश्यकता हो तो वे तैयार रहें और आपका एनीमेशन तेज़ी से चलेगा।

--- task ---

`image_mode(center)` पंक्ति कहती है कि आप चित्र के केंद्र (ऊपरी बाएँ कोने के बजाय) के निर्देशांक देकर चित्रों को स्थित करेंगे।

अपनी चुनी हुई छवि को `planet()` फंक्शन में `planet` वैश्विक वेरिएबल में लोड करने के लिए कोड भी जोड़ें। वेरिएबल को वैश्विक होने की आवश्यकता है ताकि आप इसे बाद में तब उपयोग कर सकें जब आप ग्रह को स्क्रीन पर खींचते हैं।

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 21-23
---

def setup():   
#Setup your animation here   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet   
planet = load_image('planet.png') #Your chosen planet


--- /code ---

--- /task ---

--- task ---

एक `draway_background()` फंक्शन परिभाषित करें, पृष्ठभूमि बनाने के लिए, उस टिप्पणी के नीचे जो आपको बताती है कि उसे कहां जाना चाहिए।

पृष्ठभूमि के रंग को काले रंग में सेट करने के लिए `background(0)` का उपयोग करें और ग्रह को खींचने के लिए `image()` फंक्शन जोड़ें। `image()` फ़ंक्शन रखा गया है:

`image(image filename, x-coordinate, y-coordinate, image_width, image_height)`

`p5` लाइब्रेरी वैश्विक `width` और `height` वेरिएबल्स को स्क्रीन के आकार के आधार पर सेट करती है। इन का उपयोग अपने कोड में करें ताकि ग्रह को उसके केंद्र के अर्ध-मार्ग से स्थिति में रखा जा सके (`width/2`) और स्क्रीन के निचले भाग (`height`) पर।

--- code ---
---
language: python filename: main.py — draw_background() line_numbers: true line_number_start: 14
line_highlights: 15-17
---

# draway_background फ़ंक्शन यहाँ जाता है
def draw_background():   
background(0) #Short for background(0, 0, 0) — black    
image(planet, width/2, height, 300, 300) #Draw the image


--- /code ---

पृष्ठभूमि को एक फ़ंक्शन में खींचने के लिए सभी कोड रखना आपके कोड को समझना आसान बनाता है।

--- /task ---

--- task ---

पृष्ठभूमि को प्रकट करने के लिए, `drawage_background()` को `drawing()` में कॉल करें। इसके कारण पृष्ठभूमि हर बार `draway()` को फिर से बनाया जाएगा, जो किसी भी पुराने ड्राइंग पर कवर करती है:

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 28
line_highlights: 30
---

def draw():   
#Things to do in every frame    
draw_background()

--- /code ---

--- /task ---

--- task ---

**परीक्षण:** अपना कोड चलाएं और जांचें कि यह नीचे आधे ग्रह के साथ एक काली पृष्ठभूमि बनाता है।

--- /task ---

--- save ---
