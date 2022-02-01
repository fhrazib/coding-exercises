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


SOLVING APPROACHES:
    - ONE: Brute force => O(n*k) => O(n^2)
    - TWO: Sliding window with the help of external for loop that find only the sum of the first window => O(n)
    - THREE: Sliding window with no help of external for loop to find the first window sum => O(n) # TODO
        - little improvement over the second approach but time complexity is still O(n). Since we don't need to use the
        external for loop to find the initial/first window sum.
"""


# ATTEMPT ONE: Brute force approach
def maximum_window_sum_bf(a, k):
    n = len(a)

    max_sum = float('-inf')
    for i in range(n - k + 1):
        window_sum = 0
        for j in range(i, i + k):
            # print(a[j], end=' ')
            window_sum = window_sum + a[j]
        max_sum = max(max_sum, window_sum)
        # print(': ', window_sum, '\n')
    return max_sum


# Sliding window  + with the help of external for loop that fine only the sum of the first window
def sliding_window_sum(a, k):
    n = len(a)
    max_sum = float('-inf')
    ws = sum(a[:k])

    for i in range(1, n - k + 1):
        ws = ws - a[i - 1] + a[i + k - 1]  # FOOT_NOTE-1
        max_sum = max(max_sum, ws)
    return max_sum


if __name__ == '__main__':
    a1 = [1, 2, 3, 4, 5, 6, 7]
    a2 = [5, 7, -3, 1, 2, 8]
    a3 = [5, 7, -3, 1, 2, 8, 99, 78, -3, -54, 98, -87, 21, 0, -91, 23, 45, 56, -98, 50, 101, 1]
    a4 = [198, 2, 83, 989, 5, 7, -3, -87, 21, 0, -91, 23, 1005, -45, 56, -9, 150, 101, -11, 34, 98, 234, 10]

    array = a4
    window_size = 3
    bf_result = maximum_window_sum_bf(array, window_size)
    print(bf_result)

    sld_result = sliding_window_sum(array, window_size)
    print(sld_result)


"""
FOOT_NOTES: (assuming k=3 and array=a2)
    - 1:  a[i + k -1] Note here, we write (k-1) not k. 
        - Because we started the for loop from 1. So if we add (i+k) it will point 4th index  which is '2'. 
        - But we want to point the 3rd index which is '1'. So we have to shift 1 index left. that's why it is a[i+k-1]
        - Also note replacing i with '(n-k+1)' => (i + k - 1) => {(n-k+1) + k - 1} => n = length of the array 
"""