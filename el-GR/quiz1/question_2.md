
--- question ---
---
legend: Ερώτηση 2 από 3
---

Ένα έργο έχει αυτόν τον κώδικα `αρχικοποίησης` για να φορτωθεί η εικόνα ενός πλανήτη και για να υποδείξει ότι οι εικόνες πρέπει να τοποθετηθούν στο κέντρο τους:

--- code ---
---
language: python
---

def setup():   
  size(400, 400)   
  image_mode(CENTER)   
  global planet   
  planet = load_image('planet.png')

--- /code ---

Οι συντεταγμένες ξεκινούν από (0, 0) που είναι στην επάνω αριστερή γωνία. Στο έργο σχεδίασες εικόνες πλανήτη και πυραύλου χρησιμοποιώντας τη συνάρτηση `image(αρχείο εικόνας, τετμημένη, τεταγμένη, πλάτος x, ύψος y)`.

Πού θα τοποθετήσει αυτός ο κώδικας την εικόνα του πλανήτη;

--- code ---
---
language: python
---

image(planet, 300, 100, 128, 128)

--- /code ---

--- choices ---

- ( ) ![Μια εικόνα πλανήτη τοποθετημένη οριζόντια στα δεξιά της οθόνης και κάθετα στη μέση.](images/planet400200.png)

  --- feedback ---

Το δεύτερο και τρίτο όρισμα στη συνάρτηση `image()` είναι οι συντεταγμένες `x` και `y` για το κέντρο της εικόνας. Αυτός ο πλανήτης έχει τις συντεταγμένες `(400, 200)`.

  --- /feedback ---

- ( ) ![Μια εικόνα πλανήτη τοποθετημένη στη μέση του κάτω αριστερού τεταρτημορίου.](images/planet100300.png)

  --- feedback ---

Το δεύτερο και τρίτο όρισμα στη συνάρτηση `image()` είναι οι συντεταγμένες `x` και `y` για το κέντρο της εικόνας. Αυτός ο πλανήτης έχει συντεταγμένες `(100, 300)`.

  --- /feedback ---

- (x) ![Μια εικόνα πλανήτη τοποθετημένη στη μέση του πάνω δεξιά τεταρτημορίου.](images/planet300100.png)

  --- feedback ---

Σωστό! Το δεύτερο και τρίτο όρισμα στη συνάρτηση `image()` είναι οι συντεταγμένες `x` και `y` για το κέντρο της εικόνας. Αυτή η εικόνα έχει συντεταγμένες (300, 100), επομένως είναι 300 (από 400) εικονοστοιχεία από τα αριστερά για τις συντεταγμένες `x` και 100 (από 400) εικονοστοιχεία από την κορυφή.

  --- /feedback ---

- () ![Μια εικόνα πλανήτη τοποθετημένη στο επάνω αριστερό τεταρτημόριο.](images/planet128128.png)

  --- feedback ---

Το τέταρτο και η πέμπτο όρισμα δίνουν το μέγεθος της εικόνας. Το δεύτερο και τρίτο όρισμα στη συνάρτηση `image()` είναι οι συντεταγμένες `x` και `y` για το κέντρο της εικόνας. Αυτός ο πλανήτης έχει συντεταγμένες `(128, 128)`.

  --- /feedback ---

--- /choices ---

--- /question ---
