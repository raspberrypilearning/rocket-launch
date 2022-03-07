#!/bin/python3

# استيراد مكتبة الشفرات البرمجية
from p5 import *
from random import randint

# تهيئة المتغيرات العامة
screen_size = 400
rocket_y = screen_size # تبدأ من الأسفل
burn = 100 # كمية الوقود المحروقة في كل إطار
orbit_radius = 250
orbit_y = screen_size - orbit_radius

# يتم وضع دالة draw_rocket هنا
def draw_rocket():

  global rocket_y, fuel, burn
  
  if fuel >= burn and rocket_y > orbit_y: # لا يزال يطير
    rocket_y - = 1 # حرك الصاروخ
    fuel -= burn # حرق الوقود
    print('Fuel left: ', fuel)
  
    no_stroke() # Turn off the stroke
  
    for i in range(25): # draw 25 burning exhaust ellipses
      fill(255, 255 - i*10, 0) # yellow
      ellipse(width/2, rocket_y + i, 8, 3) # i increases each time the loop repeats
    
    fill(200, 200, 200, 100) # transparent grey
    for i in range(20): # draw 20 random smoke ellipses
      ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))
  
  if fuel < burn and rocket_y > orbit_y: # لا مزيد من الوقود ولست على المدار
    tint(255, 0, 0) # فشل
  elif fuel < 1000 and rocket_y <= orbit_y:
    tint(0, 255, 0) # نجاح
  elif fuel >= 1000 and rocket_y <= orbit_y: 
    tint(255, 200, 0) # وقود كثير
  
  image(rocket, width/2, rocket_y, 64, 64)
  no_tint()
  

# يتم وضع دالة draw_background هنا
def draw_background():
  background(0) # اختصار للخلفية (0, 0, 0) - اسود 
  image(planet, width/2, height, 300, 300) # ارسم الصورة
  
  no_fill() # اطفاء أي fill
  stroke(255) # تعيين خط ابيض
  stroke_weight(2)
  ellipse(width/2, height, orbit_radius*2, orbit_radius*2)
  

def setup():
  # قم بإعداد الرسوم المتحركة الخاصة بك هنا
  size(screen_size, screen_size)
  image_mode(CENTER)
  global planet, rocket
  planet = load_image('planet.png') # الكوكب الذي تختاره
  rocket = load_image('rocket.png')


def draw():
  # أشياء للقيام بها في كل إطار
  draw_background()  
  draw_rocket()
  

fuel = int(input('How many kilograms of fuel do you want to use?'))
run()
