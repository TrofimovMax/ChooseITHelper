# tests/load_structure_from_db.py

# run script with
# $env:ENV_FILE=".env.test"; python tests/load_structure_from_db.py

import psycopg2
from sqlalchemy import create_engine, text
from models import Base
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env.test")

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


def drop_and_create_database():
    print("🔄 Connecting to PostgreSQL default database to reset test DB...")
    conn = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"""
        SELECT pg_terminate_backend(pid)
        FROM pg_stat_activity
        WHERE datname = '{DB_NAME}' AND pid <> pg_backend_pid();
    """)

    cur.execute(f"DROP DATABASE IF EXISTS {DB_NAME};")
    print(f"🗑️  Dropped database '{DB_NAME}'.")

    cur.execute(f"CREATE DATABASE {DB_NAME};")
    print(f"✅ Created new database '{DB_NAME}'.")

    cur.close()
    conn.close()


def migrate_structure():
    print("📦 Creating tables from models...")
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    print("✅ All models migrated.")


if __name__ == "__main__":
    drop_and_create_database()
    migrate_structure()
