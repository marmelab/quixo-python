from game.constants import N_ROWS, INDEX_LAST_ROW


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


def check_rows(board, player=0):
    winner=0
    for row in board:
        winner = get_winner(sum(row)) if get_winner(sum(row)) != 0 else winner
        if winner < 0 and player == 1 or winner > 0 and player == -1:
            return winner
    return winner


def check_cols(board, player=0):
    # invert cols and rows
    inverted_board = list(map(list, zip(*board)))
    return check_rows(inverted_board, player)


def check_success(board, player=0):
    """
    Arguments:
        board
    Returns:
        integer -- 0 if no winner else value of winner
    """
    first_diag = check_diag(board)
    second_diag = check_diag(board, True)
    rows = check_rows(board, player)
    cols = check_cols(board, player)
    winner = 0
    for result in [first_diag, second_diag, rows, cols]:
        if result != 0:
            winner = result
        # If the player not playing align, he won whatever
        if winner < 0 and player == 1 or winner > 0 and player == -1 :
            return winner
    return winner
