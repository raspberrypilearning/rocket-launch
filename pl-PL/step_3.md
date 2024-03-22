## Startuj!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Za każdym razem, gdy rysowana jest nowa klatka, rakieta musi przesunąć się w górę ekranu, aby stworzyć efekt animacji.
</div>
<div>

![rakieta latająca ze stałą prędkością od dołu do góry ekranu.](images/fly.gif){:width="300px"}

</div>
</div>

--- task ---

Projekt startowy ma obraz rakiety dla Ciebie.

![Obrazek rakiety w galerii obrazów edytora kodu.](images/rocket_image.png)

--- /task ---

--- task ---

Dodaj kod do funkcji ` setup()` , aby załadować obraz rakiety do zmiennej globalnej ` ` .

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 24, 26
---

def setup():   
# Ustaw swoją animację tutaj    
rozmiar(screen_size, screen_size)   
Image_mode(CENTER)   
globalna planeta, rakieta    
planeta = load_image('planet.png')    
rocket = load_image('rocket.png')

--- /code ---

--- /task ---

### Spraw, aby rakieta latała

Pozycja rakiety `.` rozpocznie się od 400 (wysokość ekranu), a następnie zmniejszy się o 1 za każdym razem, gdy zostanie narysowana nowa klatka.

--- task ---

Dodaj zmienną globalną ` rocket_`, aby śledzić pozycję rakiety `.`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9
---

# Ustaw zmienne globalne
Screen_size = 400     
ROCKET_y = screen_size # Zacznij od dołu

--- /code ---

--- /task ---

--- task ---

Zdefiniuj funkcję ` draw_rocket()` , aby zmienić pozycję rakiety `.` i ją przerysować.

` rocket_y -= 1 ` to krótszy sposób powiedzenia ` rocket_y = rocket_y - 1 `.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12-16
---

# Tutaj pojawi się funkcja draw_rocket
def draw_rocket():   
Global ROCKET_y # Użyj globalnej zmiennej ROCKET_y     
Rocket_y -= 1 # Przesuń rakietę     
image(rakieta, width/2, rocket_y, 64, 64)


--- /code ---

--- /task ---

--- task ---

Wywołaj swój nowy ` draw_rocket()` w funkcji ` draw()`, aby rakieta była rysowana ponownie w każdej klatce.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 33
line_highlights: 36
---

def draw():   
# rzeczy do zrobienia w każdej ramce    
draw_background()   
draw_rocket()


--- /code ---

--- /task ---

--- task ---

** Test:** Uruchom swój kod, aby sprawdzić, czy rakieta zaczyna się u dołu ekranu i przesuwa się w górę każdej klatki.

![Animacja rakiety lecącej w połowie drogi w górę ekranu.](images/rocket_fly.gif)

--- /task ---

--- save ---
