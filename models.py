from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
import sqlite3

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__="users"

    id=Column(Integer, primary_key=True)
    name=Column(String)
    age=Column(Integer)

Base.metadata.create_all(engine)