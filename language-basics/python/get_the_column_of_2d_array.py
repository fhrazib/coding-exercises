
def main():
    graph = [
        [0, 1, 4, 0, 0, 0],
        [1, 0, 4, 2, 7, 0],
        [4, 4, 0, 3, 5, 0],
        [5, 2, 3, 0, 4, 6],
        [0, 7, 5, 4, 0, 7],
        [0, 0, 0, 6, 7, 0]
    ]

    col0 = [v[0] for v in graph]
    col1 = [v[1] for v in graph]
    col2 = [v[2] for v in graph]
    col3 = [v[3] for v in graph]
    col4 = [v[4] for v in graph]
    col5 = [v[5] for v in graph]
    print(col0)
    print(col1)
    print(col2)
    print(col3)
    print(col4)
    print(col5)


if __name__ == "__main__":
    main()
