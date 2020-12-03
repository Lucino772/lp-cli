from utils.parsers import SubParsers
from .functions import create_project

parser = SubParsers.commands.add_parser("projects", help="Manage your projects")

sub_parsers = parser.add_subparsers(title="Actions", description="Available actions", metavar="action", required=True)

parser_create = sub_parsers.add_parser("create", help="Create a project")
parser_create.add_argument("name", help="The name of your project")
parser_create.add_argument("-g", "--github", help="Create a repo for your project on github",dest="use_github", action="store_true")
parser_create.add_argument("-d", "--description", help="Describe your project (github)", dest="description")
parser_create.add_argument("-p", "--private", help="Make repo private", dest="is_private", action="store_true")
parser_create.add_argument("--auto-init", help="Create an initial commit with README", dest="use_auto_init", action="store_true")
parser_create.add_argument("--gitignore-template", help="Select a gitignore template", dest="gitignore_template")
parser_create.add_argument("--licence-template", help="Select a licence template", dest="licence_template")
parser_create.set_defaults(handler=create_project)
