import game.board as Board
import game.success as Success
import game.moves as Moves
# import playerio as Io
import cursesio as Io
from curses import wrapper
import curses


def init_curses():
    # curses.nonl()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)


def launch_game(stdscr):
    init_curses()

    player_team = 1
    board = Board.create_board()
    while True:
        Io.clear(stdscr)

        movables = Board.get_movables_tiles(board, player_team)

        (x_start, y_start) = Io.get_player_selection(stdscr, board, movables)

        destinations = Board.get_possibles_destinations(board, x_start, y_start)

        (x_end, y_end) = Io.get_player_selection(stdscr, board, destinations, (x_start, y_start))

        board = Moves.move_tile(board, (x_start, y_start), (x_end, y_end), player_team)

        winner = Success.check_success(board, player_team)
        if winner != 0:
            Io.clear(stdscr)
            Io.print_board(stdscr, board)
            Io.print_winner(winner)
            break

        player_team *= -1
        # Io.clear()

        # Io.print_board(board, movables)

        # movables_choices = list(range(1, len(movables) + 1))
        # player_input = Io.get_player_choice('Tile to move : ', movables_choices, player_team)

        # Io.clear()

        # (x_start, y_start) = Board.get_coords_from_movables(movables, player_input)

        # destinations = Board.get_possibles_destinations(board, x_start, y_start)
        # Io.print_board(board, destinations, (x_start, y_start))

        # destinations_choices = list(range(1, len(destinations) + 1))
        # destination_input = Io.get_player_choice('Destination of the tile : ', destinations_choices, player_team)

        # (x_end, y_end) = Board.get_coords_from_movables(destinations, destination_input)
        # board = Moves.move_tile(board, (x_start, y_start), (x_end, y_end), player_team)



        # player_team *= -1

wrapper(launch_game)
