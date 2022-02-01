nums = [0, 9, 2, 3, 4, 4, 6, 7, 8, 8]


def main():

    # All numbers in the list will print
    for n in nums:
        print(n, end=' ')
        # 0, 9, 2, 3, 4, 4, 6, 7, 8, 8

    # Note 10 will not print - it will print up to 10; but not 10
    # It will process total (n) = 10 elements ****
    # But max index (max value of i) will be 9
    print('\n')
    for i in range(10):
        print(i, end=' ')
        # 0 1 2 3 4 5 6 7 8 9

    # 2 will print 10 will not print
    # It will process total (end-start) = (10-2) = 8 elements ****
    # Max index of i = 9
    print('\n')
    for i in range(2, 10):
        print(i, end=' ')
        # 2 3 4 5 6 7 8 9
    pass


if __name__ == '__main__':
    main()
