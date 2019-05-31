import play
import sys


def goodbye():
    return 'Goodbye!'


if __name__ == '__main__':
    try:
        play.launch_game()
    except KeyboardInterrupt:
        print('\n' + goodbye())
        sys.exit(0)
