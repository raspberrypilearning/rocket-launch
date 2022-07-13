## Preparando o cenário

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
A animação precisa de um cenário espacial com um planeta para lançar o foguete.
</div>
<div>

![Um planeta contra um fundo preto.](images/step_2.png){:width="300px"}

</div>
</div>

--- task ---

Abra o [modelo de projeto](https://trinket.io/python/f7354cbf88){:target="_blank"}.

Se você tiver uma conta Trinket, você pode clicar no botão **Remix** para salvar uma cópia em sua biblioteca `My Trinkets`.

--- /task ---

Você usará uma variável `tamanho_tela` para definir o tamanho da tela e nos cálculos. As variáveis definidas fora das funções são **global** para que você possa usá-las em qualquer lugar do seu programa.

--- task ---

Encontre o comentário `Configurar variáveis globais` e adicione uma linha de código para criar sua variável `tamanho_tela`:

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 7
line_highlights: 8
---

#Configurar variáveis globais
tamanho_tela = 400

--- /code ---

--- /task ---

--- task ---

Use a variável `tamanho_tela` para criar um quadrado de 400 por 400 pixels:

--- code ---
---
language: python
filename: main.py — setup()
line_numbers: true
line_number_start: 18
line_highlights: 20
---

def setup():   
  #Configure sua animação aqui   
  size(tamanho_tela, tamanho_tela)   


--- /code ---

--- /task ---

--- task ---

O projeto inicial tem três imagens diferentes de planetas e a lua fornecidas para você. Você pode visualizá-las na biblioteca de imagens Trinket selecionando o botão **Ver e adidionar imagens**.

![Um símbolo de adição, um símbolo de upload e um símbolo de imagem. O símbolo da imagem é realçado.](images/trinket_image.png)

**Escolha:** Decida qual imagem deseja usar e anote o nome do arquivo. Por exemplo, `orange_planet.png`.

--- /task ---

É uma boa idéia carregar imagens em `setup()` para que estejam prontas quando você precisar usá-las e sua animação será executada rapidamente.

--- task ---

A linha `image_mode(CENTER)` diz que você posicionará as imagens fornecendo as coordenadas do centro da imagem (em vez do canto superior esquerdo).

Adicione também código à função `setup()` para carregar sua imagem escolhida em uma variável global `planeta`. A variável precisa ser global para que você possa usá-la mais tarde quando desenhar o planeta na tela.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18 
line_highlights: 21-23
---

def setup():   
  #Configure sua animação aqui   
  size(tamanho_tela, tamanho_tela)   
  image_mode(CENTER)   
  global planeta   
  planeta = load_image('planet.png') #Seu planeta escolhido



--- /code ---

--- /task ---

--- task ---

Defina uma função `desenhar_plano_de_fundo()`, para desenhar o plano de fundo, abaixo do comentário que informa para onde deve ir.

Use `background(0)` para definir a cor de fundo para preto e adicione uma função `image()` para desenhar o planeta. A função `image()` é apresentada:

`image(nome do arquivo de imagem, coordenada x, coordenada y, largura_imagem, altura_imagem)`

A biblioteca `p5` define variáveis globais `width` e `height` com base no tamanho da tela. Use-os em seu código para posicionar o planeta com o centro a meio da largura (`width/2`) e na parte inferior (`height`) da tela.

--- code ---
---
language: python 
filename: main.py — desenhar_plano_de_fundo() 
line_numbers: true 
line_number_start: 14
line_highlights: 15-17
---

#A função desenhar_plano_de_fundo vai aqui
def desenhar_plano_de_fundo():   
  background(0) #Abreviação de plano de fundo (0, 0, 0) — preto    
  image(planeta, width/2, height, 300, 300) #Desenhe a imagem


--- /code ---

Colocar todo o código para desenhar o plano de fundo em uma função torna seu código mais fácil de entender.

--- /task --- 

--- task ---

Para fazer o plano de fundo aparecer, chame `desenhar_plano_de_fundo()` in `draw()`. Isso fará com que o plano de fundo seja redesenhado toda vez que `draw()` for chamado, cobrindo qualquer desenho mais antigo:

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 28
line_highlights: 30
---

def draw():   
  #O que fazer em cada quadro    
  desenhar_plano_de_fundo()

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu código e verifique que ele desenha um fundo preto com meio planeta na parte inferior.

--- /task ---

--- save ---
