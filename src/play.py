import game.board as Board
import game.success as Success
import game.moves as Moves
import cursesio as Ui
from curses import wrapper
import curses


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
    wrapper(launch_game_curses)
