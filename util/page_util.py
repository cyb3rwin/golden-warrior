from util.getpwd import getpwd
import json

def load_decoration(filename):
    data = None
    with open(getpwd()+"%s.txt"%filename, "r") as f:
        data = f.read()
    return data
