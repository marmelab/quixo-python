import game.board as Board
import game.success as Success
import game.moves as Moves
import cursesio as Io
from curses import wrapper
import curses


def init_curses():
    # curses.nonl()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)


def launch_game_curses(stdscr):
    init_curses()

    player_team = 1
    board = Board.create_board()
    while True:
        Io.clear(stdscr)

        movables = Board.get_movables_tiles(board, player_team)

        (x_start, y_start) = Io.get_player_selection(stdscr, board, player_team, movables)

        destinations = Board.get_possibles_destinations(board, x_start, y_start)

        (x_end, y_end) = Io.get_player_selection(stdscr, board, player_team, destinations, (x_start, y_start))

        board = Moves.move_tile(board, (x_start, y_start), (x_end, y_end), player_team)

        winner = Success.check_success(board, player_team)
        if winner != 0:
            Io.clear(stdscr)
            Io.print_board(stdscr, board)
            Io.print_winner(stdscr, winner)
            break

        player_team *= -1


def launch_game():
    wrapper(launch_game_curses)
