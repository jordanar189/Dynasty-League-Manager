import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    SLEEPER_BASE_URL = os.getenv("SLEEPER_BASE_URL", "https://api.sleeper.app/v1")
