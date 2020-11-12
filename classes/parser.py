import sys
from argparse import ArgumentParser

class ArgParser(ArgumentParser):

    def error(self, message):
        print(f"error: {message}")
        self.print_help()
        sys.exit(2)
