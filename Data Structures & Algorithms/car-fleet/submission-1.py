class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # calculate the number of seconds it will take for the car to hit the target
        # traverse the cars backwards
        
        cars = [0] * len(position)
        stack = []
        for i in range(len(position)):
            cars[i] = [position[i], ((target - position[i]) / speed[i])]

        cars.sort()

        for i in range(len(cars) - 1, -1, -1):
            if not stack or cars[i][1] > stack[-1]:
                stack.append(cars[i][1])
            else:
                continue

        return len(stack)
            

