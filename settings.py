from os.path import join, dirname
from dotenv import load_dotenv
import os
from utils import config

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get('TOKEN')

PREFIX = config.PREFIX
CHANNEL = config.CHANNEL
ROLES = sorted(config.ROLES.items())
TITLES = config.TITLES
MESSAGES = config.MESSAGES
