"""
Name: Plus One
URL: https://leetcode.com/problems/plus-one/
Tags: #array, #stack
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # print(digits)

        carry = 1
        result = []
        for digit in reversed(digits):
            _sum = digit + carry
            if _sum >= 10:
                carry = 1
                result.append(0)
            else:
                carry = 0
                result.append(_sum)
        result.reverse()
        if result[0] == 0:
            result = [1] + result
        # print(result)
        return result

#
# s = Solution()
# a = [1, 2, 3]
# b = [4, 3, 2, 1]
# c = [1, 2, 8, 9]
# e = [1, 2, 8, 9, 9]
# f = [9, 9, 9]
# g = [0]
# s.plusOne(g)
