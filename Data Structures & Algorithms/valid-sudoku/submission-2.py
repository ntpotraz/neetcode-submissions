class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                sqr = (i // 3, j // 3)
                if cell in rows[i] or cell in cols[j] or cell in sqrs[sqr]:
                    return False
                rows[i].add(cell)
                cols[j].add(cell)
                sqrs[sqr].add(cell)

        return True
