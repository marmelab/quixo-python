from copy import deepcopy
from constants import N_ROWS, N_COLS, INDEX_LAST_ROW, INDEX_LAST_COL


def create_board():
    return [[0 for j in range(N_COLS)] for i in range(N_ROWS)]


def get_symbol(value):
    if value < 0:
        return 'X'
    if value > 0:
        return 'O'
    return ' '


def print_board(board, movables, selected = (None, None)):
    choice_number = 1
    for x in range(len(board)):
        for y in range(len(board[x])):
            symbol = get_symbol(board[x][y])
            if (x, y) in movables:
                tile_text = f'\t[{symbol}]({choice_number})'
                choice_number += 1
            else:
                tile_text = f'\t[{symbol}]'

            if (x, y) == selected:
                tile_text = f'\033[5m{tile_text}\033[0m'
            print(f'{tile_text}', end='\t')
        print('\n')
    print('')


def is_movable_tile(x, y):
    return x == 0 or y == 0 or x == N_ROWS - 1 or y == N_COLS - 1


def get_movables_tiles(board, player_value=0):
    """Get movable tiles with an associated number

    Arguments:
        board {Matrix} -- the board
        player_value {integer} -- -1 or 1 (cirle or cross)

    Returns:
        Dictionnary -- A dictionnary with coords in key and instruction in value
    """
    movable = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            value = board[x][y]
            if is_movable_tile(x, y) and (value == 0 or value == player_value):
                movable.append((x, y))

    return movable


def get_coords_from_movables(movables, n):
    if n < len(movables):
        return movables[n - 1]
    return None

def get_possibles_destinations(board, x, y, value):
    destinations = []
    is_available = lambda x, y: board[x][y] == 0 or board[x][y] == value

    print(x, y)
    if x == 0 or x == INDEX_LAST_ROW:
        if is_available(x, 0) and y != 0:
            destinations.append((x, 0))
        if is_available(x, INDEX_LAST_COL) and y != INDEX_LAST_COL:
            destinations.append((x, INDEX_LAST_COL))
        opposite = 0 if x == INDEX_LAST_ROW else INDEX_LAST_ROW
        if is_available(opposite, y):
            destinations.append((opposite, y))

    if y == 0 or y == INDEX_LAST_COL:
        if is_available(0, y) and x != 0:
            destinations.append((0, y))
        if is_available(INDEX_LAST_ROW, y) and x != INDEX_LAST_ROW:
            destinations.append((INDEX_LAST_COL, 4))
        opposite = 0 if x == INDEX_LAST_COL else INDEX_LAST_COL
        if is_available(x, opposite):
            destinations.append((x, opposite))

    return destinations


