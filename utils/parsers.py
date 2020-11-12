from classes.parser import ArgParser
from classes.formatters import SubcommandHelpFormatter

_main_parser = ArgParser()

def parse_args():
    args = _main_parser.parse_args()
    if 'handler' in args:
        args.handler(**args.__dict__)

class SubParsers:
    commands = _main_parser.add_subparsers(title="Commands", description="Available commands", metavar="command", required=True)
