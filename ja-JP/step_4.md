## 排気効果

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

ロケットは、排気ガスの軌跡をシミュレートする特殊効果を使うと、よりリアルに見えます。 

`for`ループを使用してフレームごとにたくさんの図形を描くことで、クールな効果を生み出すことができます。

</div>
<div>

![排気ガスの軌跡を出しながら飛ぶロケット](images/flying_rocket.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
コーディングは、映画やゲームの <span style="color: #0faeb0">**グラフィック効果**</span> を作成するために使用されます。 アニメーションの各フレームを個別に描画するよりも、コードを作成する方がはるかに速いです。 </p>

### Draw your exhaust

さまざまな `y` 座標の位置に黄色の楕円をたくさん描くと、底が丸い排気ガスの軌跡ができます。

--- task ---

`draw_rocket()` 関数を更新して、 排気ガスに見立てた楕円の描画を`25` 回繰り返す `for`ループを追加しましょう。 **ループ変数**`i` が `rocket_y`に追加され、各楕円がロケットのさらに下に描画されます。

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 12
line_highlights: 16-22
---

global rocket_y   
rocket_y -= 1   

    for i in range(25): #燃焼廃棄に見立てた楕円を 25 個描画<br x-id="3" />
        fill(255, 255, 0) #黄色<br x-id="3" />
        ellipse(width/2, rocket_y + i, 8, 3) #i はループが繰り返されるたびに増加


--- /code ---

--- /task ---

fill(200, 200, 200, 100) #透明な灰色   
for i in range(20): #排煙をランダムに20回描画    
ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

`for` ループでコードを特定の回数実行するには、 `range()` 関数が使えます。 たとえば、 `range(5)` は、0から始まる5つの数値を順に並べたものを作るので、[0, 1, 2, 3, 4] となります。

`for` ループが繰り返されるたびに、変数にその時々の数値がセットされ、ループ内で使用できます。

--- task ---

**テスト：** コードを実行して、ロケットに新しい排気ガスの軌跡があることを確認します。

![排気ガスの軌跡があるロケットのクローズアップ。](images/rocket_exhaust.png){:width="300px"}

--- /task ---

### Add a gradient

`i` 変数を使用して、緑の割合が描画のたびに少なくなって色が変化する楕円を描くこともできます。

--- task ---

`fill()`の呼び出しをに変更して、緑の量を `255 - i*10` に設定すると、最初は赤と緑の量が等しく、最後に緑が非常に少なくなるようにできます。

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 19
line_highlights: 20
---

    for i in range(25):<br x-id="3" />
        fill(255, 255 - i * 10, 0) #緑の量を減らす<br x-id="4" />
        ellipse(width/2, rocket_y + i, 8, 3)

--- /code ---

--- /task ---

--- task ---

**テスト：** 楕円でできた軌跡が黄色から赤に徐々に変化することを確認します。

--- /task ---

### Create a smoke effect

各フレームのさまざまな位置にわずかに透明な灰色の楕円をたくさん描くことによって排気の煙が作成されます。

![煙の効果の遅いアニメーション。](images/rocket_smoke.gif)

--- task ---

今回は、排煙に見立てた楕円の色は変えないので、 `fill()` はループの外側にあります。 `fill()` への4番目の入力は不透明度です。 不透明度の値を低くすると、色がより透明になり、図形の下にあるものを見ることができます。

アニメーションのフレームごとに、ランダムなサイズの20個の楕円がランダムな位置に描画されます。

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 19
line_highlights: 23-26
---

    for i in range(25):<br x-id="2" />
        fill(255, 255 - i * 10, 0)<br x-id="3" />
        ellipse(width/2, rocket_y + i, 8, 3)

--- /code ---

--- /task ---

--- task ---

**テスト：** プログラムを実行し、排気ガスが見えることを確認します。

![排気ガスの軌跡に排煙が追加されたロケットのクローズアップ。](images/rocket_exhaust_circles.gif)

--- /task ---

--- save ---
