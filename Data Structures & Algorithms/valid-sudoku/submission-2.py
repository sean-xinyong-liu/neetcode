class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == '.':
                    continue
                if (value in rows[row] or
                    value in cols[col] or
                    value in boxes[(row // 3, col //3)]):
                    return False
                rows[row].add(value)
                cols[col].add(value)
                boxes[row // 3, col // 3].add(value)
        return True