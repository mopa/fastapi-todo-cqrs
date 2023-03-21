import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "postgresql://todo_user:todo_pass@postgredb:5432/todo")

settings = Settings()
