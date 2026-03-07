import os 
from anyio import Path
from dotenv import load_dotenv
load_dotenv()


class Settings:
    """Bot settings."""
    TOKEN = os.getenv("TOKEN")
    DOWNLOADS_DIR = Path("downloads")

settings = Settings()