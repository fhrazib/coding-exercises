"""
Name: Two Sum II - Input array is sorted
URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sort
Tags: #array, #two-pointers
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []

        start = 0
        end = len(numbers) - 1
        while start <= end:
            _sum = numbers[start] + numbers[end]
            if target == _sum:
                result = [start + 1, end + 1]
                break
            elif _sum > target:
                end = end - 1
            elif _sum < target:
                start = start + 1

        return result

#
# s = Solution()
# a, at = [2, 7, 11, 15], 9  # [1, 2]
# b, bt = [2, 3, 4], 6  # [1, 3]
# c, ct = [-1, 0], -1  # [1, 2]
# print(s.twoSum(a, at))

