# Finger Exercises Lecture 12
# Name: Matias Ezequiel Petenatti
# Time Spent: 0:15

def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    return len([x for x in nums_list if x ** 0.5 in nums_list])

# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3