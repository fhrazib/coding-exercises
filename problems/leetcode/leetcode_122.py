"""
Name: Best Time to Buy and Sell Stock II
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Tags: #array
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0

        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i = i + 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i = i + 1
            peak = prices[i]
            max_profit = max_profit + (peak - valley)

        return max_profit


# s = Solution()
# a = [7, 1, 5, 3, 6, 4]  # 7
# b = [1, 2, 3, 4, 5]  # 4
# c = [7, 6, 4, 3, 1]  # 0
# print(s.maxProfit(a))


