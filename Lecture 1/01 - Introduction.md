un ordenador hace dos cosas, y sólo dos: realiza **cálculos** y __recuerda__ los resultados de esos cálculos. Pero hace esas dos cosas extremadamente bien.

# Pensamiento computacional

Todo conocimiento puede considerarse declarativo o imperativo.

- **Declarativo**: se compone de _afirmaciones de hecho_. Por ejemplo, «la raíz cuadrada de x es un número y tal que $y*y = x$ y «es posible viajar en tren de París a Roma». Son afirmaciones de hecho. Por desgracia, no nos dicen nada sobre cómo hallar una raíz cuadrada o cómo viajar en tren de París a Roma.
- **Imperativo**: son _conocimientos «prácticos», o recetas para deducir información_. Herón de Alejandría fue el primero en documentar una forma de calcular la raíz cuadrada de un número. Su método para hallar la raíz cuadrada de un número, llámese $x$, puede resumirse así:

1. Empieza con una suposición, $g$.
2. Si $g*g$ se aproxima lo suficiente a $x$, detente y di que $g$ es la respuesta.
3. En caso contrario, crea una nueva conjetura promediando $g$ y $x/g$, es decir, $(g + x/g)/2$.
4. Utilizando esta nueva suposición, a la que volveremos a llamar $g$, repite el proceso hasta que $g*g$ se acerque lo suficiente a $x$.

Consideremos la búsqueda de la raíz cuadrada de $25$.

1. Establezca $g$ en algún valor arbitrario, por ejemplo, $3$.
2. Decidimos que $3*3 = 9$ no está suficientemente cerca de $25$.
3. Establecemos $g$ en $(3 + 25/3)/2 = 5,67$
4. Decidimos que $5,67*5,67 = 32,15$ sigue sin acercarse lo suficiente a $25$.
5. Fijamos $g$ en $(5,67 + 25/5,67)/2 = 5,04$.
6. Decidimos que $5,04*5,04 = 25,4$ es suficientemente próximo, así que nos detenemos y declaramos que $5,04$ es una aproximación adecuada a la raíz cuadrada de $25$.

> [!NOTE]
> Observe que la descripción del método es una _secuencia de pasos simples_, junto con un _flujo de control_ que especifica cuándo ejecutar cada paso. Una descripción de este tipo se denomina **algoritmo**. 
> El algoritmo que utilizamos para aproximar la raíz cuadrada es un ejemplo de algoritmo "**guess-and-check**" (conjetura y comprobación). Se basa en el hecho de que es fácil comprobar si una conjetura es suficientemente buena o no.

Una definición mas formal de **algoritmo** es: una _lista finita_ de instrucciones que describen un conjunto de cálculos que, cuando se ejecutan en un conjunto de entradas, pasan por una secuencia de estados bien definidos y finalmente producen una _salida_.

Las primeras máquinas de computación eran, de hecho, **ordenadores de programa fijo**, lo que significa que estaban diseñados para _resolver un problema matemático específico_, por ejemplo, calcular la trayectoria de un proyectil de artillería. 
Uno de los primeros ordenadores (construido en 1941 por Atanasoff y Berry) resolvía sistemas de ecuaciones lineales, pero no podía hacer nada más. La máquina bomba de Alan Turing, desarrollada durante la Segunda Guerra Mundial, fue diseñada para descifrar los códigos Enigma alemanes. 

Algunos ordenadores sencillos siguen utilizando este método. Por ejemplo, _una calculadora de cuatro funciones es un ordenador de programa fijo_. Puede realizar operaciones aritméticas básicas, pero no puede utilizarse como procesador de textos ni para ejecutar videojuegos. Para cambiar el programa de una máquina de este tipo, hay que sustituir los circuitos.

El primer ordenador verdaderamente moderno fue el **Manchester Mark 1**. Se distinguía de sus predecesores por ser un **ordenador de programa almacenado**. Un ordenador de este tipo _almacena_ (y _manipula_) una secuencia de instrucciones y tiene componentes que ejecutan cualquier instrucción de esa secuencia. El corazón de un ordenador de este tipo es un **intérprete** que puede ejecutar cualquier conjunto legal de instrucciones y, por tanto, puede utilizarse para calcular cualquier cosa que pueda describirse utilizando esas instrucciones. El resultado del cálculo puede ser incluso una nueva secuencia de instrucciones, que puede ser ejecutada por el ordenador que las generó. En otras palabras, es posible que un ordenador se programe a sí mismo. 

