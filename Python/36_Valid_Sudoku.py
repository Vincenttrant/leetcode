class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for x in range(9)]
        columns = [set() for x in range(9)]
        squares = [[set() for x in range(3)] for y in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in squares[i // 3][j // 3]:
                    return False
                
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                squares[i // 3][ j // 3].add(board[i][j])
        return True