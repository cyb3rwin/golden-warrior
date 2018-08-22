import math
import time
import os
from util.screen_util import clear
from page.main_page import main_page
from page.start_page import start_game
from page.adventure_page import adventure
from chars.character_list import CharactersList
from setting.char_type import CharacterType

clist = CharactersList()

#################
# Golden Warrior
#################

def switch_choice(choice):
	if choice == 1:
		start_game(adventure_callback=adventure, clist=clist)
	else:
		print("Thank you for playing the game")
		exit()

if __name__ == '__main__':
	clear()
	get_choice = main_page()
	switch_choice(get_choice)