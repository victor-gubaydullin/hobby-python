import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        env_path = os.path.join(os.getcwd(), 'vityanki', 'variables.env')

        if not os.path.exists(env_path):
            raise FileNotFoundError("The 'variables.env' file is missing in the 'vityanki' directory.")
        else:
            load_dotenv(env_path)
            
            self.TOKEN = os.getenv("BOT_TOKEN")
            self.LOG_DIR = os.getenv("LOG_DIR")

def load_config():
    return Config()