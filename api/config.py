from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///db.sqlite3"
    SQLALCHEMY_DATABASE_TEST_URL: str = "sqlite:///test.sqlite3"

settings = Settings()