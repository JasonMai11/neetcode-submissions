class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        t = list(zip(position, speed))
        t.sort()
        times = []
        for i in t:
            times.append((target - i[0]) / i[1])
        
        fleet = float('-inf')
        res = 0
        for i in range(len(times) - 1, -1, -1):
            if fleet < times[i]:
                fleet = times[i]
                res += 1

        print(times)
        return res
