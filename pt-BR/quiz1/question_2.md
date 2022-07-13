
--- question ---
---
legend: Pergunta 2 de 3
---

Um projeto tem este código de `setup` para carregar uma imagem de um planeta e dizer que as imagens devem ser posicionadas em seu centro:

--- code ---
---
language: python
---

def setup():   
size(400, 400)   
image_mode(CENTER)   
global planeta   
planeta = load_image('planet.png')

--- /code ---

As coordenadas começam em (0, 0) no canto superior esquerdo. No projeto, você desenhou imagens de planetas e foguetes usando a função `image((nome do arquivo de imagem, x-coord, y-coord, x-largura, y-altura)`.

Onde irá esse código posicionar a imagem do planeta?

--- code ---
---
language: python
---

image(planeta, 300, 100, 128, 128)

--- /code ---

--- choices ---

- ( ) ![Uma imagem de planeta posicionada horizontalmente à direita da tela e verticalmente no meio.](images/planet400200.png)

  --- feedback ---

A segunda e terceira entradas para a função `image()` são as coordenadas `x` e `y` para o centro da imagem. Este planeta tem as coordenadas `(400, 200)`.

  --- /feedback ---

- ( ) ![Uma imagem do planeta posicionada no meio do quadrante inferior esquerdo.](images/planet100300.png)

  --- feedback ---

A segunda e terceira entradas para a função `image()` são as coordenadas `x` e `y` para o centro da imagem. Este planeta tem as coordenadas `(100, 300)`.

  --- /feedback ---

- (x) ![Uma imagem do planeta posicionada no meio do quadrante superior direito.](images/planet300100.png)

  --- feedback ---

Correto! A segunda e terceira entradas para a função `image()` são as coordenadas `x` e `y` para o centro da imagem. Esta imagem tem as coordenadas (300, 100), portanto, está a 300 (de 400) pixels da esquerda para a coordenada `x` e 100 (de 400) pixels para baixo a partir do topo.

  --- /feedback ---

- () ![Uma imagem do planeta posicionada no quadrante superior esquerdo.](images/planet128128.png)

  --- feedback ---

A quarta e quinta entradas dão o tamanho da imagem. A segunda e terceira entradas para a função `image()` são as coordenadas `x` e `y` para o centro da imagem. Este planeta tem as coordenadas `(128, 128)`.

  --- /feedback ---

--- /choices ---

--- /question ---
