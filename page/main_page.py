from util.page_util import load_decoration
from enum.page import PAGE

def main_page(**kwargs):
    choice = 0
    flagChoiceError = True
    decor = load_decoration(PAGE.DECORATION_BASE_DIR+"loading-decoration")
    print(decor)

    while flagChoiceError:
        try:
            choice = int(input("Please choose the menu[1..2]: "))
            flagChoiceError = False
        except ValueError:
         print("You chose the wrong option")
    return choice
