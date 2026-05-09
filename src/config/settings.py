from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Environment-based settings for the backend service."""

    app_env: str = "dev"
    service_name: str = "backend-service"
    host: str = "0.0.0.0"
    port: int = 8080


settings = Settings()
