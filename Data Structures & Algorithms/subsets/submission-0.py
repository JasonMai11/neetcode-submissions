class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # decision to take or not take the value at hand

        res = []
        def backtrack(i, ret):
            if i >= len(nums):
                res.append(ret.copy())
                return

            # take the value
            ret.append(nums[i])
            backtrack(i + 1, ret)
            # don't take the value
            ret.pop()
            backtrack(i + 1, ret)
        backtrack(0, [])
        return res