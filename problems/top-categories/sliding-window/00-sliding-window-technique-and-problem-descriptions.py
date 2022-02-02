"""
PROBLEM STATEMENT:
    - PROBLEM_STATEMENT_ONE: You have given an array 'A' and an integer 'K'. Find the maximum SUM for each and every
    contiguous subarray of size K
        - See this file for code implementation- 01-maximum-sum-in-window-of-size-k.py
        - aks maximum sum subarray of size K
        - aks sliding window maxSum
        - DO NOT CONFUSE with 'maximum subarray (of any length) sum'. Here the subarray could be of any length. We can
        not apply sliding window technique here. Sliding window technique could be applied when you have a subarray of
        fixed length. To solve 'maximum subarray (of any length) sum' in liner time we could use Kaden's algorithm

    - PROBLEM_STATEMENT_TWO: You have given an array 'A' and an integer 'K'. Find the maximum for each and every
    contiguous subarray of size K
        - See this file for code implementation - 02-sliding-window-maximum.py
        - aks maximum of all subarray of size K
        - aks sliding window maximum

SLIDING WINDOW TECHNIQUE:
    - to understand sliding window technique better lets first analyze PROBLEM_STATEMENT_ONE's brute force solution.
    - say you have given an array A = [2, -1, 3, 5, -3, 8, 7, 5] and K = 4
    - Now with brute force approach possible all sub-arrays of size 4 are
        - [2 -1 3 5]      : 4      #1
        - [-1 3 5 -3]     : 7      #2
        - [3 5 -3  8]     : 5      #3
        - [5 -3 8  7]     : 10     #4
        - [-3 8 7  5]     : 12     #5
    - if you observe all these subarray (no. 1-5) you will notice two consecutive subarray differ by only one element.
    #1 and #2 has 3 common elements [-1 3 5]. So these subarray are overlapping by 3 elements. But in brute force
    approach we are evaluating these overlapping  subarray again and again.
    - sliding window technique take the advantage of overlapping portion of these 2 sub array.
    - From subarray #1 we know the sum is 4.  At subarray #2 only '2' is removed from #1 and '-3' is being added to #1
    - The same is true for any 2 consecutive subarray like - #2-#3, #3-#4 #4-#5... #(n-k)-#(n-k+1)
    - If we consider a window of size k. Its something like we are sliding a window from the array - a's left to right
    one element at a time.
    - In t his sliding window of size k - one element is being REMOVED from LEFT and another element is being ADDED at
    RIGHT. So we don't need to process these element in between at all. For example while going from #1 to #2 we don't
    need to process [-1 3 5] second time. Since this [-1 3 5] has already been processed in #1 we don't need to process
    it #2. We just need to remove '2' from #1 and add '-3' to #1
    - This will give you a O(n) time complexity. While the brute force approach gives you O(n*k) => O(n^2)

    - NOTE:
        - total window of size k are: (n-k+1). Why? - I know it :)
        - number of overlapping elements between 2 consecutive subarray : k-1

"""