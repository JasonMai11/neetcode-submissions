class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom-up solution w/ memoization

        memo = {}
        def dp(steps): 

            # base case
            if steps >= len(cost) - 2:
                return 0

            if steps in memo:
                return memo[steps]

            onestep = cost[steps + 1] + dp(steps + 1)
            twostep = cost[steps + 2] + dp(steps + 2)

            memo[steps] = min(onestep, twostep)

            return memo[steps]

        return dp(-1)

