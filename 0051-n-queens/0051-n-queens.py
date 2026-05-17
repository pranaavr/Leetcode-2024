class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []

        posD = set() # r+c
        negD = set() # r-c
        col = set()

        board = [['.']*n for _ in range(n)]

        def dfs(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or r+c in posD or r-c in negD:
                    continue
                
                board[r][c] = "Q"
                posD.add(r+c)
                negD.add(r-c)
                col.add(c)
                dfs(r+1)
                posD.remove(r+c)
                negD.remove(r-c)
                col.remove(c)
                board[r][c] = "."
        
        dfs(0)
        return res

