--- question ---
---
legend: Pergunta 3 de 3
---

Este código usa `tint()` para colorir um foguete em um jogo para mostrar ao jogador como ele está se saindo.

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

Se a variável `pontos` tiver o valor `99` e a variável `vidas` tiver o valor `1`, como será o foguete?

--- choices ---

- (x)

![Uma imagem de foguete com tonalidade âmbar.](images/rocket_amber.png) <div style="text-align: center;">Âmbar

 --- feedback ---

 Correto! O jogador tem menos de 100 pontos e apenas 1 vida restante. The rocket is coloured amber to let them know that this is their last chance to win!

 --- /feedback ---

- ( )

![Uma imagem de foguete sem tonalidade](images/rocket_original.png) <div style="text-align: center;">Sem tonalidade

 --- feedback ---

 Não é bem assim, o foguete tem uma tonalidade pois uma das afirmações é verdadeira.

 --- /feedback ---

- ( )

![Uma imagem de foguete com tonalidade verde](images/rocket_green.png) <div style="text-align: center;">Verde

 --- feedback ---

 Não exatamente, o jogador precisaria de `>= 100` pontos para vencer e deixar seu foguete verde. Eles têm `99`, o que não é suficiente. Verifique cuidadosamente as condições.

 --- /feedback ---

- ( )

![Uma imagem de foguete com tonalidade vermelha](images/rocket_red.png) <div style="text-align: center;">Vermelho

 --- feedback ---

 Não é bem assim, o jogador tem `< 100` pontos mas a vida não é igual a `0`. Verifique cuidadosamente as condições.

 --- /feedback ---

--- /choices ---

--- /question ---
