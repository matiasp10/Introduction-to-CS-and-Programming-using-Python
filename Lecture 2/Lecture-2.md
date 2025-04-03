# Resumen Completo: "Strings, Input/Output, y Branching" en Python

## 1. Strings (Cadenas de texto)

### Concepto básico
- Los strings son un nuevo tipo de dato en Python, diferente de los números
- Representan secuencias de caracteres (letras, números, símbolos, espacios)
- Se definen usando comillas simples (`'texto'`) o dobles (`"texto"`)

### Indexación de strings
- Cada carácter en un string tiene una posición o índice
- **Importante**: La indexación comienza en 0, no en 1
- Ejemplos:
  ```python
  s = "Python"
  # P está en el índice 0
  # y está en el índice 1
  # n está en el índice 5
  ```
- Para acceder a un carácter: `s[índice]` (ej. `s[0]` devuelve 'P')

### Slicing (rebanado)
- Permite extraer porciones de un string usando la sintaxis `s[inicio:fin]`
- El carácter en la posición `inicio` se incluye, pero el carácter en `fin` no
- Ejemplos:
  ```python
  s = "Python"
  s[0:2]  # Devuelve "Py"
  s[2:6]  # Devuelve "thon"
  s[:3]   # Desde el inicio hasta índice 2: "Pyt"
  s[3:]   # Desde índice 3 hasta el final: "hon"
  ```

### Operaciones con strings
- Concatenación: `"Hola" + " " + "mundo"` → "Hola mundo"
- Repetición: `"Py" * 3` → "PyPyPy"
- Longitud: `len("Python")` → 6

## 2. Input (Entrada)

### Comando `input()`
- Permite recibir datos del usuario durante la ejecución del programa
- Sintaxis: `input("Mensaje opcional: ")`
- **Crucial**: Todo lo que se recibe mediante `input()` es un string

### Conversión de tipos
- Para trabajar con números ingresados por el usuario, es necesario convertirlos:
  ```python
  edad_str = input("Ingresa tu edad: ")  # Recibe "25" como string
  edad = int(edad_str)  # Convierte "25" al número entero 25
  ```
- Funciones de conversión comunes:
  - `int()`: Convierte a entero
  - `float()`: Convierte a número decimal
  - `str()`: Convierte a string

## 3. Output (Salida)

### Comando `print()`
- Muestra información en la consola/terminal
- Sintaxis: `print(valor1, valor2, ...)` 
- Puede mostrar múltiples valores separados por comas
- En archivos `.py`, solo se ven los resultados de lo que se imprime con `print()`

### Características de `print()`
- Concatena automáticamente los valores con espacios
- Añade un salto de línea al final por defecto
- Parámetros opcionales:
  - `sep`: Cambia el separador entre valores (por defecto es espacio)
  - `end`: Cambia el carácter final (por defecto es salto de línea)
  ```python
  print("Hola", "mundo", sep="-")  # Imprime: Hola-mundo
  print("Hola", end="! ")  # Imprime: Hola! (sin salto de línea)
  ```

## 4. Branching (Ramificación)

### Concepto
- Permite que el programa tome decisiones y ejecute diferentes bloques de código según las condiciones
- Las estructuras de control permiten alterar el flujo secuencial del programa

### Estructura `if`
- Ejecuta un bloque de código solo si la condición es verdadera
```python
if condición:
    # Código a ejecutar si la condición es True
```

### Estructura `if-else`
- Proporciona una alternativa cuando la condición es falsa
```python
if condición:
    # Código si la condición es True
else:
    # Código si la condición es False
```

### Estructura `if-elif-else`
- Permite evaluar múltiples condiciones en secuencia
- **Importante**: Solo se ejecuta el primer bloque cuya condición sea True
```python
if condición1:
    # Código si condición1 es True
elif condición2:
    # Código si condición2 es True (y condición1 es False)
elif condición3:
    # Código si condición3 es True (y las anteriores son False)
else:
    # Código si todas las condiciones son False
```

### Indentación
- En Python, la indentación (espacios al inicio de línea) define bloques de código
- **Crítico**: La indentación incorrecta causa errores de sintaxis
- Se recomienda usar 4 espacios para cada nivel de indentación
- Todos los comandos con el mismo nivel de indentación pertenecen al mismo bloque

### Operadores de comparación
- `==`: Igual a
- `!=`: Diferente de
- `>`, `<`: Mayor que, menor que
- `>=`, `<=`: Mayor o igual que, menor o igual que

### Operadores lógicos
- `and`: Verdadero si ambas condiciones son verdaderas
- `or`: Verdadero si al menos una condición es verdadera
- `not`: Invierte el valor de verdad

## Ejemplo Integrador

```python
nombre = input("¿Cómo te llamas? ")
edad_str = input("¿Cuántos años tienes? ")
edad = int(edad_str)

print("Hola", nombre + "!")

if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
```

Este resumen abarca todos los conceptos fundamentales presentados en la Lectura 2 del curso de la Dra. Ana Bell, destacando las características esenciales de strings, operaciones de entrada/salida y estructuras de control en Python.