import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # General config
    APP_NAME: str = "Cotador Assistente API"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # CORS - Allowed origins
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",  # Local development
        "http://127.0.0.1:5173",  # Local development
        "https://*.github.io",    # GitHub Pages (any user)
    ]
    
    # If custom FRONTEND_URL in .env, add it
    frontend_url = os.getenv("FRONTEND_URL")
    if frontend_url:
        CORS_ORIGINS.append(frontend_url)
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

settings = Settings()
