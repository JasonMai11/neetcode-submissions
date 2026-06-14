class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        ret = 0

        while l < r:
            hL = heights[l]
            hR = heights[r]

            ar = min(hL, hR)
            area = ar * (r - l)
            ret = max(ret, area)

            if hL < hR:
                l += 1
            else:
                r -= 1

        return ret