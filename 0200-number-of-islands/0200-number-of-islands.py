class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def sink(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == '1':
                grid[r][c] = '0'
                sink(r+1, c)
                sink(r-1, c)
                sink(r, c+1)
                sink(r, c-1)

        
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    sink(i, j)
                    islands += 1

        return islands
        