class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = time = 0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def valid(row, col):
            return 0<=row<m and 0<=col<n and grid[row][col] == 1

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        
        while fresh > 0 and q:
            length = len(q)
            time += 1
            for _ in range(length):
                row, col = q.popleft()
    
                for dy, dx in dirs:
                    nrow, ncol = dy + row, dx + col
                    if valid(nrow, ncol):
                        grid[nrow][ncol] = 2
                        q.append((nrow, ncol))
                        fresh -= 1
        
        return time if fresh == 0 else -1

