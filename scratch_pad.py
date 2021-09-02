def mss_brute_force(array):
    n = len(array)

    for i in range(0, n):
        for j in range(i, n):
            for k in range(i, j + 1):
                print(array[k], end=' ')
            print('\n')
        print('................................................')


def maximum_sum_subarray(nums):
    n = len(nums)

    max_sum = float('-inf')
    for i in range(0, n):
        for j in range(i, n):
            _sum = 0
            for k in range(i, j + 1):
                _sum = _sum + nums[k]
                print(nums[k], end=' ')
            max_sum = max(_sum, max_sum)
            print(': ', _sum)
        print('------------------------------------------')
    return max_sum


 a = [1, 2, 3, 4]
b = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
c = [1]
d = [5, 4, -1, 7, 8]
result = maximum_sum_subarray(a)
print(result)
