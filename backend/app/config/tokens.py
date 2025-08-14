import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = os.environ['ALGORITHM']
TOKEN_EXPIRATION_HOURS = os.environ['TOKEN_EXPIRATION_HOURS']
