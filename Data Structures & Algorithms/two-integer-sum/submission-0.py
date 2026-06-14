class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # common intuition: nested for loop => O(n^2) 
        dic = {}

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in dic:
                return [dic[remainder], i]
            else:
                dic[nums[i]] = i

    
        return [-1, -1]