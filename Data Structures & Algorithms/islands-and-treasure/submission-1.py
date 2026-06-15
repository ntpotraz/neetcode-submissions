class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] != -1

        def bfs(row, col):
            q = deque([(row, col)])
            seen = set((row, col))
            steps = 0

            while q:
                length = len(q)
                for _ in range(length):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dy, dx in dirs:
                        nrow, ncol = dy + row, dx + col
                        if valid(nrow, ncol) and (nrow, ncol) not in seen:
                            seen.add((nrow, ncol))
                            q.append((nrow, ncol))
                steps += 1
            return 2147483647
        
        for row in range(m):
            for col in range(n):
                if valid(row, col):
                    grid[row][col] = bfs(row, col)
