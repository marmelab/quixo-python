from moves import is_movable_tile, get_opposite_tile, move_tile
from board import create_board, print_board, get_movables_tiles, get_coords_from_movables
import os


def clear():
    os.system('clear')


def get_player_choice(question, choices):
    while True:
        choice = input(question)
        if choice in choices:
            return choice
        try:
            if int(choice) in choices:
                return int(choice)
        except ValueError:
            pass
        print("I didn't understood your answer. Try again.")


def play():
    clear()
    player_team = 1
    board = create_board()
    while True:
        movables = get_movables_tiles(board, player_team)
        print_board(board, movables)

        player_choices = movables.values()
        player_input = get_player_choice('Tile to move : ', player_choices)

        (x_start, y_start) = get_coords_from_movables(movables, player_input)
        (x_end, y_end) = get_opposite_tile(x_start, y_start)

        board = move_tile(board, (x_start, y_start), (x_end, y_end), player_team)
        player_team *= -1
        clear()
