# config.py

from dotenv import load_dotenv
import os

env_file = os.getenv("ENV_FILE", ".env.development")
load_dotenv(dotenv_path=env_file)

DATABASE_URL = os.getenv("DATABASE_URL")
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")
