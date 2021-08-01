"""
reverse_v1:
- reversing array using simple naive method
- time complexity O(n)
- space complexity O(n)
"""


def reverse_v1(arr):
    result = []
    start = len(arr) - 1
    end = 0

    while start >= end:
        result.append(arr[start])
        start = start - 1
    return result


"""
reverse_v2:
- reversing array using better technique
- time complexity O(n)
- space complexity O(1)
"""


def reverse_v2(arr):
    start = 0
    end = len(arr) - 1

    while end > start:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1
    return arr


def main():
    array = [11, 34, 98, 25, 29, 38, 99]
    # array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print('The original array: ', array)

    # reversed_array = reverse_v1(array)
    reversed_array = reverse_v2(array)
    print('After reversing the array: ', array)

    # array[::-1]
    # finally array.reverse() also reverse the array in space, it doesnt' return anything


if __name__ == "__main__":
    main()
