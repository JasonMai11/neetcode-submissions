class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # return the number of different ways we can sum up to the target
        memo = {}

        def dp(i, acc):
            if acc == target and i == len(nums): # target seen case
                return 1
            elif i == len(nums): # out of bounds case
                return 0
            if (i, acc) in memo: # memo case
                return memo[(i, acc)]

            # add the number
            memo[(i, acc)] = dp(i + 1, acc + nums[i]) + dp(i + 1, acc - nums[i])

            return memo[(i, acc)]

        return dp(0, 0)