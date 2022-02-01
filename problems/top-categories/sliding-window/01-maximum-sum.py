def sliding_window(a, k):
    n = len(a)

    max_sum = float('-inf')
    for i in range(n - k + 1):
        window_sum = 0
        for j in range(i, i + k):
            print(a[j], end=' ')
            window_sum = window_sum + a[j]
        max_sum = max(max_sum, window_sum)
        print(': ', window_sum, '\n')
    return max_sum


if __name__ == '__main__':
    a1 = [1, 2, 3, 4, 5, 6, 7]
    a2 = [5, 7, -3, 1, 2, 8]
    a3 = [5, 7, -3, 1, 2, 8, 99, 78, -3, -54, 98, -87, 21, 0, -91, 23, 45, 56, -98, 50, 101, 1]
    window_size = 3
    maximum_window_sum = sliding_window(a1, window_size)
    print(maximum_window_sum)


"""
WHY there are (n-k+1) windows?
a = [1, 2, 3, 4, 5, 6, 7] and k=3

- its clear the last window is [5, 6, 7] => 1 window/subarray
- before that we have total (n-k) = (7-3) = 4 windows/subarray
    - because before we have total (n-k) = 4 elements in the array and we are sliding the window one by one element at 
    a time 
    - and for each element there will be a subarray starting with this element (see below). So the total number of 
    subarrays are: (n-k+1)
    - subarrays:
        - [1, 2, 3]   
        - [2, 3, 4]   
        - [3, 4, 5]   
        - [4, 5, 6]
        - [5, 6, 7]   
"""
