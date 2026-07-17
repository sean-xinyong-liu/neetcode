class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == '.':
                    continue
                row_entry = ('r', row, value)
                col_entry = ('c', col, value)
                box_entry = ('b', row // 3, col //3, value)
                if (row_entry in seen or
                   col_entry in seen or 
                   box_entry in seen):
                   return False
                seen.add(row_entry)
                seen.add(col_entry)
                seen.add(box_entry)
        return True
     