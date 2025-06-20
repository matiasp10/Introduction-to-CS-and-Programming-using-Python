# Finger Exercises Lecture 13
# Name: Matias Ezequiel Petenatti
# Time Spent: 0:15

def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    length = 0
    for elem in L:
        if isinstance(elem, list):
            for subelem in elem:
                if not isinstance(subelem, str):
                    raise ValueError("Subelement is not a string")
                length += len(subelem)
        elif not isinstance(elem, str):
            raise ValueError("Element is not a string or a list")
        else:
            length += len(elem)
    return length

# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError

