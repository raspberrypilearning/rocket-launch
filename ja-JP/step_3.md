## 発射！

スタータープロジェクトには、ロケットの画像が用意されています。

![Image of the rocket in the code editor image gallery.](images/rocket_image.png)

--- task ---

`setup()` 関数にコードを追加して、ロケットの画像を `rocket` グローバル変数にロードします。

<div class="c-project-code">

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 24, 26
---

def setup():   
#ここでアニメーションをセットアップします   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet, rocket   
planet = load_image('planet.png')    
rocket = load_image('rocket.png')

--- /code ---

--- /task ---

--- task ---

`rocket_y` グローバル変数を追加して、ロケットの `y`座標を追跡します。

--- code ---
---
def draw_rocket():
line_highlights: 9
---

# グローバル変数を設定する
screen_size = 400    
rocket_y = screen_size #一番下から開始

--- /code ---

--- /task ---


ロケットの`y`位置は、400(画面の高さ) から始まり、新しいフレームが描画されるたびに1ずつ減少します。

--- task ---

画面の途中にあるロケットの画像。

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 12-16
---

# draw_rocket関数はここにあります
`draw_rocket()` 関数を定義して、ロケットの `y`座標置を変更して再描画させます。


--- /code ---

--- /task ---

--- task ---

`draw_rocket()` 関数を定義して、ロケットの `y`座標置を変更して再描画させます。

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 34
line_highlights: 37
---

def draw():   
#フレームごとにやること   
draw_background()   
draw_rocket()


--- /code ---

--- /task ---

--- task ---

Trinket画像ライブラリのロケットの画像。

--- /task ---


新しいフレームが描画されるたびに、ロケットはアニメーション効果を生み出すために画面を上に移動する必要があります。


--- task ---

`rocket_y -= 1` は、 `rocket_y = rocket_y - 1`の短縮形です。


--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12
---

def draw_rocket():   
global rocket_position     
rocket_position = rocket_position - 1    
image(rocket, width/2, rocket_position, 64, 64)

--- /code ---

--- /task ---


--- task ---

**テスト：** コードを実行して、ロケットが画面の下部から始まり、フレームごとに上に移動することを確認します。


![![画面の下から上に一定の速度で飛んでいるロケット。](images/fly.gif)](images/fly.gif){:width="300px"}

--- /task ---

