# 1. Desafíos de la Computación Numérica

## Limitaciones en Soluciones Exactas
- Muchos problemas no tienen soluciones numéricas exactas calculables
- Ejemplos:
  - Raíces no exactas (como √2 = 1.4142...)
  - Soluciones de ecuaciones complejas
  - Puntos de intersección de curvas

## El Concepto "Suficientemente Bueno"
- En lugar de buscar soluciones exactas, buscamos aproximaciones aceptables
- Definimos un margen de error tolerable (epsilon)
- Una solución es "suficientemente buena" si está dentro de este margen

## Representación de Punto Flotante
- Los números decimales son almacenados en formato binario
- Muchos decimales exactos en base 10 son periódicos en binario
- Esto crea imprecisiones inherentes al trabajar con floats
- Ejemplo: 0.1 + 0.2 ≠ exactamente 0.3 en la computadora

## Comparación de Números Flotantes
- **Regla fundamental**: Nunca usar `==` para comparar floats
- La práctica correcta es usar un epsilon:
  ```python
  abs(x - y) < epsilon  # Verifica si x e y son "suficientemente cercanos"
  ```
- El valor de epsilon depende del contexto y la precisión requerida

# 2. Búsqueda Biseccional (Bisection Search)

## Concepto Básico
- Algoritmo eficiente para encontrar valores en un rango ordenado
- Divide repetidamente el intervalo de búsqueda a la mitad
- En cada paso, se descarta la mitad del espacio de búsqueda

## Requisitos para Aplicar Búsqueda Biseccional
1. **Dos extremos definidos**: Un rango conocido que contiene la solución
2. **Valores ordenados**: Una función continua o secuencia ordenada
3. **Retroalimentación sobre las conjeturas**: Saber si el valor actual es demasiado alto, bajo o correcto

## Algoritmo General
```python
bajo = valor_mínimo
alto = valor_máximo
respuesta = (bajo + alto) / 2

while no_es_suficientemente_bueno(respuesta):
    if respuesta_es_demasiado_baja:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (bajo + alto) / 2
```

## Ejemplo: Cálculo de Raíz Cuadrada
```python
objetivo = 25
epsilon = 0.01
bajo = 0
alto = objetivo
respuesta = (alto + bajo) / 2
iteraciones = 0

while abs(respuesta**2 - objetivo) >= epsilon:
    iteraciones += 1
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo) / 2
    
print(f"La raíz cuadrada de {objetivo} es aproximadamente {respuesta}")
print(f"Encontrada en {iteraciones} iteraciones")
```

## Eficiencia de la Búsqueda Biseccional
- **Complejidad**: O(log n) donde n = rango/epsilon
- Significativamente más rápida que la búsqueda por incrementos (O(n))
- Ejemplos comparativos:
  - Para encontrar un valor en un rango de 1 millón:
    - Búsqueda lineal: hasta 1,000,000 pasos
    - Búsqueda biseccional: aproximadamente 20 pasos (log₂(1,000,000) ≈ 20)

## Consideraciones Prácticas
- Asegurarse de que la solución está en el rango inicial
- Cuidado con condiciones de parada que puedan causar bucles infinitos
- Definir un epsilon apropiado para el problema

# 3. Método de Newton-Raphson

## Introducción
- Método para encontrar raíces de polinomios de manera aún más eficiente
- Basado en el cálculo diferencial
- Utiliza tangentes para aproximarse rápidamente a la raíz

## Fórmula Básica
Para encontrar la raíz de f(x) = 0:
```
x_{n+1} = x_n - f(x_n)/f'(x_n)
```
Donde:
- x_n es la aproximación actual
- f'(x_n) es la derivada de f en el punto x_n

## Ejemplo: Raíz Cuadrada con Newton-Raphson
Para encontrar √k, buscamos la raíz de f(x) = x² - k

```python
def sqrt_newton(k, epsilon=0.01, max_iter=100):
    """Calcula la raíz cuadrada de k usando el método de Newton."""
    guess = k/2  # Suposición inicial
    iter_count = 0
    
    while abs(guess*guess - k) >= epsilon and iter_count < max_iter:
        # Aplicar fórmula de Newton: x_{n+1} = x_n - f(x_n)/f'(x_n)
        # donde f(x) = x^2 - k, f'(x) = 2x
        guess = guess - (guess**2 - k)/(2*guess)
        iter_count += 1
    
    return guess, iter_count
```

## Ventajas de Newton-Raphson
- Convergencia cuadrática (muy rápida cerca de la solución)
- Menos iteraciones que la búsqueda biseccional para el mismo nivel de precisión
- Especialmente eficiente para funciones "bien comportadas"

## Limitaciones de Newton-Raphson
- Requiere conocer y calcular la derivada de la función
- Puede diverger o comportarse erráticamente para ciertas funciones
- Sensible a la elección del punto inicial
- Problemas con puntos donde f'(x) = 0 o cercano a cero

# 4. Comparación de Métodos de Aproximación

## Método de Incremento Constante
- **Ventajas**: Simple de implementar, funciona para cualquier función
- **Desventajas**: Muy lento, complejidad O(n)
- **Mejor para**: Comprensión inicial, funciones muy irregulares

## Búsqueda Biseccional
- **Ventajas**: Rápida (O(log n)), garantiza convergencia si la solución existe en el rango
- **Desventajas**: Requiere un rango inicial que contenga la solución
- **Mejor para**: La mayoría de problemas prácticos, especialmente con grandes rangos

## Newton-Raphson
- **Ventajas**: Extremadamente rápido cerca de la solución (convergencia cuadrática)
- **Desventajas**: Requiere derivadas, sensible a condiciones iniciales
- **Mejor para**: Polinomios y funciones bien comportadas cuando se necesita alta precisión

# 5. Aplicaciones Prácticas

## Raíces de Polinomios
- Ecuaciones algebraicas complejas
- Soluciones numéricas cuando no existen fórmulas analíticas

## Modelado Computacional
- Simulaciones físicas
- Modelos económicos y financieros

## Inteligencia Artificial y Aprendizaje Automático
- Optimización de funciones de costo
- Entrenamiento de modelos mediante descenso de gradiente (relacionado con Newton-Raphson)

## Gráficos por Computadora
- Intersección de rayos con superficies
- Cálculo de puntos de colisión en simulaciones

# Conclusión

La clase sobre Búsqueda Biseccional y métodos de aproximación presenta conceptos fundamentales para la resolución de problemas numéricos:

1. **Aceptación de aproximaciones**: Muchos problemas requieren soluciones "suficientemente buenas" en lugar de exactas.

2. **Limitaciones de punto flotante**: Es crucial entender las imprecisiones inherentes a la representación binaria de decimales.

3. **Eficiencia algorítmica**: La búsqueda biseccional ofrece un rendimiento exponencialmente mejor que métodos lineales.

4. **Métodos avanzados**: Newton-Raphson proporciona convergencia aún más rápida para ciertos tipos de problemas.

Estos conceptos son esenciales en ciencias de la computación ya que forman la base de numerosos algoritmos utilizados en aplicaciones reales que requieren cálculos numéricos eficientes y precisos.