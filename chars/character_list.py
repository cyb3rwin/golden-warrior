from enum.config import CONFIG
from util.json_to_dict import json2dict

class CharactersList:
    def __init__(self):
        self.characters = {}

    def create_new(self, name):
        character_template = json2dict(
            CONFIG.CHARS_DICTIONARY_BASEDIR+CONFIG.CHARS_DICTIONARY_JSONFILES
            )
        novice_type = character_template["novice"]
        novice_type["name"] = name
        
        if name not in self.characters:
            self.characters.setdefault(name, novice_type)
            return name
        else:
            return None