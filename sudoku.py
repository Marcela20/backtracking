import numpy as np
import pprint

def generate_board():
    board = np.zeros((9,9))
    board[0][1] = 8
    board[8][8] = 8
    board[3][8] = 5
    board[3][7] = 8
    board[8][7] = 5

    return board


class Sudoku:

    def check_if_empty(self, board):
        not_empty = []
        for row in range(9):
            for c in range(9):
                if board[row][c] != 0:
                    not_empty.append((row, c))
        return not_empty

    def check_row(self, n, row, board):
        if n in board[row]:
            return False
        return True
            

    def check_column(self, n, col, board): 
        column = []
        for num in range(9):
            column.append(board[num][col])
        if n in column:
            return False
        return True

        
    def check_subboard(self, n, row, col_pos, board):
            row = row - (row%3)
            col_pos = col_pos - (col_pos%3)
            for r in range(3):
                for c in range(3):
                    if board[r+row][c+col_pos] == n:

                        return False
            return True
    def check_if_board_valid(self, board):
        not_empty = self.check_if_empty(board)
        not_empty_dict = {}
        for position in not_empty:
            not_empty_dict[position] = board[position[0]][position[1]]

        for pos, val in not_empty_dict.items():
            column = []
            for num in range(9):

                column.append(board[num][pos[1]])
            row = pos[0] - (pos[0]%3)
            col_pos = pos[1] - (pos[1]%3)
            square_positions = []
            for r in range(3):
                for c in range(3):
                    if board[r+row][c+col_pos] == val:
                        square_positions.append(val)
            if board[pos[0]].count(val) > 1 and column.count(val) > 1 and len(square_positions) > 1:
                return False
        return True 


    def solve_sudku(self, board):
        not_empty = self.check_if_empty(board)
        def backtrack(row, column):
            if column == 9:
                row += 1
                column = 0
            if row == 9:
                return True
            
            if (row, column) in not_empty:
                return backtrack(row, column +1)

            for digit in range(1, 10):
                if self.check_column(digit, column, board) and self.check_row(digit, row, board) and self.check_subboard(digit, row, column, board): 
                    board[row][column] = digit 

                    if backtrack(row, column +1):
                        return True
                board[row][column] = 0

            return False

        if self.check_if_board_valid(board):
            print(backtrack(0, 0))
            return board
        else:
            return 'not a valid board'

        


 
if __name__=="__main__":
    board = [[1, 0, 0, 3, 4, 5, 6, 7, 9],
            [3, 4, 5, 6, 7, 9, 8, 1, 2],
            [6, 7, 9, 1, 2, 8, 5, 3, 4,],
            [2, 1, 3, 4, 6, 7, 9, 8, 5],
            [4, 5, 6, 8, 9, 1, 7, 2, 3],
            [7, 9, 0, 5, 3, 2, 4, 6, 1],
            [8, 3, 1, 9, 5, 6, 2, 4, 7],
            [5, 2, 4, 7, 8, 3, 1, 9, 6],
            [9, 6, 7, 2, 1, 4, 3, 5, 8]]

    board_2 =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    board_3 = generate_board()
    inst = Sudoku()

    pprint.pprint(inst.solve_sudku(board))



