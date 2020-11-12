import importlib
from config import MODULES

def load_modules():
    for module in MODULES:
        importlib.import_module(module)