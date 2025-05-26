# 1. Números de Punto Flotante (Floats)

### Concepto Básico
- Los números de punto flotante (float) representan números decimales en Python
- Se utilizan para cálculos que requieren precisión decimal
- Ejemplos: `3.14`, `2.71828`, `-0.5`

### Representación en Memoria
- **Problema fundamental**: Los floats no pueden representarse exactamente en memoria
- Las computadoras usan el sistema binario (base 2) para almacenar números
- Muchos decimales que son exactos en base 10 son infinitos en base 2
- Ejemplo: El decimal 0.1 en binario es 0.0001100110011... (periódico)

### Errores de Representación
- Debido a la representación limitada, se producen pequeños errores
- Ejemplo práctico:
  ```python
  print(0.1 + 0.2)  # Resultado: 0.30000000000000004 (no exactamente 0.3)
  ```

### Acumulación de Errores
- Las operaciones matemáticas con floats acumulan errores
- **Problema crítico**: Múltiples operaciones magnifican estos errores
- Ejemplo:
  ```python
  suma = 0
  for i in range(1000):
      suma += 0.1
  print(suma)  # El resultado no es exactamente 100
  ```

### Comparación de Floats
- **Regla importante**: Nunca usar `==` para comparar números flotantes
- Solución: Comparar si la diferencia está dentro de un margen aceptable (epsilon)
  ```python
  x = 0.1 + 0.2
  epsilon = 0.0001
  print(abs(x - 0.3) < epsilon)  # True, están "suficientemente cerca"
  ```

# 2. Métodos de Aproximación

### Evolución desde Guess-and-Check
- Los métodos de aproximación extienden la técnica de guess-and-check
- Diferencias principales:
  1. Usan incrementos decimales (floats) en lugar de enteros
  2. Buscan soluciones "suficientemente cercanas" en lugar de exactas

### Aproximación por Incrementos Constantes
- Se usa un pequeño incremento constante para acercarse a la solución
- Más preciso que guess-and-check con enteros, pero más lento

#### Ejemplo: Raíz cuadrada por aproximación
```python
objetivo = 25
epsilon = 0.01
paso = 0.1
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta**2 <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) < epsilon:
    print(f"La raíz cuadrada de {objetivo} es aproximadamente {respuesta}")
else:
    print(f"No se encontró una solución con incremento {paso}")
```

### Criterio de Parada
- En lugar de buscar igualdad exacta, se usa un umbral de error aceptable (epsilon)
- La condición de parada típica es: `abs(guess - target) < epsilon`
- Cuanto menor sea epsilon, más precisa (pero más lenta) será la aproximación

### Problemas Comunes

#### 1. Sobrepasarse de la Solución (Overshooting)
- Si el incremento es demasiado grande, podemos saltar sobre la solución exacta
- Ejemplo: Buscando √2 con incremento 0.5: 1.0, 1.5 (sobrepasa), no encontramos 1.414...
- Solución: Usar incrementos más pequeños

#### 2. Tiempo de Ejecución vs. Precisión
- Incrementos más pequeños dan mayor precisión pero aumentan el tiempo de ejecución
- Ejemplo: Con incremento 0.001 vs. 0.1, la solución es 1000 veces más lenta pero más precisa

# 3. Técnicas Avanzadas de Aproximación

### Búsqueda Biseccional (Binary Search)
- Más eficiente que incrementos constantes
- Divide repetidamente el intervalo de búsqueda a la mitad
- Funciona bien para funciones monótonas (siempre crecientes o decrecientes)

#### Algoritmo:
```python
objetivo = 25
epsilon = 0.01
bajo = 0
alto = objetivo
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo) / 2

print(f"La raíz cuadrada de {objetivo} es aproximadamente {respuesta}")
```

### Análisis de Eficiencia
- Búsqueda por incrementos: O(n) donde n = rango/paso
- Búsqueda biseccional: O(log n) donde n = rango/epsilon
- La búsqueda biseccional es exponencialmente más rápida

# 4. Aplicaciones Prácticas

### Cálculo de Raíces
- Raíz cuadrada, cúbica y de cualquier orden
- Implementación de funciones matemáticas (sqrt, cbrt, etc.)

### Solución de Ecuaciones
- Encontrar raíces de polinomios
- Resolver ecuaciones que no tienen soluciones analíticas

### Optimización
- Encontrar máximos y mínimos de funciones
- Ajuste de modelos a datos experimentales

### Simulaciones Científicas
- Cálculos de física, ingeniería, economía
- Modelado de sistemas complejos

# 5. Buenas Prácticas al Trabajar con Floats

## Uso de Módulos Especializados
- `decimal`: Para operaciones financieras que requieren precisión exacta
- `fractions`: Para trabajar con fracciones exactas
- `numpy`: Para cálculos científicos con mejor manejo de precisión

## Técnicas de Programación
- Elegir un epsilon adecuado para el problema
- Usar tolerancias relativas en lugar de absolutas para números de diferentes magnitudes
- No confiar en la igualdad exacta de floats
- Ser consciente de la posibilidad de errores acumulativos en cálculos complejos

# Conclusión

Esta lección aborda desafíos fundamentales en la computación numérica:

1. **Limitaciones inherentes** en la representación de números decimales en computadoras
2. **Métodos de aproximación** como alternativa a soluciones exactas
3. **Estrategias eficientes** para encontrar soluciones con precisión controlada

Comprender estos conceptos es crucial para desarrollar algoritmos robustos que manejen cálculos numéricos de manera fiable, especialmente en aplicaciones científicas, de ingeniería y financieras donde la precisión es crítica.