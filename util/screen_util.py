import os
from enum.config import CONFIG

def clear():
	os.system(CONFIG.CLEAR_CMD)
	for _ in range(10):
		print("")