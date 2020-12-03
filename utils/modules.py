import importlib

def include(module):
    importlib.import_module(module)
    return module
