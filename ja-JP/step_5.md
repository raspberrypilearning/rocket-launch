## 燃料を燃やす

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

ロケットに搭載する燃料の量を決めることは、ロケットを打ち上げるときに決定する最も重要なことの1つです。 

これを行うには、飛行中に燃焼する燃料の量をシミュレートする必要があります。
</div>

![出力領域に必要な燃料の量を尋ねる質問があるプログラム](images/burn_question_full.png){:width="300px"}

</div>

--- task ---

変数を追加して、ロケットが(フレームごとに) 燃焼する燃料の量を追跡します。

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 7
line_highlights: 10
---

#グローバル変数を設定する
screen_size = 400   
rocket_y = screen_size  
burn = 100 #フレームごとに燃焼される燃料の量

--- /code ---

--- /task ---


--- task ---

プログラムの下部に、ロケットに搭載する燃料の量をユーザーに尋ねるコードを追加し、その答えを `fuel` グローバル変数に格納します。

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 52
line_highlights: 52
---

fuel = int(input('燃料を何キログラム使いますか?'))   
run()

--- /code ---

--- /task ---

ロケットは、燃料をすべて燃焼するまで動くことができます。

--- task ---

`draw_rocket()` 関数にコードを追加して、残りの `fuel(燃料)` をフレームごとに `burn(燃焼)` だけ減らします。 `print()` を使用して、フレームごとに残っている燃料の量を表示します。

`fuel` および `burn` 変数をグローバル変数として使用することを宣言しなければなりません。

--- code ---
---
language: python 
filename: main.py — draw_rocket() 
line_numbers: true 
line_number_start: 15
line_highlights: 15, 17-18
---

  global rocket_y, fuel, burn   
  rocket_y -= 1   
  fuel -= burn #燃料の燃焼   
  print('燃料の残り: ', fuel)

--- /code ---

--- /task ---

--- task ---

**テスト：** プログラムを実行して、`燃料を何キログラム使いますか？` に回答するまでアニメーションが開始されないことを確認します。 燃料の量として`30000` を入力してみてください。

燃料が残っていなくてもロケットは動き続けます。

![出力領域で必要な燃料の量を尋ねる質問を含むプログラム。](images/burn_question.png)

--- /task ---

--- task ---

ロケットは、十分な燃料が残っている場合にのみ動くようにする必要があります。 `if` ステートメントを追加して、 `fuel >= burn`であることを確認します。

`image()` 関数を呼び出す前のコードのすべての行をインデントする必要があります。 これを行うには、マウスですべての行を強調表示してから、キーボードの <kbd>Tab</kbd> をタップします。すべての行を一度にインデントできます。

ロケットを描くのは常に行うので、 `image()` 行をインデントする必要はありません。

--- code ---
---
language: python 
filename: main.py — draw_rocket() 
line_numbers: true 
line_number_start: 15
line_highlights: 16-31
---

  global rocket_y, fuel, burn

  if fuel >= burn: #まだ燃料が残っている   
    rocket_y -= 1   
    fuel -= burn   
    print('燃料の残り: ', fuel)   

    no_stroke() #境界線なし   
    
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

**テスト：** プログラムを実行して、燃料がなくなったときにロケットが停止することを確認します。

![画面中央にロケットがあり、「燃料の残り：0」という文章が表示された画像。](images/burn_empty.png){:width="300px"}

--- /task ---

このコンピュータシミュレーションはあまり正確ではありませんが、アニメーションには十分です。

--- save ---

