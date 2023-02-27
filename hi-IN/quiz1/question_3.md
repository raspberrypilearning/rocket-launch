--- question ---
---
किंवदंती: ३ का प्रश्न ३
---

यह कोड खिलाड़ी को यह दिखाने के लिए कि वे कैसे कर रहे हैं, एक गेम में रॉकेट को रंग देने के लिए `tint()` का उपयोग करता है।

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

यदि `points` वेरिएबल का मान `99` है और `lives` वेरिएबल का मान `1` है, तो रॉकेट कैसा दिखेगा?

--- choices ---

- (एक्स)

![एम्बर टिंट के साथ रॉकेट चित्र।](images/rocket_amber.png) <div style="text-align: center;">पीला

 --- feedback ---

 सही! खिलाड़ी के पास 100 से कम अंक हैं और केवल 1 जीवन शेष है। The rocket is coloured amber to let them know that this is their last chance to win!

 --- /feedback ---

- ( )

![बिना टिंट के एक रॉकेट चित्र](images/rocket_original.png) <div style="text-align: center;">tint नहीं

 --- feedback ---

 बिल्कुल नहीं, रॉकेट का टिंट है क्योंकि एक कथन सत्य है।

 --- /feedback ---

- ( )

![हरा टिंट के साथ एक रॉकेट चित्र](images/rocket_green.png) <div style="text-align: center;">हरा

 --- feedback ---

 बिल्कुल नहीं, खिलाड़ी को अपने रॉकेट को हरा कर जीतने के लिए `>= 100` बिंदुओं की आवश्यकता होगी। उनके पास `99` है, जो पर्याप्त नहीं है। शर्तों को ध्यान से जांचें।

 --- /feedback ---

- ( )

![लाल टिंट के साथ एक रॉकेट चित्र](images/rocket_red.png) <div style="text-align: center;">लाल

 --- feedback ---

 बिल्कुल नहीं, खिलाड़ी के पास `< 100` बिंदु हैं लेकिन जीवन `0` के बराबर नहीं है। शर्तों को ध्यान से जांचें।

 --- /feedback ---

--- /choices ---

--- /question ---
