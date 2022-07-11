## Alcançando a órbita

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

O objetivo do lançamento do foguete é colocar um satélite em órbita. 

Uma órbita é um caminho curvo que um objeto percorre em torno de outro devido à gravidade.

O foguete pode mudar de cor para mostrar o sucesso do lançamento. 

</div>
<div>

![Três imagens lado a lado mostrando lançamento bem-sucedido (tonalidade verde), lançamento sobrecarregado (tonalidade âmbar) e lançamento mal sucedido (tonalidade vermelha).](images/check_orbit.png){:width="400px"}

</div>
</div>

--- task ---

Crie duas novas variáveis globais para definir o raio do círculo da órbita e a coordenada `y` da órbita para o ponto que o centro do foguete precisa alcançar para lançar o satélite.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11-12
---

# Configurar variáveis globais
screen_size = 400   
rocket_y = screen_size   
burn = 100   
orbit_radius = 250   
orbit_y = screen_size - orbit_radius

--- /code ---

--- /task ---

--- task ---

Atualize a função `desenhar_plano_de_fundo()` para desenhar uma elipse para representar a órbita do satélite que o foguete precisa alcançar.

--- code ---
---
language: python filename: main.py - draw_background() line_numbers: true line_number_start: 37
line_highlights: 42-45
---

def draw_background():   
background(0) #Short for background(0, 0, 0) — black   
image(planet, width/2, height, 300, 300)

  no_fill() #Turn off any fill  
stroke(255) #Set a white stroke   
stroke_weight(2)   
ellipse(width/2, height, orbit_radius * 2, orbit_radius * 2)

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu programa e verifique que uma linha de órbita branca foi desenhada.

![A tela com o planeta e nova linha de órbita.](images/draw_orbit.png){:width="300px"}

--- /task ---

O foguete deve parar quando atingir a órbita do satélite – o fim da missão.

--- task ---

Atualize seu código `if combustivel >= queima` para verificar também se o foguete não atingiu a órbita.

Você pode usar as instruções `and` em `if` para verificar se duas ou mais condições são verdadeiras.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 14
line_highlights: 19
---

# A função desenhar_foguete vai aqui
def draw_rocket():

  global rocket_y, fuel, burn

    if fuel >= burn and rocket_y > orbit_y: #Still flying

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu projeto e digite `50000` para a quantidade de combustível. Isso deve ser bastante combustível para alcançar a órbita. O foguete deve parar de se mover quando atingir a órbita.

--- /task ---

O foguete deve ficar vermelho se ficar sem combustível antes de ficar alto o suficiente para lançar o satélite.

--- task ---

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 30
line_highlights: 34-35
---

    fill(200, 200, 200, 100)   
    for i in range(20):   
      ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

  if fuel < burn and rocket_y > orbit_y: #No more fuel and not in orbit tint(255, 0, 0) #Failure

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu código e digite `20000` para a quantidade de combustível. Verifique que o foguete fica vermelho quando para abaixo da órbita.

![Um foguete vermelho que ficou sem combustível antes do círculo orbital. O planeta também ficou vermelho.](images/orbit_failure.png){:width="300px"}

Oh não, o planeta ficou vermelho!

--- /task ---

--- task ---

A função `tint()` define a cor do tom para todas as imagens que são desenhadas até que você altere o tom ou use `no_tint()` para desativá-lo.

**Escolha:** Adicione uma chamada para `no_tint()` depois de desenhar a imagem para que o planeta não fique vermelho no próximo quadro — ou deixe-o se você gosta do planeta ficando vermelho!

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 34
line_highlights: 38
---

if fuel < burn and rocket_y > orbit_y: tint(255, 0, 0) #Failure

image(rocket, width/2, rocket_y, 64, 64)   
no_tint() #So the planet isn't tinted red in the next frame!


--- /code ---

--- /task ---

--- task ---

Use a função `tint()` novamente, desta vez para colorir o foguete de verde se o foguete tiver combustível suficiente para alcançar a órbita do satélite:

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 34
line_highlights: 36-37
---

if fuel < burn and rocket_y > orbit_y: tint(255, 0, 0) #Failure   
elif rocket_y <= orbit_y:   
tint(0, 255, 0) #Success

image(rocket, width/2, rocket_y, 64, 64)   
no_tint()

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu projeto e digite `50000` para a quantidade de combustível. Verifique que o seu foguete fica verde quando atinge a órbita do satélite.

![Um foguete verde que atingiu o círculo orbital e ainda tem combustível.](images/orbit_success.png){:width="300px"}

--- /task ---

Agora você tem uma simulação que pode ser usada para mostrar quanto combustível é necessário no mínimo para alcançar a órbita do satélite. Isso é ótimo; no entanto, você pode consumir uma enorme quantidade de combustível e ainda ter sucesso, mas isso é caro e um desperdício!

--- task ---

Altere as condições em seu código de sucesso para que o foguete só fique verde se atingir a órbita `e` tiver menos de 1.000 kg de combustível restante.

Adicione um código para colorir o foguete de amarelo se o foguete tiver mais de 1.000 kg de combustível restante quando atingir a órbita.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 34
line_highlights: 36, 38-39
---

if fuel < burn and rocket_y > orbit_y: tint(255, 0, 0) #Failure   
elif fuel < 1000 and rocket_y <= orbit_y:   
tint(0, 255, 0) #Success   
elif fuel >= 1000 and rocket_y <= orbit_y:    
tint(255, 200, 0) #Too much fuel

image(rocket, width/2, rocket_y, 64, 64)    
no_tint() #So the planet isn't tinted in the next frame!

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu programa várias vezes com números diferentes; por exemplo, 25.000 kg de combustível deve ser a quantidade necessária para tornar o foguete verde, mas também verifique se a tonalidade amarela também funciona usando um número maior.

![Um foguete amarelo que atingiu o círculo orbital e ainda tem combustível.](images/orbit_meh.png){:width="300px"}

--- /task ---

--- save ---
