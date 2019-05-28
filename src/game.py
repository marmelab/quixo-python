from moves import is_movable_tile, get_opposite_tile, move_tile
from board import create_board, print_board
import os

clear = lambda : os.system('clear')

def get_movables_tiles(board, player_value=0):
    """Get movable tiles with an associated number

    Arguments:
        board {Matrix} -- the board
        player_value {integer} -- -1 or 1 (cirle or cross)

    Returns:
        Dictionnary -- A dictionnary with coords in key and instruction in value
    """
    movable = {}
    n = 1
    for x in range(len(board)):
        for y in range(len(board[x])):
            value = board[x][y]
            if is_movable_tile(x, y) and (value == 0 or value == player_value):
                movable[(x, y)] = n
                n += 1

    return movable


def get_coords_from_movables(movables, n):
    for coord, number in movables.items():
        if number == n:
            return coord

    return None


def play():
    clear()
    player_team = 1
    board = create_board()
    while True:
        movables = get_movables_tiles(board, player_team)
        print_board(board, movables)
        player_input = int(input('Which tile do you want to move ?'))
        # check_input()
        (x_start, y_start) = get_coords_from_movables(movables, player_input)
        (x_end, y_end) = get_opposite_tile(x_start, y_start)
        board = move_tile(board, (x_start, y_start), (x_end, y_end), player_team)
        player_team *= -1
        clear()
