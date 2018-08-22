from util.json_to_dict import json2dict
from enum.config import CONFIG
from random import randint

def monster_generator():
	monsters = json2dict(CONFIG.MONSTER_DICTIONARY_BASEDIR+CONFIG.MONSTER_DICTIONARY_JSONFILES)
	generate_monster = monsters[randint(0, 2)]
	return generate_monster