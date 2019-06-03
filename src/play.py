import game.board as Board
import game.success as Success
import game.moves as Moves
import cursesio as Ui
import playerio as Ui_term
from curses import wrapper
import curses
import sys


def launch_game_simple():
    player_team = 1
    board = Board.create_board()
    while True:
        Ui_term.clear()

        movables = Board.get_movables_tiles(board, player_team)
        Ui_term.print_board(board, movables)

        movables_choices = list(range(1, len(movables) + 1))
        player_input = Ui_term.get_player_choice('Tile to move : ', movables_choices, player_team)

        Ui_term.clear()

        (x_start, y_start) = Board.get_coords_from_movables(movables, player_input)

        destinations = Board.get_possibles_destinations(board, x_start, y_start)
        Ui_term.print_board(board, destinations, (x_start, y_start))

        destinations_choices = list(range(1, len(destinations) + 1))
        destination_input = Ui_term.get_player_choice('Destination of the tile : ', destinations_choices, player_team)

        (x_end, y_end) = Board.get_coords_from_movables(destinations, destination_input)
        board = Moves.move_tile(board, (x_start, y_start), (x_end, y_end), player_team)

        winner = Success.check_success(board, player_team)
        if winner != 0:
            Ui_term.clear()
            Ui_term.print_board(board)
            Ui_term.print_success(board, winner)
            break

        player_team *= -1


def launch_game_curses(stdscr):
    Ui.init_curses()

    player_team = 1
    board = Board.create_board()
    while True:
        Ui.clear(stdscr)

        movables = Board.get_movables_tiles(board, player_team)

        (x_start, y_start) = Ui.get_player_selection(stdscr, board, player_team, movables)

        destinations = Board.get_possibles_destinations(board, x_start, y_start)

        (x_end, y_end) = Ui.get_player_selection(stdscr, board, player_team, destinations, (x_start, y_start))

        board = Moves.move_tile(board, (x_start, y_start), (x_end, y_end), player_team)

        winner = Success.check_success(board, player_team)
        if winner != 0:
            Ui.clear(stdscr)
            Ui.print_board(stdscr, board)
            Ui.print_winner(stdscr, winner)
            break

        player_team *= -1


def launch_game():
    if len(sys.argv) > 1 and sys.argv[1] == '-simple':
        launch_game_simple()
    else:
        try:
            wrapper(launch_game_curses)
        except curses.error:
            print('Your terminal seems to not be supported for the "good looking" version. Try to make it bigger')
            choice = input('Do you want to play the "simplified" version ? (y/n) ')
            if choice == 'y':
                launch_game_simple()
            else:
                print('Ok, bye.')
