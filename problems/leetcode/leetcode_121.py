"""
Name: Best Time to Buy and Sell Stock
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Tags: #array
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = float('inf'), 0

        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i];
            elif (prices[i] - min_price) > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

    def maxProfitV2(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(0, len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)

        return max_profit

#
# s = Solution()
# p1 = [7, 1, 5, 3, 6, 4]  # 5
# p2 = [7, 6, 4, 3, 1]  # 0
# print(s.maxProfit(p1))
