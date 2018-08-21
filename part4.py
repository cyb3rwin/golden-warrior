# start game
# game flow
# try-catch


import math
import time
import os

#################
# Golden Warrior
#################

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
	clear()
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

	adventure()


def adventure():
	global character
	actionChoice = 0
	flagActionError = True

	while actionChoice != 5:
		actionChoice = 0
		flagActionError = True
		clear()
		print("=============================================")
		print("===============ADVENTURE MODE================")
		print("=============================================")
		print("Hey %s now you're on battlefield" % (character["name"]))
		print("Please choose your action to survive")
		print("1. Show status")
		print("2. Take a rest")
		print("3. Hunting")
		print("4. Set up stat")
		print("5. Back to main menu")

		while flagActionError:
			try:
				actionChoice = int(input("Your action [1..5]: "))
					
				if actionChoice == 1:
					print("-> Status: %s " % (character))
					temp = input("Please press any key to continue")
				elif actionChoice == 2:
					print("You are now taking a rest")
					time.sleep(5)

					character["hp"] = character["max_hp"]
					character["mp"] = character["max_mp"]

					print("You are fully restored")
					print("-> Status: %s " % (character))

					temp = input("Please press any key to continue")

				elif actionChoice == 3:
					print("not available")
					
					temp = input("Please press any key to continue")
				elif actionChoice == 4:
					set_stat()
				else:
					sure = 0
					flagSureError = True

					while flagSureError:
						try:
							print("The current game will be erased")
							print("Are you sure to restart a new whole game?")
							print("1. Yes")
							print("2. No")
							sure = int(input("Choice[1..2]: "))
							flagSureError = False
						except ValueError:
							print("You chose the wrong option")

					if sure == 1:
						choice = loading_page()
						switch_choice(choice)	
					actionChoice = 0

					temp = input("Please press any key to continue")

				flagActionError = False
			except ValueError as e:
				print("You chose the wrong option")

if __name__ == '__main__':
	clear()
	get_choice = loading_page()
	switch_choice(get_choice)