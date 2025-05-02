from pydantic_settings import BaseSettings, SettingsConfigDict
from secret_manager import SecretManager



class Settings(BaseSettings):
    secret_manager: SecretManager = SecretManager()

    API_KEY: str = secret_manager.get_secret("news_api_key")
    API_URL: str = "https://newsapi.org/v2/everything?q=apple"

    @property
    def PARAMS(self):
        return {
        "from": "2025-04-28",
        "to": "2025-04-28",
        "apiKey": self.API_KEY
    }
SETTINGS = Settings()
print(SETTINGS.PARAMS)