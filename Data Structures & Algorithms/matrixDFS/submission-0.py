class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        paths = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 1 or (r, c) in paths:
                return 0
            elif (r, c) == (len(grid) - 1, len(grid[0]) - 1):
                return 1  

            paths.add((r, c))
            res = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            paths.remove((r, c))

            return res

        return dfs(0, 0)