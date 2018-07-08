import curses
from curses import wrapper
import sys


stdscr = curses.initscr()


def main(screen):
    home(screen)


def getconfig():
    return


def home(screen):
    while True:
        screen.nodelay(True)

        #init curses object
        interface = curses.initscr()
        interface.border(0)
        interface.addstr(0, 30, "Softlayer:Setup", curses.A_TOP)

        #refresh screen
        interface.refresh()


if __name__ == "__main__":
    try:
        wrapper(main(stdscr))
    except KeyboardInterrupt:
        sys.exit(1)
sys.exit(1)