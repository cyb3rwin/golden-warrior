# file I/O
# save
# load
# json

import math
import time
import os
import json
from random import randint

#################
# Golden Warrior
#################

character = {"name":"Albeit","role":"novice","level":1, "hp":200, "max_hp":200, "exp":90, "next_exp":100, "mp":150, "max_mp":150, "str":10, "agi":1, "dex":10, "int":1, "bonus_stat":10, "attack":15, "money":1000, "bag":{"items"[],"max-weight":50}}
character_type = {"warrior":{"str":20, "agi":11, "dex":15, "int":5, "attack":20}, "knight":{"str":25, "agi":15, "dex":10, "int":10, "attack":20}}
enum_ctype = ["warrior", "knight"]
enum_stype = ["str", "agi", "int", "dex"]

def clear():
	os.system('clear')
	for _ in range(10):
		print("")

def load_game():
	global character

	try:
		f = open("gwgame.dat", "r")
		character = json.loads(f.read())
		f.close()
		print("Game loaded successfully")
		print("Welcome back %s" % (character["name"]))
	except FileNotFoundError:
		print("No saved game")

	temp = input("Please press any key to continue")
	clear()

def save_game():
	global character
	f = open("gwgame.dat", "w")
	f.write(json.dumps(character))
	f.close()
	print("Game saved successfully")
	temp = input("Please press any key to continue")
	

def loading_page():
	choice = 0
	flagChoiceError = True
	
	clear()
	print("-----------------------------")
	print("- WELCOME TO GOLDEN WARRIOR -")
	print("-----------------------------")
	print("Golden Warrios is a game where you have to save the city while")
	print("1. Start Game")
	print("2. Load A Game")
	print("3. Exit")

	while flagChoiceError:
		try:
			choice = int(input("Please choose the menu[1..3]: "))
			flagChoiceError = False
		except ValueError:
			print("You chose the wrong option")
	return choice

def monster_generator():
	monsters = [{"name":"spore","hp":20, "attack":10, "dodge":10, "bonus_exp":10, "dropped-items":[{"item_name":"potion", "item_weight":2, "price":1}]},{"name":"king spore","hp":10, "attack":900, "dodge":50, "bonus_exp":30},{"name":"fishman", "hp":20, "attack":5, "dodge":5, "bonus_exp":20}]
	generate_monster = monsters[randint(0, 2)]
	return generate_monster

def switch_choice(choice):
	if choice == 1:
		start_game()
	elif choice ==2:
		load_game()
		adventure()
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

def raise_exp(bonus_exp):
	if character["exp"] + bonus_exp >= character["next_exp"]:
		character["exp"] = abs(character["next_exp"] - (character["exp"] + bonus_exp))
		character["next_exp"] += character["next_exp"] + character["level"]*2
		character["bonus_stat"] =  int(bonus_exp/10)*2
		character["level"] += 1
		character["attack"] += (character["level"]*2)/10

		print("Congratulation %s!! Your level has grown up" % (character["name"]))
		print("You have %s bonus stats" % (character["bonus_stat"]))
		print("Your current level is %s" % (character["level"]))
	else:
		character["exp"] = character["exp"] + bonus_exp

	temp = input("Please press any key to continue")
				

def set_stat():
	choiceStat = 0
	while character["bonus_stat"] > 0 and choiceStat != 5:
		clear()
		print("==========SET UP STATUS=========")
		print("Hello, what status do you want yo raise?")
		print("1. strenght(str): incresing your attack power")
		print("2. agility(agi): incresing your speed")
		print("3. intelligence(int): incresing your magic/skill power and skill point")
		print("4. dexterity(dex): incresing your accuracy")
		print("5. back")
		print("Your current bonus_stat: %s" % (character["bonus_stat"]))
		
		flagErrorStat = True
		
		while flagErrorStat:
			try:
				choiceStat = int(input("Which one do you want to raise?[1..5] "))
				flagErrorStat = False
				if choiceStat != 5:
					numStat = int(input("How much do you want to raise?[1..%s] " % (character["bonus_stat"])))
					character["bonus_stat"] -= numStat
					character[enum_stype[choiceStat+1]] += numStat
			except ValueError:
				print("You chose an invalid option")

	temp = input("Please press any key to continue")

def adventure():
	global character
	actionChoice = 0
	flagActionError = True

	while actionChoice != 6:
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
		print("5. Save game")
		print("6. Back to main menu")

		while flagActionError:
			try:
				actionChoice = int(input("Your action [1..6]: "))
					
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
					runChoice = 0
					flagRunError = True

					print("Let's hunt")
					print("Finding a monster")

					time.sleep(3)
					
					print("A monster is appearing")
					monster = monster_generator()

					print("======Monster Profile======")
					print("Monster's name:%s"%monster["name"])
					print("Monster's health:%s"%monster["hp"])
					print("Monster's attack:%s"%monster["attack"])

					print("Hey %s, would you like to kill the monster?" % character["role"])

					if character["attack"]*(character["str"]/2) >= monster["attack"]:
						print("I suggest you to kill it, go without doubt sir")
					else:
						print("This creature is too strong to be defeated, I suggest you to run!!")
					
					flagMonsterHasBeenKilled = False
					while runChoice != 2 or monster["hp"] > 0:
						if monster["hp"] <= 0:
							raise_exp(monster["bonus_exp"])
						else:
							if character["hp"] <= 0:
								print("You're defeated")
								temp = input("Please press any key to respawn")
								adventure()

						print("== Action ==")
						print("1. Attack")
						print("2. Runaway")
						
						flagRunError = True

						while flagRunError:
							runChoice = 0
							flagRunError = True
							try:
								runChoice = int(input("Your action[1..2]: "))
								flagRunError = False

								if runChoice == 1:

									#player attack
									dodge_point = monster["dodge"] - (character["dex"]*2)
									
									if dodge_point <= 0:
										monster["hp"] -= character["attack"]+(character["str"]/2)
										print("You hit the monster with %s damage point" % (character["attack"]+(character["str"]/2)))
									else:
										print("You missed the hit!")

									if int(monster["hp"]) <= 0:
										raise_exp(monster["bonus_exp"])
										adventure()

									print("Waiting for the monster to fight you back")
									
									time.sleep(3)

									#monster attack
									dodge_point = monster["attack"] - (character["dex"]*2)
									
									if dodge_point > 0:
										character["hp"] -= (monster["attack"]/2)+(monster["dodge"]/2)
										print("You were hit by the monster with %s damage point" % ((monster["attack"]/2)+(monster["dodge"]/2)))
									else:
										print("You've dodged it safely")
									
									if character["hp"] <= 0:
										print("You're defeated")
										temp = input("Please press any key to respawn")
										adventure()

									print("======Monster Profile======")
									print("Monster's name:%s"%monster["name"])
									print("Monster's health:%s"%monster["hp"])
									print("Monster's attack:%s"%monster["attack"])

									print("-> Status: %s " % (character))

								else:
									print("You get away safely")
									adventure()
							except ValueError:
								print("You chose the wrong option")


					
					temp = input("Please press any key to continue")
				elif actionChoice == 4:
					set_stat()
				elif actionChoice == 5:
					save_game()
					adventure()
				else:
					sure = 0
					flagSureError = True

					while flagSureError:
						try:
							print("The current game will be erased if you don't save the game")
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