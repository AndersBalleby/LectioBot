import os

from dotenv import load_dotenv
from lectiobot import LectioBot

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

if __name__ == "__main__":
    lectio_bot = LectioBot()
    lectio_bot.launch(TOKEN)
