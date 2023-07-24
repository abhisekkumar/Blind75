# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)-1):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - minPrice)
        return maxProfit


#optimize solution

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         minPrice = float('inf')
#         maxProfit = 0
#
#         for price in prices:
#             minPrice = min(minPrice, price)
#             maxProfit = max(maxProfit, price - minPrice)
#         return maxProfit
