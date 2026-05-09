"""Configuration package."""

from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    """Base settings class for environment-driven configuration."""

    app_env: str = "dev"
