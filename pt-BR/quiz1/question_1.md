## Teste rápido

Responda às três perguntas. Existem dicas para guiá-lo para a resposta correta.

Após cada pergunta, pressione **Ver minha resposta**.

Divirta-se!

--- question ---
---
legend: Pergunta 1 de 3
---

Qual resultado você esperaria se executasse o programa abaixo?

```python
for i in range(5):
  print("Ciclo", i)
```

--- choices ---

- ( ) Ciclo 1 <br> Ciclo 2 <br> Ciclo 3 <br> Ciclo 4 <br> Ciclo 5

  --- feedback ---

Não exatamente, um ciclo `for` em Python repete seu código uma vez para cada item em uma sequência que é fornecida, e aqui `range` cria uma sequência começando em `0`.

  --- /feedback ---

- ( ) i <br> i <br> i <br> i <br> i

  --- feedback ---

Não exatamente, a **variável de ciclo** de um ciclo `for` — neste caso `i` — mantém o valor atual da sequência pela qual o ciclo está trabalhando.

  --- /feedback ---

- (x) Ciclo 0 <br> Ciclo 1 <br> Ciclo 2 <br> Ciclo 3 <br> Ciclo 4

  --- feedback ---

Correto. O ciclo é executado uma vez, em ordem, para cada item `i` no intervalo [0, 1, 2, 3, 4].

  --- /feedback ---

- ( ) Ciclo 1 <br> Ciclo 2 <br> Ciclo 3 <br> Ciclo 4 <br> Ciclo 0

  --- feedback ---

Not quite. Unless you have specified otherwise, a `for` loop will start at 0 and count up the number of times specified in the range.

  --- /feedback ---

--- /choices ---

--- /question ---
