# config.py

import os
from dotenv import load_dotenv

# Autoload .env.test if running with pytest and ENV_FILE is not explicitly set
if not os.getenv("ENV_FILE") and "PYTEST_VERSION" in os.environ:
    os.environ["ENV_FILE"] = ".env.test"

load_dotenv(dotenv_path=os.getenv("ENV_FILE", ".env.development"))

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

if not all([DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT]):
    raise ValueError("❌ Missing one or more required DB environment variables")

print(f"📦 DATABASE_URL in use: {DATABASE_URL}")
