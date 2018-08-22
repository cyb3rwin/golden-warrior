from util.getpwd import getpwd
import json

def json2dict(filename):
    data = None
    with open(getpwd()+"%s.json"%filename, "r") as f:
        data = json.loads(f.read())
    
    return data
