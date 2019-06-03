import curses
from tiles import cross, circle, empty

GREEN = 1
OFFSET_X = 5
DIRECTIONS = ['KEY_LEFT', 'KEY_RIGHT']


def init_curses():
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)
    curses.init_pair(GREEN, curses.COLOR_GREEN, -1)


def clear(stdscr):
    stdscr.clear()


def get_player(number):
    if number == 1:
        return '1'
    if number == -1:
        return '2'
    return None


def get_symbol(value):
    if value < 0:
        return 'O'
    if value > 0:
        return 'X'
    return ' '


def print_winner(stdscr, winner):
    stdscr.addstr(f'\n\nThe player {get_player(winner)} has aligned 5 symbols. Game Won !', curses.A_BOLD)
    stdscr.addstr('\nPress any key to quit !')
    stdscr.getkey()


def print_player(stdscr, player, phase=1):
    stdscr.addstr(f'\n\nPlayer {get_player(player)} ({get_symbol(player)})')
    text = 'Press space to select a '
    text += 'cube to move' if phase == 1 else 'destination for the cube'
    stdscr.addstr(f'\n{text}')


def get_attr(pos, movables, selected, picked):
    if pos == picked:
        return curses.A_BLINK
    if pos == selected:
        return curses.color_pair(GREEN) + curses.A_BOLD
    if pos in movables:
        return curses.A_BOLD
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
            stdscr.addstr(y + y_start, x + x_start, tile[y][x], attr)

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


def get_next_in_direction(movables, selected, key):
    index = movables.index(selected)
    if key == 'KEY_RIGHT':
        index = 0 if index >= len(movables) - 1 else index + 1
    else:
        index = len(movables) - 1 if index == 0 else index - 1
    return movables[index]


def get_player_selection(stdscr, board, player_team, movables, picked=(-1, -1)):
    if len(movables) < 1:
        return False

    key = None
    selected = movables[0]
    while key != ' ':
        clear(stdscr)
        print_board(stdscr, board, movables, selected, picked)
        phase = 1 if picked == (-1, -1) else 2
        print_player(stdscr, player_team, phase)
        stdscr.refresh()
        key = stdscr.getkey()

        if key in DIRECTIONS:
            tmp_selected = get_next_in_direction(movables, selected, key)
            if tmp_selected is not None:
                selected = tmp_selected

    return selected
