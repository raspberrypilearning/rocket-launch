
--- question ---
---
legend: Cwestiwn 2 o 3
---

Mae gan brosiect y cod `setup` hwn i lwytho delwedd o blaned a dweud y dylid lleoli delweddau ar eu canol:

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

Mae'r cyfesurynnau'n dechrau o (0, 0) yn y gornel chwith uchaf. Yn y prosiect, fe wnaethoch chi lunio delweddau o blaned a roced gan ddefnyddio'r swyddogaeth `image(image_file, x-coord, y-coord, x-width, y-width)`.

Ble bydd y cod hwn yn lleoli'r ddelwedd o blaned?

--- code ---
---
language: python
---

image(planet, 300, 100, 128, 128)

--- /code ---

--- choices ---

- ( ) ![Delwedd o blaned wedi'i lleoli'n llorweddol ar dde'r sgrin ac yn fertigol yn y canol.](images/planet400200.png)

  --- feedback ---

Yr ail a'r trydydd mewnbwn i'r swyddogaeth `image()` yw'r cyfesurynnau `x` ac `y` ar gyfer canol y ddelwedd. `(400, 200)` yw cyfesurynnau'r blaned hon.

  --- /feedback ---

- ( ) ![Delwedd o blaned wedi'i lleoli yng nghanol y cwadrant chwith isaf.](images/planet100300.png)

  --- feedback ---

Yr ail a'r trydydd mewnbwn i'r swyddogaeth `image()` yw'r cyfesurynnau `x` ac `y` ar gyfer canol y ddelwedd. `(100, 300)` yw cyfesurynnau'r blaned hon.

  --- /feedback ---

- (x) ![Delwedd o blaned wedi'i lleoli yng nghanol y cwadrant dde uchaf.](images/planet300100.png)

  --- feedback ---

Cywir! Yr ail a'r trydydd mewnbwn i'r swyddogaeth `image()` yw'r cyfesurynnau `x` ac `y` ar gyfer canol y ddelwedd. (300, 100) yw cyfesurynnau'r ddelwedd hon felly mae 300 (allan o 400) picsel o'r chwith ar gyfer y cyfesuryn `x` a 100 (allan o 400) picsel o'r brig.

  --- /feedback ---

- () ![Delwedd o blaned wedi'i lleoli yn y cwadrant chwith uchaf.](images/planet128128.png)

  --- feedback ---

Mae'r pedwerydd a'r pumed mewnbwn yn rhoi maint y ddelwedd. Yr ail a'r trydydd mewnbwn i'r swyddogaeth `image()` yw'r cyfesurynnau `x` ac `y` ar gyfer canol y ddelwedd. `(128, 128)` yw cyfesurynnau'r blaned hon.

  --- /feedback ---

--- /choices ---

--- /question ---
