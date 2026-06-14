
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dictionary k = occurences, v = integer
        # add occurrences into a heap
        # pop the k most elements from the heap and add it into the return lst

        from collections import Counter
        import heapq

        counterNums = Counter(nums)
        lst, ret = [], []
        
        for t in counterNums:
            v = counterNums[t]
            heapq.heappush(lst, [-v, t])

        while k > 0:
            x = heapq.heappop(lst)
            ret.append(x[1])
            k -= 1
            
        return ret
        
        