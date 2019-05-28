from constants import N_ROWS, N_COLS


def create_board():
    return [[0 for j in range(N_COLS)] for i in range(N_ROWS)]


def get_symbol(value):
    if value < 0:
        return 'X'
    if value > 0:
        return 'O'
    return ' '


def print_board(board, instructions={}):
    for x in range(len(board)):
        for y in range(len(board[x])):
            symbol = get_symbol(board[x][y])
            instruction = instructions[(x, y)] if (x, y) in instructions else None
            tileText = f'\t[{symbol}]' if instruction is None else f'\t[{symbol}]({instruction})'
            print(f'{tileText}', end='\t')
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
