class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        seen = set()
        dirs = [(0, 1), (1,0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        
        def dfs(row, col):
            ans = 0
            for dy, dx in dirs:
                nrow, ncol = dy + row, dx + col
                if valid(nrow, ncol) and (nrow, ncol) not in seen:
                    seen.add((nrow, ncol))
                    ans += dfs(nrow, ncol) + 1
            return ans
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    max_area = max(max_area, dfs(row, col) + 1)
        
        return max_area
