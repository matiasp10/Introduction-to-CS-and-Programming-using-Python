# Finger Exercises Lecture 4
# Name: Matias Ezequiel Petenatti
# Time Spent: 

# Assume you are given a positive integer variable named N. 
# Write a piece of Python code that finds the cube root of N. 
# The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. 
# Hint: use a loop that increments a counter—you decide when the counter should stop.

N = 27

cube = 0
while cube**3 < N:
    cube += 1
if cube**3 == N:
    print(cube)
else:
    print("error")