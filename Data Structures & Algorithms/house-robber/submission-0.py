class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, nums[0]

        for r in nums[1:]:
            temp = rob2
            rob2 = max(rob1 + r, rob2)
            rob1 = temp
        return rob2