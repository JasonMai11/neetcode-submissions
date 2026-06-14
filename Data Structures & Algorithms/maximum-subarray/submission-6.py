class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadanes algorithm

        acc = 0
        maxSum = nums[0]

        for n in nums:
            acc = max(0, acc)
            acc += n
            maxSum = max(maxSum, acc)
        
        return maxSum