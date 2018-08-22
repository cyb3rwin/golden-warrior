from util.page_util import load_decoration
from util.screen_util import clear
from util.dict_to_table import dict2table

from enum.page import PAGE
from setting.char_type import CharacterType


def start_game(**kwargs):
    flagRoleError = True
    resp = None
    clist = kwargs['clist']

    while(resp == None):	
        clear()
        decor = load_decoration(PAGE.DECORATION_BASE_DIR+"start-decoration")
        print(decor)

        name = input("Your name: ")
        resp = clist.create_new(name)
        character = clist.characters[resp]

        print("Hello %s, what a good name!"%(character["name"]))
        print("So, these are the following role you have to choose")

        rcount = 1
        for role in CharacterType.character_type:
            print("%s. Role: %s " % (rcount, role))
            dict2table(CharacterType.character_type[role], ['Status','Pts'])
            rcount += 1

        while flagRoleError:
            try:
                character["role"] = CharacterType.enum_ctype[int(input("What role do you want?[1..2]: "))-1]
                flagRoleError = False
            except ValueError as e:
                print("You chose the wrong option")

        kwargs['adventure_callback'](character=character)
