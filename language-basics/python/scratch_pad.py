a = [i for i in range(1, 101)]
b = [2, 3, 3, 3, 2, 2, 4, 9, 33, 2, 18, 2]
print(a)
key = 2
print(list(filter(lambda x: x != key, b)))
