class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
       # there will always be an answer

       # common intuition: nested for loop O(n^2)

       hashmap = {}

       for i in range(len(nums)):
            n = nums[i]
            remainder = target - n
            if remainder in hashmap:
                return [hashmap[remainder], i]
            hashmap[n] = i

        