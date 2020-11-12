import sys
from argparse import ArgumentParser
from .formatters import SubcommandHelpFormatter

class ArgParser(ArgumentParser):

    def __init__(self, **kwargs):
        kwargs['formatter_class'] = SubcommandHelpFormatter
        super().__init__(**kwargs)

    def error(self, message):
        print(f"error: {message}")
        self.print_help()
        sys.exit(2)
