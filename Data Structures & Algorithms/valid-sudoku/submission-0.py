class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkRow(board):
            for i in range(len(board)):
                row = set()
                for j in range(len(board[i])):
                    if board[i][j] != '.' and board[i][j] not in row:
                        row.add(board[i][j])
                    elif board[i][j] != '.':
                        return False
            return True
        
        def checkCol(board):
            for i in range(len(board)):
                col = set()
                for j in range(len(board[i])):
                    if board[j][i] != '.' and board[j][i] not in col:
                        col.add(board[j][i])
                    elif board[j][i] != '.':
                        return False
            return True
        
        def checkGrid(board):
            for grid_ind in range(9):
                grid = set()
                for pos in range(9):
                    row = (grid_ind // 3) * 3 + (pos // 3)
                    col = (grid_ind % 3) * 3 + (pos % 3)
                    if board[row][col] != '.' and board[row][col] not in grid:
                        grid.add(board[row][col])
                    elif board[row][col] != '.':
                        return False
            return True
        
        return checkRow(board) and checkCol(board) and checkGrid(board)
            