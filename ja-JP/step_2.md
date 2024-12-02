## Draw the background

--- task ---

[プロジェクトテンプレート](https://trinket.io/python/ace602d441){:target="_blank"}を開きます。

--- /task ---

First, you will create a black background to represent space.

背景を描画する`draw_background()` 関数をコメントの下のあるべき位置で定義します。

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# draw_background関数はここにあります
def setup():   
#ここでアニメーションをセットアップします   
size(screen_size, screen_size)

--- /code ---

--- /task ---

--- task ---

Add this function to the list of things to `draw()` in every frame.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 28
line_highlights: 20
---

def draw():   
#フレームごとにやること    
draw_background()

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and you should see a black square. --- /task ---



--- task ---

Add a line of code to display an image of a planet.

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 21-23
---
def draw_background():   
background(0) #background(0, 0, 0) の省略形 - 黒    
image(planet, width/2, height, 300, 300) #画像を描く

`image()` 関数の構成は以下のとおりです：

- image filename - we have already loaded the planet image
- x coordinate - we have already set the screen size
- y coordinate
- image width
- image height

--- /task ---

--- task ---

**テスト：** コードを実行し、下部に惑星が半分描かれた黒い背景が描画されることを確認します。

![![黒い背景の惑星。](images/step_2.png)](images/step_2.png){:width="300px"}

--- /task ---

### A different planet?

--- task ---

Click on the image icon to the left to view the image gallery.

![Choose a different planet](images/image_gallery.png)

また、 `setup()` 関数にコードを追加して、選択した画像を `planet` グローバル変数にロードします。 後で惑星を画面に描画するときに使用するので、変数はグローバルである必要があります。

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 15-17
---
def setup():   
#ここでアニメーションをセットアップします   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet   
planet = load_image('planet.png') #あなたが選んだ惑星

--- /task ---

