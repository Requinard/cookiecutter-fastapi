"""
Handles centralized settings management
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Configuration management.

    All settings here are filled in with Environment Variables. This allows us to configure stages and platforms.
    """
    stage: str = 'default'


settings = Settings()
