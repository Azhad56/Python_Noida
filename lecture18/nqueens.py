def queens(board, row, n):

    if row == n:
        print("solution mil gya")
        return

    for col in range(0, n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            queens(board, row+1, n)
            board[row][col] = False


def is_safe(board, row, col, n):

    max_steps = max(row, col)

    for step in range(1, max_steps + 1):

        # if we can go up
        if row - step >= 0:
            if board[row - step][col]:
                return False

            # let's check left diag
            if col - step >= 0:
                if board[row-step][col-step]:
                    return False

            # let's check right diag
            if col + step < n:
                if board[row - step][col + step]:
                    return False

    return True
board = [[False]*4 for i in range(4)]
print(queens(board,row=0,n=4))