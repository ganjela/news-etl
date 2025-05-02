from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from secret_manager import SecretManager
import os

load_dotenv()



class Settings(BaseSettings):
    secret_manager: SecretManager = SecretManager()

    API_KEY: str = secret_manager.get_secret("news_api_key")
    API_URL: str

    PARAMS: dict = {
        "from": "2025-04-28",
        "to": "2025-04-28",
        "apiKey": API_KEY
        }

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


SETTINGS = Settings()