def queens(board,row,n):
    if row == n:
        print("Solution mil gya")
        return
    for col in range(0,n):
        if is_safe(board,row,col,n):
            board[row][col] = True
            queens(board,row+1,n)
            board[row][col] = False
def is_safe(board,row,col,n):
    for i in range(0,col):
        if board[row][i]:
            return False
    steps = min(row,col)
    for step in steps:
        if board[row-step][col-step]:
            return False
    steps = min(row,)
