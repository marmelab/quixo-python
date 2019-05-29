from moves import is_movable_tile, get_opposite_tile, move_tile
from board import create_board, print_board, get_movables_tiles, get_coords_from_movables, get_possibles_destinations, get_symbol
from constants import N_ROWS, N_COLS, INDEX_LAST_ROW, INDEX_LAST_COL
import os


def clear():
    os.system('clear')


def get_player_choice(question, choices, player_team=0):
    n_player = 1 if player_team == 1 else 2
    if player_team != 0:
        input_text = f'PLAYER {n_player} ({get_symbol(player_team)}) :\n{question}'
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


def check_diag(board, inverted=False):
    tiles_sum = 0
    for i in range(N_ROWS):
        x = i
        y = i if not inverted else INDEX_LAST_ROW - i
        tiles_sum += board[x][y]

    return tiles_sum == 5


def check_rows(board):
    for row in board:
        if sum(row) == 5:
            return True
    return False


def check_cols(board):
    # invert cols and rows
    inverted_board = list(map(list, zip(*board)))
    return check_rows(inverted_board)


def check_success(board):
    first_diag = check_diag(board)
    second_diag = check_diag(board, True)
    rows = check_rows(board)
    cols = check_cols(board)

    return first_diag or second_diag or rows or cols


def print_success(board):
    print_board(board)
    print('The player 1 has aligned 5 cross. Game Won !')


def play():
    player_team = 1
    board = create_board()
    while True:
        clear()

        if check_success(board):
            print_success(board)
            break

        movables = get_movables_tiles(board, player_team)
        print_board(board, movables)

        movables_choices = list(range(1, len(movables) + 1))
        player_input = get_player_choice('Tile to move : ', movables_choices, player_team)

        clear()

        (x_start, y_start) = get_coords_from_movables(movables, player_input)

        destinations = get_possibles_destinations(board, x_start, y_start)
        print_board(board, destinations, (x_start, y_start))

        destinations_choices = list(range(1, len(destinations) + 1))
        destination_input = get_player_choice('Destination of the tile : ', destinations_choices, player_team)

        (x_end, y_end) = get_coords_from_movables(destinations, destination_input)
        board = move_tile(board, (x_start, y_start), (x_end, y_end), player_team)

        player_team *= -1
