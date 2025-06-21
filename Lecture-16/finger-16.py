# Finger Exercises Lecture 16
# Name: Matias Ezequiel Petenatti
# Time Spent: 0:15

def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    if L == []:
        return []
    else:
        if isinstance(L[0], list):
            return flatten(L[0]) + flatten(L[1:])
        else:
            return [L[0]] + flatten(L[1:])
        
# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]