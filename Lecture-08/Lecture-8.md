# 1. Funciones como Objetos de Primera Clase

## Concepto Fundamental
- En Python, las funciones son "objetos de primera clase" (first-class objects)
- Esto significa que las funciones son tratadas como cualquier otro objeto (números, strings, listas)
- Pueden ser manipuladas dinámicamente durante la ejecución del programa

## Características de Funciones como Objetos
- **Tienen un tipo**: `<class 'function'>`
  ```python
  def saludar():
      print("Hola")
  
  print(type(saludar))  # Muestra: <class 'function'>
  ```

- **Pueden ser asignadas a variables**
  ```python
  def sumar(a, b):
      return a + b
  
  operacion = sumar  # Asignamos la función (sin llamarla) a una variable
  resultado = operacion(5, 3)  # Equivalente a sumar(5, 3)
  print(resultado)  # Muestra: 8
  ```

- **Pueden ser pasadas como argumentos a otras funciones**
  ```python
  def aplicar_operacion(func, x, y):
      return func(x, y)
  
  def multiplicar(a, b):
      return a * b
  
  resultado = aplicar_operacion(multiplicar, 4, 5)  # Pasamos la función como parámetro
  print(resultado)  # Muestra: 20
  ```

- **Pueden ser devueltas como valores de retorno**
  ```python
  def crear_sumador(n):
      def sumador(x):
          return x + n
      return sumador
  
  sumar_cinco = crear_sumador(5)  # Recibimos una función que suma 5
  print(sumar_cinco(10))  # Muestra: 15
  ```

# 2. Entornos (Environments) y Alcance de Variables

## Concepto de Entorno
- Un entorno es un contexto que contiene variables y sus valores
- Cada función crea un nuevo entorno temporal cuando se ejecuta

## Entorno Global vs. Entorno Local
- **Entorno Global**: Donde se ejecuta el programa principal
  - Variables definidas fuera de cualquier función
  - Accesibles desde cualquier parte del programa

- **Entorno Local**: Creado cuando se llama a una función
  - Variables definidas dentro de la función
  - Solo existen durante la ejecución de la función
  - Se destruyen cuando la función termina

## Reglas de Búsqueda de Variables
- Cuando se accede a una variable, Python busca:
  1. Primero en el entorno local actual
  2. Luego en los entornos de funciones que envuelven la actual (closures)
  3. Finalmente en el entorno global
  4. Si no se encuentra, se levanta un error `NameError`

## Ejemplo de Entornos Anidados
```python
x = 10  # Variable global

def outer_func():
    y = 5  # Variable local a outer_func
    
    def inner_func():
        z = 3  # Variable local a inner_func
        print(x, y, z)  # Puede acceder a x (global), y (del entorno que la envuelve) y z (local)
    
    inner_func()
    # print(z)  # Esto causaría error, z no existe en este entorno

outer_func()
```

# 3. Closures (Clausuras)

## Concepto de Closure
- Una closure es una función que recuerda el entorno en el que fue creada
- Permite que una función tenga acceso a variables de la función externa que la creó
- Útil para crear funciones "personalizadas" o "configurables"

## Ejemplo Detallado
```python
def crear_contador():
    contador = 0  # Variable en el entorno de crear_contador
    
    def incrementar():
        nonlocal contador  # Indica que contador no es local a incrementar
        contador += 1
        return contador
    
    return incrementar  # Devuelve la función incrementar

mi_contador = crear_contador()
print(mi_contador())  # 1
print(mi_contador())  # 2
print(mi_contador())  # 3
```

## Aplicaciones de Closures
- Funciones personalizadas basadas en parámetros
- Memorización de resultados (caching)
- Implementación de comportamiento con estado

# 4. Funciones de Orden Superior

## Definición
- Funciones que toman otras funciones como argumentos o devuelven funciones
- Permiten abstraer patrones de comportamiento y crear código más modular

## Ejemplos Comunes

#### Map: Aplicar una función a cada elemento de una secuencia
```python
def cuadrado(x):
    return x * x

numeros = [1, 2, 3, 4, 5]
cuadrados = map(cuadrado, numeros)  # Aplica cuadrado a cada número
print(list(cuadrados))  # [1, 4, 9, 16, 25]
```

