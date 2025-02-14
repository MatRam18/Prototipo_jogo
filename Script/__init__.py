import os.path

def ii(arq):
    ca = arq
    if os.path.isfile(ca):
        return True
    else:
        return False