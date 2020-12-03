import os
from os import path
from configparser import ConfigParser

from utils.paths import ensure_directory

HOME_DIR = path.expanduser('~')
ROOT_DIR = ensure_directory(path.join(HOME_DIR, '.lp-cli'))
CONFIG_FILE = path.join(ROOT_DIR,'config.ini')

# Parse configuration
configuration = ConfigParser()
if path.exists(CONFIG_FILE):
    configuration.read(CONFIG_FILE)

GITHUB_ACCESS_TOKEN = configuration.get('GITHUB','access_token',fallback=None)