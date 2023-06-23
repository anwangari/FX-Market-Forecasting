import os
from dotenv import load_dotenv
from pydantic import BaseSettings

# Search for .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)


class Settings(BaseSettings):
    api_key: str
    db_name: str
    username: str
    port: str
    pw: str
    host: str

    class Config:
        env_file = env_path

settings = Settings()
