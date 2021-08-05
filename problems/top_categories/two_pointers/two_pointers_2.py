"""
Problem Statement (remove duplicates):
 - Given an array of sorted numbers (non decreasingly), remove all duplicates from it. You should not use any extra
 space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

Based on the problem statement the input array could be like either of this pattern
    - [2, 2, 2, 2, 2, 2, 2]
    - [2, 3, 3, 3, 4, 6, 9, 8, 11, 11, 13]
    - [4, 5, 9, 45, 56]

Solution Approach:
    - It's clear however the array is there will be at least one unique number - the first number at index 0.
    - Our purpose is to just scan the array (using a for/while loop - first pointer) from start to end. And use another
    pointer to point the position where the next unique number will be inserted if it's found.
    - so our two pointers are:
        - i
            - loop index to scan the array through
            - 1; will compare 0th and 1th; there is nothing to compare a number to itself.
        - next_unique_number
            - point to the position where the next unique number will be inserted
            - initial value: 1; cause there will be at least 1 unique number; the earlier unique number is stored at 0
"""


def remove_duplicates(a):
    next_unique_element = 1  # the position where the next unique element will be stored
    i = 1

    while i < len(a):
        if a[i] != a[next_unique_element - 1]:
            a[next_unique_element] = a[i]
            next_unique_element = next_unique_element + 1
        i = i + 1
    return next_unique_element


a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 96, 208]
b = [2, 2, 2, 2, 2, 2, 2, 2]
c = [2, 3, 3, 3, 6, 9, 9]
d = []
print(remove_duplicates(c))
print(b)
