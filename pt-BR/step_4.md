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

### Desenhe sua combustão

Desenhar muitas elipses amarelas em diferentes posições `y` cria uma trilha de combustão com fundo redondo.

--- task ---

Atualize sua função `desenhar_foguete()` para incluir um ciclo `for` que repete o desenho de `25` elipses da combustão. A **variável de ciclo** `i` é adicionada a `foguete_y` para desenhar cada elipse mais abaixo do foguete.

--- code ---
---
language: python filename: main.py - desenhar_foguete() line_numbers: true line_number_start: 12
line_highlights: 16-20
---

def desenhar_foguete(): global foguete_y   
foguete_y -= 1   

    no_stroke()  # Desliga o traço
    
    for i in range(25):  # Desenhe 25 elipses de combustão em chamas   
        fill(255, 255, 0)  # Amarelo   
        ellipse(width/2, foguete_y + i, 8, 3)  # i aumenta cada vez que o ciclo se repete    
    
    image(foguete, width/2, foguete_y, 64, 64)


--- /code ---

--- /task ---

Um ciclo `for` repete um pedaço de código uma vez para cada item que é fornecido.

Para executar o código em um ciclo `for` um certo número de vezes, você pode usar a função `range()`. Por exemplo, `range(5)` cria uma sequência de cinco números começando em 0, então [0, 1, 2, 3, 4].

Cada vez que o ciclo `for` se repete, ele define uma variável para o item atual para que você possa usá-lo no ciclo.

--- task ---

**Teste:** Execute seu código para verificar que o foguete tem um novo rastro de combustão.

![Uma vista de perto do foguete com uma trilha de combustão.](images/rocket_exhaust.png){:width="300px"}

--- /task ---

### Adicione um gradiente

A variável `i` também pode ser usada para criar um gradiente de cor com menos verde em cada elipse desenhada.

--- task ---

Altere a chamada para `fill()` para definir a quantidade de verde para `255 - i*10` para que a primeira elipse tenha quantidades iguais de vermelho e verde e a última elipse tenha muito pouco verde.

--- code ---
---
language: python filename: main.py - desenhar_foguete() line_numbers: true line_number_start: 18
line_highlights: 19
---

    for i in range(25):   
        fill(255, 255 - i * 10, 0)  # Reduz a quantidade de verde    
        ellipse(width/2, foguete_y + i, 8, 3)

--- /code ---

--- /task ---

--- task ---

**Teste:** Verifique que você obtém um rastro de elipses mudando gradualmente de amarelo para vermelho.

--- /task ---

### Crie um efeito de fumaça

A trilha de gases de escape é criada desenhando muitas elipses cinzas levemente transparentes em diferentes posições em cada quadro.

![Uma animação lenta do efeito de fumaça.](images/rocket_smoke.gif)

--- task ---

Desta vez, o `fill()` está fora do laço, pois a cor é a mesma para cada elipse de fumaça. A quarta entrada para `fill()` é a opacidade, um valor de opacidade baixo torna a cor mais transparente para que você possa ver as formas abaixo.

Em cada quadro da animação, 20 elipses de tamanhos aleatórios serão desenhadas em posições aleatórias.

--- code ---
---
language: python filename: main.py - desenhar_foguete() line_numbers: true line_number_start: 18
line_highlights: 22-24
---

    for i in range(25):  
        fill(255, 255 - i * 10, 0)   
        ellipse(width/2, foguete_y + i, 8, 3)    
    
    fill(200, 200, 200, 100)  # Cinza transparente   
    for i in range(20):  # Desenhar 20 elipses de fumaça aleatórias    
        ellipse(width/2 + randint(-5, 5), foguete_y + randint(20, 50), randint(5, 10), randint(5, 10))    
    
    image(foguete, width/2, foguete_y, 64, 64)

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute o seu programa e verifique que os gases de escape estão visíveis.

![Uma vista de perto do foguete e da trilha de exaustão com fumaça adicional.](images/rocket_exhaust_circles.gif)

--- /task ---

--- save ---
