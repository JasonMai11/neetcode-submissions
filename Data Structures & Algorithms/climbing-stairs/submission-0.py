class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def dp(steps):
            if steps in memo:
                return memo[steps]
            if steps == 0:
                return 1
            if steps < 0:
                return 0
            
            memo[steps] = dp(steps - 1) + dp(steps - 2)
            return memo[steps]
        return dp(n)