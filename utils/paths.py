import os
from os import path

def ensure_directory(_path: str,parent=False):
    if not path.exists(_path):
        if parent:
            os.makedirs(_path)
        else:
            os.mkdir(_path)
    return _path