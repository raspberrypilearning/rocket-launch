## 軌道に到達

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

ロケットを打ち上げるポイントは、衛星を軌道に乗せることです。 

軌道とは、重力によって1つの物体が別の物体の周りをまわる曲線状の通り道です。

ロケットの色を変えて、打ち上げがどれほど成功したかを示します。 

</div>
<div>

![発射に成功(緑の色合い), 燃料過剰(アンバーの色合い)、失敗(赤の色合い)を示す3つの画像が並べられたもの](images/check_orbit.png){:width="400px"}

</div>
</div>

--- task ---

2つの新しいグローバル変数を作成して、軌道円の半径と、衛星を発射するためにロケットの中心が到達する必要のあるポイントまでの軌道の `y` 座標を設定します。

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 7
line_highlights: 11-12
---

#グローバル変数を設定する
screen_size = 400   
rocket_y = screen_size   
burn = 100   
orbit_radius = 250   
orbit_y = screen_size - orbit_radius

--- /code ---

--- /task ---

--- task ---

`draw_background()` 関数を更新して、ロケットが到達する必要のある衛星軌道を表す楕円を描画するようにします。

--- code ---
---
language: python 
filename: main.py - draw_background() 
line_numbers: true 
line_number_start: 37
line_highlights: 42-45
---

def draw_background():   
  background(0) #background(0, 0, 0) の省略形 - 黒   
  image(planet, width/2, height, 300, 300)

  no_fill() #塗りつぶしなし  
  stroke(255) #白の境界線を設定   
  stroke_weight(2)   
  ellipse(width/2, height, orbit_radius * 2, orbit_radius * 2)

--- /code ---

--- /task ---

--- task ---

**テスト：** プログラムを実行し、白い軌道線が引かれていることを確認します。

![惑星と新しい軌道線のある画面。](images/draw_orbit.png){:width="300px"}

--- /task ---

ロケットは衛星軌道に到達したとき - ミッションの終わり - に停止する必要があります。

--- task ---

`if fuel >= burn` のコードを更新して、ロケットが軌道に到達していないかも確認します。

`if` ステートメントで`and`を使用して、2つ以上の条件が真であるかどうかを確認できます。

--- code ---
---
language: python 
filename: main.py - draw_rocket() 
line_numbers: true 
line_number_start: 14
line_highlights: 19
---

#draw_rocket関数はここにあります
def draw_rocket():

  global rocket_y, fuel, burn

    if fuel >= burn and rocket_y > orbit_y: #まだ飛行中

--- /code ---

--- /task ---

--- task ---

**テスト：** プロジェクトを実行し、燃料の量として `50000` を入力します。 これは軌道に到達するのに十分な燃料です。 ロケットは軌道に到達すると動きを停止するはずです。

--- /task ---

ロケットが衛星を打ち上げるのに十分な高さになる前に燃料がなくなった場合、ロケットは赤色になります。

--- task ---

--- code ---
---
language: python 
filename: main.py — draw_rocket() 
line_numbers: true 
line_number_start: 30
line_highlights: 34-35
---

    fill(200, 200, 200, 100)   
    for i in range(20):   
      ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

  if fuel < burn and rocket_y > orbit_y: #燃料がなくなり、軌道上にもない 
    tint(255, 0, 0) #失敗

--- /code ---

--- /task ---

--- task ---

**テスト：** コードを実行し、燃料の量として `20000` を入力します。 ロケットが軌道の下で止って赤くなることを確認してください。

![軌道円の前で燃料がなくなった赤いロケット。 惑星も赤くなっています。](images/orbit_failure.png){:width="300px"}

おや、惑星も赤くなりました！

--- /task ---

--- task ---

`tint()` 関数は、色合いを変更するか、 `no_tint()` を使用して色合いをオフにするまで、描画されるすべての画像の色合いの色を変えます。

**選択：** 次のフレームで惑星が赤く染まらないように、画像を描画した後に `no_tint()` の呼び出しを追加します。または、惑星が赤くなるのが好きな場合はそのままにしておきます。

--- code ---
---
language: python 
filename: main.py - draw_rocket() 
line_numbers: true 
line_number_start: 34
line_highlights: 38
---

if fuel < burn and rocket_y > orbit_y: 
  tint(255, 0, 0) #失敗

image(rocket, width/2, rocket_y, 64, 64)   
no_tint() #次のフレームで惑星が赤い色合いにならないように!


--- /code ---

--- /task ---

--- task ---

`tint()` 関数をもう一度使用します。今回は、ロケットに衛星軌道に到達するのに十分な燃料がある場合に、ロケットを緑色に着色します。

--- code ---
---
language: python 
filename: main.py - draw_rocket() 
line_numbers: true 
line_number_start: 34
line_highlights: 36-37
---

if fuel < burn and rocket_y > orbit_y: 
  tint(255, 0, 0) #失敗   
elif rocket_y <= orbit_y:   
  tint(0, 255, 0) #成功

image(rocket, width/2, rocket_y, 64, 64)   
no_tint()

--- /code ---

--- /task ---

--- task ---

**テスト：** プロジェクトを実行し、燃料の量として `50000` を入力します。 ロケットが衛星軌道に到達したときに緑色に変わることを確認します。

![軌道円に到達し、燃料が残っている緑色のロケット。](images/orbit_success.png){:width="300px"}

--- /task ---

これで、衛星軌道に到達するために最低限必要な燃料の量を示すために使用できるシミュレーションができました。 それは素晴らしいことです; ただし、大量の燃料を使用しても成功する可能性がありますが、これにはコストと無駄が伴います。

--- task ---

成功の条件を修正して、ロケットが軌道に到達し、 `and(なおかつ)` 燃料の残りが1,000kg未満の場合にのみ緑色に変わるようにします。

ロケットが軌道に到達したときに1,000kgを超える燃料が残っている場合は、ロケットを黄色に着色するコードを追加します。

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 34
line_highlights: 36, 38-39
---

if fuel < burn and rocket_y > orbit_y: 
  tint(255, 0, 0) #失敗   
elif fuel < 1000 and rocket_y <= orbit_y:   
  tint(0, 255, 0) #成功   
elif fuel >= 1000 and rocket_y <= orbit_y:    
  tint(255, 200, 0) #燃料が多すぎる

image(rocket, width/2, rocket_y, 64, 64)    
no_tint() #次のフレームで惑星が色付けされないように!

--- /code ---

--- /task ---

--- task ---

**テスト：** 異なる数値でプログラムを数回実行します。たとえば、25,000kgの燃料は、ロケットを緑色に変えるのに必要な量である必要がありますが、より大きな数値を使用して、黄色の色合いも機能することを確認してください。

![軌道円に到達し、燃料が残っている黄色いロケット。](images/orbit_meh.png){:width="300px"}

--- /task ---

--- save ---
