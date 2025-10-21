from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = os.getenv("DEBUG", "False") == "True"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///tasks.db")  # Default to SQLite for simplicity
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")  # Change this in production
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")  # Comma-separated list of allowed hosts

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}