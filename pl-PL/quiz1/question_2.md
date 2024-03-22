
--- question ---
---
legend: Pytanie 2 z 3
---

Projekt ma ten kod ` `, aby załadować obraz planety i powiedzieć, że obrazy powinny być umieszczone w ich środku:

--- code ---
---
language: python
---

def setup():   
size(400, 400)   
image_mode(CENTER)   
global    
planet = load_image('planet.png')

--- /code ---

Współrzędne zaczynają się od (0, 0) w lewym górnym rogu. W projekcie narysowałeś obrazy planet i rakiet za pomocą funkcji ` image(image_file, x-coord, y-coord, x-width, y-width)` .

Gdzie ten kod będzie umieszczał obraz planety?

--- code ---
---
language: python
---

obraz(planeta, 300, 100, 128, 128)

--- /code ---

--- choices ---

- ( ) ![Obraz planety ustawiony poziomo z prawej strony ekranu i pionowo pośrodku.](images/planet400200.png)

  --- feedback ---

Drugim i trzecim wejściem do funkcji ` image()` są współrzędne ` ` i ` ` dla środka obrazu. Ta planeta ma współrzędne `(400, 200)`.

  --- /feedback ---

- ( ) ![Obraz planety umieszczony pośrodku lewego dolnego kwadrantu.](images/planet100300.png)

  --- feedback ---

Drugim i trzecim wejściem do funkcji ` image()` są współrzędne ` ` i ` ` dla środka obrazu. Ta planeta ma współrzędne `(100, 300)`.

  --- /feedback ---

- (x) ![Obraz planety umieszczony pośrodku prawego górnego kwadrantu.](images/planet300100.png)

  --- feedback ---

Poprawna odpowiedź! Drugim i trzecim wejściem do funkcji ` image()` są współrzędne ` ` i ` ` dla środka obrazu. Ten obraz ma współrzędne (300, 100), więc wynosi 300 (z 400) pikseli od lewej strony dla współrzędnej ` ` i 100 (z 400) pikseli od góry.

  --- /feedback ---

- () ![Obraz planety umieszczony w lewym górnym kwadrancie.](images/planet128128.png)

  --- feedback ---

Czwarte i piąte wejścia określają rozmiar obrazu. Drugim i trzecim wejściem do funkcji ` image()` są współrzędne ` ` i ` ` dla środka obrazu. Ta planeta ma współrzędne `(128, 128)`.

  --- /feedback ---

--- /choices ---

--- /question ---
