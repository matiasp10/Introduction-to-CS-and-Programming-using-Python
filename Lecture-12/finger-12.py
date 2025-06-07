# Finger Exercises Lecture 12
# Name: Matias Ezequiel Petenatti
# Time Spent: 0:15

def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    result = 0
    for num in nums_list:
        if num * num in nums_list:
            result += 1
    return result

# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3