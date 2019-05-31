import curses
from tiles import cross, circle, empty

OFFSET_X = 5

DIRECTIONS = ['KEY_LEFT', 'KEY_RIGHT']


def clear(stdscr):
    stdscr.clear()


def get_player(number):
    if number == 1:
        return '1'
    if number == -1:
        return '2'
    return None


def print_winner(stdscr, winner):
    stdscr.addstr(f'The player {get_player(winner)} has aligned 5 symbols. Game Won !', curses.A_BOLD)


def get_attr(pos, movables, selected, picked):
    if pos == picked:
        return curses.A_BOLD
    if pos == selected:
        return curses.A_BLINK
    if pos in movables:
        return curses.A_NORMAL
    return curses.A_DIM


def get_tile(value):
    if value == 1:
        return cross
    if value == -1:
        return circle
    return empty


def print_tile(stdscr, tile, y_start, x_start, attr):
    wide = 0
    for y in range(len(tile)):
        wide = wide if len(tile[y]) < wide else len(tile[y])
        for x in range(len(tile[y])):
            stdscr.addch(y + y_start, x + x_start, tile[y][x], attr)

    return wide


def print_row(stdscr, row, cursor_y, x, movables, selected, picked):
    cursor_x = OFFSET_X
    for y in range(len(row)):
        attr = get_attr((x, y), movables, selected, picked)
        wide = print_tile(stdscr, get_tile(row[y]), cursor_y, cursor_x, attr)
        cursor_x += wide


def print_board(stdscr, board, movables=[], selected=(-1, -1), picked=(-1, -1)):
    for x in range(len(board)):
        (cursor_y, cursor_x) = stdscr.getyx()
        print_row(stdscr, board[x], cursor_y + 1, x, movables, selected, picked)


def get_next_in_direction(stdscr, movables, selected, key):
    index = movables.index(selected)
    if key == 'KEY_RIGHT':
        if index >= len(movables) - 1:
            index = 0
        else:
            index += 1
    else:
        if index == 0:
            index = len(movables) -1
        else:
            index -= 1

    return movables[index]


def get_player_selection(stdscr, board, movables=[], picked=(-1, -1)):
    if len(movables) < 1:
        return False
    key = None
    selected = movables[0]
    while key != ' ':
        clear(stdscr)
        print_board(stdscr, board, movables, selected, picked)
        (x, y) = selected
        stdscr.refresh()
        key = stdscr.getkey()
        if key in DIRECTIONS:
            tmp_selected = get_next_in_direction(stdscr, movables, selected, key)
            if tmp_selected is not None:
                selected = tmp_selected
                (x, y) = selected

    return selected
