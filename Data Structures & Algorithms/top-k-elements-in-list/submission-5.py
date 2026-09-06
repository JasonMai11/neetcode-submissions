import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        counterNums = Counter(nums)
        for key,val in counterNums.items():
            arr.append([-val,key])

        heapq.heapify(arr)

        ret = []
        while k > 0:
            freq, num = heapq.heappop(arr)
            ret.append(num)
            k -= 1
        return ret

        