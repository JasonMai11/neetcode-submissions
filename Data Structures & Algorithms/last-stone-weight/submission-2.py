import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # choose the two heaviest stone and smash them together:
        # return the weight of the last stone

        res = 0
        arr = [-x for x in stones]
        heapq.heapify(arr)
        print(arr)
        while len(arr) >= 2:
            y, x = -heapq.heappop(arr), -heapq.heappop(arr)
            if x == y:
                continue
            elif x < y:
                heapq.heappush(arr, -(y - x))
            

        return -arr[0] if arr else 0