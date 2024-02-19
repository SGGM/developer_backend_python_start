import os

from databases import Database
from sqlalchemy import Column, Integer, Float, TIMESTAMP, MetaData, Table, create_engine
from sqlalchemy.sql import func


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()
track_points = Table(
    "track_points",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("device_id", Integer),
    Column("timestamp", default=func.current_timestamp(), type_=TIMESTAMP(timezone=True)),
    Column("x", Float),
    Column("y", Float),
    Column("z", Float)
)

database = Database(DATABASE_URL)
