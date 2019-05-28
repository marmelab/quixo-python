def create_board():
    return [[0 for j in range(5)] for i in range(5)]


def get_symbol(value):
    if value < 0:
        return 'x'
    if value > 0:
        return 'o'
    return ' '


def print_board(board, instructions={}):
    for x in range(len(board)):
        for y in range(len(board[x])):
            symbol = get_symbol(board[x][y])
            instruction = instructions[(x, y)] if (x, y) in instructions else None
            tileText = f'\t[{symbol}]' if instruction is None else f'\t({instruction})[{symbol}]'
            print(f'{tileText}', end='\t')
        print('\n')
    print('')
