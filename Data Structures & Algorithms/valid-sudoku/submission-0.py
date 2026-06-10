class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[i][j]
                square = (i // 3, j // 3)

                if cell == ".":
                    continue
                
                if cell in rows[i] or cell in cols[j] or cell in squares[square]:
                    print(f"rows: {rows}")
                    print(f"cols: {cols}")
                    print(f"squares: {squares}")
                    return False
                rows[i].add(cell)
                cols[j].add(cell)
                squares[square].add(cell)
        print(f"rows: {rows}")
        print(f"cols: {cols}")
        print(f"squares: {squares}")

        return True
                