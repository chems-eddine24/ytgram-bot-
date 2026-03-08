import os 
from dotenv import load_dotenv
load_dotenv()


class Settings:
    """Bot settings."""
    TOKEN = os.getenv("TOKEN")

settings = Settings()