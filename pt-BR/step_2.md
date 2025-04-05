## Desenhar o plano de fundo

--- task ---

Abra o [modelo de projeto](https://trinket.io/python/f7354cbf88){:target="_blank"}.

--- /task ---

First, you will create a black background to represent space.

--- task ---

Defina uma função `desenhar_plano_de_fundo()`, para desenhar o plano de fundo, abaixo do comentário que informa para onde deve ir.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# A função desenhar_plano_de_fundo vai aqui
def setup():   
#Configure sua animação aqui   
size(tamanho_tela, tamanho_tela)

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
#O que fazer em cada quadro    
desenhar_plano_de_fundo()

--- /code ---

--- /task ---

--- task ---

Se você possui uma conta Raspberry Pi, em seu editor de código, você pode clicar no botão **Salvar** para salvar uma cópia do seu projeto em seus Projetos.

--- /task ---



--- task ---

Add a line of code to display an image of a planet.

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 21-23
---
def draw_background():  
background(0,0,0) image(planet, screen_size/2, screen_size, 300, 300)

--- /code ---


A função `image()` é apresentada:

- image filename - we have already loaded the planet image
- x coordinate - we have already set the screen size
- y coordinate
- image width
- image height

--- /task ---

--- task ---

**Teste:** Execute seu código e verifique que ele desenha um fundo preto com meio planeta na parte inferior.

![![Um planeta contra um fundo preto.](images/step_2.png){:width="300px"}](images/step_2.png){:width="300px"}

--- /task ---

### A different planet?

--- task ---

Click on the image icon to the left to view the image gallery.

![Choose a different planet](images/image_gallery.png)

Por exemplo, `orange_planet.png`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 15-17
---
def setup(): # Set up your animation here size(screen_size, screen_size) image_mode(CENTER) global planet planet = load_image('planet.png')

--- /code ---

--- /task ---

