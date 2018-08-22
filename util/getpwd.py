def getpwd():
    import os
    return "/".join((os.path.dirname(os.path.realpath(__file__))+"/").split("/")[0:-2]) + "/"