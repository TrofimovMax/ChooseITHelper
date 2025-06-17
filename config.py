# config.py

from dotenv import load_dotenv
import os

env_file = os.getenv("ENV_FILE", ".env.development")
load_dotenv(dotenv_path=env_file)

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

if not all([DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT]):
    raise ValueError("❌ Missing one or more required DB environment variables")

print(f"📦 DATABASE_URL in use: {DATABASE_URL}")