_Tanto el programa como los datos que manipula residen en la memoria_. Normalmente, un "programa contador" apunta a un lugar concreto de la memoria, y el cálculo comienza ejecutando la instrucción en ese punto. La mayoría de las veces, el intérprete simplemente pasa a la siguiente instrucción de la secuencia, pero no siempre. En algunos casos, realiza una prueba y, basándose en ella, la ejecución puede saltar a otro punto de la secuencia de instrucciones. Esto se llama **flujo de control**, y es esencial para permitirnos escribir programas que realicen tareas complejas.

A veces se utilizan diagramas para representar el flujo de control. Por convención, utilizamos cajas rectangulares para representar un paso del proceso, un rombo para representar una prueba y flechas para indicar el orden en que se hacen las cosas.

Para crear algoritmos, o secuencias de instrucciones, necesitamos un **lenguaje de programación** con el que describirlas, una forma de dar al ordenador sus órdenes de marcha.

En 1936, el matemático británico _Alan Turing_ describió un hipotético dispositivo informático que se le llamo **Máquina Universal de Turing**. La máquina tenía memoria ilimitada en forma de «cinta» en la que se podían escribir ceros y unos, y un puñado de sencillas instrucciones primitivas para mover, leer y escribir en la cinta. La tesis de _Church-Turing_ afirma que **si una función es computable, se puede programar una máquina de Turing para que la compute**.

El «``if``» de la tesis _Church-Turing_ es importante. No todos los problemas tienen soluciones computacionales. Turing demostró, por ejemplo, que es imposible escribir un programa que tome un programa arbitrario como entrada e imprima ``true`` si y sólo si el programa de entrada se ejecuta para siempre. Es lo que se conoce como "**halting problem**" (_problema de la detención_).

La tesis de _Church-Turing_ conduce directamente a la noción de completitud de Turing. Se dice que **un lenguaje de programación es completo de Turing si puede utilizarse para simular una máquina de Turing universal**. Todos los lenguajes de programación modernos son completos de Turing. En consecuencia, _cualquier cosa que pueda programarse en un lenguaje de programación_ (por ejemplo, Python) _puede programarse en cualquier otro lenguaje de programación_ (por ejemplo, Java). Por supuesto, algunas cosas pueden ser más fáciles de programar en un lenguaje concreto, pero todos los lenguajes son fundamentalmente iguales en cuanto a potencia de cálculo.

Afortunadamente, ningún programador tiene que construir programas a partir de las instrucciones primitivas de Turing. En su lugar, los lenguajes de programación modernos ofrecen un conjunto de primitivas más amplio y cómodo. Sin embargo, la idea fundamental de la programación como el proceso de ensamblar una secuencia de operaciones sigue siendo central.

Sea cual sea el conjunto de primitivas que tenga y los métodos que utilice para ensamblarlas, lo mejor y lo peor de la programación es lo mismo: **el ordenador hará exactamente lo que usted le diga que haga, ni más ni menos**. Esto es bueno porque significa que puedes hacer que el ordenador haga todo tipo de cosas divertidas y útiles. Es malo porque _cuando no hace lo que quieres que haga, no tienes a nadie a quien culpar excepto a ti mismo_.

Hay cientos de lenguajes de programación en el mundo. _No existe el mejor lenguaje_. Diferentes lenguajes son mejores o peores para diferentes tipos de aplicaciones. **MATLAB**, por ejemplo, es un buen lenguaje para _manipular vectores y matrices_. **C** es un buen lenguaje para _escribir programas que controlan redes de datos_. **PHP** es un buen lenguaje para _crear sitios web_. Y **Python** es un excelente lenguaje de _propósito general_.

Cada lenguaje de programación tiene un conjunto de **construcciones primitivas**, una **sintaxis**, una **semántica estática** y una **semántica**. Por analogía con un lenguaje natural, como el inglés, las _construcciones primitivas son palabras_, la _sintaxis describe qué cadenas de palabras constituyen oraciones bien formadas_, la _semántica estática define qué oraciones tienen sentido_ y la _semántica define el significado de esas oraciones_. Las construcciones primitivas en Python incluyen literales (por ejemplo, el número ``3.2`` y la cadena ``'abc'``) y operadores infijos (por ejemplo, ``+`` y ``/``).

## Sintaxis

