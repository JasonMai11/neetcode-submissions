class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix, postfix
        ret = [1] * len(nums)
        prefix = 1

        for i in range(len(nums) - 1):
            ret[i + 1] = prefix * nums[i]
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            ret[i] *= postfix
            postfix *= nums[i]

        return ret
