import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Configurações gerais
    APP_NAME: str = "Cotador Assistente API"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # CORS - Origins permitidas
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",  # Desenvolvimento local
        "http://127.0.0.1:5173",  # Desenvolvimento local
        "https://*.github.io",    # GitHub Pages (qualquer usuário)
    ]
    
    # Se houver FRONTEND_URL customizada no .env, adiciona
    frontend_url = os.getenv("FRONTEND_URL")
    if frontend_url:
        CORS_ORIGINS.append(frontend_url)
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

settings = Settings()
