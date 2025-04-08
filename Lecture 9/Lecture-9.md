# Lambda Functions
- Son funciones anónimas (sin nombre) que se pueden definir en una sola línea
- Útiles cuando necesitas una función simple que se usará una sola vez
- Sintaxis: `lambda parámetros: expresión`
- No requieren la palabra clave `return`, automáticamente devuelven el resultado de la expresión
- Ejemplo: `lambda x, y: x + y` es una función que suma dos números

# Tuples (Tuplas)
- Son secuencias indexables de objetos (similar a las listas)
- **Inmutables**: una vez creadas, no se pueden modificar sus elementos
- No se pueden añadir, eliminar o cambiar elementos
- Sintaxis: se utilizan paréntesis `()`
- Ejemplo: `mi_tupla = (1, 2, "hola", 3.14)`
- Se pueden acceder a los elementos por su índice: `mi_tupla[0]` retorna `1`
- Son útiles para agrupar datos relacionados que no deben cambiar

# Lists (Listas)
- Son secuencias indexables de objetos
- **Mutables**: se pueden modificar sus elementos después de crearlas
- Se pueden añadir, eliminar o cambiar elementos
- Sintaxis: se utilizan corchetes `[]`
- Ejemplo: `mi_lista = [1, 2, "hola", 3.14]`

# Características comunes entre Tuples, Lists y Strings
- **Indexación**: se accede a los elementos mediante índices (que comienzan en 0)
  - `mi_lista[0]`, `mi_tupla[0]`, `"hola"[0]`
- **Slicing** (rebanado): permite obtener subsecuencias
  - `mi_lista[1:3]`, `mi_tupla[1:3]`, `"hola"[1:3]`
- **Iteración**: se pueden recorrer en bucles
  - `for elemento in mi_lista:`, `for elemento in mi_tupla:`, `for char in "hola":`
- **Concatenación**: se pueden unir con el operador `+`
- **Longitud**: se puede obtener con la función `len()`