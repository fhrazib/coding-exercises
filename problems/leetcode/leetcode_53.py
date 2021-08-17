"""
Name: Maximum Subarray
URL: https://leetcode.com/problems/maximum-subarray/
Tags: #array
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        new_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            new_sum = max(nums[i], nums[i] + new_sum)
            max_sum = max(new_sum, max_sum)
        return max_sum

    def maxSubArrayV2(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                # print(i, ': ', nums[i:j + 1])
                _sum = sum(nums[i:j + 1])
                max_sum = max(_sum, max_sum)

        return max_sum

#
# s = Solution()
# a = [1, 2, 3, 4, 5, 6]  # 21
# b = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # 6
# c = [5, 4, -1, 7, 8]  # 23
# d = [1]  # 1
# result = s.maxSubArray(d)
# print(result)

