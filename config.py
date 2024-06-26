import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, ".env"))
except FileNotFoundError:
    print(".env not found")


TOKEN_GPT = os.getenv('TOKEN_GPT')
TOKEN_DISCORD = os.getenv('TOKEN_DISCORD')
