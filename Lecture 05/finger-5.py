# Finger Exercises Lecture 5
# Name: Matias Ezequiel Petenatti
# Time Spent: 0:15

# Assume you are given a string variable named my_str. 
# Write a piece of Python code that prints out a new string containing the even indexed characters of my_str. 
# For example, if my_str = "abcdefg" then your code should print out aceg.

mi_cadena = input("Ingrese un texto para devolver solo las cadenas pares:")
nueva_cadena = mi_cadena[::2]
print(nueva_cadena)