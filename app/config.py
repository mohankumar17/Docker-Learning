from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict()

    DB_HOST: str
    DB_PORT: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_DATABASE_NAME: str
    ENV: str

settings = Settings(_env_file='.env', _env_file_encoding='utf-8')