class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                # topleft
                temp = matrix[top][l + i]
                
                # topleft <- botleft
                matrix[top][l + i] = matrix[bottom - i][l]
                # botleft <- botright
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # botright <- topright
                matrix[bottom][r - i] = matrix[top + i][r]
                # topright <- topleft
                matrix[top + i][r] = temp

            r -= 1
            l += 1
                
    