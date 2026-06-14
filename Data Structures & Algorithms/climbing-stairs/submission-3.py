class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}
        def dp(x):
            if x < 0:
                return 0
            if x == 0:
                return 1
            if x in cache:
                return cache[x]
            #return the number of distinct ways to climb to the target
            cache[x] = dp(x - 1) + dp(x - 2)

            return cache[x]

        return dp(n)