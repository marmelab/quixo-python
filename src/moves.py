def move_row(board, row, yFrom, yTo, value):
    step = -1 if yTo > yFrom else 1
    for y in range(yTo, yFrom - 1, step):
        prevVal = board[row][y]
        board[row][y] = value
        value = prevVal

    return board


def move_line(board, line, xFrom, xTo, value):
    step = -1 if xTo > xFrom else 1
    for x in range(xTo, xFrom - 1, step):
        prevVal = board[x][line]
        board[x][line] = value
        value = prevVal

    return board


def move_tile(board, posFrom, posTo, value):
    """Move a tile from a place to another one

    Arguments:
        board {Matrix} -- The game board
        posFrom {tupplet} -- The coord of the tile to be move
        posTo {[type]} -- The coord of the destination of the tile
        value {[type]} -- The value affected to the tile

    Raises:
        GameException: Can't change the value of a not null tile
        GameException: Can't move the tile to an illegal position

    Returns:
        The game board
    """

    (x, y) = posFrom
    (xTo, yTo) = posTo

    if board[x][y] != 0 and board[x][y] != value:
        raise Exception(f"You can't change the value of tile {x} - {y}")

    if x == xTo:
        return move_row(board, x, y, yTo, value)
    elif y == yTo:
        return move_line(board, y, x, xTo, value)
    else:
        raise Exception("Can't move this tile to this position")
