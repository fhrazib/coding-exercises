"""
Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set,
dictionary etc.) from sequences that have been already defined.

Python supports 4 types of comprehension:
    - list comprehension
    - dictionary comprehension
    - set comprehension
    - generator comprehension
"""

"""
List comprehension:
    output_list = [output_expression for var in input_list if (var satisfies this condition)]
    output_list = [output_expression for var in input_list]

    NOTE:
        - list comprehension may or may not contain if condition
        - list comprehension may contains multiple for loop (nested comprehension)
"""

# Constructing output list WITHOUT comprehension
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_list = []

# Using loop for constructing output list
for var in input_list:
    if var % 2 == 0:
        output_list.append(var)
print("Output List using for loop:", output_list)

list_using_comp = [n for n in input_list if n % 2 == 0]
print("Output List using list comprehensions:", list_using_comp)

squares_up_to10 = [num ** 2 for num in range(1, 10)]
print("squares up to 10 ", squares_up_to10)

odd_squares_up_to50 = [num ** 2 for num in range(1, 50) if num % 2 != 0]
print("squares of odd numbers up to 50 ", odd_squares_up_to50, '\ntotal: ', len(odd_squares_up_to50))

# making list from string using comprehension
raw_string = "1.some Given raW stRing: :)"
s = [c for c in raw_string.lower() if c.isalnum()]
print(s)  # ['1', 's', 'o', 'm', 'e', 'g', 'i', 'v', 'e', 'n', 'r', 'a', 'w', 's', 't', 'r', 'i', 'n', 'g']

#######################################################################################################################


"""
Generator comprehension:
    - 
"""

#######################################################################################################################
