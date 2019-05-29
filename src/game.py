from moves import is_movable_tile, get_opposite_tile, move_tile
from board import create_board, print_board, get_movables_tiles, get_coords_from_movables, get_possibles_destinations, get_symbol
from constants import N_ROWS, N_COLS, INDEX_LAST_ROW, INDEX_LAST_COL
import os


def clear():
    os.system('clear')


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


def get_winner(total):
    requirement = N_ROWS
    if total == requirement:
        return 1
    if -total == requirement:
        return -1
    return 0


def check_diag(board, inverted=False):
    sum_diag = 0
    for i in range(N_ROWS):
        x = i
        y = i if not inverted else INDEX_LAST_ROW - i
        sum_diag += board[x][y]

    return get_winner(sum_diag)


def check_rows(board):
    sum_row = 0
    for row in board:
        winner = get_winner(sum(row))
        if (winner != 0):
            return winner

    return get_winner(sum_row)


def check_cols(board):
    # invert cols and rows
    inverted_board = list(map(list, zip(*board)))
    return check_rows(inverted_board)


def check_success(board):
    """
    Arguments:
        board
    Returns:
        integer -- 0 if no winner else value of winner
    """
    first_diag = check_diag(board)
    second_diag = check_diag(board, True)
    rows = check_rows(board)
    cols = check_cols(board)
    for result in [first_diag, second_diag, rows, cols]:
        if result != 0:
            return result
    return 0


def print_success(board, winner):
    print_board(board)
    print(f'The player {get_player(winner)} has aligned 5 symbols. Game Won !')


def play():
    player_team = 1
    board = create_board()
    while True:
        clear()

        winner = check_success(board)
        if winner != 0:
            print_success(board, winner)
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
