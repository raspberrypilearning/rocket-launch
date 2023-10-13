## Απογείωση!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Κάθε φορά που σχεδιάζεται ένα νέο καρέ, ο πύραυλος πρέπει να ανεβαίνει στην οθόνη για να δημιουργήσει ένα εφέ κίνησης.
</div>
<div>

![Ένας πύραυλος που πετά με σταθερή ταχύτητα από το κάτω μέρος προς το επάνω μέρος της οθόνης.](images/fly.gif){:width="300px"}

</div>
</div>

--- task ---

Το αρχικό έργο σου προσφέρει μια εικόνα πυραύλου.

![Εικόνα του πυραύλου στη βιβλιοθήκη εικόνων Trinket.](images/rocket_image.png)

--- /task ---

--- task ---

Πρόσθεσε επίσης κώδικα στη συνάρτηση `setup()` για να φορτώσεις την εικόνα του πύραυλου σε μια καθολική μεταβλητή `rocket`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 20
line_highlights: 24, 26
---

def setup():   
#Ορισμός της κινούμενης εικόνας εδώ   
size(screen_size, screen_size)   
image_mode(CENTER)   
global planet, rocket   
planet = load_image('planet.png')    
rocket = load_image('rocket.png')

--- /code ---

--- /task ---

### Make the rocket fly

Η θέση `y` του πυραύλου θα ξεκινά από το 400 (το ύψος της οθόνης) και στη συνέχεια θα μειώνεται κατά 1 κάθε φορά που σχεδιάζεται ένα νέο καρέ.

--- task ---

Πρόσθεσε μια καθολική μεταβλητή `rocket_y` για να παρακολουθείς τη θέση `y` του πυραύλου.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 9
---

# Ρύθμιση καθολικών μεταβλητών
screen_size = 400    
rocket_y = screen_size #Ξεκινάει από την κάτω πλευρά

--- /code ---

--- /task ---

--- task ---

Όρισε μια συνάρτηση `draw_rocket()` για να αλλάξεις τη θέση του `y` του πυραύλου και σχεδίασέ τον ξανά.

`rocket_y -= 1` είναι ένας πιο σύντομος τρόπος για το `rocket_y = rocket_y - 1`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 11
line_highlights: 12-16
---

# Η συνάρτηση draw_rocket πηγαίνει εδώ
def draw_rocket():


--- /code ---

--- /task ---

--- task ---

Call your new `draw_rocket()` in the `draw()` function so that the rocket gets redrawn every frame.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 33
line_highlights: 37
---

language: python filename: main.py line_numbers: true line_number_start: 34


--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to check that the rocket starts at the bottom of the screen and moves up each frame.

![Animation of the rocket flying half way up the screen.](images/rocket_fly.gif)

--- /task ---

--- save ---
