## Dotarcie na orbitę

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Celem wystrzelenia rakiety jest wypchnięcie satelity na orbitę. 

Orbita jest zakrzywioną ścieżką, którą jeden obiekt pokonuje wokół drugiego ze względu na grawitację.

Rakieta może zmienić kolor, aby pokazać, jak udany był start. 

</div>
<div>

![uruchamia się trzy obrazy obok siebie pokazujące sukces (zielony odcień), przepełnienie (bursztynowy odcień) i niepowodzenie (czerwony odcień).](images/check_orbit.png){:width="400px"}

</div>
</div>

### Narysuj linię orbity

--- task ---

Utwórz dwie nowe zmienne globalne, aby ustawić promień koła orbity i współrzędną ` ` orbity do punktu, do którego centrum rakiety musi dotrzeć, aby wystrzelić satelitę.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 11-12
---

# Ustaw zmienne globalne
screen_size = 400    
rocket_y = screen_   
burn = 100    
orbit _radius = 250    
orbit_y = screen_size - orbit_radius

--- /code ---

--- /task ---

--- task ---

Zaktualizuj funkcję ` draw_background()`, aby narysować elipsę reprezentującą orbitę satelity, do której musi dotrzeć rakieta.

--- code ---
---
language: python filename: main.py - draw_background() line_numbers: true line_number_start: 38
line_highlights: 42-45
---

def draw_background():   
background(0) # Krótkie dla tła(0, 0, 0) —    
obraz(planeta, szerokość/2, wysokość, 300, 300)   

    No_fill() # Wyłącz dowolny
    skok wypełnienia(255) # Ustaw biały skok
    stroke_weight(2)
    elipse(width/2, height, orbit_radius * 2, orbit_radius * 2)

--- /code ---

--- /task ---

--- task ---

Test **:** Uruchom swój program i sprawdź, czy została narysowana biała linia orbity.

![Ekran z planetą i nową linią orbity.](images/draw_orbit.png){:width="300px"}

--- /task ---

### Wystrzel rakietę na orbitę

Rakieta powinna się zatrzymać, gdy dotrze na orbitę satelity — koniec misji.

--- task ---

Zaktualizuj swój kod ` jeśli paliwo >= `, aby sprawdzić, czy rakieta nie dotarła na orbitę.

Możesz użyć instrukcji ` ` in ` `, aby sprawdzić, czy dwa lub więcej warunków są prawdziwe.

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 19
---

# Tutaj pojawi się funkcja draw_rocket
def draw_rocket():   
global rocket_y, paliwo, spalanie

        IF fuel >= spal i ROCKET_y > orbit_y: # Nadal leci

--- /code ---

--- /task ---

--- task ---

** Test:** Uruchom swój projekt i wpisz ` ` jako ilość paliwa. To powinno być dużo paliwa, aby dotrzeć na orbitę. Rakieta powinna przestać się poruszać, gdy osiągnie orbitę.

--- /task ---

### Sprawdź, czy uruchomienie powiodło się

Rakieta powinna być zabarwiona na czerwono, jeśli skończy się jej paliwo, zanim będzie wystarczająco wysoka, aby wystrzelić satelitę.

--- task ---

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 30
line_highlights: 34-35
---

    fill(200, 200, 200, 100)
    for i in range(20):
    elipsa(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))
    
    IF fuel < burn and rocket_y > orbit_y: # Brak paliwa i nie na orbicie
    Tint(255, 0, 0) # Niepowodzenie

--- /code ---

--- /task ---

--- task ---

Test **:** Uruchom swój kod i wpisz ` ` jako ilość paliwa. Sprawdź, czy rakieta zmienia kolor na czerwony, gdy zatrzymuje się poniżej orbity.

![Czerwona rakieta, której zabrakło paliwa przed okrążeniem orbity. Planeta również zmieniła kolor na czerwony.](images/orbit_failure.png){:width="300px"}

O nie, planeta stała się czerwona!

--- /task ---

--- task ---

Funkcja ` tint()` ustawia kolor odcień dla wszystkich rysowanych obrazów, dopóki nie zmienisz odcień lub nie użyjesz ` no_tint()`, aby go wyłączyć.

** Wybierz:** Dodaj połączenie do ` no_tint()` po narysowaniu obrazu, aby planeta nie była zabarwiona na czerwono w następnej klatce — lub zostaw ją, jeśli chcesz, aby planeta zmieniła kolor na czerwony!

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 34
line_highlights: 38
---

    if paliwo < spalanie i rocket_y > orbit_y:
    Tint(255, 0, 0) # Niepowodzenie
    
    Image(rakieta, width/2, rocket_y, 64, 64)
    no_tint() # więc planeta nie jest zabarwiona na czerwono w następnej klatce!


--- /code ---

--- /task ---

--- task ---

Ponownie użyj funkcji ` tint()`, tym razem aby pokolorować rakietę na zielono, jeśli rakieta ma wystarczająco dużo paliwa, aby dotrzeć na orbitę satelity:

--- code ---
---
language: python filename: main.py - draw_rocket() line_numbers: true line_number_start: 34
line_highlights: 36-37
---

    if paliwo < spalanie i rocket_y > orbit_y:
    Tint(255, 0, 0) # Usterka
    elif ROCKET_y <= ORBIT_y:
    Tint(0, 255, 0) # sukces
    
    image(rakieta, width/2, rocket_y, 64, 64)
    no_tint()

--- /code ---

--- /task ---

--- task ---

** Test:** Uruchom swój projekt i wpisz ` ` jako ilość paliwa. Sprawdź, czy Twoja rakieta zmienia kolor na zielony, gdy dotrze do orbity satelity.

![Zielona rakieta, która dotarła do koła orbity i ma paliwo.](images/orbit_success.png){:width="300px"}

--- /task ---

Masz teraz symulację, która może być użyta do pokazania, ile paliwa jest potrzebne jako minimum, aby dotrzeć na orbitę satelity. To świetnie, jednak możesz wziąć ogromną ilość paliwa i nadal odnieść sukces, ale jest to kosztowne i marnotrawstwo!

--- task ---

Zmień warunki w swoim kodzie sukcesu, aby rakieta zmieniła kolor na zielony tylko wtedy, gdy osiągnie orbitę ` ` ma mniej niż 1000 kg paliwa.

Dodaj kod, aby pokolorować rakietę na żółto, jeśli rakieta ma więcej niż 1000 kg paliwa, gdy osiągnie orbitę.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 34
line_highlights: 36, 38-39
---

    if paliwo < spalanie i rocket_y > orbit_y:
    Tint(255, 0, 0) # Usterka
    paliwa elif < 1000 i rocket_y <= orbita_y:
    Tint(0, 255, 0) # Success
    elif fuel >= 1000 and rocket_y <= orbit_y:
    Tint(255, 200, 0) # za dużo paliwa
    
    image(rakieta, width/2, rocket_y, 64, 64)
    No_tint() # więc planeta nie jest zabarwiona w następnej klatce!

--- /code ---

--- /task ---

--- task ---

Test **:** Uruchom swój program kilka razy z różnymi liczbami; na przykład 25000 kg paliwa powinno być ilością potrzebną do obrócenia rakiety na zielono, ale także sprawdź, czy żółty odcień działa, używając większej liczby.

![Żółta rakieta, która dotarła do koła orbity i ma paliwo.](images/orbit_meh.png){:width="300px"}

--- /task ---

--- save ---
