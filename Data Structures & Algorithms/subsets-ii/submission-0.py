class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        def backtrack(i, ret):
            if i >= len(nums):
                subset = ret.copy()
                if tuple(sorted(subset)) not in seen:
                    seen.add(tuple(sorted(subset)))
                    res.append(ret.copy())
                return

            # take the current
            ret.append(nums[i])
            backtrack(i + 1, ret)
            # don't take the current
            ret.pop()
            backtrack(i + 1, ret)

        backtrack(0, [])
        return res