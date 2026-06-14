class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        from collections import defaultdict
        rowSet, colSet, boxSet = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != '.': 
                    num = board[r][c]
                    box = (r // 3, c // 3)
                    if num in rowSet[r] or num in colSet[c] or num in boxSet[box]:
                        return False                
                    else:
                        rowSet[r].add(num)
                        colSet[c].add(num)
                        boxSet[box].add(num)

        return True