#### Filter: Filtrar elementos de una secuencia según una condición
```python
def es_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]
pares = filter(es_par, numeros)  # Conserva solo los números pares
print(list(pares))  # [2, 4, 6]
```

#### Reduce: Acumular valores aplicando una función
```python
from functools import reduce

def sumar(a, b):
    return a + b

numeros = [1, 2, 3, 4, 5]
suma = reduce(sumar, numeros)  # Suma todos los valores
print(suma)  # 15
```

# 5. Funciones Lambda (Anónimas)

## Definición
- Funciones pequeñas, de una sola expresión, definidas sin nombre
- Útiles cuando necesitamos una función simple por un breve período
- Sintaxis: `lambda argumentos: expresión`

## Ejemplos
```python
# Función lambda que calcula el cuadrado
cuadrado = lambda x: x * x
print(cuadrado(5))  # 25

# Uso de lambda con map
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x * x, numeros)
print(list(cuadrados))  # [1, 4, 9, 16, 25]

# Uso de lambda con sort (para ordenar)
pares = [(1, 'uno'), (3, 'tres'), (2, 'dos')]
pares.sort(key=lambda par: par[0])  # Ordenar por el primer elemento
print(pares)  # [(1, 'uno'), (2, 'dos'), (3, 'tres')]
```

# 6. Decoradores

## Concepto
- Funciones que modifican el comportamiento de otras funciones
- Implementadas mediante el concepto de funciones de orden superior
- Sintaxis especial con `@nombre_decorador`

## Ejemplo Básico
```python
def decorador_simple(funcion):
    def wrapper():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    return wrapper

@decorador_simple
def saludar():
    print("¡Hola!")

saludar()
# Imprime:
# Antes de llamar a la función
# ¡Hola!
# Después de llamar a la función
```

## Aplicaciones de Decoradores
- Registro de llamadas a funciones (logging)
- Medición de tiempo de ejecución
- Verificación de precondiciones
- Control de acceso/autenticación

# 7. Beneficios de Tratar Funciones como Objetos

## Código Más Conciso
- Evita repetición de código similar
- Permite abstraer patrones de comportamiento

## Mayor Legibilidad
- Separa conceptos en funciones especializadas
- Expresa intenciones de forma más clara

## Flexibilidad
- Facilita la modificación y extensión del código
- Permite comportamiento dinámico en tiempo de ejecución

## Reusabilidad
- Componentes reutilizables para diferentes partes del programa
- Bibliotecas bien diseñadas con funciones de orden superior

# 8. Ejemplos Prácticos Complejos

## Ejemplo 1: Función que genera funciones especializadas
```python
def crear_multiplicador(factor):
    """Crea una función que multiplica por un factor específico."""
    return lambda x: x * factor

duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

print(duplicar(5))   # 10
print(triplicar(5))  # 15
```

## Ejemplo 2: Función que acepta múltiples operaciones
```python
def procesar_datos(datos, operaciones):
    """Aplica una serie de operaciones a los datos."""
    resultado = datos
    for operacion in operaciones:
        resultado = operacion(resultado)
    return resultado

datos = [1, 2, 3, 4, 5]
operaciones = [
    lambda x: [i * 2 for i in x],           # Duplicar cada elemento
    lambda x: [i for i in x if i > 5],      # Filtrar elementos > 5
    lambda x: sum(x)                        # Sumar los elementos
]

resultado = procesar_datos(datos, operaciones)
print(resultado)  # 16 (suma de [6, 8, 10] que son los números > 5 después de duplicar)
```

# Conclusión

El tratamiento de funciones como objetos de primera clase en Python es un concepto poderoso que:

1. **Amplía las posibilidades de diseño de programas** permitiendo mayor abstracción y modularidad
2. **Facilita la creación de código más conciso y legible** al separar comportamientos en funciones especializadas
3. **Permite técnicas avanzadas de programación** como closures, decoradores y funciones de orden superior
4. **Requiere comprensión de entornos y alcance de variables** para evitar errores sutiles

Estos conceptos no solo son fundamentales para Python, sino que representan paradigmas de programación funcional que pueden encontrarse en muchos lenguajes modernos, permitiendo escribir código más elegante, mantenible y expresivo.