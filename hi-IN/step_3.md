## liftcof!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
हर बार जब एक नया फ्रेम बनाया जाता है, तो एनीमेशन प्रभाव बनाने के लिए रॉकेट को स्क्रीन पर ऊपर जाने की आवश्यकता होती है।
</div>
<div>

![स्क्रीन के नीचे से ऊपर तक एक स्थिर गति से उड़ते हुए एक रॉकेट।](images/flight.gif){:width="300px"}

</div>
</div>

--- task ---

स्टार्टर प्रोजेक्ट में आपके लिए प्रदान की गई एक रॉकेट चित्र है।

![Trinket इमेज लाइब्रेरी में रॉकेट की छवि।](images/trinket_rocket_image.png)

--- /task ---

--- task ---

रॉकेट की छवि को `रॉकेट` वैश्विक वेरिएबल में लोड करने के लिए `setup()` फंक्शन में कोड जोड़ें।

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 24, 26
---

def setup():   
#Setup your animation here   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet, rocket   
planet = load_image('planet.png')    
rocket = load_image('rocket.png')

--- /code ---

--- /task ---

रॉकेट की `y` स्थिति 400 (स्क्रीन की ऊंचाई) से शुरू होगी और फिर हर बार एक नया फ्रेम बनाए जाने पर 1 तक कम हो जाएगी।

--- task ---

रॉकेट के `y` स्थिति का ट्रैक रखने के लिए एक `roct_y` वैश्विक वेरिएबल जोड़ें।

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9
---

# वैश्विक वेरिएबल सेटअप करें
screen_size = 400    
rocket_y = screen_size #Start at the bottom

--- /code ---

--- /task ---

--- task ---

रॉकेट की `y` स्थिति को बदलने और इसे फिर से बनाने के लिए `drag_rock()` फंक्शन परिभाषित करें।

`rock_y -= 1` यह कहने का छोटा तरीका है `rocast_y = roct_y - 1`।

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12-16
---

# draway_crock फ़ंक्शन यहाँ जाता है
def draw_rocket():

  global rocket_y #Use the global rocket_y variable    
rocket_y -= 1 #Move the rocket    
image(rocket, width/2, rocket_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

`draway()` फ़ंक्शन में अपने नए `drawing_rotरॉकेट()` को कॉल करें ताकि रॉकेट हर फ्रेम में फिर से बनाया जा सके।

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 34
line_highlights: 37
---

def draw():   
#Things to do in every frame   
draw_background()   
draw_rocket()


--- /code ---

--- /task ---

--- task ---

**परीक्षण:** यह जांचने के लिए अपना कोड चलाएं कि रॉकेट स्क्रीन के नीचे से शुरू होता है और प्रत्येक फ्रेम को ऊपर ले जाता है।

![रॉकेट की छवि स्क्रीन के आधे रास्ते में।](images/trinket_rocket_fly.gif)

--- /task ---

--- save ---
