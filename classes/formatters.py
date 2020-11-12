from argparse import RawDescriptionHelpFormatter, PARSER


class SubcommandHelpFormatter(RawDescriptionHelpFormatter):
    
    def _format_action(self, action):
        parts = super(RawDescriptionHelpFormatter, self)._format_action(action)
        if action.nargs == PARSER:
            parts = "\n".join(parts.split("\n")[1:])
        return parts