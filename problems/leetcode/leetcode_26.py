"""
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
tag: #array, #two-pointers
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next = 1
        i = 1
        n = len(nums)
        while i < n:
            if nums[i] != nums[next - 1]:
                nums[next] = nums[i]
                next = next + 1
            i = i + 1
        return next

#
# s = Solution()
# a = [2, 2, 3, 4, 6, 8, 8, 9, 9, 13, 13, 13, 19, 21]
# print(id(a))
# print(s.removeDuplicates(a))
# print(id(a))
# print(a)
