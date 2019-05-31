import os


def clear():
    os.system('clear')


def get_symbol(value):
    if value < 0:
        return 'O'
    if value > 0:
        return 'X'
    return ' '


def print_board(board, movables=[], selected=(None, None)):
    for x in range(len(board)):
        for y in range(len(board[x])):
            symbol = get_symbol(board[x][y])
            tile_text = f'\t[{symbol}]'
            if (x, y) in movables:
                tile_text = f'{tile_text}({movables.index((x, y)) + 1})'
            if (x, y) == selected:
                tile_text = f'\033[5m{tile_text}\033[0m'
            print(f'{tile_text}', end='\t')
        print('\n')
    print('')


def get_player(number):
    if number == 1:
        return '1'
    if number == -1:
        return '2'
    return None


def get_player_choice(question, choices, player_team=0):
    if player_team != 0:
        input_text = f'PLAYER {get_player(player_team)} ({get_symbol(player_team)}) :\n{question}'
    else:
        input_text = question
    while True:
        choice = input(input_text)
        if choice in choices:
            return choice
        try:
            if int(choice) in choices:
                return int(choice)
        except ValueError:
            pass
        print("I didn't understood your answer. Try again.")


def print_success(board, winner):
    print(f'The player {get_player(winner)} has aligned 5 symbols. Game Won !')
