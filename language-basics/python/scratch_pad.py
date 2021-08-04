n1 = [1, 2, 3, 4, 5, 6]
n2 = [7, 8, 9, 10, 11, 12]
n3 = n1 + n2 + [13, 14, 15, 16, 17, 18, 19, 20]
n4 = [n for n in range(0, 100)]
# print(n1)
# print(n3)
# print(n4)
#
# print(list(map(lambda x: x ** 2, n1)))
# print(list(map(lambda x: x ** 2, n2)))
# print(list(map(lambda x, y: '(' + str(x) + ',' + str(y) + ')', n1, n2)))
# print(list(filter(lambda x: x % 2 == 0, n4)))

for n in range(1, 10):
    print(n)
