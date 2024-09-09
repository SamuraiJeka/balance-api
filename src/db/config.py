from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    @property
    def sync_url(self):
        return f"postgre+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_PORT}/{self.DB_NAME}"

    @property
    def async_url(self):
        return f"postgre+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
