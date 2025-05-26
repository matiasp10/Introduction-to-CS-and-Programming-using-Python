# 1. Conceptos Fundamentales de Organización de Código

## Descomposición
- **Definición**: División de un problema complejo en componentes más simples y manejables
- **Beneficios**:
  - Facilita la comprensión de problemas complejos
  - Permite trabajar en partes separadas del problema
  - Promueve la reutilización de soluciones
- **Enfoque**: "Divide y vencerás" aplicado a la programación

## Abstracción
- **Definición**: Separación de uso (qué hace) de implementación (cómo lo hace)
- **Principio**: Ocultar detalles innecesarios al usuario
- **Analogía**: Un "caja negra" con interfaces bien definidas
- **Niveles**: La abstracción puede aplicarse a diferentes niveles de complejidad

# 2. Funciones en Python

## Concepto y Propósito
- Las funciones son bloques de código reutilizables que realizan tareas específicas
- Permiten implementar tanto la descomposición como la abstracción
- Proporcionan una manera de organizar el código en unidades lógicas

## Estructura de una Función
```python
def nombre_función(parámetro1, parámetro2, ...):
    """Docstring: descripción de lo que hace la función"""
    # Cuerpo de la función
    # Operaciones y cálculos
    return valor_retorno  # Opcional
```

## Componentes Principales
- **Palabra clave `def`**: Indica el inicio de una definición de función
- **Nombre**: Identificador único para la función
- **Parámetros**: Valores de entrada (0 o más)
- **Docstring**: Documentación que explica qué hace la función (opcional pero recomendado)
- **Cuerpo**: Código que se ejecuta cuando se llama a la función
- **Return**: Valor que la función devuelve al completarse (opcional)

# 3. Parámetros y Argumentos

## Definiciones
- **Parámetros**: Variables usadas en la definición de la función
- **Argumentos**: Valores reales pasados a la función cuando se llama

## Tipos de Parámetros
- **Obligatorios**: Deben ser proporcionados al llamar la función
- **Con valores predeterminados**: Tienen un valor por defecto si no se especifica
  ```python
  def saludar(nombre, mensaje="Hola"):
      return f"{mensaje}, {nombre}"
  ```

## Formas de Pasar Argumentos
- **Posicional**: Basado en el orden de los parámetros
  ```python
  resultado = suma(5, 3)  # 5 es el primer parámetro, 3 es el segundo
  ```
- **Nominal**: Especificando el nombre del parámetro
  ```python
  resultado = suma(b=3, a=5)  # El orden no importa cuando se usan nombres
  ```

# 4. Valor de Retorno y Expresiones

## Concepto de Retorno
- **Instrucción `return`**: Especifica el valor que la función devuelve
- **Comportamiento**: La función termina inmediatamente cuando encuentra `return`
- **Múltiple `return`**: Una función puede tener varios puntos de retorno

## Funciones como Expresiones
- **Principio clave**: Una llamada a función se reemplaza por su valor de retorno
- **Evaluación**: Similar a cómo se evalúan las expresiones matemáticas
- Ejemplo:
  ```python
  def cuadrado(x):
      return x * x
  
  resultado = cuadrado(4) + cuadrado(3)  # Se evalúa como 16 + 9 = 25
  ```

## Funciones sin Return Explícito
- Si no hay instrucción `return`, la función devuelve `None` implícitamente
- `None` es un valor especial que representa "nada" o "sin valor"
- Útil para funciones que realizan acciones pero no necesitan devolver datos

# 5. Ámbito de Variables (Scope)

## Variables Locales
- Definidas dentro de una función
- Solo accesibles dentro de la función donde se definen
- Se crean cuando se llama a la función y se destruyen cuando termina

## Variables Globales
- Definidas fuera de cualquier función
- Accesibles desde cualquier parte del programa
- Se mantienen durante toda la ejecución del programa

## Reglas de Ámbito
- Una función puede acceder a variables globales
- Si una función define una variable con el mismo nombre que una global, la local tiene precedencia
- Para modificar una variable global dentro de una función, se debe usar la palabra clave `global`

# 6. Diseño de Funciones Efectivas

## Principios de Diseño
- **Una tarea, una función**: Cada función debe realizar una sola tarea bien definida
- **Cohesión**: Todas las operaciones dentro de la función deben estar relacionadas
- **Acoplamiento bajo**: Minimizar dependencias entre funciones

## Buenas Prácticas
- **Nombres descriptivos**: Usar nombres que indiquen claramente lo que hace la función
- **Documentación**: Incluir docstrings que expliquen el propósito, parámetros y valor de retorno
- **Manejo de errores**: Anticipar y manejar posibles errores o casos límite
- **Tamaño adecuado**: Las funciones no deben ser demasiado largas (principio de descomposición)

# 7. Beneficios de Usar Funciones

## Reutilización de Código
- Escribir una vez, usar muchas veces
- Evita duplicación de código

## Facilidad de Mantenimiento
- Aislar cambios a partes específicas del programa
- Facilita la corrección de errores

## Pruebas Unitarias
- Probar funciones individualmente
- Verificar comportamiento correcto de manera aislada

## Legibilidad del Código
- Organización más clara y estructurada
- Nombres de funciones que describen comportamientos

# 8. Ejemplos Prácticos

## Ejemplo 1: Función Simple
```python
def es_par(numero):
    """Determina si un número es par."""
    return numero % 2 == 0

# Uso
if es_par(42):
    print("Es par")
```

## Ejemplo 2: Función con Múltiples Parámetros
```python
def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números."""
    return sum(numeros) / len(numeros)

# Uso
notas = [85, 90, 78, 92, 88]
promedio = calcular_promedio(notas)
print(f"El promedio es {promedio}")
```

## Ejemplo 3: Descomposición de un Problema
```python
def calcular_área_círculo(radio):
    """Calcula el área de un círculo dado su radio."""
    return 3.14159 * radio ** 2

def calcular_volumen_cilindro(radio, altura):
    """Calcula el volumen de un cilindro dados su radio y altura."""
    área_base = calcular_área_círculo(radio)
    return área_base * altura

# Uso
volumen = calcular_volumen_cilindro(5, 10)
print(f"El volumen del cilindro es {volumen}")
```

# Conclusión

Las funciones son herramientas fundamentales en la programación que implementan los principios de descomposición y abstracción. Permiten:

1. **Organizar el código** en unidades lógicas y manejables
2. **Ocultar detalles de implementación** detrás de interfaces bien definidas
3. **Reutilizar soluciones** a problemas comunes
4. **Tratar llamadas a funciones como expresiones** que se evalúan a un valor específico

Dominar el diseño y uso de funciones es esencial para escribir programas claros, eficientes y mantenibles. La capacidad de pensar en términos de funciones es una habilidad crucial para resolver problemas complejos mediante programación.