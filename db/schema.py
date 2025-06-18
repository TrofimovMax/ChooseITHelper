# db/schema.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy.schema import CreateTable
from database import engine
from models import Base

for table in Base.metadata.sorted_tables:
    print(str(CreateTable(table).compile(engine)))

with open("db/schema.sql", "w") as f:
    for table in Base.metadata.sorted_tables:
        f.write(str(CreateTable(table).compile(engine)) + ";")
