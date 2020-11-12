import os
import config

from utils.modules import load_modules
from utils.parsers import parse_args

load_modules()

if __name__ == "__main__":
    parse_args()