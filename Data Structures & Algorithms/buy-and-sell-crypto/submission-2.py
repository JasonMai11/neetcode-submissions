class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float('-inf')
        minStock = prices[0]

        for i in prices:
            maxProfit = max(maxProfit, i - minStock)
            minStock = min(minStock, i)

        return maxProfit
            