import curses
from curses import wrapper
import sys

def main(stdscr):
    home()


def getconfig():
    return


def home():
    while True:
        # Clear screen
        #stdscr.clear()
        #stdscr.nodelay(True)

        #init curses object
        interface = curses.initscr()
        interface.border(0)
        interface.addstr(0, 30, "Softlayer:Setup", curses.A_TOP)

        #refresh screen
        interface.refresh()
        #interface.getch()

        #curses.endwin()

if __name__ == "__main__":
    try:
        wrapper(main)
    except KeyboardInterrupt:
        sys.exit(1)
sys.exit(1)