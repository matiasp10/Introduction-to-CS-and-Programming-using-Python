# Finger Exercises Lecture 9
# Name: Matias Ezequiel Petenatti
# Time Spent: 0:15

# Implement the function that meets the specifications below:

def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    sum = 0
    for element in range(len(tA)):
        sum += tA[element] * tB[element]
    return (len(tA), sum)

# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB)) # prints (3,32)
