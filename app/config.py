import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
    DEBUG = os.getenv("FLASK_ENV") == "development"
    GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "unknown")
