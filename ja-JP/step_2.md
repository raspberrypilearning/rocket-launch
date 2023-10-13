## シーンを設定する

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
アニメーションには、ロケットが発射される惑星がある宇宙の背景が必要です。
</div>
<div>

![黒い背景の惑星。](images/step_2.png){:width="300px"}

</div>
</div>

--- task ---

[プロジェクトテンプレート](https://trinket.io/python/ace602d441){:target="_blank"}を開きます。

### Create the screen

--- /task ---

`screen_size` 変数を、画面のサイズを設定と、計算に使用します。 関数の外部で定義された変数は **グローバル** であるため、プログラム内のどこでも使用できます。

--- task ---

`グローバル変数を設定する` コメントを見つけ、`screen_size`変数を作成するコードを追加してください。

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# グローバル変数を設定する
screen_size = 400

--- /code ---

--- /task ---

--- task ---

`screen_size` 変数を使用して、400 x 400ピクセルの正方形を作成します。

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 20
---

def setup():   
#ここでアニメーションをセットアップします   
size(screen_size, screen_size)


--- /code ---

--- /task ---

### Choose an image

--- task ---

スタータープロジェクトには、3つの異なる惑星と月の画像が用意されています。 これらは、[ **View and Add Images**] ボタンを選択することにより、Trinket画像ライブラリで表示できます。

![A screenshot of the code editor, with the image gallery highlighted containing images of planets and the moon.](images/image_gallery.png)

**選択：** 使いたい画像を決め、ファイル名をメモします。 例えば、`orange_planet.png`などです。

--- /task ---

--- task ---

`setup()` で画像をロードすることをお勧めします。

`image_mode(CENTER)` の行は、（左上隅ではなく）画像の中心の座標を指定して画像を配置することを示しています。

また、 `setup()` 関数にコードを追加して、選択した画像を `planet` グローバル変数にロードします。 後で惑星を画面に描画するときに使用するので、変数はグローバルである必要があります。

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 21-23
---

def setup():   
#ここでアニメーションをセットアップします   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet   
planet = load_image('planet.png') #あなたが選んだ惑星


--- /code ---

--- /task ---

### Draw background

--- task ---

背景を描画する`draw_background()` 関数をコメントの下のあるべき位置で定義します。

`background(0)` を使用して背景色を黒に設定し、 `image()` 関数を追加して惑星を描画します。 `image()` 関数の構成は以下のとおりです：

`image(画像ファイル名, x座標, y座標, 画像の幅, 画像の高さ)`

`p5` ライブラリは、画面のサイズに基づいて`幅` および `高さ` のグローバの変数を設定します。 これらをコードで使用して、惑星を画面の真ん中(`幅の半分`) の下部(`高さ`) の位置に配置します。

--- code ---
---
language: python filename: main.py — draw_background() line_numbers: true line_number_start: 14
line_highlights: 15-17
---

# draw_background関数はここにあります
def draw_background():   
background(0) #background(0, 0, 0) の省略形 - 黒    
image(planet, width/2, height, 300, 300) #画像を描く


--- /code ---

背景を描画するためのすべてのコードを1つの関数にまとめると、コードが理解しやすくなります。

--- /task ---

--- task ---

背景を表示するには、 `draw()`から`draw_background()` を呼び出します。 これにより、 `draw()` が呼び出されるたびに背景が再描画され、古い描画が上書きされます。

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 28
line_highlights: 30
---

def draw():   
#フレームごとにやること    
draw_background()

--- /code ---

--- /task ---

--- task ---

**テスト：** コードを実行し、下部に惑星が半分描かれた黒い背景が描画されることを確認します。

--- /task ---

If you have a Raspberry Pi account, on your code editor you can click on the **Save** button to save a copy of your project to your Projects.

--- save ---
