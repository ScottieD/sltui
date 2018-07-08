import curses
from curses import wrapper
import sys

def main(stdscr):
    while True:
        # Clear screen
        stdscr.clear()
        stdscr.nodelay(True)

        #init curses object
        interface = curses.initscr()
        interface.border(0)
        interface.addstr(5,5, "Softlayer:Control:Home")

        #refresh screen
        interface.refresh()
        interface.getch()

        curses.endwin()
wrapper(main)