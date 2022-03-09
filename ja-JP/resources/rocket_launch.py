#!/bin/python3

# ライブラリコードをインポートする
from p5 import *
from random import randint

# グローバル変数を設定する
screen_size = 400
rocket_y = screen_size # 一番下から開始
burn = 100 # 各フレームで燃焼する燃料の量
orbit_radius = 250
orbit_y = screen_size - orbit_radius

# draw_rocket関数はここにあります
def draw_rocket():

  global rocket_y, fuel, burn
  
  if fuel >= burn and rocket_y > orbit_y: # まだ飛行中
    rocket_y -= 1 # ロケットを動かす
    fuel -= burn # 燃料を燃焼させる
    print('残りの燃料: ', fuel)
  
    no_stroke() # 境界線をなしにする
  
    for i in range(25): # 排気ガスを25個描く
      fill(255, 255 - i*10, 0) # 黄色
      ellipse(width/2, rocket_y + i, 8, 3) # ループが繰り返されるたびに i が増加する
    
    fill(200, 200, 200, 100) # 透明な灰色
    for i in range(20): # ランダムな排煙を20個描く
      ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))
  
  if fuel < burn and rocket_y > orbit_y: # 燃料がなくなり、軌道に乗っていない
    tint(255, 0, 0) # 失敗
  elif fuel < 1000 and rocket_y <= orbit_y:
    tint(0, 255, 0) # 成功
  elif fuel >= 1000 and rocket_y <= orbit_y: 
    tint(255, 200, 0) # 燃料が多すぎる
  
  image(rocket, width/2, rocket_y, 64, 64)
  no_tint()
  

# draw_background関数はここにあります
def draw_background():
  background(0) # background(0, 0, 0) の省略形 - 黒 
  image(planet, width/2, height, 300, 300) # 描画する
  
  no_fill() # 塗りつぶしをなしにする
  stroke(255) # 境界線を白にする
  stroke_weight(2)
  ellipse(width/2, height, orbit_radius*2, orbit_radius*2)
  

def setup():
  # ここでアニメーションをセットアップします
  size(screen_size, screen_size)
  image_mode(CENTER)
  global planet, rocket
  planet = load_image('planet.png') # 選択した惑星
  rocket = load_image('rocket.png')


def draw():
  # フレームごとに行うこと
  draw_background()  
  draw_rocket()
  

fuel = int(input('燃料を何キログラム使いますか?'))
run()
