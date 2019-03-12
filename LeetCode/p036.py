class Solution(object):
    def isValidSudoku(self, board):
        row_sets = [set() for x in range(9)]
        col_sets = [set() for x in range(9)]
        box_sets = [[set() for x in range(3)] for y in range(3)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                number = int(board[i][j])
                box_row = i // 3
                box_col = j // 3
                if number in row_sets[i] or number in col_sets[j] or number in box_sets[box_row][box_col]:
                    return False
                row_sets[i].add(number)
                col_sets[j].add(number)
                box_sets[box_row][box_col].add(number)

        return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
print(sol.isValidSudoku(board))