from unicurses import *

stdscr = initscr()
move(0, 5)
addstr("test")

getch()
endwin()