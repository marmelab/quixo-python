def create_board():
    return [[0 for j in range(5)] for i in range(5)]


def get_symbol(value):
    if value < 0:
        return 'x'
    if value > 0:
        return 'o'
    return ' '


def print_board(board):
    for line in board:
        for tile in line:
            symbol = get_symbol(tile)
            print(f'[{symbol}]', end='')
        print('')
