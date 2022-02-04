from sqlite3 import Date
from sqlalchemy import Column, Integer, String

from .database import Base


class Event(Base):
    __tablename__ = "data"

    asin = Column(String, index=True)
    brand = Column(String, index=True)
    id = Column(String, primary_key=True, index=True)
    source = Column(String, index=True)
    stars = Column(Integer, index=True)
    timestamp = Column(Integer, index=True)