La **sintaxis** de un idioma _define qué cadenas de caracteres y símbolos están bien formadas_. Por ejemplo, en inglés la cadena «``Cat dog boy``.» no es una frase sintácticamente válida, porque la sintaxis inglesa no acepta frases de la forma ``<noun> <noun> <noun>``. En Python, la secuencia de primitivas ``3.2 + 3.2`` está bien formada sintácticamente, pero la secuencia ``3.2 3.2`` no lo está.

## Semántica estática

La **semántica estática** _define qué cadenas sintácticamente válidas tienen un significado_. Consideremos, por ejemplo, las cadenas «``He run quickly``» y «``I runs quickly``». Cada una tiene la forma ``<pronombre> <verbo regular> <adverbio>``, que es una secuencia sintácticamente aceptable.
Sin embargo, ninguna de las dos es válida en inglés, debido a la regla bastante peculiar de que para un verbo regular cuando el sujeto de una frase es primera o segunda persona, el verbo no termina con «``s``», pero cuando el sujeto es tercera persona del singular, sí. Son ejemplos de errores semánticos estáticos.

## Semántica

La **semántica** de una lengua _asocia un significado a cada cadena de símbolos sintácticamente correcta que no tiene errores semánticos estáticos_. En las lenguas naturales, la semántica de una frase puede ser ambigua. Por ejemplo, la frase «No puedo elogiar demasiado a este estudiante» puede ser halagadora o condenatoria. Los lenguajes de programación están diseñados para que cada programa legal tenga exactamente un significado.

Aunque los errores sintácticos son el tipo de error más común (especialmente para quienes están aprendiendo un nuevo lenguaje de programación), son el tipo de error menos peligroso. Todos los lenguajes de programación serios detectan todos los errores sintácticos y no permiten que los usuarios ejecuten un programa con un solo error sintáctico. Además, en la mayoría de los casos el sistema del lenguaje da una indicación lo suficientemente clara de la localización del error como para que el programador sea capaz de solucionarlo sin pensárselo demasiado.

Identificar y resolver errores semánticos estáticos es más complejo. Algunos lenguajes de programación, como Java, realizan muchas comprobaciones semánticas estáticas antes de permitir la ejecución de un programa. Otros, como C y Python (por desgracia), hacen relativamente menos comprobaciones semánticas estáticas antes de que se ejecute un programa. Python realiza una cantidad considerable de comprobaciones semánticas mientras se ejecuta un programa.

Si un programa no tiene errores sintácticos ni errores semánticos estáticos, tiene un significado, es decir, tiene semántica. Por supuesto, puede que no tenga la semántica que su creador pretendía. Cuando un programa significa algo distinto de lo que su creador cree que significa, pueden ocurrir cosas malas.

¿Qué puede ocurrir si el programa tiene un error y se comporta de forma no deseada?

- Puede bloquearse, es decir, dejar de ejecutarse y producir una indicación obvia de que lo ha hecho. En un sistema informático bien diseñado, cuando un programa se bloquea, no daña el sistema en su conjunto. Por desgracia, algunos sistemas informáticos muy populares no tienen esta agradable propiedad. Casi todo el mundo que utiliza un ordenador personal ha ejecutado alguna vez un programa que ha conseguido que sea necesario reiniciar todo el sistema.
- Puede que siga ejecutándose, y ejecutándose, y ejecutándose, y nunca se detenga. Si no tienes ni idea de cuánto tiempo se supone que tarda el programa en hacer su trabajo, esta situación puede ser difícil de reconocer.
- Es posible que se ejecute hasta el final y produzca una respuesta que puede ser correcta o no.

Cada uno de estos resultados es malo, pero el último es sin duda el peor. Cuando un programa parece estar haciendo lo correcto pero no lo está haciendo, pueden ocurrir cosas malas: se pueden perder fortunas, los pacientes pueden recibir dosis mortales de radioterapia, los aviones pueden estrellarse.

