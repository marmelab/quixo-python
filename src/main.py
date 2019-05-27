from board import create_board, print_board
from moves import move_tile

board = create_board()

board = move_tile(board, (0, 0), (0, 4), 1)
board = move_tile(board, (0, 0), (0, 4), 1)
board = move_tile(board, (0, 0), (0, 4), 1)
board = move_tile(board, (0, 0), (0, 4), 1)
board = move_tile(board, (0, 0), (0, 4), -1)
board = move_tile(board, (0, 4), (4, 4), -1)
board = move_tile(board, (4, 0), (4, 4), 1)
board = move_tile(board, (0, 4), (4, 4), -1)
print_board(board)
