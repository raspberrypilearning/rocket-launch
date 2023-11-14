## Quemar combustible

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

Una de las cosas más importantes que hay que decidir al lanzar un cohete es cuánto combustible cargar en él. 

Para hacer esto, debes simular cuánto combustible se quemará en el viaje.
</div>

![El programa con una pregunta en el área de salida preguntando cuánto combustible se requiere.](images/burn_question_full.png){:width="300px"}

</div>

### Crear una variable de combustible

--- task ---

Agrega una variable para realizar un seguimiento de la cantidad de combustible que quema tu cohete (en cuadros).

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 7
line_highlights: 10
---

# Configurar variables globales
screen_size = 400   
rocket_y = screen_size  
burn = 100  # la cantidad de combustible que se usa en cada fotograma

--- /code ---

--- /task ---


--- task ---

En la parte inferior de tu programa, agrega código para preguntarle al usuario cuánto combustible agregar al cohete y almacena su respuesta en una variable global `combustible`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 51
line_highlights: 51
---

combustible = int(input('¿Cuántos kilogramos de combustible quieres usar?'))   
run()

--- /code ---

--- /task ---

### Comprueba el combustible contra lo que se usa

El cohete solo debería moverse si no ha quemado todo su combustible.

--- task ---

Agrega código a la función `dibujar_cohete()` para reducir los `combustible` restantes por los `quemar` de cada cuadro. Use `print()` para mostrar cuánto combustible queda en cada cuadro.

Debes decir que deseas utilizar las variables globales `combustible` y `quemar`.

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 15, 17-18
---

    global rocket_y, fuel, burn   
    rocket_y -= 1   
    fuel -= burn  # Burn fuel   
    print('Fuel left: ', fuel)

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu programa para verificar que la animación no comience hasta que se conteste la pregunta `¿Cuántos kilogramos de combustible deseas usar?`. Intenta ingresar `30000` como la cantidad de combustible.

El cohete seguirá funcionando aunque no le quede combustible.

![El programa con una pregunta en el área de salida que pregunta cuánto combustible se requiere.](images/burn_question.png)

--- /task ---

--- task ---

El cohete solo debe moverse si le queda suficiente combustible. Agrega una declaración `if` para verificar que `combustible >= burn`.

Deberá sangrar todas las líneas de código antes de la llamada a la función `image()`. Para hacer esto, resalta todas las líneas con el mouse y luego toca el <kbd>Tab</kbd> en el teclado para sangrar todas las líneas a la vez.

No es necesario sangrar la línea `image()` porque siempre querrás dibujar el cohete.

--- code ---
---
language: python filename: main.py — draw_rocket() line_numbers: true line_number_start: 15
line_highlights: 17-30
---

    global rocket_y, fuel, burn  
    
    if fuel >= burn:  # Todavía tengo combustible
        rocket_y -= 1   
        fuel -= burn   
        print('Combustible restante: ', fuel)   
    
        no_stroke()  # apaga el trazado
    
        for i in range(25):   
            fill(255, 255 - i*10, 0)   
            ellipse(width/2, rocket_y + i, 8, 3)    
    
        fill(200, 200, 200, 100)   
        for i in range(20):   
            ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))   
    
    image(rocket, width/2, rocket_y, 64, 64)

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu programa para comprobar que el cohete se detiene cuando no le queda combustible.

![Imagen de un cohete en el centro de la pantalla con la declaración "Combustible restante: 0".](images/burn_empty.png){:width="300px"}

--- /task ---

¿Tu cohete se detuvo cuando se quedó sin combustible? ¡Bien hecho, enviaste un cohete al espacio exterior!

--- save ---

