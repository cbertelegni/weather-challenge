from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Weather Challenge - Cristian Bertelegni"
    WEATHER_API_BASE_URL: str
    WEATHER_API_KEY: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()