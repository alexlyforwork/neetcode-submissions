class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROW,COL = len(board),len(board[0])
        def backtrack(r,c,i):
            if i==len(word)-1:
                return True if board[r][c]==word[i] else False
            if board[r][c]!=word[i]:
                return False
            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            for dr, dc in directions:
                next_dr, next_dc = r+dr, c+dc
                if (not (0<=next_dr<ROW and 0<=next_dc<COL)) or (next_dr,next_dc) in visited:
                    continue
                visited.add((next_dr,next_dc))
                if backtrack(next_dr,next_dc,i+1):
                    return True
                visited.remove((next_dr,next_dc))
        for r in range(ROW):
            for c in range(COL):
                visited.add((r,c))
                if backtrack(r,c,0):
                    return True          
                visited.remove((r,c))
        return False
            