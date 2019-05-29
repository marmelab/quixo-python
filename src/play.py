import game.board as Board
import game.success as Success
import game.moves as Moves
import playerio as Io


def launch_game():
    player_team = 1
    board = Board.create_board()
    while True:
        Io.clear()

        winner = Success.check_success(board)
        if winner != 0:
            Io.print_success(board, winner)
            break

        movables = Board.get_movables_tiles(board, player_team)
        Io.print_board(board, movables)

        movables_choices = list(range(1, len(movables) + 1))
        player_input = Io.get_player_choice('Tile to move : ', movables_choices, player_team)

        Io.clear()

        (x_start, y_start) = Board.get_coords_from_movables(movables, player_input)

        destinations = Board.get_possibles_destinations(board, x_start, y_start)
        Io.print_board(board, destinations, (x_start, y_start))

        destinations_choices = list(range(1, len(destinations) + 1))
        destination_input = Io.get_player_choice('Destination of the tile : ', destinations_choices, player_team)

        (x_end, y_end) = Board.get_coords_from_movables(destinations, destination_input)
        board = Moves.move_tile(board, (x_start, y_start), (x_end, y_end), player_team)

        player_team *= -1
