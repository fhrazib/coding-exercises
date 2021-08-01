"""
map(function, iterable, ...)
    - map could be think as transform of iterables
    - map pass each of the value from the iterable to the function to transform (or do anything)
    - map returns a map object
    - later you can pass this map object to functions like - list()(to create list), set() (to create set) and so on

NOTE:
    - map doesnt return an ITERABLE
    - map process EACH element of an ITERABLE.
    - though you pass an whole ITERABLE to a map, map itself send EACH ELEMENT from that iterable to your given function
"""


def calculate_square(n):
    return n * n


"""
    i1elem: represent an element from iterable 1
    i2elem: represent an element from iterable 2
"""


def make_pairs(i1elem, i2elem):
    result = str(i1elem) + ':' + str(i2elem)
    # print(result)
    return result


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 7]
    map_obj = map(calculate_square, numbers)
    print(map(calculate_square, numbers))  # <map object at 0x7f0009e94670>
    print(type(map(calculate_square, numbers)))  # <class 'map'>
    print(list(map_obj))  # [1, 4, 9, 16, 25, 36, 49, 49]

    # using lambda function with map
    map_obj2 = map(lambda x: x * x, numbers)
    print(set(map_obj2))  # {1, 4, 36, 9, 16, 49, 25}
    print(dict(map_obj2))  # {}

    # map with multiple iterable
    fruits = ['apple', 'orange', 'banana', 'lemon', 'mango', 'pineapple', 'cherry']
    index = (1, 2, 3, 4, 5, 6, 7)
    map_obj3 = map(make_pairs, index, fruits)
    print(list(map_obj3))  # ['1:apple', '2:orange', '3:banana', '4:lemon', '5:mango', '6:pineapple', '7:cherry']
    print(dict(map_obj3))  # {}
    pass


if __name__ == "__main__":
    main()
