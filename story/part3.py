# import something
# function (yield or not)
# loop
# flagging
# game-flow
# list
# character
# ctype
# enum
# enum_stype

import os

character = {"name":"Albeit","role":"novice","level":1, "hp":200, "max_hp":200, "exp":90, "next_exp":100, "mp":150, "max_mp":150, "str":10, "agi":1, "dex":10, "int":1, "bonus_stat":10, "attack":15}
character_type = {"warrior":{"str":20, "agi":11, "dex":15, "int":5, "attack":20}, "knight":{"str":25, "agi":15, "dex":10, "int":10, "attack":20}}
enum_ctype = ["warrior", "knight"]
enum_stype = ["str", "agi", "int", "dex"]

def clear():
	os.system('clear')
	for _ in range(10):
		print("")

def loading_page():
	choice = 0
	flagChoiceError = True
	
	print("-----------------------------")
	print("- WELCOME TO GOLDEN WARRIOR -")
	print("-----------------------------")
	print("Golden Warrios is a game where you have to save the city while")
	print("1. Start Game")
	print("2. Exit")

	while flagChoiceError:
		try:
			choice = int(input("Please choose the menu[1..2]: "))
			flagChoiceError = False
		except ValueError:
			print("You chose the wrong option")
	return choice


def switch_choice(choice):
	if choice == 1:
		start_game()
	else:
		print("Thank you for playing the game")
		exit()

def start_game():
	global character, character_type
	flagRoleError = True

	clear()
	# greeting message
	print("=============================================")
	print("===============SPORE CITY====================")
	print("=============================================")
	print("Hello, welcome to the Spore City.")
	print("I'm Kyle, and I'm going to assist you.")
	print("Firstly, would you mind to tell me your name?")
	
	character["name"] = input("Your name: ")

	print("Hello %s, what a good name!"%(character["name"]))
	print("So, these are the following role you have to choose")

	rcount = 1
	for role in character_type:
		print("%s. Role: %s " % (rcount, role))
		print("-> Detail: %s " % (character_type[role]))
		rcount += 1

	while flagRoleError:
		try:
			character["role"] = enum_ctype[int(input("What role do you want?[1..2]: "))-1]
			flagRoleError = False
		except ValueError as e:
			print("You chose the wrong option")


if __name__ == '__main__':
	clear()
	get_choice = loading_page()
	switch_choice(get_choice)