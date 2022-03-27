import numpy as np

class NQueens():
    def solve_n_queens(self, n):
        cols = set()
        neg_diag = set() #r-c
        pos_diag = set() #r+c
        board = np.zeros((n, n))
        res = []

        def backtrack(r):
            if r == n:
                copy = board.copy()
                res.append(copy)
                return 
            for column_field in range(n):
                if column_field not in cols and r- column_field not in neg_diag and r + column_field not in pos_diag:
                    board[r][column_field] = 1
                    cols.add(column_field)
                    neg_diag.add(r-column_field)
                    pos_diag.add(r+column_field)

                    backtrack(r+1)

                    cols.remove(column_field)
                    neg_diag.remove(r-column_field)
                    pos_diag.remove(r+column_field)
                    board[r][column_field] = 0

        backtrack(0)
        return res
inst = NQueens()
print(inst.solve_n_queens(8))
