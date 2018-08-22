class CharacterType:
    # fill your character types variants
    character_type = {
        "warrior":{"str":20, "agi":11, "dex":15, "int":5, "attack":20}, 
        "knight":{"str":25, "agi":15, "dex":10, "int":10, "attack":20}
        }

    # define the list of character types
    enum_ctype = ["warrior", "knight"]

    # define the list of character's components
    enum_stype = ["str", "agi", "int", "dex"]