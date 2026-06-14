class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ret = 0

        for i in seen:
            if i-1 not in seen:
                acc = 0
                x = i
                while x in seen:
                    x += 1
                    acc += 1
                ret = max(ret, acc)
        return ret