class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = float('-inf')
        minstock = float('inf')
        for p in prices:
            minstock = min(minstock, p)
            maxProf = max(maxProf, p - minstock)

        return maxProf