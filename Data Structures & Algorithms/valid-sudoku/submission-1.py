class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                square = (r // 3, c // 3)
                if cell in rows[r] or cell in cols[c] or cell in sqrs[square]:
                    print(f"cell: {cell}")
                    print(f"rows: {rows[r]}")
                    print(f"cols: {cols[c]}")
                    print(f"sqrs: {sqrs[square]}")
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                sqrs[square].add(cell)
        
        return True
