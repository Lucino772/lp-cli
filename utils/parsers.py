from classes.parser import ArgParser
from classes.formatters import SubcommandHelpFormatter

_main_parser = ArgParser(formatter_class=SubcommandHelpFormatter)

def parse_args():
    return _main_parser.parse_args()

