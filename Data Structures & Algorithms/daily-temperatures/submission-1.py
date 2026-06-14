class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # at current index i, when is the next highest value in the array other than i

        stack = []
        res = [0] * (len(temperatures))

        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            # keep track of the temperature and the index 
            while stack and curr_temp > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((curr_temp, i))
        print(stack[-1][1])
        return res