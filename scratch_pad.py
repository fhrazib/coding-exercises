nums = [23, 39, 36, 37, 38, 47, 48, 22, 96, 1002, 10001, 2041, 20, 2089, 1]

print(list(map(lambda x: x * x, list(filter(lambda x: x % 2 != 0, nums)))))

r = [n * n for n in nums if n % 2 != 0]

print(r)
