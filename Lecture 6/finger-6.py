# Assume you are given an integer 0 \<= N \\<= 1000. 
# Write a piece of Python code that uses bisection search to guess N. 
# The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N. 
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.

N = 35

count = 0
low = 0
high = 1000

response = (high + low) / 2

while abs(response - N) >= 0.01:
    if response < N:
        low = response
    else:
        high = response
    response = (high + low) / 2
    count += 1

print(count)
print(response)