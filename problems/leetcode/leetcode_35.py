"""
Name: Search Insert Position
URL: https://leetcode.com/problems/search-insert-position/
Tags: #binary-search #search
"""
from typing import List

"""
NOTE:
    - [2]
    - initial left = 0, right = 0, mid = 0
    - while we search target=0 in the above array after one iteration 
        - left = 0, right = -1 (which is not possible)
        - that indicates we have to insert an element at left=0, so we return left
    - while we search for target=3 in the above array after one iteration
        - left = 1, right = 0. That means we have to insert 3 at the next position, and so we return left
    - [2, 7, 9, 11]
        - same is true for while we are trying to search 10 nad 8.
            - while searching 10 at the end left = 3
            - while searching 8 at the end left = 2  
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return left


# s = Solution()
# a = [2, 3, 4, 5, 9, 23, 98, 103, 107]
# b = [2, 3, 4]
# c = [2]
# d = [2, 7, 9, 11]
# print(s.searchInsert(c, 3))


