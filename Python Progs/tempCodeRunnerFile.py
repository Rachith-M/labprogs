def get_empty_cells(board1):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

print(get_empty_cells(board))