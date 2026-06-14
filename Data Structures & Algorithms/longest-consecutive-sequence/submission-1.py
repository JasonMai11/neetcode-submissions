class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for i in nums:
            acc=0
            f=i
            while f in nums:
                f += 1
            res = max(res, f-i)
        return res