from util.page_util import load_decoration
from util.screen_util import clear
from util.dict_to_table import dict2table
from monster.monster_generator import monster_generator
from enum.page import PAGE
import time

def adventure(**kwargs):
    clear()

    actionChoice = 0
    flagActionError = True
    character = kwargs['character']

    decor = load_decoration(PAGE.DECORATION_BASE_DIR+"adventure-decoration")
    print(decor)

    while actionChoice != 5:
        actionChoice = 0
        flagActionError = True

        while flagActionError:
            try:
                actionChoice = int(input("Your action [1..5]: "))
                    
                if actionChoice == 1:
                    dict2table(character, ['Status','Pts'])
                    temp = input("Please press any key to continue")
                    adventure(**kwargs)
                elif actionChoice == 2:
                    print("You are now taking a rest")
                    time.sleep(5)

                    character["hp"] = character["max_hp"]
                    character["mp"] = character["max_mp"]

                    print("You are fully restored")
                    dict2table(character, ['Status','Pts'])

                    temp = input("Please press any key to continue")
                    adventure(**kwargs)

                elif actionChoice == 3:
                    runChoice = 0
                    flagRunError = True

                    print("Let's hunt")
                    print("Finding a monster")

                    time.sleep(3)
                    
                    clear()
                    print("A monster is appearing")
                    monster = monster_generator()
                    decor = load_decoration(PAGE.DECORATION_BASE_DIR+"monster-decoration")
                    print(decor)
                    
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
                                adventure(**kwargs)

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
                                        adventure(**kwargs)

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
                                        adventure(**kwargs)

                                    print("======Monster Profile======")
                                    print("Monster's name:%s"%monster["name"])
                                    print("Monster's health:%s"%monster["hp"])
                                    print("Monster's attack:%s"%monster["attack"])

                                    print("-> Status: %s " % (character))

                                else:
                                    print("You get away safely")
                                    adventure(**kwargs)
                            except ValueError:
                                print("You chose the wrong option")

                    temp = input("Please press any key to continue")
                elif actionChoice == 4:
                    chaaracter = set_stat(character)
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

def set_stat(character):
    choiceStat = 0
    while character["bonus_stat"] > 0 and choiceStat != 5:
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
    return character