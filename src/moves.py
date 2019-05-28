from copy import deepcopy
from board import is_movable_tile
from constants import N_ROWS, N_COLS


def move_row(board, row, y_start, y_end, value):
    board_copy = deepcopy(board)

    step = -1 if y_end > y_start else 1
    index_start = y_start - 1 if y_end > y_start else y_start + 1
    for y in range(y_end, index_start, step):
        prevVal = board_copy[row][y]
        board_copy[row][y] = value
        value = prevVal

    return board_copy


def move_col(board, line, x_start, x_end, value):
    board_copy = deepcopy(board)

    step = -1 if x_end > x_start else 1
    index_start = x_start - 1 if x_end > x_start else x_start + 1
    for x in range(x_end, index_start, step):
        prevVal = board_copy[x][line]
        board_copy[x][line] = value
        value = prevVal

    return board_copy


def move_tile(board, pos_start, pos_end, value):
    """Move a tile from a place to another one

    Arguments:
        board {Matrix} -- The game board
        pos_start {tupplet} -- The coord of the tile to be move
        pos_end {tupplet} -- The coord of the destination of the tile
        value {integer} -- The value affected to the tile

    Raises:
        GameException: Can't change the value of a not null tile
        GameException: Can't change the value of a not null tile
        GameException: Can't move the tile to an illegal position

    Returns:
        The game board
    """
    board_copy = deepcopy(board)

    (x, y) = pos_start
    (x_end, y_end) = pos_end

    if not is_movable_tile(x, y):
        raise Exception("Can't move a tile that is in the center of the board")

    if board_copy[x][y] != 0 and board_copy[x][y] != value:
        raise Exception(f"Can't change the value of tile {x} - {y}")

    if x == x_end:
        return move_row(board_copy, x, y, y_end, value)
    elif y == y_end:
        return move_col(board_copy, y, x, x_end, value)
    else:
        raise Exception("Can't move this tile to this position")


def get_opposite_tile(x, y):
    """Get opposite tile for the 1st version of the game

    Arguments:
        x {integer}
        y {integer}

    Raises:
        GameException: Can't move a tile that is in the center of the board
        GameException: Can't move a tile that is in the corner (for the moment)

    Returns:
        tupplet -- x & y coords of the opposing tile
    """

    if not is_movable_tile(x, y):
        raise Exception("Can't move a tile that is in the center of the board")

    if x == y or x == 0 and y == N_COLS or x == N_ROWS and y == 0:
        raise Exception("Can't move a tile that is in the corner (for the moment)")

    opposite_x = x
    opposite_y = y

    if x == 0:
        opposite_x = N_COLS - 1
    elif x == N_COLS - 1:
        opposite_x = 0

    if y == 0:
        opposite_y = N_ROWS - 1
    elif y == N_ROWS - 1:
        opposite_y = 0

    return (opposite_x, opposite_y)
