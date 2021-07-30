def reverse_v1(arr):
    result = []
    start = len(arr) - 1
    end = 0

    while start >= end:
        result.append(arr[start])
        start = start - 1

    return result


def main():
    array = [11, 34, 98, 25, 29, 38, 99]
    print('The original array: ', array)
    #
    # array.reverse()
    # print('After reversing the array: ', array)

    print(reverse_v1(array))


if __name__ == "__main__":
    main()
