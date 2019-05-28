from constants import N_ROWS, N_COLS


def move_row(board, row, y_from, y_to, value):
    step = -1 if y_to > y_from else 1
    for y in range(y_to, y_from - 1, step):
        prevVal = board[row][y]
        board[row][y] = value
        value = prevVal

    return board


def move_col(board, line, x_from, x_to, value):
    step = -1 if x_to > x_from else 1
    for x in range(x_to, x_from - 1, step):
        prevVal = board[x][line]
        board[x][line] = value
        value = prevVal

    return board


def check_allowed_tile(x, y):
    """Check if a tile is allowed to be moved (On the edge of the board)

    Arguments:
        x {integer}
        y {integer}

    Returns:
        boolean -- true if move is allowed
    """
    return x == 0 or y == 0 or x == N_ROWS - 1 or y == N_COLS - 1


def move_tile(board, posFrom, posTo, value):
    """Move a tile from a place to another one

    Arguments:
        board {Matrix} -- The game board
        posFrom {tupplet} -- The coord of the tile to be move
        posTo {[type]} -- The coord of the destination of the tile
        value {[type]} -- The value affected to the tile

    Raises:
        GameException: Can't change the value of a not null tile
        GameException: Can't change the value of a not null tile
        GameException: Can't move the tile to an illegal position

    Returns:
        The game board
    """

    (x, y) = posFrom
    (x_to, y_to) = posTo

    if not check_allowed_tile(x, y):
        raise Exception("Can't move a tile that is in the center of the board")

    if board[x][y] != 0 and board[x][y] != value:
        raise Exception(f"Can't change the value of tile {x} - {y}")

    if x == x_to:
        return move_row(board, x, y, y_to, value)
    elif y == y_to:
        return move_col(board, y, x, x_to, value)
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

    if not check_allowed_tile(x, y):
        raise Exception("Can't move a tile that is in the center of the board")

    if x == y or x == 0 and y == 4 or x == 4 and y == 0:
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

