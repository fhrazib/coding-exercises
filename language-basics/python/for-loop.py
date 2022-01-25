nums = [0, 9, 2, 3, 4, 4, 6, 7, 8, 8]


def main():

    # All numbers in the list will print
    for n in nums:
        print(n, end=' ')
        # 0, 9, 2, 3, 4, 4, 6, 7, 8, 8

    # Note 10 will not print - it will print up to 10; but not 10
    print('\n')
    for i in range(10):
        print(i, end=' ')
        # 0 1 2 3 4 5 6 7 8 9

    # 2 will print 10 will not print
    print('\n')
    for i in range(2, 10):
        print(i, end=' ')
        # 2 3 4 5 6 7 8 9
    pass


if __name__ == '__main__':
    main()
