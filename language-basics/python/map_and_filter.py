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


filter(function, iterable)
    - filter filters out only those elements from the iterator for which the given function returns true
    - (while map apply the given function to each element of the iterable)
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

    # map with double argument lambda
    print('double argument lambda: ', list(map(lambda a, b: a + b, [1, 2, 3, 7, 9], [1, 1, 4, 6, 6])))

    # filter out only the even numbers
    nums = [23, 39, 36, 37, 38, 47, 48, 22, 96, 1002, 10001, 2041, 20, 2089, 1]
    print('the even numbers from the list are: ', list(filter(lambda x: x % 2 == 0, nums)))
    pass


if __name__ == "__main__":
    main()
