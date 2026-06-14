class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = float('-inf')
        curr = 0
        for i in nums:
            if curr < i and curr < 0: # we don't want to add a negative to the current
                curr = i
            else:
                curr += i
            ret = max(ret, curr)
        return ret
