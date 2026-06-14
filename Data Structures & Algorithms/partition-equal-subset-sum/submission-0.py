class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        capacity = sum(nums) / 2

        memo = {}

        # if we find a subarray that equals to the cap, return True
        def dp(i, capacity):
            if (i, capacity) in memo: # memoization type
                return memo[(i, capacity)]
            if capacity == 0: # we found a sub array 
                return True
            if i == len(nums): # out of bounds checking
                return False

            take = dp(i + 1, capacity) # don't take
            memo[(i, capacity)] = take
            if capacity - nums[i] >= 0:
                dont = dp(i + 1, capacity - nums[i])
                memo[(i, capacity)] = take or dont
            return memo[(i, capacity)]

        return dp(0, capacity)
            