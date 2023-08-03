
#Data validation and "settings management"?
#go back and add .env file
from pydantic import BaseSettings
#"least recently used" strategy, keeps data inside a cache so we do not have to reuse?
from functools import lru_cache

#base settings set up
class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortner.db"

    class Config:
        env_file = ".env"
#caching the result of get settings
@lru_cache
def get_settings() -> Settings:
    settings= Settings()
    print(f"Load settings for: {settings.env_name}")
    return settings



