class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ans = 0
        seen = set()
        dirs = [(0,1), (1,0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])


        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"
        
        def dfs(row, col):
            for dy, dx in dirs:
                n_row, n_col = dy + row, dx + col
                if valid(n_row, n_col) and (n_row, n_col) not in seen:
                    seen.add((n_row, n_col))
                    dfs(n_row, n_col)
                
            
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in seen:
                    dfs(row, col)
                    ans += 1
        return ans
