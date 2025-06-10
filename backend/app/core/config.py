import json
from typing import Dict, List

from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings configuration.
    """

    # General settings
    app_name: str = "MyApp"
    app_version: str = "1.0.0"
    postgres_user: str = "postgres"
    postgres_password: str = "password"
    postgres_db: str = "myapp_db"
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    allowed_hosts: List[str] = ["*"]
    cors_origins: List[str] = ["*"]
    debug: bool = True
    secret_key: str = "your_secret_key"

    # Logging settings
    log_level: str = "INFO"
    log_format: str = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # Standard to keep here for flexibility
    )

    # Redis settings
    redis_url: str = "redis://localhost:6379/0"
    redis_password: str = ""
    redis_db: int = 0

    # Email settings
    smtp_server: str = "smtp.example.com"
    smtp_port: int = 587
    smtp_user: EmailStr = "user@example.com"
    smtp_password: str = "password"
    email_from: EmailStr = "user@example.com"
    email_to: List[EmailStr] = ["recipient@example.com"]

    # Feature flags
    # feature_flags: Dict[str, bool] = {
    #     "enable_feature_x": True,
    #     "enable_feature_y": False,
    # }

    # Third-party API keys
    # third_party_api_keys: Dict[str, str] = {
    #     "api_service_1": "your_api_key_1",
    #     "api_service_2": "your_api_key_2",
    # }

    # Custom settings
    custom_settings: Dict[str, str] = {}

    def __init__(self, **values):
        super().__init__(**values)
        # Load custom settings from a JSON file if it exists
        try:
            with open("custom_settings.json") as f:
                custom_settings = json.load(f)
                self.custom_settings.update(custom_settings)
        except FileNotFoundError:
            pass

    class Config:
        env_file = ".env"
        case_sensitive = True
