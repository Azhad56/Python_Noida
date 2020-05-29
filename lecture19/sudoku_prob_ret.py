import numpy as np


def sudoku(board, row=0, col=0):
    if row == 9:
        return [board.copy()]

    if col == 9:
        return sudoku(board, row + 1, 0)

    if board[row, col] != 0:
        return sudoku(board, row, col + 1)
    else:
        acc = []
        for item in range(1, 10):
            if isSafe(board, row, col, item):
                board[row, col] = item
                acc.extend(sudoku(board, row, col + 1))
                board[row, col] = 0

        return acc


def isSafe(board, row, col, item):
    if item in board[row, :]:
        return False

    if item in board[:, col]:
        return False

    row_s = row - (row % 3)
    col_s = col - (col % 3)
    cut = board[row_s:row_s + 3, col_s:col_s + 3]

    if item in cut:
        return False

    return True


grid = [[0, 0, 0, 0, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

arr = np.array(grid)
answers = sudoku(arr)
print(answers)
