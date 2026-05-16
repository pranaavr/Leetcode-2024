class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # bfs
        def rot(r, c, time):
            # in bounds and is an orange
            if 0 <= r < m and 0 <= c < n:
                # time == 2 is the start condition
                # only bfs on fresh oranges
                if grid[r][c] == 1 or time == 2 or time < grid[r][c]:
                    grid[r][c] = time

                    rot(r+1, c, time+1)
                    rot(r-1, c, time+1)
                    rot(r, c+1, time+1)
                    rot(r, c-1, time+1)

        # multi source
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rot(i, j, 2)
        
        maxT = 2
        for row in grid:
            if 1 in row:
                return -1
            maxT = max(maxT, max(row))
        return maxT-2