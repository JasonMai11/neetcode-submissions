import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        counterNums = Counter(nums)
        
        for key in counterNums:
            heapq.heappush(arr, (counterNums[key], key))
            if len(arr) > k:
                heapq.heappop(arr)
        
        ret = []
        for _ in range(k):
            ret.append(heapq.heappop(arr)[1])
        return ret

        