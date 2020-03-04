import numpy as np


def is_safe(board, row, col, item):
    if item in board[row,:]:
        return False
    if item in board[col,:]:
        return False
    r_s = row - (row%3)
    c_s = col -(col%3)
    cut = board[r_s:r_s+3,c_s:c_s+3]
    if item in cut:
        return False
    return True
def sudoku(board,row,col):
    if row==9:
        print(board)
        return
    if col==9:
        sudoku(board,row+1,0)
        return
    if board[row,col] != 0:
        sudoku(board,row,col+1)
    else:
        for item in range(1,10):
            if is_safe(board,row,col,item):
                board[row,col] = item
                sudoku(board,row,col+1)
                board[row,col] = 0


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

arr = np.array(grid)
sudoku(arr)