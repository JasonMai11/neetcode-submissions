class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}
        def dp(x):
            if x < 0:
                return 0
            if x == 0:
                return 1
            #return the number of distinct ways to climb to the target
            numberofways = dp(x - 1) + dp(x - 2)

            return numberofways

        return dp(n)