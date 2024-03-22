## Ustaw scenę

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Animacja potrzebuje kosmicznego tła z planetą, z której można wystrzelić rakietę.
</div>
<div>

![Planeta na czarnym tle.](images/step_2.png){:width="300px"}

</div>
</div>

--- task ---

Otwórz szablon projektu [ ](https://editor.raspberrypi.org/en/projects/rocket-launch-starter){:target="_blank"}.

### Utwórz ekran

--- /task ---

Użyjesz zmiennej ` screen_`, aby ustawić rozmiar ekranu i w obliczeniach. Zmienne zdefiniowane funkcje zewnętrzne to ** global **, więc możesz ich używać w dowolnym miejscu w swoim programie.

--- task ---

Znajdź komentarz ` Konfiguracja zmiennych ` i dodaj wiersz kodu, aby utworzyć zmienną ` screen_`:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 8
---

# Ustaw zmienne globalne
screen_size = 400

--- /code ---

--- /task ---

--- task ---

Użyj zmiennej ` screen_` , aby utworzyć kwadrat 400 na 400 pikseli:

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 18
line_highlights: 20
---

def setup():   
# Ustaw swoją animację tutaj    
rozmiar(screen_size, screen_size)


--- /code ---

--- /task ---

### Wybierz obraz

--- task ---

Projekt startowy ma trzy różne obrazy planet i księżyc dla Ciebie. Możesz je wyświetlić w galerii obrazów **.** po lewej stronie edytora kodu.

![Zrzut ekranu edytora kodu z podświetloną galerią obrazów zawierającą obrazy planet i księżyca.](images/image_gallery.png)

** Wybierz:** Zdecyduj, którego obrazu chcesz użyć i zanotuj nazwę pliku. Na przykład: ` orange_`.

--- /task ---

--- task ---

Dodaj kod do funkcji ` setup()`, aby załadować i ustawić obraz.

Linia ` image_mode(CENTER)` mówi, że będziesz pozycjonować obrazy, podając współrzędne środka obrazu (zamiast lewego górnego rogu).

Następnie załaduj swój obraz do globalnej zmiennej ` `. Zmienna musi być globalna, więc możesz jej użyć później podczas rysowania planety na ekranie.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 18
line_highlights: 21-23
---

def setup():   
# Ustaw swoją animację tutaj    
rozmiar(screen_size, screen_size)   
Image_mode(CENTER) # ustawia obraz na środku globalna planeta    
planeta = load_image('planet.png') # wybrana planeta


--- /code ---

--- /task ---

### Narysuj tło

--- task ---

Zdefiniuj funkcję ` draw_background()`, aby narysować tło pod komentarzem, który powie, gdzie powinno się udać.

Użyj ` background(0)`, aby ustawić kolor tła na czarny i dodać funkcję ` image()`, aby narysować planetę. Funkcja ` image()` jest podzielona:

`image(nazwa pliku obrazu, współrzędna x, współrzędna y, szerokość_obrazu, wysokość_obrazu)`

Linia kodu ` z importu p5 *` daje globalne zmienne ` ` i ` ` w zależności od rozmiaru ekranu. Użyj ich w swoim kodzie, aby umieścić planetę w połowie poprzek (szerokość ` / 2 `) i u dołu (wysokość ` `) ekranu.

--- code ---
---
language: python filename: main.py — draw_background() line_numbers: true line_number_start: 14
line_highlights: 15-17
---

# Pojawi się tutaj funkcja draw_background
def draw_background():   
background(0) # Krótkie dla tła(0, 0, 0) —     
Image(planeta, szerokość/2, wysokość, 300, 300) # Rysuj obraz


--- /code ---

Umieszczenie całego kodu do rysowania tła w jednej funkcji ułatwia zrozumienie kodu.

--- /task ---

--- task ---

Aby wyświetlić tło, wywołaj ` draw_background()` in ` draw()`. Spowoduje to ponowne narysowanie tła za każdym razem, gdy zostanie wywołany ` losw()`, zakrywając każdy starszy rysunek:

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 28
line_highlights: 30
---

def draw():   
# rzeczy do zrobienia w każdej ramce     
draw_background()

--- /code ---

--- /task ---

--- task ---

** Test:** Uruchom swój kod i sprawdź, czy rysuje czarne tło z połową planety na dole.

--- /task ---

Jeśli masz konto Raspberry Pi, w edytorze kodu możesz kliknąć przycisk ** Saved ** , aby zapisać kopię swojego projektu w swoich projektach.

--- save ---
