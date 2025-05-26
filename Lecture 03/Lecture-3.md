# Estructuras de Repetición (Loops)

La Dra. Ana Bell introduce en esta clase dos mecanismos fundamentales para realizar tareas repetitivas en Python: los bucles `while` y los bucles `for`. Estas estructuras son esenciales para la programación y permiten ejecutar bloques de código múltiples veces bajo ciertas condiciones.

# 1. Bucles While

## Concepto básico
- Un bucle `while` ejecuta un bloque de código repetidamente mientras una condición específica sea verdadera
- La condición se evalúa antes de cada iteración
- Si la condición es falsa desde el principio, el bloque no se ejecuta ni una sola vez

## Sintaxis
```python
while condición:
    # Bloque de código a repetir
    # mientras la condición sea True
```

## Características importantes
- **Control de la condición**: Dentro del bucle debe haber código que eventualmente haga que la condición se vuelva falsa
- **Inicialización**: Las variables usadas en la condición deben ser inicializadas antes del bucle
- **Actualización**: Las variables de control deben actualizarse dentro del bucle

## Ejemplo básico
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa contador en cada iteración
```

## Peligro: Bucles infinitos
- Un bucle infinito ocurre cuando la condición nunca se vuelve falsa
- Ejemplo de bucle infinito:
```python
x = 10
while x > 0:
    print(x)
    # Error: olvidamos decrementar x
```
- Para detener un bucle infinito durante la ejecución: `Ctrl+C`

# 2. Bucles For

## Concepto básico
- Los bucles `for` están diseñados para iterar sobre una secuencia de elementos
- A diferencia de `while`, los bucles `for` tienen un número predefinido de iteraciones
- Son generalmente más seguros (menos propensos a bucles infinitos)

## Sintaxis
```python
for variable_iteradora in secuencia:
    # Bloque de código a repetir
    # para cada elemento de la secuencia
```

## Iteración sobre rangos de números

### Función `range()`
- `range(fin)`: Genera números desde 0 hasta fin-1
- `range(inicio, fin)`: Genera números desde inicio hasta fin-1
- `range(inicio, fin, paso)`: Genera números desde inicio hasta fin-1, incrementando de paso en paso

### Ejemplos
```python
# Imprime números del 0 al 4
for i in range(5):
    print(i)

# Imprime números del 2 al 8
for i in range(2, 9):
    print(i)

# Imprime números pares del 0 al 10
for i in range(0, 11, 2):
    print(i)
```

## Iteración sobre cadenas de texto (strings)
- Los strings son secuencias de caracteres, por lo que se pueden recorrer con bucles `for`
- Cada iteración asigna un carácter a la variable iteradora

### Ejemplo
```python
palabra = "Python"
for letra in palabra:
    print(letra)
# Imprime cada letra en una línea separada
```

# 3. Control Adicional de Bucles

## Break
- La instrucción `break` termina el bucle inmediatamente, incluso si la condición sigue siendo verdadera
```python
for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es 5
    print(i)
```

## Continue
- La instrucción `continue` salta a la siguiente iteración sin ejecutar el resto del código en el bloque
```python
for i in range(10):
    if i % 2 == 0:
        continue  # Salta los números pares
    print(i)  # Solo imprime números impares
```

# 4. Bucles Anidados

- Se pueden colocar bucles dentro de otros bucles
- Por cada iteración del bucle externo, el bucle interno se ejecuta completamente
```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

# 5. Patrones Comunes con Bucles

## Acumuladores
```python
suma = 0
for i in range(1, 6):
    suma += i  # Acumula la suma de 1+2+3+4+5
print(suma)  # Imprime 15
```

## Búsqueda
```python
texto = "programación"
for letra in texto:
    if letra == 'a':
        print("¡Encontré una 'a'!")
```

## Conteo
```python
contador = 0
palabra = "Mississippi"
for letra in palabra:
    if letra == 's':
        contador += 1
print(f"La letra 's' aparece {contador} veces")  # Imprime 4
```

# Conclusión

Los mecanismos de bucle son fundamentales en la programación, ya que permiten:
- Procesar grandes cantidades de datos
- Repetir tareas sin duplicar código
- Implementar algoritmos iterativos

Como mencionó la Dra. Bell, es importante practicar mucho estos conceptos para dominarlos adecuadamente. Con práctica, podrás:
- Elegir el tipo de bucle más adecuado para cada situación
- Evitar errores comunes como los bucles infinitos
- Combinar bucles con otras estructuras para resolver problemas complejos

Pronto aprenderás a iterar sobre otras estructuras de datos como listas, diccionarios y archivos, expandiendo significativamente la utilidad de los bucles en tus programas.