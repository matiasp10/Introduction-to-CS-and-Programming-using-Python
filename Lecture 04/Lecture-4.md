# 1. Iteración sobre Secuencias con Bucles

## Bucles sobre Rangos Numéricos
- Python permite iterar sobre secuencias numéricas usando la función `range()`
- Variantes de uso:
  ```python
  # Del 0 al 4
  for i in range(5):
      print(i)
      
  # Del 2 al 9
  for i in range(2, 10):
      print(i)
      
  # Del 0 al 10, de 2 en 2 (números pares)
  for i in range(0, 11, 2):
      print(i)
  ```

## Bucles sobre Strings (Cadenas de Texto)
- Los strings son secuencias de caracteres que pueden recorrerse carácter por carácter
- Ejemplos:
  ```python
  palabra = "Python"
  
  # Iteración directa sobre caracteres
  for letra in palabra:
      print(letra)
      
  # Iteración usando índices
  for i in range(len(palabra)):
      print(f"En posición {i} está la letra: {palabra[i]}")
  ```

## Técnicas de Procesamiento de Strings en Bucles
- **Conteo de caracteres específicos**:
  ```python
  texto = "Mississippi"
  contador_s = 0
  for letra in texto:
      if letra == 's':
          contador_s += 1
  print(f"La letra 's' aparece {contador_s} veces")  # Resultado: 4
  ```

- **Búsqueda de patrones**:
  ```python
  frase = "programación en python"
  if 'python' in frase:
      print("La palabra 'python' está en la frase")
  ```

- **Acumulación de resultados**:
  ```python
  nombre = "Ana Bell"
  mayúsculas = ""
  for c in nombre:
      if c.isupper():
          mayúsculas += c
  print(mayúsculas)  # Resultado: "AB"
  ```

# 2. Algoritmo de Guess-and-Check (Conjetura y Verificación)

## Concepto Básico
- Es una técnica de resolución de problemas que consiste en:
  1. Realizar una conjetura sobre la posible solución
  2. Verificar si la conjetura resuelve el problema
  3. Si no resuelve, hacer otra conjetura y repetir

## Aplicación en Programación
- Se implementa frecuentemente usando bucles
- Útil cuando el espacio de búsqueda es finito y manejable

## Ejemplo: Buscar la Raíz Cuadrada
```python
# Buscar la raíz cuadrada entera de un número
n = 25
resultado = 0

# Probamos desde 0 hasta n
while resultado * resultado < n:
    resultado += 1

if resultado * resultado == n:
    print(f"La raíz cuadrada de {n} es {resultado}")
else:
    print(f"{n} no tiene una raíz cuadrada exacta")
```

## Ejemplos de Problemas Adecuados para Guess-and-Check
- Encontrar divisores de un número
- Buscar valores que satisfagan una ecuación
- Determinar si un número es primo
- Buscar subcadenas dentro de un texto

## Enumeración Exhaustiva
- Prueba sistemáticamente todas las posibles soluciones
- Garantiza encontrar la solución si existe
- Puede ser ineficiente para espacios de búsqueda grandes

## Limitaciones
- Ineficiente para problemas con muchas posibles soluciones
- Puede llevar a tiempos de ejecución muy largos
- No viable cuando el espacio de búsqueda es infinito

# 3. Números Binarios

## Concepto Básico
- Sistema numérico de base 2 (usa solo 0 y 1)
- Fundamental para entender cómo las computadoras almacenan y procesan información
- Cada posición representa una potencia de 2

## Representación Binaria
- Posiciones en representación binaria (de derecha a izquierda):
  - 2⁰ = 1
  - 2¹ = 2
  - 2² = 4
  - 2³ = 8
  - 2⁴ = 16
  - ...

## Conversión de Decimal a Binario
- Método de división sucesiva por 2:
  1. Dividir el número por 2
  2. Registrar el residuo (0 o 1)
  3. Continuar con el cociente
  4. Leer los residuos de abajo hacia arriba

### Ejemplo: Convertir 13 a binario
```
13 ÷ 2 = 6 con residuo 1
6 ÷ 2 = 3 con residuo 0
3 ÷ 2 = 1 con residuo 1
1 ÷ 2 = 0 con residuo 1
```
Resultado: 13₁₀ = 1101₂

## Conversión de Binario a Decimal
- Sumar el valor de cada posición multiplicado por su dígito:
  - 1101₂ = 1×2³ + 1×2² + 0×2¹ + 1×2⁰
  - 1101₂ = 8 + 4 + 0 + 1 = 13₁₀

## Implementación en Python
```python
# Conversión de decimal a binario
def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero //= 2
    
    return binario

# Ejemplo de uso
num = 13
print(f"{num} en binario es {decimal_a_binario(num)}")  # Resultado: 1101
```

## Importancia en Computación
- Las computadoras almacenan y procesan toda la información en binario
- Entender la representación binaria es fundamental para:
  - Comprender cómo se almacenan diferentes tipos de datos
  - Analizar cuestiones de precisión en operaciones aritméticas
  - Entender algoritmos de bajo nivel
  - Comprender técnicas de manipulación de bits

## Conexión con el Próximo Algoritmo (Búsqueda Binaria)
- La Dra. Bell menciona que comprender los números binarios ayudará a entender el próximo algoritmo (búsqueda binaria)
- La búsqueda binaria es un algoritmo eficiente para encontrar elementos en colecciones ordenadas
- Utiliza el principio de "dividir y conquistar", similar a la representación posicional binaria

# Conclusión

Esta lectura abarca tres conceptos fundamentales:

1. **Bucles sobre secuencias**: Permiten procesar eficientemente colecciones de datos como rangos numéricos y strings.

2. **Guess-and-Check**: Una técnica algorítmica simple pero poderosa para resolver problemas cuando el espacio de soluciones es enumerable.

3. **Números binarios**: Base para entender cómo las computadoras almacenan y procesan la información, y fundamental para comprender algoritmos más avanzados.

Estos conceptos son bloques constructivos esenciales para desarrollar algoritmos más complejos y eficientes, y proporcionan herramientas importantes para resolver una amplia gama de problemas computacionales.