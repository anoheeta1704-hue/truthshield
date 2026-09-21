from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    cors_origins: str = "http://localhost:5173"

    @property
    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]

    class Config:
        env_file = ".env"

settings = Settings()
