## Questionnaire rapide

Réponds aux trois questions. Il y a des indices pour te guider vers la bonne réponse.

Lorsque tu as répondu à chaque question, clique sur **Vérifier ma réponse**.

Amuse-toi bien !

--- question ---
---
legend : Question 1 sur 3
---

Quel résultat t'attendrais-tu si tu exécutais le programme ci-dessous ?

```python
for i in range(5):
  print("Looping", i)
```

--- choices ---

- ( ) Looping 1 <br> Looping 2 <br> Looping 3 <br> Looping 4 <br> Looping 5

  --- feedback ---

Pas tout à fait, une boucle `for` en Python répète son code une fois pour chaque élément dans une séquence qui lui est donnée, et ici `range` crée une séquence à partir de `0`.

  --- /feedback ---

- ( ) i <br> i <br> i <br> i <br> i

  --- feedback ---

Pas tout à fait, la **variable de boucle** d'une boucle `for` - dans ce cas `i` - contient la valeur actuelle de la séquence sur laquelle la boucle travaille.

  --- /feedback ---

- (x) Looping 0 <br> Looping 1 <br> Looping 2 <br> Looping 3 <br> Looping 4

  --- feedback ---

Correct. La boucle s'exécute une fois, dans l'ordre, pour chaque élément `i` dans la plage [0, 1, 2, 3, 4].

  --- /feedback ---

- ( ) Looping 4 <br> Looping 3 <br> Looping 2 <br> Looping 1 <br> Looping 0

  --- feedback ---

Not quite. Unless you have specified otherwise, a `for` loop will start at 0 and count up the number of times specified in the range.

  --- /feedback ---

--- /choices ---

--- /question ---
