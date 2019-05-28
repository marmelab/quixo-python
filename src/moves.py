from constants import N_ROWS, N_COLS


def move_row(board, row, yFrom, yTo, value):
    step = -1 if yTo > yFrom else 1
    for y in range(yTo, yFrom - 1, step):
        prevVal = board[row][y]
        board[row][y] = value
        value = prevVal

    return board


def move_col(board, line, xFrom, xTo, value):
    step = -1 if xTo > xFrom else 1
    for x in range(xTo, xFrom - 1, step):
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
    (xTo, yTo) = posTo

    if not check_allowed_tile(x, y):
        raise Exception("can't move a tile that is in the center of the board")

    if board[x][y] != 0 and board[x][y] != value:
        raise Exception(f"Can't change the value of tile {x} - {y}")

    if x == xTo:
        return move_row(board, x, y, yTo, value)
    elif y == yTo:
        return move_col(board, y, x, xTo, value)
    else:
        raise Exception("Can't move this tile to this position")
