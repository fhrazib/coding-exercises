"""
- PROBLEM_STATEMENT_TWO: You have given an array 'A' and an integer 'K'. Find the maximum for each and every
contiguous subarray of size K

Same as LeetCode Problem : 239:
- You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the
array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one
position.

-
SOLVING APPROACHES:
    - ONE: Brute force Naive approach => O(N*K) => O(N^2)
    - TWO: Using self balancing tree => log(N*logK) # TODO
    - THREE: Using heap data structure. Max heap for finding maximum, mean heap for finding minimum => O(N*logK) # TODO
    - FOUR: Using dequeue: Use a double ended queue to store elements of the window => O(N)
    - All these above four approaches are described here - https://afteracademy.com/blog/sliding-window-maximum
"""
import collections


def maximum_in_a_window_bf(arr, k):
    n = len(arr)

    max_list = []

    for i in range(n - k + 1):

        _max = float('-inf')

        for j in range(i, i + k):
            _max = max(_max, arr[j])
        max_list.append(_max)

    return max_list


"""
- FOUR: Using dequeue: Use a double ended queue to store elements of the window
- Time Complexity: O(N)
- Space Complexity: O(K)

- THE MAIN IDEA BEHIND  THE ALGORITHM: 
    - we have to find the maximum from the each window of size K. With naive brute force approach We have to find this 
    max value so many times that it gives time limit exceed error. 
    - SO IF WE CAN manage a datastructures that provide us the max value with minimum cost then we can use this data 
    structure here. 
    - There are 2 datastructures here  that gives us the max value with lowest cost (no searching) - (1) Self balancing 
    binary tree (BST) (2) Max heap.
    - We also could use dequeue
        - We have to manage the deque such a way that the max element will always be at the front of the queue. And the 
        dequeue always remains decreasing. We weill larger remove value/index  from front and add smaller value/index at
        rear. 

- STEPS USED IN THIS ALGORITHM
    - Step 1 - Popping Smaller and Appending (current) Right Index : appending the appropriate right index of the 
    sliding window. (Smaller index will be popped from right)
    - Step 2 - Removing left values from the window (queue)
    - STEP 3 - Picking and Sliding: picking the max element and slide the window
"""


def finding_maximum_with_sliding_window(arr, k):
    output = []
    queue = collections.deque()
    l, r = 0, 0  # left and right index, pointer to the start/left and end/right of the sliding window

    # Will run our algorithm while our right pointer still inbound.
    while r < len(arr):
        """
        STEP 1 - Popping Smaller and Appending (current) Right Index : appending the appropriate right index of the 
        sliding window
        ----------------------------------------------------------------------------------------------------------------
        - How we determine the appropriate right index 'r' ?
            - Before appending we have to check : arr[queue[-1]] < arr[r]
            - That means we are checking whether the right most element (which is arr[queue[-1]] ) is less than the 
            current indexed (r) element (arr[r]). See # NOTE-1
            - That means we can not bigger element at right
        
        - Why we can not bigger element at right?
            - because we want to manage the queue in such a way that it the bigger element stay at the left. 
            So we can easily say the left most element int he queue is the larger. We don't need to search the whole 
            queue to find the max value 
        
        """
        while queue and arr[queue[-1]] < arr[r]:  # NOTE-1
            queue.pop()
        queue.append(r)

        """
        Step 2 - Removing left values from the older window (queue)
        ----------------------------------------------------------------------------------------------------------------
        - When we need to remove the left value?
            - When our left values out of bound
            - queue[0] ==> max index
            - window is bounded by index ==> (l, r)
            - so queue[0]>=l and queue[0]<=r
            - so we have to remove from left while l>queue[0]
            
        - WHY WE ARE REMOVING THE LEFT VALUE BEFORE WE PICKING AND PUBLISHING IT (which is done at STEP 3)?
            - because we are removing the older value from the front of the queue. 
            - this step will not execute at first iteration. at first iteration the window just slide right. 
            - because at the first iteration the window slided right. So there is a old value at the left of the queue 
            and we have to remove it.  
        """
        if l > queue[0]:
            queue.popleft()

        """
        STEP 3 - Picking and Sliding: picking the max element and slide the window
        ----------------------------------------------------------------------------------------------------------------
        - slide the right border of the window each of this iteration
        - if we want to publish max value to output we have to make sure our window is full. That means we have to make 
        sure our window is currently containing at least k number ==> window is full. When the window is full then  
        we can take the left most element from the window as max.
        - when the window is full we also forward the left pointer
        """
        if (r + 1) >= k:
            output.append(arr[queue[0]])
            l += 1
        r += 1
    return output


"""
Time complexity: O(n)
Space complexity: O(n)

QUESTION: How this algorithm has O(n) complexity while is has 2 nested loops?
- Because 
    - (1) The inner for loop run only once (up to length K) to fill the window up to K elements. The while loop runs 
    full for r=0 (may be). There is no way the inner for loop run for each value of 'r' 
    - (2) From the second iteration (r=1) and onward the window will be filled up by k elements. So we won't never enter 
    into the inner loop again.  
    - (3) Since the window is full now. Then inner for loop only works as an if condition. It will just pop (remove) the 
    right most element from the queue.
    - (4) The window might be empty at the very end of the array. In that case it's OK. Since we have no element to 
    iterate again
    
- NOTE-1: 
    - the inner for loop could be replaced with  a outer for loop  (like in 
    01-maximum-sum-in-window-of-size-k.py.sliding_window_sum(a, k))
"""

if __name__ == '__main__':
    a1, k1 = [1, 2, 3, 4, 10, 6, 9, 8, 7, 5], 3  # [3, 4, 10, 10, 10, 9, 9, 8]
    a2, k2 = [9, 8, 6, 4, 3, 1], 4  # [9, 8, 6]
    a3, k3 = [4, 3, 8, 9, 0, 1], 3  # [8, 9, 9, 9]
    a4, k4 = [198, 2, 83, 989, 5, 98, 7, -3, -87, 21, 0, -91, 23, 1005, -45, 56, -9, 150, 101, -11, 34, 98, 234, 10], 5
    # [989, 989, 989, 989, 98, 98, 21, 21, 23, 1005, 1005, 1005, 1005, 1005, 150, 150, 150, 150, 234, 234]

    array = a4
    window_size = k4
    result = maximum_in_a_window_bf(array, window_size)
    print(result)

    result = finding_maximum_with_sliding_window(array, window_size)
    print(result)
