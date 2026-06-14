class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # return the number of different ways we can sum up to the target
        memo = {}

        def dp(i, acc):
            if i == len(nums): # out of bounds
                return 1 if acc == target else 0 # target has been seen
            if (i, acc) in memo: # memo case
                return memo[(i, acc)]

            add = dp(i + 1, acc + nums[i]) # add the number
            subtract = dp(i + 1, acc - nums[i]) # subtract the number

            memo[(i, acc)] = add + subtract

            return memo[(i, acc)]

        return dp(0, 0)