class Solution:
    def updateBoard(self, board, click):
        row = click[0]
        col = click[1]
        
        if self.is_mine(board, row, col):
            board[row][col] = 'X'
            return board
        
        adjacent_mines = 0
        adjacent_empties = []
        board[row][col] = 'B'

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                elif self.is_mine(board, row + i, col + j):
                    adjacent_mines += 1
                elif self.is_empty(board, row + i, col + j):
                    adjacent_empties.append([row + i, col + j])
        
        if adjacent_mines > 0:
            board[row][col] = str(adjacent_mines)
            return board

        for adjacent in adjacent_empties:
            board = self.updateBoard(board, adjacent)

        return board

    
    def is_mine(self, board, row, col):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        return board[row][col] == 'M'
    
    def is_empty(self, board, row, col):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        return board[row][col] == 'E'
        


board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3, 0]
sol = Solution()
print(sol.updateBoard(board, click))