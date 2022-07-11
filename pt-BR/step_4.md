## Efeitos da combustão

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

O foguete ficará mais realista com alguns efeitos especiais para simular a trilha dos gases resultantes da combustão. 

Você pode criar efeitos legais usando um ciclo `for` para desenhar muitas formas em cada quadro.

</div>
<div>

![O foguete no meio do voo com uma trilha de combustão.](images/flying_rocket.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A programação é usada para fazer <span style="color: #0faeb0">**efeitos gráficos**</span> para filmes e jogos. É muito mais rápido escrever código do que desenhar cada quadro de uma animação individualmente. </p>

Desenhar muitas elipses amarelas em diferentes posições `y` cria uma trilha de combustão com fundo redondo.

--- task ---

Um ciclo `for` repete um pedaço de código uma vez para cada item que é fornecido. Para executar o código em um ciclo `for` um certo número de vezes, você pode usar a função `range()`. Por exemplo, `range(5)` cria uma sequência de cinco números começando em 0, então [0, 1, 2, 3, 4].

Cada vez que o ciclo `for` se repete, ele define uma variável para o item atual para que você possa usá-lo no ciclo.

Atualize sua função `desenhar_foguete()` para incluir um ciclo `for` que repete o desenho de `25` elipses da combustão. A variável de ciclo **** `i` é adicionada a `foguete_y` para desenhar cada elipse mais abaixo do foguete.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 12
line_highlights: 16-22
---

def draw_rocket():

  global rocket_y   
rocket_y -= 1

  no_stroke() #Turn off the stroke

  for i in range(25): #Draw 25 burning exhaust ellipses   
fill(255, 255, 0) #Yellow   
ellipse(width/2, rocket_y + i, 8, 3) #i increases each time the loop repeats

  image(rocket, width/2, rocket_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu código para verificar que o foguete tem um novo rastro de combustão.

![Uma vista de perto do foguete com uma trilha de combustão.](images/rocket_exhaust.png){:width="300px"}

--- /task ---

A variável `i` também pode ser usada para criar um gradiente de cor com menos verde em cada elipse desenhada.

--- task ---

Altere a chamada para `preencher()` para definir a quantidade de verde para `255 - i*10` para que a primeira elipse tenha quantidades iguais de vermelho e verde e a última elipse tenha muito pouco verde.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 19
line_highlights: 20
---

  for i in range(25):   
fill(255, 255 - i * 10, 0) #Reduce the amount of green    
ellipse(width/2, rocket_y + i, 8, 3)

--- /code ---

--- /task ---

--- task ---

**Teste:** Verifique que você obtém um rastro de elipses mudando gradualmente de amarelo para vermelho.

--- /task ---

A trilha de gases de escape é criada desenhando muitas elipses cinzas levemente transparentes em diferentes posições em cada quadro.

![Uma animação lenta do efeito de fumaça.](images/rocket_smoke.gif)

--- task ---

Desta vez, o `preencher()` está fora do laço, pois a cor é a mesma para cada elipse de fumaça. A quarta entrada para `preencher()` é a opacidade, um valor de opacidade baixo torna a cor mais transparente para que você possa ver as formas abaixo.

Em cada quadro da animação, 20 elipses de tamanhos aleatórios serão desenhadas em posições aleatórias.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 19
line_highlights: 23-26
---

  for i in range(25):  
fill(255, 255 - i * 10, 0)   
ellipse(width/2, rocket_y + i, 8, 3)

  fill(200, 200, 200, 100) #Transparent grey   
for i in range(20): #Draw 20 random smoke ellipses    
ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

  image(rocket, width/2, rocket_y, 64, 64)

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute o seu programa e verifique que os gases de escape estão visíveis.

![Uma vista de perto do foguete e da trilha de exaustão com fumaça adicional.](images/rocket_exhaust_circles.gif)

--- /task ---

--- save ---