> [!NOTE]
> Los ordenadores pueden ser muy literales. Si no les dices exactamente lo que quieres que hagan, es probable que se equivoquen. Intenta escribir un algoritmo para conducir entre dos destinos. Escríbelo como lo harías para una persona e imagina qué pasaría si esa persona fuera tan estúpida como un ordenador y ejecutara el algoritmo exactamente como está escrito. (Para una divertida ilustración de esto, echa un vistazo al vídeo https://www.youtube.com/watch?v=FN2RM-CHkuI&t=24s.)

# Introducción a Python

Aunque cada lenguaje de programación es diferente (aunque no tanto como sus diseñadores nos quieren hacer creer), pueden relacionarse a lo largo de algunas dimensiones.

## Nivel de abstracción

**Bajo nivel** vs. **alto nivel** se refiere a si programamos utilizando instrucciones y objetos de datos al nivel de la máquina (por ejemplo, mover 64 bits de datos de esta ubicación a aquella) o si programamos utilizando operaciones más abstractas (por ejemplo, desplegar un menú en la pantalla) que han sido proporcionadas por el diseñador del lenguaje.

## Lenguajes de Propósito General vs. Lenguajes Específicos de Dominio

Esto se refiere a si las operaciones primitivas del lenguaje de programación son ampliamente aplicables o están ajustadas específicamente a un dominio. Por ejemplo, **SQL está diseñado para extraer información de bases de datos relacionales**, pero no querrías usarlo para construir un sistema operativo.

## Interprete vs Compilador

Esto se refiere a si la secuencia de instrucciones escrita por el programador, llamada **código fuente**, se ejecuta _directamente_ (mediante un **intérprete**) o si primero se _convierte_ (mediante un **compilador**) en una secuencia de operaciones primitivas a nivel de máquina. 

>[!NOTE]
> En los primeros tiempos de los ordenadores, la gente tenía que escribir el código fuente en un lenguaje cercano al código máquina que pudiera ser interpretado directamente por el hardware del ordenador

Ambos enfoques tienen sus ventajas. A menudo es más fácil depurar programas escritos en lenguajes diseñados para ser interpretados, porque el intérprete puede producir mensajes de error fáciles de relacionar con el código fuente. Los lenguajes compilados suelen producir programas que se ejecutan más rápidamente y ocupan menos espacio.

___
Python es un lenguaje de programación de propósito general que puede utilizarse eficazmente para construir casi cualquier tipo de programa que no necesite acceso directo al hardware del ordenador. Python no es óptimo para programas que tengan restricciones de alta fiabilidad (debido a su débil comprobación semántica estática) o que sean construidos y mantenidos por muchas personas o durante un largo periodo de tiempo (de nuevo debido a la débil comprobación semántica estática).

Python tiene varias ventajas sobre muchos otros lenguajes. Es un lenguaje relativamente sencillo y fácil de aprender. Como Python está diseñado para ser interpretado, puede proporcionar el tipo de retroalimentación en tiempo de ejecución que es especialmente útil para los programadores principiantes. Existe un gran número, cada vez mayor, de bibliotecas gratuitas que se conectan a Python y proporcionan funciones ampliadas de gran utilidad. En este libro utilizamos varias de estas bibliotecas.

Estamos listos para introducir algunos de los elementos básicos de Python. Estos son comunes a casi todos los lenguajes de programación en concepto, aunque no en detalle.

Este libro no es sólo una introducción a Python. Utiliza Python como vehículo para presentar conceptos relacionados con la resolución de problemas y el pensamiento computacional. El lenguaje se presenta a cuentagotas, según sea necesario para este propósito ulterior. Las características de Python que no necesitamos para ese fin no se presentan en absoluto. Nos sentimos cómodos no cubriendo cada detalle porque excelentes recursos en línea describen cada aspecto del lenguaje. Sugerimos que utilices estos recursos gratuitos en línea según sea necesario.

Python es un lenguaje vivo. Desde su introducción por Guido von Rossum en 1990, ha experimentado muchos cambios. Durante la primera década de su vida, Python fue un lenguaje poco conocido y poco utilizado. Eso cambió con la llegada de Python 2.0 en 2000. Además de incorporar importantes mejoras al propio lenguaje, marcó un cambio en la trayectoria evolutiva del mismo. Muchos grupos empezaron a desarrollar bibliotecas que interactuaban a la perfección con Python, y el apoyo y desarrollo continuos del ecosistema Python se convirtieron en una actividad basada en la comunidad.

Python 3.0 se publicó a finales de 2008. Esta versión de Python eliminó muchas de las incoherencias en el diseño de Python 2. Sin embargo, Python 3 no es compatible con Python 2. Sin embargo, Python 3 no es compatible con versiones anteriores. Esto significa que la mayoría de los programas y bibliotecas escritos para versiones anteriores de Python no pueden ejecutarse utilizando implementaciones de Python 3.
En la actualidad, todas las bibliotecas importantes de Python de dominio público han sido portadas a Python 3. Hoy en día, no hay ninguna razón para utilizar Python 2.

# Elementos básicos de Python 

Un **programa** Python, a veces llamado **script**, es una secuencia de definiciones y comandos. El intérprete de Python en el shell evalúa las definiciones y ejecuta los comandos.

Un **comando**, a menudo llamado sentencia, ordena al intérprete que haga algo. Por ejemplo, la sentencia ``{python}print('¡River manda!')`` ordena al intérprete que llame a la función ``{python}print``, que muestra la cadena ``River manda!`` en la ventana asociada al intérprete de comandos.

La secuencia de comandos seria:

```python
print('River manda!')
print('Pero no en el Monumental!')
print('River manda, ', 'Pero no en el Monumental!')
```

El interprete producirá la siguiente salida:

```
River manda!
Pero no en el Monumental!
River manda, Pero no en el Monumental!
```

Observe que se han pasado dos valores a ``{python}print`` en la tercera sentencia. La función ``{python}print`` toma un número variable de argumentos separados por comas y los imprime, separados por un carácter de espacio, en el orden en que aparecen.

_____

# Términos

- **Conocimiento declarativo**: Tipo de conocimiento que describe **qué** se quiere lograr sin especificar **cómo** hacerlo. Se enfoca en los hechos, reglas o relaciones.  Ej.: Consultas en SQL, lógica proposicional.
- **Conocimiento imperativo**: Describe **cómo** lograr algo paso a paso. Es procedimental, indica instrucciones explícitas para alcanzar un objetivo.  Ej.: Programación en C, Python.
- **Algoritmo**: Conjunto finito y ordenado de pasos o instrucciones que resuelven un problema o realizan una tarea. Debe ser preciso, finito y efectivo.
- **Computación**: Proceso de realizar cálculos o resolver problemas mediante algoritmos, ya sea de forma manual, mecánica o automática (computadoras).
- **Computadoras de programas fijos**: Computadoras cuyo comportamiento está definido por **circuitos físicos**. No se pueden reprogramar fácilmente.  Ej.: Calculadoras básicas, dispositivos electrónicos específicos.
- **Computadoras de programas almacenados**: Computadoras que pueden **almacenar instrucciones (programas)** en su memoria, permitiendo cambiar el comportamiento sin modificar el hardware.  Ej.: Todas las computadoras modernas (modelo de von Neumann).
- **Interprete**: Programa que **ejecuta código fuente línea por línea**, sin necesidad de compilarlo previamente.  Ej.: Intérprete de Python.
- **Contador de programa**: Registro de la CPU que contiene la dirección de memoria de la **siguiente instrucción a ejecutar**.
- **Flujo de control**: Orden en que se ejecutan las instrucciones en un programa. Puede ser secuencial, condicional (if), repetitivo (while/for), o por funciones/llamadas.
- **Diagrama de flujo**: Representación gráfica del flujo de control de un algoritmo o programa, usando símbolos estandarizados (óvalos, flechas, rombos, etc.).
- **Lenguaje de programación**: Lenguaje formal diseñado para **describir algoritmos y estructuras de datos**, que puede ser entendido y ejecutado por una computadora.
- **Maquina de Turing universal**: Modelo teórico de computación que puede **simular cualquier otra máquina de Turing**, es decir, puede ejecutar cualquier algoritmo describible.
- **Tesis Church-Turing**: Hipótesis que establece que **todo problema que puede resolverse mediante un procedimiento efectivo (algoritmo)** puede resolverse con una máquina de Turing.
- **Problema de detención**: Problema que consiste en determinar, dado un programa y una entrada, **si el programa terminará o se ejecutará para siempre**. Se ha demostrado que **no es resoluble** por ningún algoritmo general.
- **Completitud de Turing**: Propiedad de un lenguaje de programación o sistema computacional que indica que puede **simular cualquier máquina de Turing**, y por tanto, puede realizar cualquier cálculo computable.
- **Literales**: Valores constantes **escritos directamente** en el código fuente. Ej.: `5`, `3.14`, `'hola'`, `True`.
- **Operadores infijos**: Operadores que se colocan **entre dos operandos**.  Ej.: `a + b`, `x * y`.
- **Sintaxis**: Conjunto de reglas que define **cómo deben escribirse correctamente las expresiones** en un lenguaje de programación.
- **Semántica estática**: Propiedades del programa que se pueden verificar **en tiempo de compilación** sin ejecutarlo.  Ej.: Tipado, declaraciones previas, alcances.
- **Semántica**: Significado de los elementos del lenguaje. Describe **qué efecto produce la ejecución de una instrucción o programa**.

