"""
Name: Remove element
URL: https://leetcode.com/problems/remove-element/
Tags: #array, #two-pointers
"""
from typing import List

"""
NTOE:
    - the main idea behind the algorithm is to push all elements to the left of array - those are not equal the target
    value. 
    - By this way finally, you will able modify the existing array with two partitions - left and right. 
    - Left partition will contain all those elements whose are not equal the target value(the value need to be removed).
    - We don't have to bother about the right partition
    - To make two portions in the array we can use a pointer, say - 'valid_size'
        - 'valid_size' will represent the size of the left array or number of non-val element 
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        valid_size = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[valid_size] = nums[i]
                valid_size = valid_size + 1

        return valid_size

#
# s = Solution()
# a = [0, 1, 2, 2, 3, 0, 4, 2]
# print(len(a), id(a))
# size = s.removeElement(a, 2)
# print(len(a), id(a), size)
# print(a)
