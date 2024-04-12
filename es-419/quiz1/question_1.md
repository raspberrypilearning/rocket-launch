## Prueba Rapida

Contesta las tres preguntas. Hay pistas que te guiaran a la respuesta correcta.

Cuando haya respondido a cada pregunta, haga clic en **Verificar mi respuesta**.

¡Diviértete!

--- question ---
---
legend: Pregunta 1 de 3
---

¿Qué resultado esperarías si ejecutaras el siguiente programa?

```python
for i in range(5):
  print("Bucle", i)
```

--- choices ---

- ( ) Bucle 1 <br> Bucle 2 <br> Bucle 3 <br> Bucle 4 <br> Bucle 5

  --- feedback ---

No exactamente, un bucle `for` en Python repite su código una vez para cada elemento en una secuencia que se le da, y aquí `range` crea una secuencia que comienza en `0`.

  --- /feedback ---

- ( ) Bucle i

  --- feedback ---

No exactamente, la **variable de bucle** de un bucle `for`, en este caso `i`, contiene el valor actual de la secuencia en la que está funcionando el bucle.

  --- /feedback ---

- (x) Bucle 0 <br> Bucle 1 <br> Bucle 2 <br> Bucle 3 <br> Bucle 4

  --- feedback ---

Correcto. El bucle se ejecuta una vez, en orden, para cada elemento `i` en el rango [0, 1, 2, 3, 4].

  --- /feedback ---

- ( ) Bucle 4 <br> Bucle 3 <br> Bucle 2 <br> Bucle 1 <br> Bucle 0

  --- feedback ---

No exactamente, un bucle `for` recorre la secuencia de elementos que se le dan en orden. Debido a que `range()` da una secuencia ordenada desde 0 hasta el número que se pasa, ese es el orden que esperaría ver impreso por este bucle `for`.

  --- /feedback ---

--- /choices ---

--- /question ---
