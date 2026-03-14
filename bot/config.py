import os 
from dotenv import load_dotenv
load_dotenv()


class Settings:
    """Bot settings."""
    TOKEN = os.getenv("TOKEN")
    DB_ASYNC_URL = os.getenv("DB_ASYNC_URL")

settings = Settings()