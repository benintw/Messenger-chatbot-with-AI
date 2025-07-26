import os

from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env file


class Config:
    FB_PAGE_ACCESS_TOKEN: str = os.getenv("FB_PAGE_ACCESS_TOKEN", "")
    FB_VERIFY_TOKEN: str = os.getenv("FB_VERIFY_TOKEN", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
