class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mostWater = 0
        while l < r:
            minHeight = min(heights[l], heights[r])
            maxArea = minHeight * (r - l)
            mostWater = max(mostWater, maxArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return mostWater
