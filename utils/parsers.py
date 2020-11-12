from classes.parser import ArgParser
from classes.formatters import SubcommandHelpFormatter

_main_parser = ArgParser(formatter_class=SubcommandHelpFormatter)

def parse_args():
    return _main_parser.parse_args()

class SubParsers:
    commands = _main_parser.add_subparsers(title="Commands", description="Available commands", metavar="command", required=True)
