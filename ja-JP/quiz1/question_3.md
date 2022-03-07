--- question ---
---
legend: 質問3/3
---

このコードは、 `tint()` を使用してゲーム内のロケットに色を付け、どのようになっているかをプレーヤーに示します。

--- code ---
---
language: python
---

if points >= 100:    
tint(0, 255, 0) #緑   
elif points < 100 and lives == 1:   
tint(255, 200, 0) #アンバー    
elif points < 100 and lives == 0:     
tint(255, 0, 0) #赤     
else:      
no_tint()

image(rocket, width/2, height/2, 64, 64)

--- /code ---

`point` 変数の値が `99` で、 `lives` 変数の値が `1`の場合、ロケットはどのようになりますか？

--- choices ---

- (x)

![アンバーの色あいのロケット画像。](images/rocket_amber.png) <div style="text-align: center;">アンバー

 --- feedback ---

 正解！ プレイヤーのポイントは100未満で、残りのライフは1つだけ残っています。 ロケットはアンバーに色付けされ、これが最後の勝利のチャンスであることを知らせています！

 --- /feedback ---

- ( )

![色合いのないロケット画像](images/rocket_original.png) <div style="text-align: center;">元の色

 --- feedback ---

 残念です。ステートメントの内の1つが真なので、ロケットには色合いが付けられます。

 --- /feedback ---

- ( )

![緑の色合いのロケット画像](images/rocket_green.png) <div style="text-align: center;">緑

 --- feedback ---

 残念です。プレーヤーが勝ってロケットをグリーンに変えるには、 `>= 100` のポイントが必要です。 ポイントは`99`なので、これでは不足です。 条件をよく確認してください。

 --- /feedback ---

- ( )

![赤の色合いのロケット画像](images/rocket_red.png) <div style="text-align: center;">赤

 --- feedback ---

 残念です。プレイヤーのポイントは `< 100` ですが、ライフは `0`ではありません。 条件をよく確認してください。

 --- /feedback ---

--- /choices ---

--- /question ---
