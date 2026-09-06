class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in dictionary:
                return [dictionary[remainder], i]
            dictionary[nums[i]] = i
        return -1