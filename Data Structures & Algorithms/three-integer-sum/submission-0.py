class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        nums.sort()

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            while j < k:
                curr = [nums[i], nums[j], nums[k]]
                if sum(curr) == 0:
                    ret.append(curr)
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif sum(curr) > 0:
                    k -= 1
                else:
                    j += 1
            
        return ret