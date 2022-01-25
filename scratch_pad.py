graph = [
    [0, 1, 4, 0, 0, 0],
    [1, 0, 4, 2, 7, 0],
    [4, 4, 0, 3, 5, 0],
    [5, 2, 3, 0, 4, 6],
    ['x', 7, 5, 4, 0, 7],
    ['y', 0, 0, 6, 7, 0]
]

str = 'abacdefghi'

def main():

    col0 = [v[0] for v in graph]
    str2 = [s for s in str]
    print(str2)
    print(col0)

    pass


if __name__ == '__main__':
    main()
