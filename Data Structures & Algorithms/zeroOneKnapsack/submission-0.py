class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        def dp(i, capacity):
            max_profit = 0

            if (i, capacity) in memo:
                return memo[(i, capacity)]
            if i == len(profit): # out of bounds checking
                return 0
                
            memo[(i, capacity)] = dp(i + 1, capacity)

            if capacity - weight[i] >= 0: # we can take the item
                p = profit[i] + dp(i + 1, capacity - weight[i])
                memo[(i, capacity)] = max(memo[(i, capacity)], p)

            return memo[(i, capacity)]

        return dp(0, capacity)
