# Finger Exercises Lecture 4
# Name: Matias Ezequiel Petenatti
# Time Spent: 0:15

# Assume you are given a positive integer variable named N. 
# Write a piece of Python code that finds the cube root of N. 
# The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. 
# Hint: use a loop that increments a counter—you decide when the counter should stop.

N = int(input("Ingrese un número entero positivo: "))
encontrado = False
x = 0

while x ** 3 <= N:
    if x ** 3 == N:
        print(f"La raíz cúbica de {N} es {x}")
        encontrado = True
        break
    x += 1

if not encontrado:
    print(f"{N} no es un cubo perfecto.")