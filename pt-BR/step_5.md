## Queimar combustível

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Uma das coisas mais importantes a decidir ao lançar um foguete é quanto combustível carregar nele. 

Para fazer isso, você precisa simular quanto combustível será queimado na viagem.
</div>

![O programa com uma pergunta na área de saída perguntando quanto combustível é necessário.](images/burn_question_full.png){:width="300px"}

</div>

### Crie uma variável de combustível

--- task ---

Adicione uma variável para acompanhar a quantidade de combustível que seu foguete queima (em quadros).

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 10
---

# Configurar variáveis globais
tamanho_tela = 400   
foguete_y = tamanho_tela  
queimar = 100  # Quanto combustível é queimado em cada quadro

--- /code ---

--- /task ---


--- task ---

Na parte inferior do seu programa, adicione código para perguntar ao usuário quanto combustível adicionar ao foguete e guarde sua resposta em uma variável global `combustivel`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 51
line_highlights: 51
---

fuel = int(input('How many kilograms of fuel do you want to use?'))   
run()

--- /code ---

--- /task ---

### Verificar o combustível em relação à queima

O foguete só deve se mover se não tiver queimado todo o seu combustível.

--- task ---

Adicione código à função `desenhar_foguete()` para reduzir o restante `combustivel` pela `queima` de cada quadro. Use `imprimir()` para mostrar quanto combustível resta em cada quadro.

Você precisa dizer que deseja usar as variáveis globais `combustivel` e `queima`.

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 15, 17-18
---

    global foguete_y, combustivel, queimar   
    foguete_y -= 1   
    combustivel -= queimar  # Queimar combustível   
    print('Combustível restante: ', combustivel)

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu programa para verificar que a animação não inicia até `Quantos quilogramas de combustível você quer usar?` for respondido. Tente inserir `30000` como a quantidade de combustível.

O foguete continuará funcionando mesmo que não tenha mais combustível.

![O programa com uma pergunta na área de saída perguntando quanto combustível é necessário.](images/burn_question.png)

--- /task ---

--- task ---

O foguete só deve se mover se tiver combustível suficiente. Adicione uma declaração `if` para verificar se `combustivel >= queima`.

Você precisará indentar todas as linhas de código antes da chamada de função `image()`. Para fazer isso, destaque todas as linhas com o mouse e, em seguida, pressione a tecla <kbd>Tab</kbd> no teclado para recuar todas as linhas de uma vez.

A linha `image()` não precisa ser recuada porque você sempre quer desenhar o foguete.

--- code ---
---
language: python filename: main.py — desenhar_foguete() line_numbers: true line_number_start: 15
line_highlights: 17-30
---

    global foguete_y, combustivel, queimar  
    
    if combustivel >= queimar:  # Ainda tem combustível   
        foguete_y -= 1   
        combustivel -= queimar   
        print('Combustível restante: ', combustivel)   
    
        no_stroke()  # Desligar traço   
    
        for i in range(25):   
            fill(255, 255 - i*10, 0)   
            ellipse(width/2, foguete_y + i, 8, 3)    
    
        fill(200, 200, 200, 100)   
        for i in range(20):   
            ellipse(width/2 + randint(-5, 5), foguete_y + randint(20, 50), randint(5, 10), randint(5, 10))   
    
    image(foguete, width/2, foguete_y, 64, 64)

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu programa para verificar que o foguete para quando não há mais combustível.

![Imagem de um foguete no meio da tela com a declaração 'Combustível restante: 0'.](images/burn_empty.png){:width="300px"}

--- /task ---

Seu foguete parou quando ficou sem combustível? Muito bem, você enviou um foguete para o espaço sideral!

--- save ---

