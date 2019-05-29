from moves import is_movable_tile, get_opposite_tile, move_tile
from board import create_board, print_board, get_movables_tiles, get_coords_from_movables, get_possibles_destinations
import os


def clear():
    os.system('clear')


def get_player_choice(question, choices):
    while True:
        choice = input(question)
        print(choice, choices)
        if choice in choices:
            return choice
        try:
            if int(choice) in choices:
                return int(choice)
        except ValueError:
            pass
        print("I didn't understood your answer. Try again.")


def play():
    player_team = 1
    board = create_board()
    while True:
        clear()

        movables = get_movables_tiles(board, player_team)
        print_board(board, movables)

        movables_choices = list(range(1, len(movables) + 1))
        player_input = get_player_choice('Tile to move : ', movables_choices)

        clear()

        (x_start, y_start) = get_coords_from_movables(movables, player_input)

        destinations = get_possibles_destinations(board, x_start, y_start, player_team)
        print_board(board, destinations, (x_start, y_start))

        destinations_choices = list(range(1, len(destinations) + 1))
        destination_input = get_player_choice('Destination of the tile : ', destinations_choices)

        (x_end, y_end) = get_coords_from_movables(destinations, destination_input)

        board = move_tile(board, (x_start, y_start), (x_end, y_end), player_team)

        player_team *= -1
