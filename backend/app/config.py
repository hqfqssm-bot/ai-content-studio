import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = "AI Content Studio"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-this-to-a-secure-random-key-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    FREE_CREDITS: int = 5
    PRO_CREDITS: int = 100
    PRO_PRICE_MONTHLY: float = 19.9
    DEFAULT_MODEL: str = os.getenv("DEFAULT_MODEL", "gpt-4o-mini")
    STRIPE_SECRET_KEY: str = os.getenv("STRIPE_SECRET_KEY", "")
    STRIPE_PUBLISHABLE_KEY: str = os.getenv("STRIPE_PUBLISHABLE_KEY", "")
    STRIPE_WEBHOOK_SECRET: str = os.getenv("STRIPE_WEBHOOK_SECRET", "")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:8000")

settings = Settings()
