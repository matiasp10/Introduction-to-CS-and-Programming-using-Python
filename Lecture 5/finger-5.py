# Assume you are given a string variable named my_str. 
# Write a piece of Python code that prints out a new string containing the even indexed characters of my_str. 
# For example, if my_str = "abcdefg" then your code should print out aceg.

my_str = "abcdefg"

evenChars = ''
for i in range(0,len(my_str),2):
    evenChars += my_str[i]
print(evenChars)