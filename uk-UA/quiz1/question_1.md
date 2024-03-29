## Швидкий тест

Дай відповідь на три запитання. Підказки допоможуть знайти правильну відповідь.

Відповівши на кожне питання, натисни на **Перевірити мою відповідь**.

Розважайся!

--- question ---
---
legend: Питання 1 з 3
---

Якого результату слід очікувати, якщо запустити наведену нижче програму?

```python
for i in range(5):
  print("Зациклення", i)
```

--- choices ---

- ( ) Зациклення 1 <br> Зациклення 2 <br> Зациклення 3 <br> Зациклення 4 <br> Зациклення 5

  --- feedback ---

Не зовсім так. В Python, цикл `for` повторює код один раз для кожного рядка в заданій послідовності, а тут `range` створює послідовність, яка починається з `0`.

  --- /feedback ---

- ( ) Зациклення i

  --- feedback ---

Не зовсім так. **Змінна циклу** з петлі `for` — в даному випадку `i` — зберігає поточне значення із послідовності, яку цикл виконує.

  --- /feedback ---

- (x) Зациклення 0 <br> Зациклення 1 <br> Зациклення 2 <br> Зациклення 3 <br> Зациклення 4

  --- feedback ---

Правильно. Цикл виконується один раз, послідовно, для кожного елемента `i` в діапазоні [0, 1, 2, 3, 4].

  --- /feedback ---

- ( ) Зациклення 4 <br> Зациклення 3 <br> Зациклення 2 <br> Зациклення 1 <br> Зациклення 0

  --- feedback ---

Не зовсім так. Цикл `for` проходить через послідовність заданих йому елементів, по порядку. Оскільки `range()` забезпечує вивід впорядкованої послідовності від 0 до заданого числа, тобто тієї послідовності, яку ти очікуєш отримати при виконанні цього циклу `for`.

  --- /feedback ---

--- /choices ---

--- /question ---
