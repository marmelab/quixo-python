from copy import deepcopy
from game.constants import N_ROWS, N_COLS
from game.board import is_movable_tile

def move_row(board, row, y_start, y_end, value):
    board_copy = deepcopy(board)

    step = -1 if y_end > y_start else 1
    index_start = y_start - 1 if y_end > y_start else y_start + 1
    for y in range(y_end, index_start, step):
        prev_val = board_copy[row][y]
        board_copy[row][y] = value
        value = prev_val

    return board_copy


def move_col(board, line, x_start, x_end, value):
    board_copy = deepcopy(board)

    step = -1 if x_end > x_start else 1
    index_start = x_start - 1 if x_end > x_start else x_start + 1
    for x in range(x_end, index_start, step):
        prev_val = board_copy[x][line]
        board_copy[x][line] = value
        value = prev_val

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
