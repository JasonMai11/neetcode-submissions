class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        acc = float('-inf')
        largest = float('-inf')
        for n in nums:
            if acc < 0:
                acc = n
            else:
                acc += n
            largest = max(largest, acc)

        return largest

                